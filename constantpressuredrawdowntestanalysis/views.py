import csv
from datetime import datetime, timedelta
import os
from sqlite3 import Date
from django.shortcuts import redirect, render
from drawdowntestanalysis.functions import handle_uploaded_file
from selectedOilProducer.models import SelectedOilProducer
from .forms import ConstantPressureDrawdownTestForm
from .models import ConstantPressureDrawdowntest, filepath
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.patches as mpl_patches 
from .utils import constant_Pressure_plot
from pathlib import Path
import glob


def list_constantpressure_test_data(request):
    selectedwell = SelectedOilProducer.objects.first()   
    drawdown_test_datas = ConstantPressureDrawdowntest.objects.filter(wellid =selectedwell.wellid).all()   
    return render (request, 'constantpressuredrawdowntestanalysis/constantpressure.html', {'drawdown_test_datas': drawdown_test_datas })   
 
def create_constantpressure_test_data(request):    
    drawdown = ConstantPressureDrawdowntest()
    selectedwell = SelectedOilProducer.objects.first()  
    drawdown.fgid = selectedwell.fgid
    drawdown.wellid = selectedwell.wellid   
    # pvt_Wells = BlackoilPVT.objects.filter(fgid=selectedwell.fgid)
    form = ConstantPressureDrawdownTestForm(request.POST or None, instance=drawdown)
    if request.method =="POST": 
        drawdown.fgid = selectedwell.fgid
        drawdown.wellid = selectedwell.wellid  
        form = ConstantPressureDrawdownTestForm(request.POST, request.FILES, instance=drawdown)                    
        if form.is_valid(): 
            form.save()  
            file_Name = form.instance
            return redirect ('constantpressuredrawdowntestanalysis:list_constantpressure_test_data') 
    return render (request, 'constantpressuredrawdowntestanalysis/constantpressure_form.html', {'form': form})

def update_constantpressure_test_data(request, id): 
   drawdown= ConstantPressureDrawdowntest.objects.get(id=id)  
   form = ConstantPressureDrawdownTestForm(request.POST or None, instance=drawdown) 
   if request.method =="POST":       
        form = ConstantPressureDrawdownTestForm(request.POST, request.FILES, instance=drawdown)        
        if form.is_valid():
            form.save()           
            return redirect ('constantpressuredrawdowntestanalysis:list_constantpressure_test_data')
   return render (request, 'constantpressuredrawdowntestanalysis/constantpressure_form.html', {'form': form, 'drawdown':drawdown})

def delete_constantpressure_test_data(request, id):
   drawdown = ConstantPressureDrawdowntest.objects.get(id=id)   
   if request.method == 'POST' :
       drawdown.delete()
       drawdown.file_Name.delete()
       return redirect ('constantpressuredrawdowntestanalysis:list_constantpressure_test_data')
   return render (request, 'constantpressuredrawdowntestanalysis/constantpressure_confirm_delete.html', {'drawdown':drawdown})

def upload_Constant_Pressure_test_data(request, id): 
    drawdown= ConstantPressureDrawdowntest.objects.get(id=id)     
    chart =Calculate_Constant_Pressure_Test(request, id)   
    form = ConstantPressureDrawdownTestForm(request.POST or None, instance=drawdown)     
    if request.method =="POST":  
        if drawdown.test_Type =='Constant_Rate':     
            drawdown.liquid_Rate = request.POST['liquid_Rate']
            drawdown.guess_Value =  request.POST['guess_Value']       
            form = ConstantPressureDrawdownTestForm(request.POST, request.FILES, instance=drawdown)        
            if form.is_valid():
                form.save()  
                chart =Calculate_Constant_Pressure_Test(request, id)        
                return render (request, 'constantpressuredrawdowntestanalysis/constantpressure_upload.html', {'form': form, 'chart':chart, 'drawdown':drawdown})
    return render (request, 'constantpressuredrawdowntestanalysis/constantpressure_upload.html', {'form': form, 'chart':chart, 'drawdown':drawdown})
 
def Calculate_Constant_Pressure_Test(request, id):
    drawdown= ConstantPressureDrawdowntest.objects.get(id=id) 
    path =drawdown.file_Name  
    #filename = path.name
    #path1 =(r"C:/Intelliwell/intelligentwell/media/")
    #path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    #pa = os.path.join(path1, filename) 
    df = pd.read_csv(path)   
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
   
