from datetime import datetime, timedelta
import math
from django.shortcuts import render, redirect
from .models import WIDrillingOps
from .forms import WIDrillingOpsForm
from widrillingsummary.models import WIDrillingSummary
from selectedWaterInjector.models import SelectedWaterInjector
import numpy as np
import pandas as pd
import sqlite3
from .utils import get_pieplot
from django.contrib import messages

def list_widrilling_ops(request): 
    selectedwell = SelectedWaterInjector.objects.first()
    id1 = selectedwell.wellid 
    widrilling_opss = WIDrillingOps.objects.filter(wiwellid = id1).all()  
    cnx = sqlite3.connect('db.sqlite3', check_same_thread=False)    
    ops = pd.read_sql_query("select * from widrillingoperations_widrillingops", cnx)   
    cnx.close() 
    df = pd.DataFrame(ops)
    df_well = df[df['wiwellid']==id1]
    label = df_well['wiops_Code'].unique()
    y=df.groupby('wiops_Code')['witotalhrs'].sum()    
    chart = get_pieplot(y,label)   
    return render (request, 'widrillingoperations/widrilling_ops.html', {'widrilling_opss': widrilling_opss, 'chart':chart})   
 
def create_widrilling_ops(request):     
    selectedwell = SelectedWaterInjector.objects.all().first()
    widrillingsum = WIDrillingSummary.objects.get(gpwellid=selectedwell.wellid)
    widrilling_ops = WIDrillingOps() 
    drill =WIDrillingSummary.objects.get(wellid=selectedwell.wellid)
    widrilling_ops.widrillingid =widrillingsum
    widrilling_ops.fgId = selectedwell.fgid
    widrilling_ops.wellid = selectedwell.wellid   
    form = WIDrillingOpsForm(request.POST or None, instance=widrilling_ops)   
    if request.method =="POST":  
        form = WIDrillingOpsForm(request.POST, instance=widrilling_ops)       
        widrilling_ops.fgId = selectedwell.fgid
        widrilling_ops.wellid = selectedwell.wellid   
        widrilling_ops.widrillingid =widrillingsum 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()         
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')            
            return render (request, 'widrillingoperations/widrilling_ops_form.html', {'form': form})       
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)             
        diff = abs((t2-t1).total_seconds()/360)    
        widrilling_ops.totalhrs =round(diff,2)
        if form.is_valid():
           form.save()  
           return redirect ('widrillingoperations:list_widrilling_ops') 
    return render (request, 'widrillingoperations/widrilling_ops_form.html', {'form': form})

def update_widrilling_ops(request, id):     
    widrilling_ops = WIDrillingOps.objects.get(id=id)    
    ctid =(widrilling_ops.widrillingid).pk  
    drill =WIDrillingSummary.objects.get(id=ctid)    
    form = WIDrillingOpsForm(request.POST or None, instance=widrilling_ops)  
    if request.method =="POST": 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()        
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')           
            return render (request, 'widrillingoperations/widrilling_ops_update_form.html', {'form': form, 'id':id}) 
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)
        diff = (t2-t1).total_seconds()/3600         
        widrilling_ops.totalhrs = round(diff,2)         
        form = WIDrillingOpsForm(request.POST, instance=widrilling_ops)
        if form.is_valid():            
            form.save() 
            return redirect ('widrillingoperations:list_widrilling_ops')
    return render (request, 'widrillingoperations/widrilling_ops_update_form.html', {'form': form, 'widrilling_ops':widrilling_ops, 'id':id})


def delete_widrilling_ops(request, id):
    widrilling_ops = WIDrillingOps.objects.get(id=id)  
    if request.method == 'POST' :
        widrilling_ops.delete()
        return redirect ('widrillingoperations:list_widrilling_ops')
    return render (request, 'widrillingoperations/widrilling_ops_confirm_delete.html', {'widrilling_ops':widrilling_ops, 'id':id})




