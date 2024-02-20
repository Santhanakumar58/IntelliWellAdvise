import os
from django.shortcuts import render, redirect
from IntelligentOilWell.custom_context_processors import selectedfgi
from django.contrib import messages
from IntelligentOilWell.settings import BASE_DIR
from .models import  WaterAnalysisModel
import numpy as np
import pandas  as pd
from selectedfgi.models import Selectedfgi
from .forms import WaterAnalysisForm
from sublayers.models import Sublayer
from .utils import get_plot, stiff_diagram

import sqlite3

# Create your views here.
def list_wateranalysis(request):  
    selectedfgi = Selectedfgi.objects.first()
    wadatas = WaterAnalysisModel.objects.filter(fgId = selectedfgi.fgid)  
    x1=[x.bicarbonate for x in wadatas]
    x2=[x2.sulphate  for x2 in wadatas]   
    x3=[x3.chloride for x3 in wadatas]
    x4=[x4.sodium  for x4 in wadatas]  
    x5=[x5.calcium for x5 in wadatas]
    x6=[x6.magnesium  for x6 in wadatas]  
    x7=[x7.pottasium for x7 in wadatas]
    x8=[x8.carbonate for x8 in wadatas]    
    y=[y.wellName for y in wadatas]     
    df  = pd.DataFrame(y,columns=["Well_Name"])     
    df['HCO3'] =x1
    df['CO3'] =x8
    df['SO4'] =x2
    df['Cl'] =x3
    df['Na'] =x4
    df['Ca'] =x5
    df['Mg'] =x6
    df['K'] =x7
     
    print(selectedfgi.fgid)
    ions = {
        'HCO3': 61, 'CO3' : 30, 'Cl' : 35, 'SO4': 48,
        'Na' : 23, 'Ca' : 20, 'Mg' : 12, 'K'  : 39
        }
    for ion in ions.keys():
        df[str(ion)+'_meq'] = df[ion]/ions[ion]
    print(df)
    #SO4
    df['SO4_norm'] = df['SO4_meq'] / (df['SO4_meq'] +df['HCO3_meq']+df['CO3_meq']+df['Cl_meq']) * 100
    #HCO3
    df['HCO3_CO3_norm'] = (df['HCO3_meq']+df['CO3_meq']) / (df['SO4_meq'] + df['HCO3_meq']+df['CO3_meq']+df['Cl_meq']) * 100
    #Cl
    df['Cl_norm'] = df['Cl_meq'] / (df['SO4_meq'] + df['HCO3_meq']+df['CO3_meq']+df['Cl_meq']) * 100
    #normalizando os cátions 
    #Mg
    df['Mg_norm'] = df['Mg_meq'] / (df['Mg_meq'] +  df['Ca_meq']+df['K_meq']+df['Na_meq']) * 100
    #K
    df['Na_K_norm'] = (df['K_meq']+df['Na_meq']) / (df['Mg_meq'] +  df['Ca_meq']+df['K_meq']+df['Na_meq']) * 100
    #Ca
    df['Ca_norm'] = df['Ca_meq'] / (df['Mg_meq'] + df['Ca_meq']+df['K_meq']+df['Na_meq']) * 100
    chart = get_plot(df)
    wadata = WaterAnalysisModel.objects.filter(fgId = selectedfgi.fgid).last() 
    if wadata :
        Nak = wadata.sodium + wadata.pottasium
        Ca = wadata.calcium  
        Mg = wadata.magnesium  
        HCO3 = wadata.bicarbonate + wadata.carbonate
        SO4 = wadata.sulphate  
        Cl = wadata.chloride 
    else:
        Nak = 5
        Ca = 5
        Mg = 5 
        HCO3 = 5
        SO4 = 5 
        Cl = 5
    print(Nak, Ca, Mg, SO4, HCO3, Cl)
    chart2 = stiff_diagram(Nak, Ca, Mg, SO4, HCO3, Cl)
    return render (request, 'wateranalysis/wateranalysis.html', {'wadatas':wadatas, 'chart':chart, 'chart2':chart2})
    
def create_wateranalysis(request):    
   wadata = WaterAnalysisModel()
   selectedfgi = Selectedfgi.objects.first()
   wadata.fgId = selectedfgi.fgid
   sublayer = Sublayer.objects.get(sublayername=selectedfgi.selectedsublayername)
   wadata.subLayer = sublayer
   form = WaterAnalysisForm(request.POST or None, instance=wadata)  
   if form.is_valid():
       form.save()       
       return redirect ('wateranalysis:list_wateranalysis' )    
   return render (request, 'wateranalysis/wateranalysis_form.html', {'form': form, 'wadata':wadata})

def update_wateranalysis(request, id):
   wadata = WaterAnalysisModel.objects.get(id=id)    
   form = WaterAnalysisForm(request.POST or None, instance=wadata)
   if form.is_valid():
       form.save()
       return redirect ('wateranalysis:list_wateranalysis')
   return render (request, 'wateranalysis/wateranalysis_form.html', {'form': form, 'wadata':wadata, 'id':id})

def delete_wateranalysis(request, id):
   wadata = WaterAnalysisModel.objects.get(id=id) 
   if request.method == 'POST' :
       wadata.delete()
       return redirect ('wateranalysis:list_wateranalysis'  )
   return render (request, 'wateranalysis/wateranalysis_confirm_delete.html', {'wadata':wadata, 'id':id})
