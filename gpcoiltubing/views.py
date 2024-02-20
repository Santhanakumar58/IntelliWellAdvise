from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasProducer.models import SelectedGasProducer
from .forms import GPCoiltubingForm
from .utils import get_plot, get_plot1
from .models import GPCoiltubing


# Create your views here.
def list_gpcoil_tubing_data(request):
    selectedwell = SelectedGasProducer.objects.first()   
    gpcoil_tubing_datas = GPCoiltubing.objects.filter(gpwellid =selectedwell.wellid).all()    
    x=[x1.end_Date for x1 in gpcoil_tubing_datas] 
    y=[(y.post_ct_liquid-y.pre_ct_liquid) for y in gpcoil_tubing_datas]
    y1=[round((y1.post_ct_liquid * (1-y1.post_ct_WC/100)-y1.pre_ct_liquid * (1-y1.pre_ct_WC/100)),2) for y1 in gpcoil_tubing_datas]
    y2=[round((y2.post_ct_GOR * (y2.post_ct_liquid * (1-y2.post_ct_WC/100))/1000-y2.pre_ct_GOR * (y2.pre_ct_liquid * (1-y2.pre_ct_WC/100))/1000 ),2)  for y2 in gpcoil_tubing_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'gpcoiltubing/gpcoil_tubing_data.html', {'gpcoil_tubing_datas': gpcoil_tubing_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain  })   
 
def create_gpcoil_tubing_data(request):    
   gpcoil_tubing_data = GPCoiltubing()
   selectedwell = SelectedGasProducer.objects.first()  
   gpcoil_tubing_data.fgid = selectedwell.fgid
   gpcoil_tubing_data.wellid = selectedwell.wellid   
   form = GPCoiltubingForm(request.POST or None, instance=gpcoil_tubing_data)
   if request.method =="POST":  
        form = GPCoiltubingForm(request.POST, request.FILES, instance=gpcoil_tubing_data)       
        gpcoil_tubing_data.fgid = selectedwell.fgid
        gpcoil_tubing_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('gpcoiltubing:list_gpcoil_tubing_data') 
   return render (request, 'gpcoiltubing/gpcoil_tubing_data_form.html', {'form': form})

def update_gpcoil_tubing_data(request, id): 
   gpcoil_tubing_data = GPCoiltubing.objects.get(id=id)  
   form = GPCoiltubingForm(request.POST or None, instance=gpcoil_tubing_data) 
   if request.method =="POST":
        form = GPCoiltubingForm(request.POST, request.FILES, instance=gpcoil_tubing_data)        
        if form.is_valid():
            form.save()           
            return redirect ('gpcoiltubing:list_gpcoil_tubing_data')
   return render (request, 'gpcoiltubing/gpcoil_tubing_data_form.html', {'form': form, 'gpcoil_tubing_data':gpcoil_tubing_data})

def delete_gpcoil_tubing_data(request, id):
   gpcoil_tubing_data = GPCoiltubing.objects.get(id=id)   
   if request.method == 'POST' :
       gpcoil_tubing_data.delete()
       return redirect ('gpcoiltubing:list_gpcoil_tubing_data')
   return render (request, 'gpcoiltubing/gpcoil_tubing_data_confirm_delete.html', {'gpcoil_tubing_data':gpcoil_tubing_data})

def detail_gpcoil_tubing_data(request, id): 
    oilgain =0
    selectedwell = SelectedGasProducer.objects.first()    
    gpcoil_tubing_data = GPCoiltubing.objects.get(id=id)
    preliquid = gpcoil_tubing_data.pre_ct_liquid  
    postliquid = gpcoil_tubing_data.post_ct_liquid
    liquidgain = postliquid-preliquid
    prewater = gpcoil_tubing_data.pre_ct_WC  
    postwater = gpcoil_tubing_data.post_ct_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*gpcoil_tubing_data.pre_ct_GOR)/1000
    postgas = round(postoil * gpcoil_tubing_data.post_ct_GOR)/1000
    expoil = round(gpcoil_tubing_data.expected_liquid *(1-gpcoil_tubing_data.expected_WC/100) ,2)
    expgas = round(expoil * gpcoil_tubing_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = gpcoil_tubing_data.pre_ct_GOR 
    postgor = gpcoil_tubing_data.post_ct_GOR
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
    dat= gpcoil_tubing_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = GPCoiltubingForm(request.POST or None, instance=gpcoil_tubing_data) 
    return render (request, 'gpcoiltubing/gpcoil_tubing_data_detail.html', {'form': form, 'gpcoil_tubing_data':gpcoil_tubing_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})

   

