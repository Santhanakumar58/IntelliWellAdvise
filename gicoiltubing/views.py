from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasInjector.models import SelectedGasInjector
from .forms import GICoiltubingForm
from .utils import get_plot, get_plot1
from .models import GICoiltubing


# Create your views here.
def list_gicoil_tubing_data(request):
    selectedwell = SelectedGasInjector.objects.first()   
    gicoil_tubing_datas = GICoiltubing.objects.filter(giwellid =selectedwell.wellid).all()    
    x=[x1.end_Date for x1 in gicoil_tubing_datas] 
    y=[(y.post_ct_liquid-y.pre_ct_liquid) for y in gicoil_tubing_datas]
    y1=[round((y1.post_ct_liquid * (1-y1.post_ct_WC/100)-y1.pre_ct_liquid * (1-y1.pre_ct_WC/100)),2) for y1 in gicoil_tubing_datas]
    y2=[round((y2.post_ct_GOR * (y2.post_ct_liquid * (1-y2.post_ct_WC/100))/1000-y2.pre_ct_GOR * (y2.pre_ct_liquid * (1-y2.pre_ct_WC/100))/1000 ),2)  for y2 in gicoil_tubing_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'gicoiltubing/gicoil_tubing_data.html', {'gicoil_tubing_datas': gicoil_tubing_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain  })   
 
def create_gicoil_tubing_data(request):    
   gicoil_tubing_data = GICoiltubing()
   selectedwell = SelectedGasInjector.objects.first()  
   gicoil_tubing_data.fgid = selectedwell.fgid
   gicoil_tubing_data.wellid = selectedwell.wellid   
   form = GICoiltubingForm(request.POST or None, instance=gicoil_tubing_data)
   if request.method =="POST":  
        form = GICoiltubingForm(request.POST, request.FILES, instance=gicoil_tubing_data)       
        gicoil_tubing_data.fgid = selectedwell.fgid
        gicoil_tubing_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('gicoiltubing:list_gicoil_tubing_data') 
   return render (request, 'gicoiltubing/gicoil_tubing_data_form.html', {'form': form})

def update_gicoil_tubing_data(request, id): 
   gicoil_tubing_data = GICoiltubing.objects.get(id=id)  
   form = GICoiltubingForm(request.POST or None, instance=gicoil_tubing_data) 
   if request.method =="POST":
        form = GICoiltubingForm(request.POST, request.FILES, instance=gicoil_tubing_data)        
        if form.is_valid():
            form.save()           
            return redirect ('gicoiltubing:list_gicoil_tubing_data')
   return render (request, 'gicoiltubing/gicoil_tubing_data_form.html', {'form': form, 'gicoil_tubing_data':gicoil_tubing_data})

def delete_gicoil_tubing_data(request, id):
   gicoil_tubing_data = GICoiltubing.objects.get(id=id)   
   if request.method == 'POST' :
       gicoil_tubing_data.delete()
       return redirect ('gicoiltubing:list_gicoil_tubing_data')
   return render (request, 'gicoiltubing/gicoil_tubing_data_confirm_delete.html', {'gicoil_tubing_data':gicoil_tubing_data})

def detail_gicoil_tubing_data(request, id): 
    oilgain =0
    selectedwell = SelectedGasInjector.objects.first()    
    gicoil_tubing_data = GICoiltubing.objects.get(id=id)
    preliquid = gicoil_tubing_data.pre_ct_liquid  
    postliquid = gicoil_tubing_data.post_ct_liquid
    liquidgain = postliquid-preliquid
    prewater = gicoil_tubing_data.pre_ct_WC  
    postwater = gicoil_tubing_data.post_ct_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*gicoil_tubing_data.pre_ct_GOR)/1000
    postgas = round(postoil * gicoil_tubing_data.post_ct_GOR)/1000
    expoil = round(gicoil_tubing_data.expected_liquid *(1-gicoil_tubing_data.expected_WC/100) ,2)
    expgas = round(expoil * gicoil_tubing_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = gicoil_tubing_data.pre_ct_GOR 
    postgor = gicoil_tubing_data.post_ct_GOR
    gorgain = postgor-pregorr  
    if liquidgain>0:
        status = True
    else:
        status = False
    if watergain <=0:
        status1 = True
    else:
        status1 = False
    if gorgain <=0:
        status2 = True
    else:
        status2 = False
    if oilgain >=0:
        status3 = True
    else:
        status3 = False
    if gasgain >=0:
        status4 = True
    else:
        status4 = False

   # for plot 
    x1='Liquid'
    x2='Oil'
    x3='Gas'
    y1= liquidgain
    y2=oilgain
    y3=gasgain 
    dat= gicoil_tubing_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = GICoiltubingForm(request.POST or None, instance=gicoil_tubing_data) 
    return render (request, 'gicoiltubing/gicoil_tubing_data_detail.html', {'form': form, 'gicoil_tubing_data':gicoil_tubing_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})

   


