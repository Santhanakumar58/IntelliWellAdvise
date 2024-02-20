from datetime import datetime, timedelta
import time
import sqlite3
from django.shortcuts import render, redirect
import pandas as pd
from selectedGasProducer.models import SelectedGasProducer
from gpcoiltubing.models import GPCoiltubing
from .models import GPCoiltubingOperation
from .forms import GPCoiltubingOpsForm
from .utils import get_pieplot
from django.contrib import messages

def list_gpcoil_tubing_ops_data(request, ctid): 
    print(ctid)
    selectedwell = SelectedGasProducer.objects.all().first()
    gpcoil_tubing_ops_datas = GPCoiltubingOperation.objects.filter(wellid = selectedwell.wellid, gpcoiltubingid =ctid).all()  
    cnx = sqlite3.connect('db.sqlite3', check_same_thread=False)    
    ops = pd.read_sql_query("select * from gpcoiltubingoperations_CoiltubingOperation", cnx)   
    cnx.close() 
    df = pd.DataFrame(ops)
    df_well = df[df['wellid']==selectedwell.wellid]
    label = df_well['op_code'].unique()
    y=df.groupby('op_code')['totalhrs'].sum()    
    chart = get_pieplot(y,label)   
    return render (request, 'gpcoiltubingoperations/gpcoil_tubing_ops_data.html', {'gpcoil_tubing_ops_datas': gpcoil_tubing_ops_datas,'chart':chart, 'ctid':ctid})   
 
def create_gpcoil_tubing_ops_data(request, ctid):
    gpcoil_tubing_data = GPCoiltubing.objects.get(id=ctid)
    gpcoil_tubing_ops_data = GPCoiltubingOperation()   
    gpcoil_tubing_ops_data.gpcoiltubingid =gpcoil_tubing_data
    gpcoil_tubing_ops_data.fgid = gpcoil_tubing_data.fgid
    gpcoil_tubing_ops_data.wellid = gpcoil_tubing_data.wellid   
    form = GPCoiltubingOpsForm(request.POST or None, instance=gpcoil_tubing_ops_data)
    if request.method =="POST":  
         form = GPCoiltubingOpsForm(request.POST, request.FILES, instance=gpcoil_tubing_ops_data)       
         gpcoil_tubing_ops_data.fgid = gpcoil_tubing_data.fgid
         gpcoil_tubing_ops_data.wellid = gpcoil_tubing_data.wellid   
         gpcoil_tubing_ops_data.gpcoiltubingid =gpcoil_tubing_data 
         dat = request.POST['op_Date']
         dat1 = datetime.strptime(dat, "%Y-%m-%d")
         dat1=dat1.date()        
         if dat1 <gpcoil_tubing_data.start_Date or dat1 >gpcoil_tubing_data.end_Date:
            message = ( "The operation date falls outside the start and end date")
            print(message)
            return render (request, 'gpcoiltubingoperations/gpcoil_tubing_ops_data_form.html', {'form': form, 'message':message, 'ctid':ctid})   
         timefrom = request.POST['time_from'] 
         timeto = request.POST['time_to']
         t1 = pd.to_datetime(timefrom)
         t2 = pd.to_datetime(timeto)
         diff = (t2-t1).total_seconds()/3600         
         gpcoil_tubing_ops_data.totalhrs = round(diff,2) 
         if form.is_valid():
            form.save()  
            return redirect ('gpcoiltubingoperations:list_gpcoil_tubing_ops_data', ctid) 
    return render (request, 'gpcoiltubingoperations/gpcoil_tubing_ops_data_form.html', {'form': form,   'ctid':ctid})

def update_gpcoil_tubing_ops_data(request, id):  
    gpcoil_tubing_ops_data = GPCoiltubingOperation.objects.get(id=id) 
    ctid =(gpcoil_tubing_ops_data.gpcoiltubingid).pk  
    gpcoil_tubing_data =GPCoiltubing.objects.get(id=ctid)
    form = GPCoiltubingOpsForm(request.POST or None, instance=gpcoil_tubing_ops_data)    
    if request.method =="POST":
        dat = (datetime.strptime(request.POST['op_Date'], '%Y-%m-%d'))         
        dat111=gpcoil_tubing_data.start_Date
        dat1= datetime.combine(gpcoil_tubing_data.start_Date, datetime.min.time())        
        dat2=  datetime.combine(gpcoil_tubing_data.end_Date, datetime.min.time()) 
        if (dat < dat1 or dat >dat2):
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {gpcoil_tubing_data.start_Date}  and End Date {gpcoil_tubing_data.end_Date}')           
            return render (request, 'gpcoiltubingoperations/gpcoil_tubing_ops_data_update_form.html', {'form': form, 'gpcoil_tubing_ops_data':gpcoil_tubing_ops_data, 'id':id})
        timefrom = request.POST['time_from']
        timeto = request.POST['time_to']  
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)        
        diff =(t2-t1).total_seconds()/3600   
        gpcoil_tubing_ops_data.totalhrs = round(diff,2)
        form = GPCoiltubingOpsForm(request.POST, request.FILES, instance=gpcoil_tubing_ops_data)  
        ctid =(gpcoil_tubing_ops_data.gpcoiltubingid).pk      
        if form.is_valid():
            form.save()               
            return redirect ('gpcoiltubingoperations:list_gpcoil_tubing_ops_data', ctid)
    return render (request, 'gpcoiltubingoperations/gpcoil_tubing_ops_data_update_form.html', {'form': form, 'gpcoil_tubing_ops_data':gpcoil_tubing_ops_data, 'id':id})



def delete_gpcoil_tubing_ops_data(request, id):
    gpcoil_tubing_ops_data = GPCoiltubingOperation.objects.get(id=id)  
    ctid =(gpcoil_tubing_ops_data.gpcoiltubingid).pk   
    print(ctid)
    if request.method == 'POST' :
        gpcoil_tubing_ops_data.delete()
        ctid =(gpcoil_tubing_ops_data.gpcoiltubingid).pk
        return redirect ('gpcoiltubingoperations:list_gpcoil_tubing_ops_data', ctid)
    return render (request, 'gpcoiltubingoperations/gpcoil_tubing_ops_data_confirm_delete.html', {'gpcoil_tubing_ops_data':gpcoil_tubing_ops_data, 'id':id})


