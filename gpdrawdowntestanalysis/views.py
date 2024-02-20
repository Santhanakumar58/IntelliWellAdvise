import csv
from datetime import datetime, timedelta
import os
from sqlite3 import Date
from django.shortcuts import redirect, render
from gpdrawdowntestanalysis.functions import handle_uploaded_file
from selectedGasProducer.models import SelectedGasProducer
from .forms import GPDrawdownTestForm, GPDrawdownTestUploadForm
from .models import GPDrawdowntest, filepath
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.patches as mpl_patches 
from .utils import get_plot, multiratetestplot, constant_Pressure_plot
from pathlib import Path
import glob


def list_gpdrawdown_test_data(request):
    selectedwell = SelectedGasProducer.objects.first()   
    gpdrawdown_test_datas = GPDrawdowntest.objects.filter(gpwellid =selectedwell.wellid).all()   
    return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data.html', {'gpdrawdown_test_datas': gpdrawdown_test_datas })   
 
def create_gpdrawdown_test_data(request):    
    gpdrawdown = GPDrawdowntest()
    selectedwell = SelectedGasProducer.objects.first()  
    gpdrawdown.fgid = selectedwell.fgid
    gpdrawdown.wellid = selectedwell.wellid   
    # pvt_Wells = BlackoilPVT.objects.filter(fgid=selectedwell.fgid)
    form = GPDrawdownTestForm(request.POST or None, instance=gpdrawdown)
    if request.method =="POST": 
        gpdrawdown.fgid = selectedwell.fgid
        gpdrawdown.wellid = selectedwell.wellid  
        form = GPDrawdownTestForm(request.POST, request.FILES, instance=gpdrawdown)                    
        if form.is_valid(): 
            form.save()  
            file_Name = form.instance
            return redirect ('gpdrawdowntestanalysis:list_gpdrawdown_test_data') 
    return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data_form.html', {'form': form})

def update_gpdrawdown_test_data(request, id): 
   gpdrawdown= GPDrawdowntest.objects.get(id=id)  
   form = GPDrawdownTestForm(request.POST or None, instance=gpdrawdown) 
   if request.method =="POST":       
        form = GPDrawdownTestForm(request.POST, request.FILES, instance=gpdrawdown)        
        if form.is_valid():
            form.save()           
            return redirect ('gpdrawdowntestanalysis:list_gpdrawdown_test_data')
   return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data_form.html', {'form': form, 'gpdrawdown':gpdrawdown})

def delete_gpdrawdown_test_data(request, id):
   gpdrawdown = GPDrawdowntest.objects.get(id=id)   
   if request.method == 'POST' :
       gpdrawdown.delete()
       gpdrawdown.file_Name.delete()
       return redirect ('gpdrawdowntestanalysis:list_gpdrawdown_test_data')
   return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data_confirm_delete.html', {'gpdrawdown':gpdrawdown})

def upload_Conatant_Rate_test_data(request, id): 
    gpdrawdown= GPDrawdowntest.objects.get(id=id)      
    chart =Calculate_Constant_Rate_test_data(request, id)   
    form = GPDrawdownTestUploadForm(request.POST or None, instance=gpdrawdown)     
    if request.method =="POST":  
        if gpdrawdown.test_Type =='Constant_Rate':     
            gpdrawdown.liquid_Rate = request.POST['liquid_Rate']
            gpdrawdown.guess_Value =  request.POST['guess_Value']       
            form = GPDrawdownTestUploadForm(request.POST, request.FILES, instance=gpdrawdown)        
            if form.is_valid():
                form.save()  
                chart =Calculate_Constant_Rate_test_data(request, id)        
                return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data_upload.html', {'form': form, 'chart':chart, 'gpdrawdown':gpdrawdown})
    return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data_upload.html', {'form': form, 'chart':chart, 'gpdrawdown':gpdrawdown})
   

