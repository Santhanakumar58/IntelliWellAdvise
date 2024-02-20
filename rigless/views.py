from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedOilProducer.models import SelectedOilProducer
from .models import Rigless
from .forms import RiglessForm
from .utils import get_plot1, get_plot


# Create your views here.
def list_rigless_data(request):
    selectedwell = SelectedOilProducer.objects.first()   
    rigless_datas = Rigless.objects.filter(wellid =selectedwell.wellid).all()   
    x=[x1.end_Date for x1 in rigless_datas] 
    y=[(y.post_rigless_liquid-y.pre_rigless_liquid) for y in rigless_datas]
    y1=[round((y1.post_rigless_liquid * (1-y1.post_rigless_WC/100)-y1.pre_rigless_liquid * (1-y1.pre_rigless_WC/100)),2) for y1 in rigless_datas]
    y2=[round((y2.post_rigless_GOR * (y2.post_rigless_liquid * (1-y2.post_rigless_WC/100))/1000-y2.pre_rigless_GOR * (y2.pre_rigless_liquid * (1-y2.pre_rigless_WC/100))/1000 ),2)  for y2 in rigless_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'rigless/rigless.html', {'rigless_datas': rigless_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain})  

def create_rigless_data(request):    
   rigless_data = Rigless()
   selectedwell = SelectedOilProducer.objects.first()  
   rigless_data.fgid = selectedwell.fgid
   rigless_data.wellid = selectedwell.wellid   
   form = RiglessForm(request.POST or None, instance=rigless_data)
   if request.method =="POST":  
        form = RiglessForm(request.POST, request.FILES, instance=rigless_data)       
        rigless_data.fgid = selectedwell.fgid
        rigless_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('rigless:list_rigless_data') 
   return render (request, 'rigless/rigless_form.html', {'form': form})

def update_rigless_data(request, id): 
   rigless_data = Rigless.objects.get(id=id)  
   form = RiglessForm(request.POST or None, instance=rigless_data) 
   if request.method =="POST":
        form = RiglessForm(request.POST, request.FILES, instance=rigless_data)        
        if form.is_valid():
            form.save()           
            return redirect ('rigless:list_rigless_data')
   return render (request, 'rigless/rigless_form.html', {'form': form, 'rigless_data':rigless_data})

def delete_rigless_data(request, id):
   rigless_data = Rigless.objects.get(id=id)   
   if request.method == 'POST' :
       rigless_data.delete()
       return redirect ('rigless:list_rigless_data')
   return render (request, 'rigless/rigless_confirm_delete.html', {'rigless_data':rigless_data})


def detail_rigless_data(request, id): 
    oilgain =0
    selectedwell = SelectedOilProducer.objects.first()    
    rigless_data = Rigless.objects.get(id=id)
    preliquid = rigless_data.pre_rigless_liquid  
    postliquid = rigless_data.post_rigless_liquid
    liquidgain = postliquid-preliquid
    prewater = rigless_data.pre_rigless_WC  
    postwater = rigless_data.post_rigless_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*rigless_data.pre_rigless_GOR)/1000
    postgas = round(postoil * rigless_data.post_rigless_GOR)/1000
    expoil = round(rigless_data.expected_liquid *(1-rigless_data.expected_WC/100) ,2)
    expgas = round(expoil * rigless_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = rigless_data.pre_rigless_GOR 
    postgor = rigless_data.post_rigless_GOR
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
    dat= rigless_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = RiglessForm(request.POST or None, instance=rigless_data) 
    return render (request, 'rigless/rigless_detail.html', {'form': form, 'rigless_data':rigless_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})