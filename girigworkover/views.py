import math
from multiprocessing.connection import _ConnectionBase
from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasInjector.models import SelectedGasInjector
from .models import GIRigworkover
from .forms import GIRigworkoverForm
from .utils import get_plot, get_plot1
import datetime
import pandas as pd
import numpy as np
from django.db.models import Avg


# Create your views here.
def list_girig_workover_data(request):  
    selectedwell = SelectedGasInjector.objects.first()    
    girig_workover_datas = GIRigworkover.objects.filter(giwellid =selectedwell.wellid).all() 
    # for plot     
    girig_workover_datas = GIRigworkover.objects.filter(giwellid =selectedwell.wellid).all()  
    x=[x1.end_Date for x1 in girig_workover_datas] 
    y=[(y.post_wor_liquid-y.pre_wor_liquid) for y in girig_workover_datas]
    y1=[round((y1.post_wor_liquid * (1-y1.post_wor_WC/100)-y1.pre_wor_liquid * (1-y1.pre_wor_WC/100)),2) for y1 in girig_workover_datas]
    y2=[round((y2.post_wor_GOR * (y2.post_wor_liquid * (1-y2.post_wor_WC/100))/1000-y2.pre_wor_GOR * (y2.pre_wor_liquid * (1-y2.pre_wor_WC/100))/1000 ),2)  for y2 in girig_workover_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2)      
    return render (request, 'girigworkover1/girig_wor_data.html', {'girig_workover_datas': girig_workover_datas, 'chart':chart, 'avgliqgain':avgliqgain, 'avgoilgain':avgoilgain })   

def create_girig_workover_data(request):  
    selectedwell = SelectedGasInjector.objects.first()    
    girig_workover_data = GIRigworkover()  
    girig_workover_data.fgid = selectedwell.fgid
    girig_workover_data.wellid = selectedwell.wellid   
    form = GIRigworkoverForm(request.POST or None, instance=girig_workover_data)
    if request.method =="POST":  
        form = GIRigworkoverForm(request.POST, request.FILES, instance=girig_workover_data)       
        girig_workover_data.fgid = selectedwell.fgid
        girig_workover_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('girigworkover1:list_girig_workover_data') 
    return render (request, 'girigworkover1/girig_wor_data_form.html', {'form': form})

def update_girig_workover_data(request, id): 
    girig_workover_data = GIRigworkover.objects.get(id=id)  
    form = GIRigworkoverForm(request.POST or None, instance=girig_workover_data) 
    if request.method =="POST":
        form = GIRigworkoverForm(request.POST, request.FILES, instance=girig_workover_data)        
        if form.is_valid():
            form.save()           
            return redirect ('girigworkover1:list_girig_workover_data')
    return render (request, 'girigworkover1/girig_wor_data_form.html', {'form': form, 'girig_workover_data':girig_workover_data})

def delete_girig_workover_data(request, id):
    girig_workover_data = GIRigworkover.objects.get(id=id)   
    if request.method == 'POST' :
        girig_workover_data.delete()
        return redirect ('girigworkover1:list_girig_workover_data')
    return render (request, 'girigworkover1/girig_wor_data_confirm_delete.html', {'girig_workover_data':girig_workover_data})

def detail_girig_workover_data(request, id): 
    oilgain =0
    selectedwell = SelectedGasInjector.objects.first()    
    girig_workover_data = GIRigworkover.objects.get(id=id)
    preliquid = girig_workover_data.pre_wor_liquid  
    postliquid = girig_workover_data.post_wor_liquid
    liquidgain = postliquid-preliquid
    prewater = girig_workover_data.pre_wor_WC  
    postwater = girig_workover_data.post_wor_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*girig_workover_data.pre_wor_GOR)/1000
    postgas = round(postoil * girig_workover_data.post_wor_GOR)/1000
    expoil = round(girig_workover_data.expected_liquid *(1-girig_workover_data.expected_WC/100) ,2)
    expgas = round(expoil * girig_workover_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = girig_workover_data.pre_wor_GOR 
    postgor = girig_workover_data.post_wor_GOR
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
    dat= girig_workover_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  

    form = GIRigworkoverForm(request.POST or None, instance=girig_workover_data) 
    return render (request, 'girigworkover1/girig_wor_data_detail.html', {'form': form, 'girig_workover_data':girig_workover_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})

def intervention_home(request):
   
   return render (request, 'girigworkover1/giintervention_home.html', {})
         
