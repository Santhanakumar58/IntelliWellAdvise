from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasInjector.models import SelectedGasInjector
from .models import GIRigless
from .forms import GIRiglessForm
from .utils import get_plot1, get_plot


# Create your views here.
def list_girigless_data(request):
    selectedwell = SelectedGasInjector.objects.first()   
    girigless_datas = GIRigless.objects.filter(giwellid =selectedwell.wellid).all()   
    x=[x1.end_Date for x1 in girigless_datas] 
    y=[(y.post_girigless_liquid-y.pre_girigless_liquid) for y in girigless_datas]
    y1=[round((y1.post_girigless_liquid * (1-y1.post_girigless_WC/100)-y1.pre_girigless_liquid * (1-y1.pre_girigless_WC/100)),2) for y1 in girigless_datas]
    y2=[round((y2.post_girigless_GOR * (y2.post_girigless_liquid * (1-y2.post_girigless_WC/100))/1000-y2.pre_girigless_GOR * (y2.pre_girigless_liquid * (1-y2.pre_girigless_WC/100))/1000 ),2)  for y2 in girigless_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'girigless/girigless.html', {'girigless_datas': girigless_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain})  

def create_girigless_data(request):    
   girigless_data = GIRigless()
   selectedwell = SelectedGasInjector.objects.first()  
   girigless_data.fgid = selectedwell.fgid
   girigless_data.wellid = selectedwell.wellid   
   form = GIRiglessForm(request.POST or None, instance=girigless_data)
   if request.method =="POST":  
        form = GIRiglessForm(request.POST, request.FILES, instance=girigless_data)       
        girigless_data.fgid = selectedwell.fgid
        girigless_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('girigless:list_girigless_data') 
   return render (request, 'girigless/girigless_form.html', {'form': form})

def update_girigless_data(request, id): 
   girigless_data = GIRigless.objects.get(id=id)  
   form = GIRiglessForm(request.POST or None, instance=girigless_data) 
   if request.method =="POST":
        form = GIRiglessForm(request.POST, request.FILES, instance=girigless_data)        
        if form.is_valid():
            form.save()           
            return redirect ('girigless:list_girigless_data')
   return render (request, 'girigless/girigless_form.html', {'form': form, 'girigless_data':girigless_data})

def delete_girigless_data(request, id):
   girigless_data = GIRigless.objects.get(id=id)   
   if request.method == 'POST' :
       girigless_data.delete()
       return redirect ('girigless:list_girigless_data')
   return render (request, 'girigless/girigless_confirm_delete.html', {'girigless_data':girigless_data})


def detail_girigless_data(request, id): 
    oilgain =0
    selectedwell = SelectedGasInjector.objects.first()    
    girigless_data = GIRigless.objects.get(id=id)
    preliquid = girigless_data.pre_girigless_liquid  
    postliquid = girigless_data.post_girigless_liquid
    liquidgain = postliquid-preliquid
    prewater = girigless_data.pre_girigless_WC  
    postwater = girigless_data.post_girigless_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*girigless_data.pre_girigless_GOR)/1000
    postgas = round(postoil * girigless_data.post_girigless_GOR)/1000
    expoil = round(girigless_data.expected_liquid *(1-girigless_data.expected_WC/100) ,2)
    expgas = round(expoil * girigless_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = girigless_data.pre_girigless_GOR 
    postgor = girigless_data.post_girigless_GOR
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
    dat= girigless_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = GIRiglessForm(request.POST or None, instance=girigless_data) 
    return render (request, 'girigless/girigless_detail.html', {'form': form, 'girigless_data':girigless_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})

