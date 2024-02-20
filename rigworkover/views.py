import math
from multiprocessing.connection import _ConnectionBase
from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedOilProducer.models import SelectedOilProducer 
from .models import Rigworkover
from .forms import RigworkoverForm
from rigworkover.utils import get_plot, get_plot1
import datetime
import pandas as pd
import numpy as np
from django.db.models import Avg


# Create your views here.
def list_rig_workover_data(request):  
    selectedwell = SelectedOilProducer.objects.first()    
    rig_workover_datas = Rigworkover.objects.filter(wellid =selectedwell.wellid).all() 
    # for plot     
    rig_workover_datas = Rigworkover.objects.filter(wellid =selectedwell.wellid).all()  
    x=[x1.end_Date for x1 in rig_workover_datas] 
    y=[(y.post_wor_liquid-y.pre_wor_liquid) for y in rig_workover_datas]
    y1=[round((y1.post_wor_liquid * (1-y1.post_wor_WC/100)-y1.pre_wor_liquid * (1-y1.pre_wor_WC/100)),2) for y1 in rig_workover_datas]
    y2=[round((y2.post_wor_GOR * (y2.post_wor_liquid * (1-y2.post_wor_WC/100))/1000-y2.pre_wor_GOR * (y2.pre_wor_liquid * (1-y2.pre_wor_WC/100))/1000 ),2)  for y2 in rig_workover_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2)      
    return render (request, 'rigworkover/rig_wor_data.html', {'rig_workover_datas': rig_workover_datas, 'chart':chart, 'avgliqgain':avgliqgain, 'avgoilgain':avgoilgain })   

def create_rig_workover_data(request):  
    selectedwell = SelectedOilProducer.objects.first()    
    rig_workover_data = Rigworkover()  
    rig_workover_data.fgid = selectedwell.fgid
    rig_workover_data.wellid = selectedwell.wellid   
    form = RigworkoverForm(request.POST or None, instance=rig_workover_data)
    if request.method =="POST":  
        form = RigworkoverForm(request.POST, request.FILES, instance=rig_workover_data)       
        rig_workover_data.fgid = selectedwell.fgid
        rig_workover_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('rigworkover:list_rig_workover_data') 
    return render (request, 'rigworkover/rig_wor_data_form.html', {'form': form})

def update_rig_workover_data(request, id): 
    rig_workover_data = Rigworkover.objects.get(id=id)  
    form = RigworkoverForm(request.POST or None, instance=rig_workover_data) 
    if request.method =="POST":
        form = RigworkoverForm(request.POST, request.FILES, instance=rig_workover_data)        
        if form.is_valid():
            form.save()           
            return redirect ('rigworkover:list_rig_workover_data')
    return render (request, 'rigworkover/rig_wor_data_form.html', {'form': form, 'rig_workover_data':rig_workover_data})

def delete_rig_workover_data(request, id):
    rig_workover_data = Rigworkover.objects.get(id=id)   
    if request.method == 'POST' :
        rig_workover_data.delete()
        return redirect ('rigworkover:list_rig_workover_data')
    return render (request, 'rigworkover/rig_wor_data_confirm_delete.html', {'rig_workover_data':rig_workover_data})

def detail_rig_workover_data(request, id): 
    oilgain =0
    selectedwell = SelectedOilProducer.objects.first()    
    rig_workover_data = Rigworkover.objects.get(id=id)
    preliquid = rig_workover_data.pre_wor_liquid  
    postliquid = rig_workover_data.post_wor_liquid
    liquidgain = postliquid-preliquid
    prewater = rig_workover_data.pre_wor_WC  
    postwater = rig_workover_data.post_wor_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*rig_workover_data.pre_wor_GOR)/1000
    postgas = round(postoil * rig_workover_data.post_wor_GOR)/1000
    expoil = round(rig_workover_data.expected_liquid *(1-rig_workover_data.expected_WC/100) ,2)
    expgas = round(expoil * rig_workover_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = rig_workover_data.pre_wor_GOR 
    postgor = rig_workover_data.post_wor_GOR
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
    dat= rig_workover_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  

    form = RigworkoverForm(request.POST or None, instance=rig_workover_data) 
    return render (request, 'rigworkover/rig_wor_data_detail.html', {'form': form, 'rig_workover_data':rig_workover_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})

def intervention_home(request):
   
   return render (request, 'rigworkover/intervention_home.html', {})
         