def upload_Constant_Pressure_test_data(request, id): 
    gpdrawdown= GPDrawdowntest.objects.get(id=id)     
    chart =Calculate_Constant_Pressure_Test(request, id)   
    form = GPDrawdownTestUploadForm(request.POST or None, instance=gpdrawdown)     
    if request.method =="POST":  
        if gpdrawdown.test_Type =='Constant_Rate':     
            gpdrawdown.liquid_Rate = request.POST['liquid_Rate']
            gpdrawdown.guess_Value =  request.POST['guess_Value']       
            form = GPDrawdownTestUploadForm(request.POST, request.FILES, instance=gpdrawdown)        
            if form.is_valid():
                form.save()  
                chart =Calculate_Constant_Pressure_Test(request, id)        
                return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data_upload.html', {'form': form, 'chart':chart, 'gpdrawdown':gpdrawdown})
    return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data_upload.html', {'form': form, 'chart':chart, 'gpdrawdown':gpdrawdown})
    
def upload_Multi_Rate_test_data(request, id): 
    gpdrawdown= GPDrawdowntest.objects.get(id=id)     
    chart =Calculate_MultiRate_Test(request, id)   
    form = GPDrawdownTestUploadForm(request.POST or None, instance=gpdrawdown)     
    if request.method =="POST":  
        if gpdrawdown.test_Type =='Constant_Rate':     
            gpdrawdown.liquid_Rate = request.POST['liquid_Rate']
            gpdrawdown.guess_Value =  request.POST['guess_Value']       
            form = GPDrawdownTestUploadForm(request.POST, request.FILES, instance=gpdrawdown)        
            if form.is_valid():
                form.save()  
                chart =Calculate_MultiRate_Test(request, id)        
                return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data_upload.html', {'form': form, 'chart':chart, 'gpdrawdown':gpdrawdown})
    return render (request, 'gpdrawdowntestanalysis/gpdrawdown_test_data_upload.html', {'form': form, 'chart':chart, 'gpdrawdown':gpdrawdown})
    
def Calculate_Constant_Rate_test_data(request, id): 
    gpdrawdown= GPDrawdowntest.objects.get(id=id) 
    path =gpdrawdown.file_Name  
    filename = path.name
    #path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    path1 =(r"C:/Intelliwell/intelligentwell/media/")
    pa = os.path.join(path1, filename)   
    q=gpdrawdown.liquid_Rate  
    your_guess=0
    your_guess = gpdrawdown.guess_Value    
    df = pd.read_csv(pa)   
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df1=df.drop(index=0)
    t=df1['t'].values
    p=df1['p'].values   
    Bo = gpdrawdown.oil_FVF
    mu_oil = gpdrawdown.oil_Viscosity
    h = gpdrawdown.layer_Thickness
    poro = gpdrawdown.layer_Porosity
    ct = gpdrawdown.total_Compressibility
    rw = gpdrawdown.wellbore_Radius
    pi = gpdrawdown.initial_Res_Pres  
    def permeability(q, Bo, mu_oil, h, m_cycle):        
        return (-162.6 * q * Bo * mu_oil) / (m_cycle * h)
    def skin_factor(pi, k, poro, mu_oil, ct, rw, c1, m_cycle):   
        return 1.1513 * (((pi - c1) / -m_cycle) - np.log10(k / (poro * mu_oil * ct * (rw**2))) + 3.2275)
    def reservoir_size(q, Bo, poro, h, ct, m2):    
        return np.sqrt(-(.07447 * q * Bo) / (poro * h * ct * m2))
    def linear(x, a, b):
        return a * x + b 
    t_crop1, p_crop1 = np.log(t[1:your_guess+1]), p[1:your_guess+1]
    popt, pcov = curve_fit(linear, t_crop1, p_crop1)
    m1, c1 = popt[0], popt[1]
    m_cycle = m1 * np.log(10) # slope has unit psi/cycle
    k = permeability(q, Bo, mu_oil, h, m_cycle)
    s = skin_factor(pi, k, poro, mu_oil, ct, rw, c1, m_cycle)
    t_crop2, p_crop2 = t[your_guess:], p[your_guess:]
    popt, pcov = curve_fit(linear, t_crop2, p_crop2)
    m2, c2 = popt[0], popt[1]
    re = reservoir_size(q, Bo, poro, h, ct, m2) 
    chart =get_plot(t,p,m1,c1,m2,c2,s,k,re, your_guess)
    return chart
  
