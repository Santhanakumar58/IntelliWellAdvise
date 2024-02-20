import math
from multiprocessing.connection import _ConnectionBase
from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedObserver.models import SelectedObserver
from .models import OBRigworkover
from .forms import OBRigworkoverForm
from .utils import get_plot, get_plot1
import datetime
import pandas as pd
import numpy as np
from django.db.models import Avg


# Create your views here.
def list_obrig_workover_data(request):  
    selectedwell = SelectedObserver.objects.first()    
    obrig_workover_datas = OBRigworkover.objects.filter(obwellid =selectedwell.wellid).all() 
    # for plot     
    obrig_workover_datas = OBRigworkover.objects.filter(obwellid =selectedwell.wellid).all()  
    x=[x1.end_Date for x1 in obrig_workover_datas] 
    y=[(y.post_wor_liquid-y.pre_wor_liquid) for y in obrig_workover_datas]
    y1=[round((y1.post_wor_liquid * (1-y1.post_wor_WC/100)-y1.pre_wor_liquid * (1-y1.pre_wor_WC/100)),2) for y1 in obrig_workover_datas]
    y2=[round((y2.post_wor_GOR * (y2.post_wor_liquid * (1-y2.post_wor_WC/100))/1000-y2.pre_wor_GOR * (y2.pre_wor_liquid * (1-y2.pre_wor_WC/100))/1000 ),2)  for y2 in obrig_workover_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2)      
    return render (request, 'obrigworkover/obrig_wor_data.html', {'obrig_workover_datas': obrig_workover_datas, 'chart':chart, 'avgliqgain':avgliqgain, 'avgoilgain':avgoilgain })   

def create_obrig_workover_data(request):  
    selectedwell = SelectedObserver.objects.first()    
    obrig_workover_data = OBRigworkover()  
    obrig_workover_data.fgid = selectedwell.fgid
    obrig_workover_data.wellid = selectedwell.wellid   
    form = OBRigworkoverForm(request.POST or None, instance=obrig_workover_data)
    if request.method =="POST":  
        form = OBRigworkoverForm(request.POST, request.FILES, instance=obrig_workover_data)       
        obrig_workover_data.fgid = selectedwell.fgid
        obrig_workover_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('obrigworkover:list_obrig_workover_data') 
    return render (request, 'obrigworkover/obrig_wor_data_form.html', {'form': form})

def update_obrig_workover_data(request, id): 
    obrig_workover_data = OBRigworkover.objects.get(id=id)  
    form = OBRigworkoverForm(request.POST or None, instance=obrig_workover_data) 
    if request.method =="POST":
        form = OBRigworkoverForm(request.POST, request.FILES, instance=obrig_workover_data)        
        if form.is_valid():
            form.save()           
            return redirect ('obrigworkover:list_obrig_workover_data')
    return render (request, 'obrigworkover/obrig_wor_data_form.html', {'form': form, 'obrig_workover_data':obrig_workover_data})

def delete_obrig_workover_data(request, id):
    obrig_workover_data = OBRigworkover.objects.get(id=id)   
    if request.method == 'POST' :
        obrig_workover_data.delete()
        return redirect ('obrigworkover:list_obrig_workover_data')
    return render (request, 'obrigworkover/obrig_wor_data_confirm_delete.html', {'obrig_workover_data':obrig_workover_data})

def detail_obrig_workover_data(request, id): 
    oilgain =0
    selectedwell = SelectedObserver.objects.first()    
    obrig_workover_data = OBRigworkover.objects.get(id=id)
    preliquid = obrig_workover_data.pre_wor_liquid  
    postliquid = obrig_workover_data.post_wor_liquid
    liquidgain = postliquid-preliquid
    prewater = obrig_workover_data.pre_wor_WC  
    postwater = obrig_workover_data.post_wor_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*obrig_workover_data.pre_wor_GOR)/1000
    postgas = round(postoil * obrig_workover_data.post_wor_GOR)/1000
    expoil = round(obrig_workover_data.expected_liquid *(1-obrig_workover_data.expected_WC/100) ,2)
    expgas = round(expoil * obrig_workover_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = obrig_workover_data.pre_wor_GOR 
    postgor = obrig_workover_data.post_wor_GOR
    gorgain = postgor-pregorr  
    if liquidgain>0:
        status = True
    else:
        status = False
    if watergain <=0:
        status1 = True
    else:
        status1 = False
    if gorgain <=0:
        status2 = True
    else:
        status2 = False
    if oilgain >=0:
        status3 = True
    else:
        status3 = False
    if gasgain >=0:
        status4 = True
    else:
        status4 = False

   # for plot 
    x1='Liquid'
    x2='Oil'
    x3='Gas'
    y1= liquidgain
    y2=oilgain
    y3=gasgain 
    dat= obrig_workover_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  

    form = OBRigworkoverForm(request.POST or None, instance=obrig_workover_data) 
    return render (request, 'obrigworkover1/obrig_wor_data_detail.html', {'form': form, 'obrig_workover_data':obrig_workover_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})

def intervention_home(request):
   
   return render (request, 'obrigworkover/obintervention_home.html', {})
         

