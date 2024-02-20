from datetime import datetime, timedelta
import math
from django.shortcuts import render, redirect
from .models import GPDrillingOps
from .forms import GPDrillingOpsForm
from gpdrillingsummaary.models import GPDrillingSummary
from selectedGasProducer.models import SelectedGasProducer
import numpy as np
import pandas as pd
import sqlite3
from .utils import get_pieplot
from django.contrib import messages

def list_gpdrilling_ops(request): 
    selectedwell = SelectedGasProducer.objects.first()
    id1 = selectedwell.wellid 
    gpdrilling_opss = GPDrillingOps.objects.filter(gpwellid = id1).all()  
    cnx = sqlite3.connect('db.sqlite3', check_same_thread=False)    
    ops = pd.read_sql_query("select * from gpdrillingoperations_gpdrillingops", cnx)   
    cnx.close() 
    df = pd.DataFrame(ops)
    df_well = df[df['gpwellid']==id1]
    label = df_well['gpops_Code'].unique()
    y=df.groupby('gpops_Code')['gptotalhrs'].sum()    
    chart = get_pieplot(y,label)   
    return render (request, 'gpdrillingoperations/gpdrilling_ops.html', {'gpdrilling_opss': gpdrilling_opss, 'chart':chart})   
 
def create_gpdrilling_ops(request):     
    selectedwell = SelectedGasProducer.objects.all().first()
    gpdrillingsum = GPDrillingSummary.objects.get(gpwellid=selectedwell.wellid)
    gpdrilling_ops = GPDrillingOps() 
    drill =GPDrillingSummary.objects.get(wellid=selectedwell.wellid)
    gpdrilling_ops.gpdrillingid =gpdrillingsum
    gpdrilling_ops.fgId = selectedwell.fgid
    gpdrilling_ops.wellid = selectedwell.wellid   
    form = GPDrillingOpsForm(request.POST or None, instance=gpdrilling_ops)   
    if request.method =="POST":  
        form = GPDrillingOpsForm(request.POST, instance=gpdrilling_ops)       
        gpdrilling_ops.fgId = selectedwell.fgid
        gpdrilling_ops.wellid = selectedwell.wellid   
        gpdrilling_ops.gpdrillingid =gpdrillingsum 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()         
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')            
            return render (request, 'gpdrillingoperations/gpdrilling_ops_form.html', {'form': form})       
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)             
        diff = abs((t2-t1).total_seconds()/360)    
        gpdrilling_ops.totalhrs =round(diff,2)
        if form.is_valid():
           form.save()  
           return redirect ('gpdrillingoperations:list_gpdrilling_ops') 
    return render (request, 'gpdrillingoperations/gpdrilling_ops_form.html', {'form': form})

def update_gpdrilling_ops(request, id):     
    gpdrilling_ops = GPDrillingOps.objects.get(id=id)    
    ctid =(gpdrilling_ops.gpdrillingid).pk  
    drill =GPDrillingSummary.objects.get(id=ctid)    
    form = GPDrillingOpsForm(request.POST or None, instance=gpdrilling_ops)  
    if request.method =="POST": 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()        
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')           
            return render (request, 'gpdrillingoperations/gpdrilling_ops_update_form.html', {'form': form, 'id':id}) 
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)
        diff = (t2-t1).total_seconds()/3600         
        gpdrilling_ops.totalhrs = round(diff,2)         
        form = GPDrillingOpsForm(request.POST, instance=gpdrilling_ops)
        if form.is_valid():            
            form.save() 
            return redirect ('gpdrillingoperations:list_gpdrilling_ops')
    return render (request, 'gpdrillingoperations/gpdrilling_ops_update_form.html', {'form': form, 'gpdrilling_ops':gpdrilling_ops, 'id':id})


def delete_gpdrilling_ops(request, id):
    gpdrilling_ops = GPDrillingOps.objects.get(id=id)  
    if request.method == 'POST' :
        gpdrilling_ops.delete()
        return redirect ('gpdrillingoperations:list_gpdrilling_ops')
    return render (request, 'gpdrillingoperations/gpdrilling_ops_confirm_delete.html', {'gpdrilling_ops':gpdrilling_ops, 'id':id})



