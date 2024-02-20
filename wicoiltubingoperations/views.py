from datetime import datetime, timedelta
import time
import sqlite3
from django.shortcuts import render, redirect
import pandas as pd
from selectedWaterInjector.models import SelectedWaterInjector
from coiltubing.models import Coiltubing
from .models import WICoiltubingOperation
from .forms import WICoiltubingOpsForm
from .utils import get_pieplot
from django.contrib import messages

def list_wicoil_tubing_ops_data(request, ctid): 
    print(ctid)
    selectedwell = SelectedWaterInjector.objects.all().first()
    coil_tubing_ops_datas = WICoiltubingOperation.objects.filter(wiwellid = selectedwell.wellid, coiltubingid =ctid).all()  
    cnx = sqlite3.connect('db.sqlite3', check_same_thread=False)    
    ops = pd.read_sql_query("select * from coiltubingoperations_CoiltubingOperation", cnx)   
    cnx.close() 
    df = pd.DataFrame(ops)
    df_well = df[df['wellid']==selectedwell.wellid]
    label = df_well['op_code'].unique()
    y=df.groupby('op_code')['totalhrs'].sum()    
    chart = get_pieplot(y,label)   
    return render (request, 'wicoiltubingoperations/wicoil_tubing_ops_data.html', {'coil_tubing_ops_datas': coil_tubing_ops_datas,'chart':chart, 'ctid':ctid})   
 
def create_wicoil_tubing_ops_data(request, ctid):
    coil_tubing_data = Coiltubing.objects.get(id=ctid)
    coil_tubing_ops_data = WICoiltubingOperation()   
    coil_tubing_ops_data.coiltubingid =coil_tubing_data
    coil_tubing_ops_data.fgid = coil_tubing_data.fgid
    coil_tubing_ops_data.wellid = coil_tubing_data.wellid   
    form = WICoiltubingOpsForm(request.POST or None, instance=coil_tubing_ops_data)
    if request.method =="POST":  
         form = WICoiltubingOpsForm(request.POST, request.FILES, instance=coil_tubing_ops_data)       
         coil_tubing_ops_data.fgid = coil_tubing_data.fgid
         coil_tubing_ops_data.wellid = coil_tubing_data.wellid   
         coil_tubing_ops_data.coiltubingid =coil_tubing_data 
         dat = request.POST['op_Date']
         dat1 = datetime.strptime(dat, "%Y-%m-%d")
         dat1=dat1.date()        
         if dat1 <coil_tubing_data.start_Date or dat1 >coil_tubing_data.end_Date:
            message = ( "The operation date falls outside the start and end date")
            print(message)
            return render (request, 'wicoiltubingoperations/wicoil_tubing_ops_data_form.html', {'form': form, 'message':message, 'ctid':ctid})   
         timefrom = request.POST['time_from'] 
         timeto = request.POST['time_to']
         t1 = pd.to_datetime(timefrom)
         t2 = pd.to_datetime(timeto)
         diff = (t2-t1).total_seconds()/3600         
         coil_tubing_ops_data.totalhrs = round(diff,2) 
         if form.is_valid():
            form.save()  
            return redirect ('wicoiltubingoperations:list_wicoil_tubing_ops_data', ctid) 
    return render (request, 'wicoiltubingoperations/wicoil_tubing_ops_data_form.html', {'form': form,   'ctid':ctid})

def update_wicoil_tubing_ops_data(request, id):  
    coil_tubing_ops_data = WICoiltubingOperation.objects.get(id=id) 
    ctid =(coil_tubing_ops_data.coiltubingid).pk  
    coil_tubing_data =Coiltubing.objects.get(id=ctid)
    form = WICoiltubingOpsForm(request.POST or None, instance=coil_tubing_ops_data)    
    if request.method =="POST":
        dat = (datetime.strptime(request.POST['op_Date'], '%Y-%m-%d'))         
        dat111=coil_tubing_data.start_Date
        dat1= datetime.combine(coil_tubing_data.start_Date, datetime.min.time())        
        dat2=  datetime.combine(coil_tubing_data.end_Date, datetime.min.time()) 
        if (dat < dat1 or dat >dat2):
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {coil_tubing_data.start_Date}  and End Date {coil_tubing_data.end_Date}')           
            return render (request, 'wicoiltubingoperations/wicoil_tubing_ops_data_update_form.html', {'form': form, 'coil_tubing_ops_data':coil_tubing_ops_data, 'id':id})
        timefrom = request.POST['time_from']
        timeto = request.POST['time_to']  
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)        
        diff =(t2-t1).total_seconds()/3600   
        coil_tubing_ops_data.totalhrs = round(diff,2)
        form = WICoiltubingOpsForm(request.POST, request.FILES, instance=coil_tubing_ops_data)  
        ctid =(coil_tubing_ops_data.coiltubingid).pk      
        if form.is_valid():
            form.save()               
            return redirect ('wicoiltubingoperations:list_wicoil_tubing_ops_data', ctid)
    return render (request, 'wicoiltubingoperations/wicoil_tubing_ops_data_update_form.html', {'form': form, 'coil_tubing_ops_data':coil_tubing_ops_data, 'id':id})



def delete_wicoil_tubing_ops_data(request, id):
    coil_tubing_ops_data = WICoiltubingOperation.objects.get(id=id)  
    ctid =(coil_tubing_ops_data.coiltubingid).pk   
    print(ctid)
    if request.method == 'POST' :
        coil_tubing_ops_data.delete()
        ctid =(coil_tubing_ops_data.coiltubingid).pk
        return redirect ('wicoiltubingoperations:list_wicoil_tubing_ops_data', ctid)
    return render (request, 'wicoiltubingoperations/wicoil_tubing_ops_data_confirm_delete.html', {'coil_tubing_ops_data':coil_tubing_ops_data, 'id':id})


