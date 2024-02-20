from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedWaterInjector.models import SelectedWaterInjector
from .models import WIReservoirPressureEstimationModel
from .forms import WIRespresEstimationForm
from .utils import  get_plot1, constant_terminal_rate, get_dummy


def time_finite_acting(re, rw, poro, mu_oil, ct, k):
    r_eD = re / rw # dimensionless radius
    t_Dw = 0.25 * r_eD**2 # dimensionless time
    print((poro * mu_oil * ct * (rw**2) * t_Dw) / (0.0002637 * k))
    return (poro * mu_oil * ct * (rw**2) * t_Dw) / (0.0002637 * k)

# Create your views here.
def list_wirespres(request):
    selectedwell = SelectedWaterInjector.objects.first()  
    latest= WIReservoirPressureEstimationModel() 
    respres_datas = WIReservoirPressureEstimationModel.objects.filter(wiwellid =selectedwell.wellid).all()   
    latest = WIReservoirPressureEstimationModel.objects.filter(wiwellid =selectedwell.wellid).last()
    if latest :
        k=latest.layer_Permeability
        h=latest.layer_Thickness
        rw=latest.wellbore_Radius
        pi=latest.ini_Res_Pres
        re=latest.drainage_Radius
        ct=latest.total_Compressibility
        q=latest.oil_Prod_Rate
        Bo=latest.oil_FVF
        mu_oil=latest.mu_oil
        poro=latest.layer_Porosity
        time, distance = 24, 1*3.281-rw  
        r_eD = re / rw # dimensionless radius
        t_Dw = 0.25 * r_eD**2 # dimensionless time
        t_finite_acting =  (poro * mu_oil * ct * (rw**2) * t_Dw) / (0.0002637 * k)
        td, Pd, Pwf = constant_terminal_rate(time, distance, re, rw, pi, q, poro, ct, k, h, mu_oil, Bo)   
        chart = get_plot1(rw,re,pi,q,poro,ct,k,h,mu_oil,Bo) 
        t_finite_acting = round(t_finite_acting,2)
        Pwf=round(Pwf,2)
        td=round(td,2)
        Pd=round(Pd,2)
    else:
        rw=0.354
        re=1200
        pi=2
        q=1000
        poro=0.2
        ct=0.0000056
        k=25
        h=35
        mu_oil=0.5
        Bo=1.3
        chart = get_dummy()
        time=0
        distance=0
        t_finite_acting=100
        Pwf=0
        td=0
        Pd=0
    return render (request, 'wirespresestimation/wirespres.html', {'respres_datas': respres_datas , 'chart':chart, 'time':time, 'distance': distance, 't_finite_acting':t_finite_acting, 'Pwf':Pwf, 'td':td, 'Pd':Pd})  

def create_wirespres(request):    
   respres_data = WIReservoirPressureEstimationModel()
   selectedwell = SelectedWaterInjector.objects.first()  
   respres_data.wifgid = selectedwell.fgid
   respres_data.wiwellid = selectedwell.wellid   
   form = WIRespresEstimationForm(request.POST or None, instance=respres_data)
   if request.method =="POST":  
        form = WIRespresEstimationForm(request.POST, request.FILES, instance=respres_data)       
        respres_data.fgid = selectedwell.fgid
        respres_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('wirespresestimation:list_wirespres') 
   return render (request, 'wirespresestimation/wirespres_form.html', {'form': form})

def update_wirespres(request, id): 
   respres_data = WIReservoirPressureEstimationModel.objects.get(id=id)  
   form = WIRespresEstimationForm(request.POST or None, instance=respres_data) 
   if request.method =="POST":
        form = WIRespresEstimationForm(request.POST, request.FILES, instance=respres_data)        
        if form.is_valid():
            form.save()           
            return redirect ('wirespresestimation:list_wirespres')
   return render (request, 'wirespresestimation/wirespres_form.html', {'form': form, 'respres_data':respres_data})

def delete_wirespres(request, id):
   respres_data = WIReservoirPressureEstimationModel.objects.get(id=id)   
   if request.method == 'POST' :
       respres_data.delete()
       return redirect ('wirespresestimation:list_wirespres')
   return render (request, 'wirespresestimation/wirespres_confirm_delete.html', {'respres_data':respres_data})



