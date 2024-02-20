from datetime import datetime, timedelta
import math
from django.shortcuts import render, redirect
from .models import OBDrillingOps
from .forms import OBDrillingOpsForm
from obdrillingsummary.models import OBDrillingSummary
from selectedObserver.models import SelectedObserver
import numpy as np
import pandas as pd
import sqlite3
from .utils import get_pieplot
from django.contrib import messages

def list_obdrilling_ops(request): 
    selectedwell = SelectedObserver.objects.first()
    id1 = selectedwell.wellid 
    obdrilling_opss = OBDrillingOps.objects.filter(obwellid = id1).all()  
    cnx = sqlite3.connect('db.sqlite3', check_same_thread=False)    
    ops = pd.read_sql_query("select * from obdrillingoperations_obdrillingops", cnx)   
    cnx.close() 
    df = pd.DataFrame(ops)
    df_well = df[df['obwellid']==id1]
    label = df_well['obops_Code'].unique()
    y=df.groupby('obops_Code')['obtotalhrs'].sum()    
    chart = get_pieplot(y,label)   
    return render (request, 'obdrillingoperations/obdrilling_ops.html', {'obdrilling_opss': obdrilling_opss, 'chart':chart})   
 
def create_obdrilling_ops(request):     
    selectedwell = SelectedObserver.objects.all().first()
    obdrillingsum = OBDrillingSummary.objects.get(gpwellid=selectedwell.wellid)
    obdrilling_ops = OBDrillingOps() 
    drill =OBDrillingSummary.objects.get(wellid=selectedwell.wellid)
    obdrilling_ops.obdrillingid =obdrillingsum
    obdrilling_ops.fgId = selectedwell.fgid
    obdrilling_ops.wellid = selectedwell.wellid   
    form = OBDrillingOpsForm(request.POST or None, instance=obdrilling_ops)   
    if request.method =="POST":  
        form = OBDrillingOpsForm(request.POST, instance=obdrilling_ops)       
        obdrilling_ops.fgId = selectedwell.fgid
        obdrilling_ops.wellid = selectedwell.wellid   
        obdrilling_ops.obdrillingid =obdrillingsum 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()         
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')            
            return render (request, 'obdrillingoperations/obdrilling_ops_form.html', {'form': form})       
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)             
        diff = abs((t2-t1).total_seconds()/360)    
        obdrilling_ops.totalhrs =round(diff,2)
        if form.is_valid():
           form.save()  
           return redirect ('obdrillingoperations:list_obdrilling_ops') 
    return render (request, 'obdrillingoperations/obdrilling_ops_form.html', {'form': form})

def update_obdrilling_ops(request, id):     
    obdrilling_ops = OBDrillingOps.objects.get(id=id)    
    ctid =(obdrilling_ops.obdrillingid).pk  
    drill =OBDrillingSummary.objects.get(id=ctid)    
    form = OBDrillingOpsForm(request.POST or None, instance=obdrilling_ops)  
    if request.method =="POST": 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()        
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')           
            return render (request, 'obdrillingoperations/obdrilling_ops_update_form.html', {'form': form, 'id':id}) 
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)
        diff = (t2-t1).total_seconds()/3600         
        obdrilling_ops.totalhrs = round(diff,2)         
        form = OBDrillingOpsForm(request.POST, instance=obdrilling_ops)
        if form.is_valid():            
            form.save() 
            return redirect ('obdrillingoperations:list_obdrilling_ops')
    return render (request, 'obdrillingoperations/obdrilling_ops_update_form.html', {'form': form, 'obdrilling_ops':obdrilling_ops, 'id':id})


def delete_obdrilling_ops(request, id):
    obdrilling_ops = OBDrillingOps.objects.get(id=id)  
    if request.method == 'POST' :
        obdrilling_ops.delete()
        return redirect ('obdrillingoperations:list_obdrilling_ops')
    return render (request, 'obdrillingoperations/obdrilling_ops_confirm_delete.html', {'obdrilling_ops':obdrilling_ops, 'id':id})




