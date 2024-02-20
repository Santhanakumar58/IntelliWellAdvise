from django.shortcuts import render, redirect
from .models import GasLiftModel
from .forms import GasLiftForm
from selectedOilProducer.models import SelectedOilProducer
from selectedfgi.models import Selectedfgi
from .utils import *
import pandas as pd
import numpy as np
import os
from django.core.files.storage import FileSystemStorage
from wellcompletion.models import Wellcompletion
from perforations.models import PerforationModel
import psapy.BeggsandBrill as BB
import psapy.Hagendornandbrown as HB
from opinflow.models import ProductivityIndexModel, DarcyModel, WigginsModel, VogelModel, StandingsModel, MultirateModel
from opinflow.utility import draw_CompositePR_PI, draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins
from flowtest.models import FlowTestModel
import json


# Create your views here.
def list_gas_lift(request):     
    well = SelectedOilProducer.objects.all().first()  
    gasliftdatas = GasLiftModel.objects.filter(wellid=well.wellid).order_by("-design_Date")  
    latestdata = gasliftdatas.first()
    if latestdata:
        flowtests = FlowTestModel.objects.filter(wellid=well.wellid).order_by("-test_Date")     
        flowtestdata = FlowTestModel.objects.all().filter(wellid=well.wellid).order_by("test_Date")    
        perfortaions = PerforationModel.objects.filter(wellid=well.wellid).all().order_by('-perf_Top') 
        perforation = perfortaions.first()  
        completions = Wellcompletion.objects.filter(wellid=well.wellid).all() 
        total_depth = (perforation.perf_Top + perforation.perf_Bottom)/2   
        wellhead_pressure=latestdata.th_Pres
        Pcs = latestdata.gas_Inj_Pres
        Pko = latestdata.kick_Off_Pres
        Glf =0.4
        Gs = latestdata.kill_Fluid_Grad
        Q =latestdata.design_Liquid
        BHSP=3000
        J = 3
        Tre = 128
        Ts= latestdata.th_Temp
        R=0.1534

        df,Pwf,Pwh1,Pwh2,Pcs,Pko,total_depth,reservoir_line = gaslift_design_function(total_depth,wellhead_pressure, Pcs ,Pko,Glf,Gs,Q,BHSP,J,Tre,Ts,R)
        print(df)    
        chart = get_gaslift_design_plot(df,Pwf,Pwh1,Pwh2,Pcs,Pko,total_depth,reservoir_line)        
        return render (request, 'gaslift/gaslift.html', {'gasliftdatas': gasliftdatas, 'chart':chart, 'df':df })
    else:
         return render (request, 'gaslift/gaslift.html', {'gasliftdatas': gasliftdatas})

def create_gas_lift(request):
    gasliftdata = GasLiftModel()
    selectedwell = SelectedOilProducer.objects.first()  
    selectfgi = Selectedfgi.objects.first()    
    gasliftdata.fgId = selectedwell.fgid
    gasliftdata.wellid = selectedwell.wellid  
    form = GasLiftForm(request.POST or None, instance=gasliftdata)
    if request.method =="POST":  
        form = GasLiftForm(request.POST, request.FILES, instance=gasliftdata)  
    if form.is_valid():
        form.save()
        return redirect ('gaslift:list_gas_lift')
    return render (request, 'gaslift/gaslift_form.html', {'form': form})

def update_gas_lift(request, id):
   gasliftdata = GasLiftModel.objects.get(id=id)
   form = GasLiftForm(request.POST or None, instance=gasliftdata)
   if form.is_valid():
       form.save()
       return redirect ('gaslift:list_gas_lift')
   return render (request, 'gaslift/gaslift_form.html', {'form': form, 'gasliftdata':gasliftdata})

def delete_gas_lift(request, id):
   gasliftdata = GasLiftModel.objects.get(id=id)   
   if request.method == 'POST' :
       gasliftdata.delete()
       return redirect ('gaslift:list_gas_lift')
   return render (request, 'gaslift/gaslift_confirm_delete.html', {'gasliftdata':gasliftdata})


def design_gas_lift(request, id): 
    latestdata = GasLiftModel.objects.get(id=id)
    if latestdata:
        flowtests = FlowTestModel.objects.filter(wellid=latestdata.wellid).order_by("-test_Date")     
        flowtestdata = FlowTestModel.objects.all().filter(wellid=latestdata.wellid).order_by("test_Date")    
        perfortaions = PerforationModel.objects.filter(wellid=latestdata.wellid).all().order_by('-perf_Top') 
        perforation = perfortaions.first()  
        completions = Wellcompletion.objects.filter(wellid=latestdata.wellid).all() 
        total_depth = (perforation.perf_Top + perforation.perf_Bottom)/2   
        wellhead_pressure=latestdata.th_Pres
        Pcs = latestdata.gas_Inj_Pres
        Pko = latestdata.kick_Off_Pres
        Glf =0.4
        Gs = latestdata.kill_Fluid_Grad
        Q =latestdata.design_Liquid
        BHSP=2000
        J = 3
        Tre = 128
        Ts= latestdata.th_Temp
        R=0.1534
        df,Pwf,Pwh1,Pwh2,Pcs,Pko,total_depth,reservoir_line = gaslift_design_function(total_depth,wellhead_pressure, Pcs ,Pko,Glf,Gs,Q,BHSP,J,Tre,Ts,R)
        json_records = df.reset_index().to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        context = {'d': data}         
        chart = get_gaslift_design_plot(df,Pwf,Pwh1,Pwh2,Pcs,Pko,total_depth,reservoir_line)        
        return render (request, 'gaslift/gaslift_design.html', {'latestdata': latestdata, 'chart':chart, "df":df })
    else:
         return render (request, 'gaslift/gaslift.html', {'latestdata': latestdata})