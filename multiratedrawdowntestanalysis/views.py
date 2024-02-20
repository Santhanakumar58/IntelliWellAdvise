import csv
from datetime import datetime, timedelta
import os
from sqlite3 import Date
from django.shortcuts import redirect, render
from drawdowntestanalysis.functions import handle_uploaded_file
from selectedOilProducer.models import SelectedOilProducer
from .forms import MultiRateDrawdownTestForm, MultiRateDrawdownTestUploadForm
from .models import MultiRateDrawdowntest, filepath
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.patches as mpl_patches 
from .utils import multiratetestplot 
from pathlib import Path
import glob


def list_multirate_test_data(request):
    selectedwell = SelectedOilProducer.objects.first()   
    drawdown_test_datas = MultiRateDrawdowntest.objects.filter(wellid =selectedwell.wellid).all()   
    return render (request, 'multiratedrawdowntestanalysis/multirate_test_data.html', {'drawdown_test_datas': drawdown_test_datas })   
 
def create_multirate_test_data(request):    
    drawdown = MultiRateDrawdowntest()
    selectedwell = SelectedOilProducer.objects.first()  
    drawdown.fgid = selectedwell.fgid
    drawdown.wellid = selectedwell.wellid   
    form = MultiRateDrawdownTestForm(request.POST or None, instance=drawdown)
    if request.method =="POST": 
        drawdown.fgid = selectedwell.fgid
        drawdown.wellid = selectedwell.wellid  
        form = MultiRateDrawdownTestForm(request.POST, request.FILES, instance=drawdown)                    
        if form.is_valid(): 
            form.save()  
            file_Name = form.instance
            return redirect ('multiratedrawdowntestanalysis:list_multirate_test_data') 
    return render (request, 'multiratedrawdowntestanalysis/multirate_test_data_form.html', {'form': form})

def update_multirate_test_data(request, id): 
   drawdown= MultiRateDrawdowntest.objects.get(id=id)  
   form = MultiRateDrawdownTestForm(request.POST or None, instance=drawdown) 
   if request.method =="POST":       
        form = MultiRateDrawdownTestForm(request.POST, request.FILES, instance=drawdown)        
        if form.is_valid():
            form.save()           
            return redirect ('multiratedrawdowntestanalysis:list_multirate_test_data')
   return render (request, 'multiratedrawdowntestanalysis/multirate_test_data_form.html', {'form': form, 'drawdown':drawdown})

def delete_multirate_test_data(request, id):
   drawdown = MultiRateDrawdowntest.objects.get(id=id)   
   if request.method == 'POST' :
       drawdown.delete()
       drawdown.file_Name.delete()
       return redirect ('multiratedrawdowntestanalysis:list_multirate_test_data')
   return render (request, 'multiratedrawdowntestanalysis/multirate_test_data_confirm_delete.html', {'drawdown':drawdown})

def upload_Multi_Rate_test_data(request, id): 
    drawdown= MultiRateDrawdowntest.objects.get(id=id)     
    chart =Calculate_MultiRate_Test(request, id)   
    form = MultiRateDrawdownTestUploadForm(request.POST or None, instance=drawdown)     
    if request.method =="POST":  
        if drawdown.test_Type =='Constant_Rate':     
            drawdown.time1 = request.POST['time1']
            drawdown.pressure1 =  request.POST['pressure1']    
            drawdown.time2 = request.POST['time2']
            drawdown.pressure2 =  request.POST['pressure2']   
            drawdown.time3 = request.POST['time3']
            drawdown.pressure3 =  request.POST['pressure3']      
            form = MultiRateDrawdownTestUploadForm(request.POST, request.FILES, instance=drawdown)        
            if form.is_valid():
                form.save()  
                chart =Calculate_MultiRate_Test(request, id)        
                return render (request, 'multiratedrawdowntestanalysis/multirate_upload.html', {'form': form, 'chart':chart, 'drawdown':drawdown})
    return render (request, 'multiratedrawdowntestanalysis/multirate_upload.html', {'form': form, 'chart':chart, 'drawdown':drawdown})
 
def Calculate_MultiRate_Test(request, id):
    drawdown= MultiRateDrawdowntest.objects.get(id=id) 
    path =drawdown.file_Name  
    filename = path.name
    #path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    path1 =(r"C:/Intelliwell/intelligentwell/media/")
    pa = os.path.join(path1, filename)   
    #q=drawdown.liquid_Rate  
    #your_guess = drawdown.guess_Value    
    df = pd.read_csv(pa)   
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df1=df.drop(index=0)
    t=df1['t'].values   
    p=df1['p'].values  
    Bo = drawdown.oil_FVF
    mu_oil = drawdown.oil_Viscosity
    h = drawdown.layer_Thickness
    poro = drawdown.layer_Porosity
    ct = drawdown.total_Compressibility
    rw = drawdown.wellbore_Radius
    pi = drawdown.initial_Res_Pres  

    t_change = np.array([10, 20, 30])
    q_change = np.array([1000, 1500, 300])

    def permeability(Bo, mu_oil, h, m):   
        return (162.6 * Bo * mu_oil) / (m * h)

    def skin_factor(k, poro, mu_oil, ct, rw, c, m):
        """
        Calculate skin factor from drawdown plot
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

    # regression to the drawdown plot
    popt, pcov = curve_fit(linear, x, y)
    m, c = popt[0], popt[1]
    # calculate permeability
    k = permeability(Bo, mu_oil, h, m)
    # calculate skin factor
    s = skin_factor(k, poro, mu_oil, ct, rw, c, m)
    chart =multiratetestplot(t,p, x,y, c, m, k,s, time_arr)
    return chart
