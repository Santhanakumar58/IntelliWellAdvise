from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from .forms import OBCompletionForm
from .utils import get_plot, get_plot1, get_plot2
from obcasings.utils import get_dummyplot
from .models import OBWellcompletion
from selectedObserver.models import SelectedObserver
from obdeviationsurveydata.models import OBDeviationsurveydata
from obcasings.models import OBCasingModel, OBCasingSizeModel
import numpy as np
import pandas as pd

# Create your views here.
def list_obwellcompletion(request):
    selectedwell = SelectedObserver.objects.all().first()         
    completion_datas = OBWellcompletion.objects.filter(obwellid =selectedwell.wellid).all().order_by('obequip_Md')  
    casings = OBCasingModel.objects.filter(obwellid=selectedwell.wellid).all().order_by('obshoedepth') 
    casingdf =pd.DataFrame()
    width=0.0
    widths=[]
    depths=[]
    hangers=[]
    cements=[]
    casingdefs=[]
    for casing in casings:    
        csize = OBCasingSizeModel.objects.get(gpcasingSize = casing.casingSize)  
        if csize.casingSize =="20":
            width =20*2
        elif csize.casingSize == "18 5/8":
            width =18.625*2
        elif csize.casingSize == "16":
            width =16*2
        elif csize.casingSize == "13 3/8":
            width =13.375*2
        elif csize.casingSize == "11 3/4":
            width =11/75*2
        elif csize.casingSize == "10 3/4":
            width =10.75*2
        elif csize.casingSize == "9 5/8":
            width =9.625*2
        elif csize.casingSize == "8 5/8":
            width =8.625*2
        elif csize.casingSize == "7 3/4":
            width =7.75*2
        elif csize.casingSize == "7 5/8":
            width =7.5*2
        elif csize.casingSize == "7":
            width =7.0*2
        elif casing.Casing_Size == "6 5/8":
            width =6.625*2
        elif csize.casingSize == "5":
            width =5*2
        elif csize.casingSize == "4 1/2":
            width =4.5*2
        elif csize.casingSize == "4":
            width =4*2
        depth = casing.shoedepth
        hanger = casing.hangerDepth
        cement = casing.cementTop
        widths.append(width)
        depths.append(depth)
        hangers.append(hanger)
        cements.append(cement)
        casingdef = str(casing.casingSize)+ "  ,  " + str(casing.casingWeight) + " ppf, "
        casingdefs.append(casingdef)
    deviationdata = OBDeviationsurveydata.objects.filter(obwellid=selectedwell.wellid).all()
    equipmentDepth=[]
    equipmentName=[]
    equipmentx =[]
    east=0
    for equip in completion_datas:
        east = eastCalculation(deviationdata, equip.equip_Md)
        equipmentx.append(east)
        equipmentDepth.append(equip.equip_Md)
        equipmentN= str(equip.equip_Od) + " inch  " + equip.equipment + " at " +str(equip.equip_Md) + " ft"
        equipmentName.append(equipmentN)

     
    if deviationdata:
         chart2= get_plot2(widths, depths, hangers, cements, deviationdata, casingdefs, completion_datas, equipmentx,equipmentDepth,equipmentName ) 
    else:
        chart2 = get_dummyplot()
    return render (request, 'obwellcompletion/obwellcompletion_data.html', {'completion_datas': completion_datas, 'chart2':chart2})   
 
def create_obwellcompletion(request):    
   completion_data = OBWellcompletion() 
   selectedwell = SelectedObserver.objects.all().first()     
   completion_data.gpfgid = selectedwell.fgid
   completion_data.gpwellid = selectedwell.wellid   
   form = OBCompletionForm(request.POST or None, instance=completion_data)
   if request.method =="POST":  
        form = OBCompletionForm(request.POST, request.FILES, instance=completion_data)       
        completion_data.gpfgid = selectedwell.fgid
        completion_data.gpwellid = selectedwell.wellid    
        md =  float(request.POST['equip_Md'])       
        deviation_datas =   OBDeviationsurveydata.objects.filter(gpwellid = selectedwell.wellid).all()        
        tvd = tvdCalculation(deviation_datas, md)   
        completion_data.equip_Tvd = round(tvd[0],2) 
        completion_data.equip_Angle = round(tvd[1],2)             
        if form.is_valid(): 
            form.save()  
            return redirect ('obwellcompletion:list_obwellcompletion') 
   return render (request, 'obwellcompletion/obwellcompletion_data_form.html', {'form': form})

def update_obwellcompletion(request, id): 
   completion_data = OBWellcompletion.objects.get(id=id)  
   form = OBCompletionForm(request.POST or None, instance=completion_data) 
   if request.method =="POST":
        form = OBCompletionForm(request.POST, request.FILES, instance=completion_data)  
        md =  float(request.POST['equip_Md'])   
        deviation_datas =   OBDeviationsurveydata.objects.filter(wellid = completion_data.wellid).all()        
        tvd = tvdCalculation(deviation_datas, md)   
        completion_data.equip_Tvd = round(tvd[0],2) 
        completion_data.equip_Angle = round(tvd[1],2)                
        if form.is_valid():
            form.save()           
            return redirect ('obwellcompletion:list_obwellcompletion')
   return render (request, 'obwellcompletion/obwellcompletion_data_form.html', {'form': form, 'completion_data':completion_data})

def delete_obwellcompletion(request, id):
   completion_data = OBWellcompletion.objects.get(id=id)   
   if request.method == 'POST' :
       completion_data.delete()
       return redirect ('obwellcompletion:list_obwellcompletion')
   return render (request, 'obwellcompletion/obwellcompletion_data_confirm_delete.html', {'completion_data':completion_data})

def tvdCalculation(deviation_datas, md):   
    depth, depth1=0.0, 0.0
    tvd, tvd1=0.0, 0.0
    angle, angle1=0.0, 0.0
    computedtvd, computedangle =0.0, 0.0
    for data in deviation_datas:
        if data.measuredDepth > md:
            depth1 = data.measuredDepth
            angle1 = data.angle
            tvd1 = data.tvd          
            computedtvd = tvd + ((tvd1 - tvd) * (md - depth) / (depth1 - depth))
            computedangle = angle + ((angle1 - angle) * (md - depth) / (depth1 - depth))                                     
            break
        else:
            depth = data.measuredDepth
            angle = data.angle
            tvd = data.tvd           
    return computedtvd, computedangle

def eastCalculation(deviation_datas, md):   
    depth, depth1=0.0, 0.0
    east=0.0
    computedeast=0 
    for data in deviation_datas:
        if data.measuredDepth > md:
            depth1 = data.measuredDepth
            east1 = data.eastWest                   
            computedeast = east + ((east1 - east) * (md - depth) / (depth1 - depth))                                               
            break
        else:
            depth = data.measuredDepth
            east = data.eastWest                  
    return computedeast


