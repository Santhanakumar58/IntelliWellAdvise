from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from .forms import JetPumpDesignForm
from .utils import *
#get_ipr_plot, calculate_jetpump, calculate_inflow, Hagedorn_Brown, get_pressure_depth_plot, Orkiszewski, Beggs_Brill,Fancher_Brown, Duns_Ros, 
#calculate_oil_viscosity, get_viscosity_plot
from .models import JetPumpDesignModel
from blackoilpvt.models import BlackoilPVT
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity, get_Rs
from selectedOilProducer.models import SelectedOilProducer

import pandas as pd
from wellcompletion.models import Wellcompletion
from perforations.models import PerforationModel
from deviationsurveydata.models import Deviationsurveydata
import psapy.BeggsandBrill as BB
import psapy.Hagendornandbrown as HB
import psapy.FluidProps, psapy.GasProp
import math
import numpy as np

# Create your views here.
def list_jetpump_design_data(request):
    selectedwell = SelectedOilProducer.objects.first()   
    jetdatas = JetPumpDesignModel.objects.filter(wellid =selectedwell.wellid).all().order_by('-design_Date')  
    jetdata= jetdatas.first()   
    #inflowdf, x1, y1, pip =calculate_inflow(espdata)
    #chart = get_ipr_plot(inflowdf, espdata, x1, y1)    
    #q,q1,q2,head,eff,power, rangex, rangey, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead= Generate_pump_curves(espdata)
    #chart1= get_esp_plot1(q,q1,q2,head,eff,power, rangex, rangey, pump_name)
    #chart2= get_esp_plot2(q,head, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead)
    #chart3 = vlp_curve_for_esp(espdata)    
    return render (request, 'jetpumpdesign/jet_design_data.html', {'jetdatas': jetdatas   })   
 
def create_jetpump_design_data(request):    
    jetdata = JetPumpDesignModel()
    selectedwell = SelectedOilProducer.objects.first()  
    jetdata.fgid = selectedwell.fgid
    jetdata.wellid = selectedwell.wellid 
    form = JetPumpDesignForm(request.POST or None, instance=jetdata)
    tdh =0
    if request.method =="POST":  
         form = JetPumpDesignForm(request.POST, request.FILES, instance=jetdata)       
         jetdata.fgid = selectedwell.fgid
         jetdata.wellid = selectedwell.wellid                       
         if form.is_valid(): 
            form.save()  
            return redirect ('jetpumpdesign:list_jetpump_design_data') 
    return render (request, 'jetpumpdesign/jet_design_data_form.html', {'form': form})

def update_jetpump_design_data(request, id): 
   jetdata = JetPumpDesignModel.objects.get(id=id)  
   form = JetPumpDesignForm(request.POST or None, instance=jetdata)   
   if request.method =="POST":
        form = JetPumpDesignForm(request.POST, request.FILES, instance=jetdata)        
        if form.is_valid():            
            form.save() 
            return redirect ('jetpumpdesign:list_jetpump_design_data')
   return render (request, 'jetpumpdesign/jet_design_data_form.html', {'form': form, 'jetdata':jetdata})

def delete_jetpump_design_data(request, id):
   jetdata = JetPumpDesignModel.objects.get(id=id)   
   if request.method == 'POST' :
       jetdata.delete()
       return redirect ('jetpumpdesign:list_jetpump_design_data')
   return render (request, 'jetpumpdesign/jet_design_data_confirm_delete.html', {'jetdata':jetdata})

def jetpump_design(request, id):
    jetdata = JetPumpDesignModel.objects.get(id=id)  
    form = JetPumpDesignForm(request.POST or None, instance=jetdata) 
    inflowdf, x1, y1, pip = calculate_inflow(jetdata)
    chart, p1, p2, p3,q1,pump,horsepower,maxeff,m = calculate_jetpump(jetdata)
    chart1 = get_ipr_plot(inflowdf, jetdata, x1, y1)
    well_Depth = 5000
    tbg_Dia=1.9
    liquid_Rate =300
    gas_Oil_Ratio=700
    th_Pres =100
    oil_API =35
    water_Cut =50
    spgr_Water = 1.01
    th_Temp=120
    spgr_Gas =0.7
    wat_Salility=10000
    moleH2S =0
    moleCO2=0
    res_Temp=210
    selectedwell = SelectedOilProducer.objects.first()
    perfortaions = PerforationModel.objects.filter(wellid=selectedwell.wellid).all().order_by('-perf_Top') 
    perforation = perfortaions.first()
    midperf = (perforation.perf_Top + perforation.perf_Bottom)/2

    #delh = Hagedorn_and_Brown(well_Depth, liquid_Rate, gas_Oil_Ratio, th_Pres, oil_API, water_Cut, spgr_Water, th_Temp, spgr_Gss, tbg_Dia, wat_Salility)
    #inflowdf, x1, y1, pip =calculate_inflow(espdata)
    #chart = get_ipr_plot(inflowdf, espdata, x1, y1)    
    #q,q1,q2,head,eff,power, rangex, rangey, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead= Generate_pump_curves(espdata)
    #chart1= get_esp_plot1(q,q1,q2,head,eff,power, rangex, rangey, pump_name)
    #chart2= get_esp_plot2(q,head, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead)
    #chart3 = vlp_curve_for_esp(espdata)
    viscosity = []
    api=[]
    dead_viscosity=[]    
    viscosity1 = []    
    dead_viscosity1=[]
    for i in range(10, 50):
        vis, dead = calculate_oil_viscosity_Beal(i, 250,751)
        vis1, dead1 = calculate_oil_viscosity_Beggs(i, 250,751)         
        api.append(i)
        dead_viscosity.append(dead)
        dead_viscosity1.append(dead1)
        viscosity.append(vis) 
        viscosity1.append(vis1)

    vis, dead = calculate_oil_viscosity_Beal(47.1, 250,751)
    vis1, dead1 = calculate_oil_viscosity_Beggs(47.1, 250,751)         
    chart3=get_viscosity_plot(api, viscosity,dead_viscosity,viscosity1,dead_viscosity1 )
    pressures, depths=Hagedorn_Brown(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2 )
    pressures1, depths1=Orkiszewski(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2 )
    pressures2, depths2 = Beggs_Brill(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2)
    pressures3, depths3 = Fancher_Brown(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2)
    pressures4, depths4 = Duns_Ros(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2)
    chart2 = get_pressure_depth_plot(pressures, depths, pressures1, depths1, pressures2, depths2, pressures3, depths3, pressures4, depths4)

    return render (request, 'jetpumpdesign/jet_design.html', {'jetdata':jetdata, 'form':form, 'chart':chart, 'chart1':chart1, 'pip':pip, 'p1':p1, 'p2':p2, 'p3':p3, 'q1':q1,'pump':pump, 
    'tbg_Dia': tbg_Dia, 'midperf':midperf, 'horsepower':horsepower, 'maxeff':maxeff, 'chart2':chart2, 'chart3': chart3})


 
