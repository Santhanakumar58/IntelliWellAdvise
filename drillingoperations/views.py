from datetime import datetime, timedelta
import math
from django.shortcuts import render, redirect
from .models import DrillingOps
from .forms import DrillingOpsForm
from drillingsummary.models import DrillingSummary
from selectedOilProducer.models import SelectedOilProducer
import numpy as np
import pandas as pd
import sqlite3
from .utils import get_pieplot
from django.contrib import messages

def list_drilling_ops(request): 
    selectedwell = SelectedOilProducer.objects.first()
    id1 = selectedwell.wellid 
    drilling_opss = DrillingOps.objects.filter(wellid = id1).all()  
    cnx = sqlite3.connect('db.sqlite3', check_same_thread=False)    
    ops = pd.read_sql_query("select * from drillingoperations_drillingops", cnx)   
    cnx.close() 
    df = pd.DataFrame(ops)
    df_well = df[df['wellid']==id1]
    label = df_well['ops_Code'].unique()    
    y=df.groupby('ops_Code')['totalhrs'].sum()  
    label = df['ops_Code'].unique() 
    print(y)   
    chart = get_pieplot(y,y.index)   
    return render (request, 'drillingoperations/drilling_ops.html', {'drilling_opss': drilling_opss, 'chart':chart})   
 
def create_drilling_ops(request):     
    selectedwell = SelectedOilProducer.objects.all().first()
    drillingsum = DrillingSummary.objects.get(wellid=selectedwell.wellid)
    drilling_ops = DrillingOps() 
    drill =DrillingSummary.objects.get(wellid=selectedwell.wellid)
    drilling_ops.drillingid =drillingsum
    drilling_ops.fgId = selectedwell.fgid
    drilling_ops.wellid = selectedwell.wellid   
    form = DrillingOpsForm(request.POST or None, instance=drilling_ops)   
    if request.method =="POST":  
        #form = DrillingOpsForm(request.POST, instance=drilling_ops)       
        drilling_ops.fgId = selectedwell.fgid
        drilling_ops.wellid = selectedwell.wellid   
        drilling_ops.drillingid =drillingsum 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()         
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')            
            return render (request, 'drillingoperations/drilling_ops_form.html', {'form': form})       
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)   
        print(t1,t2)     
        diff = (t2-t1).total_seconds()/(3600)
        print(diff)
        if diff <0.0:
            diff = diff+24.0   
        print(diff)           
        drilling_ops.totalhrs =diff
        form = DrillingOpsForm(request.POST or None, instance=drilling_ops)
        if form.is_valid():
           print(drilling_ops.totalhrs)
           form.save()  
           return redirect ('drillingoperations:list_drilling_ops') 
    return render (request, 'drillingoperations/drilling_ops_form.html', {'form': form})

def update_drilling_ops(request, id):     
    drilling_ops = DrillingOps.objects.get(id=id)    
    ctid =(drilling_ops.drillingid).pk  
    drill =DrillingSummary.objects.get(id=ctid)    
    form = DrillingOpsForm(request.POST or None, instance=drilling_ops)  
    if request.method =="POST": 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()        
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')           
            return render (request, 'drillingoperations/drilling_ops_update_form.html', {'form': form, 'id':id}) 
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)
        print(t1,t2)
        diff = (t2-t1).total_seconds()/3600   
        if diff <0:
            diff = diff+24.0      
        drilling_ops.totalhrs = round(diff,2)         
        form = DrillingOpsForm(request.POST, instance=drilling_ops)
        if form.is_valid():            
            form.save() 
            return redirect ('drillingoperations:list_drilling_ops')
    return render (request, 'drillingoperations/drilling_ops_update_form.html', {'form': form, 'drilling_ops':drilling_ops, 'id':id})


def delete_drilling_ops(request, id):
    drilling_ops = DrillingOps.objects.get(id=id)  
    if request.method == 'POST' :
        drilling_ops.delete()
        return redirect ('drillingoperations:list_drilling_ops')
    return render (request, 'drillingoperations/drilling_ops_confirm_delete.html', {'drilling_ops':drilling_ops, 'id':id})


