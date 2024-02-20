from datetime import datetime, timedelta
import time
import sqlite3
from django.shortcuts import render, redirect
import pandas as pd
from selectedObserver.models import SelectedObserver
from obcoiltubing.models import OBCoiltubing
from .models import OBCoiltubingOperation
from .forms import OBCoiltubingOpsForm
from .utils import get_pieplot
from django.contrib import messages

def list_obcoil_tubing_ops_data(request, ctid): 
    print(ctid)
    selectedwell = SelectedObserver.objects.all().first()
    obcoil_tubing_ops_datas = OBCoiltubingOperation.objects.filter(wellid = selectedwell.wellid, obcoiltubingid =ctid).all()  
    cnx = sqlite3.connect('db.sqlite3', check_same_thread=False)    
    ops = pd.read_sql_query("select * from obcoiltubingoperations_CoiltubingOperation", cnx)   
    cnx.close() 
    df = pd.DataFrame(ops)
    df_well = df[df['wellid']==selectedwell.wellid]
    label = df_well['op_code'].unique()
    y=df.groupby('op_code')['totalhrs'].sum()    
    chart = get_pieplot(y,label)   
    return render (request, 'obcoiltubingoperations/obcoil_tubing_ops_data.html', {'obcoil_tubing_ops_datas': obcoil_tubing_ops_datas,'chart':chart, 'ctid':ctid})   
 
def create_obcoil_tubing_ops_data(request, ctid):
    obcoil_tubing_data = OBCoiltubing.objects.get(id=ctid)
    obcoil_tubing_ops_data = OBCoiltubingOperation()   
    obcoil_tubing_ops_data.obcoiltubingid =obcoil_tubing_data
    obcoil_tubing_ops_data.fgid = obcoil_tubing_data.fgid
    obcoil_tubing_ops_data.wellid = obcoil_tubing_data.wellid   
    form = OBCoiltubingOpsForm(request.POST or None, instance=obcoil_tubing_ops_data)
    if request.method =="POST":  
         form = OBCoiltubingOpsForm(request.POST, request.FILES, instance=obcoil_tubing_ops_data)       
         obcoil_tubing_ops_data.fgid = obcoil_tubing_data.fgid
         obcoil_tubing_ops_data.wellid = obcoil_tubing_data.wellid   
         obcoil_tubing_ops_data.obcoiltubingid =obcoil_tubing_data 
         dat = request.POST['op_Date']
         dat1 = datetime.strptime(dat, "%Y-%m-%d")
         dat1=dat1.date()        
         if dat1 <obcoil_tubing_data.start_Date or dat1 >obcoil_tubing_data.end_Date:
            message = ( "The operation date falls outside the start and end date")
            print(message)
            return render (request, 'obcoiltubingoperations/obcoil_tubing_ops_data_form.html', {'form': form, 'message':message, 'ctid':ctid})   
         timefrom = request.POST['time_from'] 
         timeto = request.POST['time_to']
         t1 = pd.to_datetime(timefrom)
         t2 = pd.to_datetime(timeto)
         diff = (t2-t1).total_seconds()/3600         
         obcoil_tubing_ops_data.totalhrs = round(diff,2) 
         if form.is_valid():
            form.save()  
            return redirect ('obcoiltubingoperations:list_obcoil_tubing_ops_data', ctid) 
    return render (request, 'obcoiltubingoperations/obcoil_tubing_ops_data_form.html', {'form': form,   'ctid':ctid})

def update_obcoil_tubing_ops_data(request, id):  
    obcoil_tubing_ops_data = OBCoiltubingOperation.objects.get(id=id) 
    ctid =(obcoil_tubing_ops_data.obcoiltubingid).pk  
    obcoil_tubing_data =OBCoiltubing.objects.get(id=ctid)
    form = OBCoiltubingOpsForm(request.POST or None, instance=obcoil_tubing_ops_data)    
    if request.method =="POST":
        dat = (datetime.strptime(request.POST['op_Date'], '%Y-%m-%d'))         
        dat111=obcoil_tubing_data.start_Date
        dat1= datetime.combine(obcoil_tubing_data.start_Date, datetime.min.time())        
        dat2=  datetime.combine(obcoil_tubing_data.end_Date, datetime.min.time()) 
        if (dat < dat1 or dat >dat2):
            messages.info(request, f'The operation date falls outside the start and end date!  Start Date {obcoil_tubing_data.start_Date}  and End Date {obcoil_tubing_data.end_Date}')           
            return render (request, 'obcoiltubingoperations/obcoil_tubing_ops_data_update_form.html', {'form': form, 'obcoil_tubing_ops_data':obcoil_tubing_ops_data, 'id':id})
        timefrom = request.POST['time_from']
        timeto = request.POST['time_to']  
        t1 = pd.to_datetime(timefrom)
        t2 = pd.to_datetime(timeto)        
        diff =(t2-t1).total_seconds()/3600   
        obcoil_tubing_ops_data.totalhrs = round(diff,2)
        form = OBCoiltubingOpsForm(request.POST, request.FILES, instance=obcoil_tubing_ops_data)  
        ctid =(obcoil_tubing_ops_data.obcoiltubingid).pk      
        if form.is_valid():
            form.save()               
            return redirect ('obcoiltubingoperations:list_obcoil_tubing_ops_data', ctid)
    return render (request, 'obcoiltubingoperations/obcoil_tubing_ops_data_update_form.html', {'form': form, 'obcoil_tubing_ops_data':obcoil_tubing_ops_data, 'id':id})



def delete_obcoil_tubing_ops_data(request, id):
    obcoil_tubing_ops_data = OBCoiltubingOperation.objects.get(id=id)  
    ctid =(obcoil_tubing_ops_data.obcoiltubingid).pk   
    print(ctid)
    if request.method == 'POST' :
        obcoil_tubing_ops_data.delete()
        ctid =(obcoil_tubing_ops_data.obcoiltubingid).pk
        return redirect ('obcoiltubingoperations:list_obcoil_tubing_ops_data', ctid)
    return render (request, 'obcoiltubingoperations/obcoil_tubing_ops_data_confirm_delete.html', {'obcoil_tubing_ops_data':obcoil_tubing_ops_data, 'id':id})



