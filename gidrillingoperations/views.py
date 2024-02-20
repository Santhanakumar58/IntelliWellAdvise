from datetime import datetime, timedelta
import math
from django.shortcuts import render, redirect
from .models import GIDrillingOps
from .forms import GIDrillingOpsForm
from gidrillingsummary.models import GIDrillingSummary
from selectedGasProducer.models import SelectedGasProducer
import numpy as np
import pandas as pd
import sqlite3
from .utils import get_pieplot
from django.contrib import messages

def list_gidrilling_ops(request): 
    selectedwell = SelectedGasProducer.objects.first()
    id1 = selectedwell.wellid 
    gidrilling_opss = GIDrillingOps.objects.filter(giwellid = id1).all()  
    cnx = sqlite3.connect('db.sqlite3', check_same_thread=False)    
    ops = pd.read_sql_query("select * from gidrillingoperations_gidrillingops", cnx)   
    cnx.close() 
    df = pd.DataFrame(ops)
    df_well = df[df['giwellid']==id1]
    label = df_well['giops_Code'].unique()
    y=df.groupby('giops_Code')['gitotalhrs'].sum()    
    chart = get_pieplot(y,label)   
    return render (request, 'gidrillingoperations/gidrilling_ops.html', {'gidrilling_opss': gidrilling_opss, 'chart':chart})   
 
def create_gidrilling_ops(request):     
    selectedwell = SelectedGasProducer.objects.all().first()
    gidrillingsum = GIDrillingSummary.objects.get(gpwellid=selectedwell.wellid)
    gidrilling_ops = GIDrillingOps() 
    drill =GIDrillingSummary.objects.get(wellid=selectedwell.wellid)
    gidrilling_ops.gidrillingid =gidrillingsum
    gidrilling_ops.fgId = selectedwell.fgid
    gidrilling_ops.wellid = selectedwell.wellid   
    form = GIDrillingOpsForm(request.POST or None, instance=gidrilling_ops)   
    if request.method =="POST":  
        form = GIDrillingOpsForm(request.POST, instance=gidrilling_ops)       
        gidrilling_ops.fgId = selectedwell.fgid
        gidrilling_ops.wellid = selectedwell.wellid   
        gidrilling_ops.gidrillingid =gidrillingsum 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()         
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')            
            return render (request, 'gidrillingoperations/gidrilling_ops_form.html', {'form': form})       
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)             
        diff = abs((t2-t1).total_seconds()/360)    
        gidrilling_ops.totalhrs =round(diff,2)
        if form.is_valid():
           form.save()  
           return redirect ('gidrillingoperations:list_gidrilling_ops') 
    return render (request, 'gidrillingoperations/gidrilling_ops_form.html', {'form': form})

def update_gidrilling_ops(request, id):     
    gidrilling_ops = GIDrillingOps.objects.get(id=id)    
    ctid =(gidrilling_ops.gidrillingid).pk  
    drill =GIDrillingSummary.objects.get(id=ctid)    
    form = GIDrillingOpsForm(request.POST or None, instance=gidrilling_ops)  
    if request.method =="POST": 
        dat = request.POST['ops_Date']
        dat1 = datetime.strptime(dat, "%Y-%m-%d")
        dat1=dat1.date()        
        if dat1 <drill.start_Date or dat1 >drill.end_Date:
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {drill.start_Date}  and End Date {drill.end_Date}')           
            return render (request, 'gidrillingoperations/gidrilling_ops_update_form.html', {'form': form, 'id':id}) 
        timefrom = request.POST['time_From'] 
        timeto = request.POST['time_To']
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)
        diff = (t2-t1).total_seconds()/3600         
        gidrilling_ops.totalhrs = round(diff,2)         
        form = GIDrillingOpsForm(request.POST, instance=gidrilling_ops)
        if form.is_valid():            
            form.save() 
            return redirect ('gidrillingoperations:list_gidrilling_ops')
    return render (request, 'gidrillingoperations/gidrilling_ops_update_form.html', {'form': form, 'gidrilling_ops':gidrilling_ops, 'id':id})


def delete_gidrilling_ops(request, id):
    gidrilling_ops = GIDrillingOps.objects.get(id=id)  
    if request.method == 'POST' :
        gidrilling_ops.delete()
        return redirect ('gidrillingoperations:list_gidrilling_ops')
    return render (request, 'gidrillingoperations/gidrilling_ops_confirm_delete.html', {'gidrilling_ops':gidrilling_ops, 'id':id})




