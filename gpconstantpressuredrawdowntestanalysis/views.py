import csv
from datetime import datetime, timedelta
import os
from sqlite3 import Date
from django.shortcuts import redirect, render
from drawdowntestanalysis.functions import handle_uploaded_file
from selectedGasProducer.models import SelectedGasProducer
from .forms import GPConstantPressureDrawdownTestForm
from .models import GPConstantPressureDrawdowntest, filepath
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.patches as mpl_patches 
from .utils import constant_Pressure_plot
from pathlib import Path
import glob


def list_gpconstantpressure_test_data(request):
    selectedwell = SelectedGasProducer.objects.first()   
    drawdown_test_datas = GPConstantPressureDrawdowntest.objects.filter(gpwellid =selectedwell.wellid).all()   
    return render (request, 'gpconstantpressuredrawdowntestanalysis/gpconstantpressure.html', {'drawdown_test_datas': drawdown_test_datas })   
 
def create_gpconstantpressure_test_data(request):    
    drawdown = GPConstantPressureDrawdowntest()
    selectedwell = SelectedGasProducer.objects.first()  
    drawdown.fgid = selectedwell.fgid
    drawdown.wellid = selectedwell.wellid   
    # pvt_Wells = BlackoilPVT.objects.filter(fgid=selectedwell.fgid)
    form = GPConstantPressureDrawdownTestForm(request.POST or None, instance=drawdown)
    if request.method =="POST": 
        drawdown.fgid = selectedwell.fgid
        drawdown.wellid = selectedwell.wellid  
        form = GPConstantPressureDrawdownTestForm(request.POST, request.FILES, instance=drawdown)                    
        if form.is_valid(): 
            form.save()  
            file_Name = form.instance
            return redirect ('gpconstantpressuredrawdowntestanalysis:list_gpconstantpressure_test_data') 
    return render (request, 'gpconstantpressuredrawdowntestanalysis/gpconstantpressure_form.html', {'form': form})

def update_gpconstantpressure_test_data(request, id): 
   drawdown= GPConstantPressureDrawdowntest.objects.get(id=id)  
   form = GPConstantPressureDrawdownTestForm(request.POST or None, instance=drawdown) 
   if request.method =="POST":       
        form = GPConstantPressureDrawdownTestForm(request.POST, request.FILES, instance=drawdown)        
        if form.is_valid():
            form.save()           
            return redirect ('gpconstantpressuredrawdowntestanalysis:list_gpconstantpressure_test_data')
   return render (request, 'gpconstantpressuredrawdowntestanalysis/gpconstantpressure_form.html', {'form': form, 'drawdown':drawdown})

def delete_gpconstantpressure_test_data(request, id):
   drawdown = GPConstantPressureDrawdowntest.objects.get(id=id)   
   if request.method == 'POST' :
       drawdown.delete()
       drawdown.file_Name.delete()
       return redirect ('gpconstantpressuredrawdowntestanalysis:list_gpconstantpressure_test_data')
   return render (request, 'gpconstantpressuredrawdowntestanalysis/gpconstantpressure_confirm_delete.html', {'drawdown':drawdown})

def upload_Constant_Pressure_test_data(request, id): 
    drawdown= GPConstantPressureDrawdowntest.objects.get(id=id)     
    chart =Calculate_Constant_Pressure_Test(request, id)   
    form = GPConstantPressureDrawdownTestForm(request.POST or None, instance=drawdown)     
    if request.method =="POST":  
        if drawdown.test_Type =='Constant_Rate':     
            drawdown.liquid_Rate = request.POST['liquid_Rate']
            drawdown.guess_Value =  request.POST['guess_Value']       
            form = GPConstantPressureDrawdownTestForm(request.POST, request.FILES, instance=drawdown)        
            if form.is_valid():
                form.save()  
                chart =Calculate_Constant_Pressure_Test(request, id)        
                return render (request, 'gpconstantpressuredrawdowntestanalysis/gpconstantpressure_upload.html', {'form': form, 'chart':chart, 'drawdown':drawdown})
    return render (request, 'gpconstantpressuredrawdowntestanalysis/gpconstantpressure_upload.html', {'form': form, 'chart':chart, 'drawdown':drawdown})
 
def Calculate_Constant_Pressure_Test(request, id):
    drawdown= GPConstantPressureDrawdowntest.objects.get(id=id) 
    path =drawdown.file_Name  
    filename = path.name
    path1 =(r"C:/Intelliwell/intelligentwell/media/")
    #path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    pa = os.path.join(path1, filename) 
    df = pd.read_csv(pa)   
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]   
    t=df['t'].values   
    q=df['q'].values  
    Bo = drawdown.oil_FVF
    mu_oil = drawdown.oil_Viscosity
    h = drawdown.layer_Thickness
    poro = drawdown.layer_Porosity
    ct = drawdown.total_Compressibility
    rw = drawdown.wellbore_Radius
    pi = drawdown.initial_Res_Pres 
    pwf = drawdown.pwf 

    def permeability(Bo, mu_oil, h, m):    
        return (162.6 * Bo * mu_oil) / (m * h * (pi - pwf))

    def skin_factor(k, poro, mu_oil, ct, rw, c, m):    
        return 1.1513 * ((c / m) - np.log10(k / (poro * mu_oil * ct * (rw**2))) + 3.2275)

    def linear(x, a, b):
        return a * x + b
  
    # linear regression
    x, y = np.log10(t), 1/q
    popt, pcov = curve_fit(linear, x, y)
    m, c = popt[0], popt[1]
    # calculate permeability
    k = permeability(Bo, mu_oil, h, m)
    # calculate skin factor
    s = skin_factor(k, poro, mu_oil, ct, rw, c, m)
 
    chart =constant_Pressure_plot(t, q, pwf, pi, Bo, mu_oil, h, poro, ct, rw, k,s,m,c)
    return chart
   

