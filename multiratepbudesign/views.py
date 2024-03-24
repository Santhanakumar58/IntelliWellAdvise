import csv
from datetime import datetime, timedelta
import os
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedOilProducer.models import SelectedOilProducer
from .forms import MultiRatePBUdesignForm
from .models import MultiRatePBUdesign
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.patches as mpl_patches 

from pathlib import Path
import glob


def list_multirate_test_pbu_design(request):
    selectedwell = SelectedOilProducer.objects.first()   
    multirate_pbu_designs = MultiRatePBUdesign.objects.filter(wellid =selectedwell.wellid).all()   
    return render (request, 'multiratepbudesign/multirate_test_pbu_design.html', {'multirate_pbu_designs': multirate_pbu_designs })   
 
def create_multirate_test_pbu_design(request):    
    pbu_design = MultiRatePBUdesign()
    selectedwell = SelectedOilProducer.objects.first()  
    pbu_design.fgid = selectedwell.fgid
    pbu_design.wellid = selectedwell.wellid   
    form = MultiRatePBUdesignForm(request.POST or None, instance=pbu_design)
    if request.method =="POST": 
        pbu_design.fgid = selectedwell.fgid
        pbu_design.wellid = selectedwell.wellid  
        form = MultiRatePBUdesignForm(request.POST, request.FILES, instance=pbu_design)                    
        if form.is_valid(): 
            form.save()              
            return redirect ('multiratepbudesign:list_multirate_test_pbu_design') 
    return render (request, 'multiratepbudesign/multirate_test_pbu_design_form.html', {'form': form})

def update_multirate_test_pbu_design(request, id): 
   pbu_design= MultiRatePBUdesign.objects.get(id=id)  
   form = MultiRatePBUdesignForm(request.POST or None, instance=pbu_design) 
   if request.method =="POST":       
        form = MultiRatePBUdesignForm(request.POST, request.FILES, instance=pbu_design)        
        if form.is_valid():
            form.save()           
            return redirect ('multiratepbudesign:list_multirate_test_pbu_design')
   return render (request, 'multiratepbudesign/multirate_test_pbu_design_form.html', {'form': form, 'pbu_design':pbu_design})

def delete_multirate_test_pbu_design(request, id):
   pbu_design = MultiRatePBUdesign.objects.get(id=id)   
   if request.method == 'POST' :
       pbu_design.delete()
       pbu_design.file_Name.delete()
       return redirect ('multiratepbudesign:list_multirate_test_pbu_design')
   return render (request, 'multiratepbudesign/multirate_test_pbu_design_confirm_delete.html', {'pbu_design':pbu_design})
 
def Calculate_MultiRate_Test(request, id):
    pbu_design= MultiRatePBUdesign.objects.get(id=id) 
    path =pbu_design.file_Name_csv  
    #filename = path.name
    #path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    #path1 =(r"C:/Intelliwell/intelligentwell/media/")
    #pa = os.path.join(path1, filename)   
    #q=pbu_design.liquid_Rate  
    #your_guess = pbu_design.guess_Value    
    df = pd.read_csv(path)   
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df1=df.drop(index=0)
    t=df1['t'].values   
    p=df1['p'].values  
    Bo = pbu_design.oil_FVF_Bo
    mu_oil = pbu_design.oil_Viscosity_cP
    h = pbu_design.layer_Thickness_ft
    poro = pbu_design.layer_Porosity_fraction
    ct = pbu_design.total_Compressibility
    rw = pbu_design.wellbore_Radius_ft
    pi = pbu_design.initial_Res_Pres_psi  

    t_change = np.array([pbu_design.time1, pbu_design.time2, pbu_design.time3])
    q_change = np.array([pbu_design.rate1, pbu_design.rate2, pbu_design.rate3])

    def permeability(Bo, mu_oil, h, m):   
        return (162.6 * Bo * mu_oil) / (m * h)

    def skin_factor(k, poro, mu_oil, ct, rw, c, m):
        """
        Calculate skin factor from pbu_design plot
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

    # regression to the pbu_design plot
    popt, pcov = curve_fit(linear, x, y)
    m, c = popt[0], popt[1]
    # calculate permeability
    k = permeability(Bo, mu_oil, h, m)
    # calculate skin factor
    s = skin_factor(k, poro, mu_oil, ct, rw, c, m)
    # chart =multiratetestplot(t,p, x,y, c, m, k,s, time_arr)
    return 
