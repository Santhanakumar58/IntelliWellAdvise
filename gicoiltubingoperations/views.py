from datetime import datetime, timedelta
import time
import sqlite3
from django.shortcuts import render, redirect
import pandas as pd
from selectedGasInjector.models import SelectedGasInjector
from gicoiltubing.models import GICoiltubing
from .models import GICoiltubingOperation
from .forms import GICoiltubingOpsForm
from .utils import get_pieplot
from django.contrib import messages

def list_gicoil_tubing_ops_data(request, ctid): 
    print(ctid)
    selectedwell = SelectedGasInjector.objects.all().first()
    gicoil_tubing_ops_datas = GICoiltubingOperation.objects.filter(wellid = selectedwell.wellid, gicoiltubingid =ctid).all()  
    cnx = sqlite3.connect('db.sqlite3', check_same_thread=False)    
    ops = pd.read_sql_query("select * from gicoiltubingoperations_CoiltubingOperation", cnx)   
    cnx.close() 
    df = pd.DataFrame(ops)
    df_well = df[df['wellid']==selectedwell.wellid]
    label = df_well['op_code'].unique()
    y=df.groupby('op_code')['totalhrs'].sum()    
    chart = get_pieplot(y,label)   
    return render (request, 'gicoiltubingoperations/gicoil_tubing_ops_data.html', {'gicoil_tubing_ops_datas': gicoil_tubing_ops_datas,'chart':chart, 'ctid':ctid})   
 
def create_gicoil_tubing_ops_data(request, ctid):
    gicoil_tubing_data = GICoiltubing.objects.get(id=ctid)
    gicoil_tubing_ops_data = GICoiltubingOperation()   
    gicoil_tubing_ops_data.gicoiltubingid =gicoil_tubing_data
    gicoil_tubing_ops_data.fgid = gicoil_tubing_data.fgid
    gicoil_tubing_ops_data.wellid = gicoil_tubing_data.wellid   
    form = GICoiltubingOpsForm(request.POST or None, instance=gicoil_tubing_ops_data)
    if request.method =="POST":  
         form = GICoiltubingOpsForm(request.POST, request.FILES, instance=gicoil_tubing_ops_data)       
         gicoil_tubing_ops_data.fgid = gicoil_tubing_data.fgid
         gicoil_tubing_ops_data.wellid = gicoil_tubing_data.wellid   
         gicoil_tubing_ops_data.gicoiltubingid =gicoil_tubing_data 
         dat = request.POST['op_Date']
         dat1 = datetime.strptime(dat, "%Y-%m-%d")
         dat1=dat1.date()        
         if dat1 <gicoil_tubing_data.start_Date or dat1 >gicoil_tubing_data.end_Date:
            message = ( "The operation date falls outside the start and end date")
            print(message)
            return render (request, 'gicoiltubingoperations/gicoil_tubing_ops_data_form.html', {'form': form, 'message':message, 'ctid':ctid})   
         timefrom = request.POST['time_from'] 
         timeto = request.POST['time_to']
         t1 = pd.to_datetime(timefrom)
         t2 = pd.to_datetime(timeto)
         diff = (t2-t1).total_seconds()/3600         
         gicoil_tubing_ops_data.totalhrs = round(diff,2) 
         if form.is_valid():
            form.save()  
            return redirect ('gicoiltubingoperations:list_gicoil_tubing_ops_data', ctid) 
    return render (request, 'gicoiltubingoperations/gicoil_tubing_ops_data_form.html', {'form': form,   'ctid':ctid})

def update_gicoil_tubing_ops_data(request, id):  
    gicoil_tubing_ops_data = GICoiltubingOperation.objects.get(id=id) 
    ctid =(gicoil_tubing_ops_data.gicoiltubingid).pk  
    gicoil_tubing_data =GICoiltubing.objects.get(id=ctid)
    form = GICoiltubingOpsForm(request.POST or None, instance=gicoil_tubing_ops_data)    
    if request.method =="POST":
        dat = (datetime.strptime(request.POST['op_Date'], '%Y-%m-%d'))         
        dat111=gicoil_tubing_data.start_Date
        dat1= datetime.combine(gicoil_tubing_data.start_Date, datetime.min.time())        
        dat2=  datetime.combine(gicoil_tubing_data.end_Date, datetime.min.time()) 
        if (dat < dat1 or dat >dat2):
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {gicoil_tubing_data.start_Date}  and End Date {gicoil_tubing_data.end_Date}')           
            return render (request, 'gicoiltubingoperations/gicoil_tubing_ops_data_update_form.html', {'form': form, 'gicoil_tubing_ops_data':gicoil_tubing_ops_data, 'id':id})
        timefrom = request.POST['time_from']
        timeto = request.POST['time_to']  
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)        
        diff =(t2-t1).total_seconds()/3600   
        gicoil_tubing_ops_data.totalhrs = round(diff,2)
        form = GICoiltubingOpsForm(request.POST, request.FILES, instance=gicoil_tubing_ops_data)  
        ctid =(gicoil_tubing_ops_data.gicoiltubingid).pk      
        if form.is_valid():
            form.save()               
            return redirect ('gicoiltubingoperations:list_gicoil_tubing_ops_data', ctid)
    return render (request, 'gicoiltubingoperations/gicoil_tubing_ops_data_update_form.html', {'form': form, 'gicoil_tubing_ops_data':gicoil_tubing_ops_data, 'id':id})



def delete_gicoil_tubing_ops_data(request, id):
    gicoil_tubing_ops_data = GICoiltubingOperation.objects.get(id=id)  
    ctid =(gicoil_tubing_ops_data.gicoiltubingid).pk   
    print(ctid)
    if request.method == 'POST' :
        gicoil_tubing_ops_data.delete()
        ctid =(gicoil_tubing_ops_data.gicoiltubingid).pk
        return redirect ('gicoiltubingoperations:list_gicoil_tubing_ops_data', ctid)
    return render (request, 'gicoiltubingoperations/gicoil_tubing_ops_data_confirm_delete.html', {'gicoil_tubing_ops_data':gicoil_tubing_ops_data, 'id':id})