def Calculate_MultiRate_Test(request, id):
    gpdrawdown= GPDrawdowntest.objects.get(id=id) 
    path =gpdrawdown.file_Name  
    filename = path.name
    path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    pa = os.path.join(path1, filename)   
    q=gpdrawdown.liquid_Rate  
    your_guess = gpdrawdown.guess_Value    
    df = pd.read_csv(pa)   
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df1=df.drop(index=0)
    t=df1['t'].values   
    p=df1['p'].values  
    Bo = gpdrawdown.oil_FVF
    mu_oil = gpdrawdown.oil_Viscosity
    h = gpdrawdown.layer_Thickness
    poro = gpdrawdown.layer_Porosity
    ct = gpdrawdown.total_Compressibility
    rw = gpdrawdown.wellbore_Radius
    pi = gpdrawdown.initial_Res_Pres  

    t_change = np.array([10, 20, 30])
    q_change = np.array([1000, 1500, 300])

    def permeability(Bo, mu_oil, h, m):   
        return (162.6 * Bo * mu_oil) / (m * h)

    def skin_factor(k, poro, mu_oil, ct, rw, c, m):
        """
        Calculate skin factor from gpdrawdown plot
        Note: k is the calculated permeability
        """
        return 1.1513 * ((c / m) - np.log10(k / (poro * mu_oil * ct * (rw**2))) + 3.2275)

    def linear(x, a, b):
        return a * x + b
  
    # calculate delta rate (Δq)
    t_change = np.append(0, t_change)
    delta_q = [j-i for i, j in zip(q_change[:-1], q_change[1:])]
    delta_q = np.concatenate((np.array([0, q_change[0]]), delta_q))

    # create rate step profile
    time_arr = []
    rate_arr = []
    x = []
    y = []

    # " Calculate the x-axis and y-axis "

    for i in range(len(t)):  
      for j in range(0, len(t_change)-1):
          if t[i] > t_change[j] and t[i] <= t_change[j+1]:
              # produce t and q profile
              time_arr.append(t[i])
              rate_arr.append(q_change[j])

              # calculate Fp as x-axis
              tn = np.log10(t[i] - t_change[:j+1])
              delta_qn = delta_q[1:j+2] / q_change[j]
              tn_mult_delta_qn = tn * delta_qn
              Fp = np.sum(tn_mult_delta_qn)
              x.append(Fp)

              # calculate ((pi - pwf) / qn) as y-axis
              y_ = (pi-p[i]) / q_change[j]
              y.append(y_)

    # regression to the gpdrawdown plot
    popt, pcov = curve_fit(linear, x, y)
    m, c = popt[0], popt[1]
    # calculate permeability
    k = permeability(Bo, mu_oil, h, m)
    # calculate skin factor
    s = skin_factor(k, poro, mu_oil, ct, rw, c, m)
    chart =multiratetestplot(t,p, x,y, c, m, k,s, time_arr)
    return chart
   
def Calculate_Constant_Pressure_Test(request, id):
    gpdrawdown= GPDrawdowntest.objects.get(id=id) 
    path =gpdrawdown.file_Name  
    filename = path.name
    path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    pa = os.path.join(path1, filename) 
    df = pd.read_csv(pa)   
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]   
    t=df['t'].values   
    q=df['q'].values  
    Bo = gpdrawdown.oil_FVF
    mu_oil = gpdrawdown.oil_Viscosity
    h = gpdrawdown.layer_Thickness
    poro = gpdrawdown.layer_Porosity
    ct = gpdrawdown.total_Compressibility
    rw = gpdrawdown.wellbore_Radius
    pi = gpdrawdown.initial_Res_Pres 
    pwf = gpdrawdown.fbhp  

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
   
