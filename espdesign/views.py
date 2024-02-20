from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from .forms import ESPDesignForm
from .utils import get_plot, get_ipr_plot,get_esp_plot1, get_esp_plot2 , calculate_esp_parameters, calculate_inflow, Generate_pump_curves, vlp_curve_for_esp, find_head_when_rate_is_given
from .models import ESPDesignModel
from blackoilpvt.models import BlackoilPVT
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity, get_Rs
from opinflow.utility import draw_CompositePR_PI, draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins
from opinflow.models import ProductivityIndexModel, DarcyModel, WigginsModel, VogelModel, StandingsModel, MultirateModel
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
def list_esp_design_data(request):
    selectedwell = SelectedOilProducer.objects.first()   
    espdatas = ESPDesignModel.objects.filter(wellid =selectedwell.wellid).all().order_by('-design_Date')  
    espdata= espdatas.first()   
    inflowdf, x1, y1, pip =calculate_inflow(espdata)
    chart = get_ipr_plot(inflowdf, espdata, x1, y1)    
    q,q1,q2,head,eff,power, rangex, rangey, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead= Generate_pump_curves(espdata)
    chart1= get_esp_plot1(q,q1,q2,head,eff,power, rangex, rangey, pump_name)
    chart2= get_esp_plot2(q,head, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead)
    chart3 = vlp_curve_for_esp(espdata)    
    return render (request, 'espdesign/esp_design_data.html', {'espdatas': espdatas, 'chart':chart , 'chart1':chart1,'chart2':chart2, 'chart3':chart3 })   
 
def create_esp_design_data(request):    
    espdata = ESPDesignModel()
    selectedwell = SelectedOilProducer.objects.first()  
    espdata.fgid = selectedwell.fgid
    espdata.wellid = selectedwell.wellid 
    form = ESPDesignForm(request.POST or None, instance=espdata)
    tdh =0
    if request.method =="POST":  
         form = ESPDesignForm(request.POST, request.FILES, instance=espdata)       
         espdata.fgid = selectedwell.fgid
         espdata.wellid = selectedwell.wellid                       
         if form.is_valid():             
            #design_Liquid= request.POST.get('design_Liquid')
            #water_Cut= request.POST.get('water_Cut')
            #oil = design_Liquid*(1.0-int(water_Cut)/100) 
            #water = design_Liquid*(water_Cut/100)  
            #gor=request.POST.get('gas_Oil_Ratio')
            #gas = oil* gor
            #pvt_Well= request.POST.get('pvt_Well')
            #pvt = BlackoilPVT.objects.filter(wellName =pvt_Well).last()
            #th_pres = request.POST.get('th_Pres') 
            #th_temp = request.POST.get('th_Temp')  
            #respres = request.POST.get('curr_Res_Pres')  
            #min_Pwf = request.POST.get('min_Pwf') 
            #water_spgr = request.POST.get('water_spgr')   
            #pump_depth = request.POST.get('pump_depth')   
            #selectedwell = SelectedOilProducer.objects.first()  
            #result= calculate_esp_parameters(selectedwell,design_Liquid, oil, water,gas,gor, pvt_Well,th_pres, th_temp, respres,min_pwf,water_spgr, pump_depth )
            #tdh=result[0]
            #pip=result[1]
            #print(tdh)
            form.save()  
            return redirect ('espdesign:list_esp_design_data') 
    return render (request, 'espdesign/esp_design_data_form.html', {'form': form})

def update_esp_design_data(request, id): 
   espdata = ESPDesignModel.objects.get(id=id)  
   form = ESPDesignForm(request.POST or None, instance=espdata)   
   if request.method =="POST":
        form = ESPDesignForm(request.POST, request.FILES, instance=espdata)        
        if form.is_valid():            
            form.save() 
            #return redirect ('espdesign:list_esp_design_data')
   return render (request, 'espdesign/esp_design_data_form.html', {'form': form, 'espdata':espdata})

def delete_esp_design_data(request, id):
   espdata = ESPDesignModel.objects.get(id=id)   
   if request.method == 'POST' :
       espdata.delete()
       return redirect ('espdesign:list_esp_design_data')
   return render (request, 'espdesign/esp_design_data_confirm_delete.html', {'espdata':espdata})

def esp_design(request, id):
    espdata = ESPDesignModel.objects.get(id=id)  
    form = ESPDesignForm(request.POST or None, instance=espdata) 
    inflowdf, x1, y1, pip =calculate_inflow(espdata)
    chart = get_ipr_plot(inflowdf, espdata, x1, y1)    
    q,q1,q2,head,eff,power, rangex, rangey, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead= Generate_pump_curves(espdata)
    chart1= get_esp_plot1(q,q1,q2,head,eff,power, rangex, rangey, pump_name)
    chart2= get_esp_plot2(q,head, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead)
    chart3 = vlp_curve_for_esp(espdata)
    return render (request, 'espdesign/esp_design.html', {'espdata':espdata, 'form':form,'chart':chart, 'chart1':chart1,'chart2':chart2, 'chart3':chart3})


 