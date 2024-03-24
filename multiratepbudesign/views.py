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
from IntelligentOilWell.custom_context_processors import time_finite_acting , simulate_multirate_test
from .utils import multirate_constant_rate_design_plot

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
 
def mulitirate_test_pbu_design(request, id):
    pbu_design= MultiRatePBUdesign.objects.get(id=id)  
    Bo = pbu_design.oil_FVF_Bo
    mu_oil = pbu_design.oil_Viscosity_cP
    h = pbu_design.layer_Thickness_ft
    poro = pbu_design.layer_Porosity_fraction
    perm = pbu_design.layer_Permeability_md
    ct = pbu_design.total_Compressibility
    rw = pbu_design.wellbore_Radius_ft
    re = pbu_design.drainage_radius_ft
    pi = pbu_design.initial_Res_Pres_psi  
    t_step = 0.1

    t_change = np.array([pbu_design.time1, pbu_design.time2, pbu_design.time3,pbu_design.time4, pbu_design.time5, pbu_design.time6])
    q_change = np.array([pbu_design.rate1, pbu_design.rate2, pbu_design.rate3, pbu_design.rate4, pbu_design.rate5, pbu_design.rate6])
    #t_finite_acting = time_finite_acting(perm, poro, mu_oil, ct, rw, re)
    t_finite_acting, t,q, t_end,pwf = simulate_multirate_test(pi, t_step, t_change, q_change,re, rw, perm, poro, mu_oil, ct, Bo, h)
    chart1 = multirate_constant_rate_design_plot(t_finite_acting,t,q, t_end, pwf)  
    
    return render (request, 'multiratepbudesign/multirate_design.html', {'chart1': chart1, 'pbu_design':pbu_design}) 
