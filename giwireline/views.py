from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasInjector.models import SelectedGasInjector
from .models import GIWireline
from .forms import GIWirelineForm
from .utils import get_plot, get_plot1

# Create your views here.
def list_giwireline_data(request):
    selectedwell = SelectedGasInjector.objects.first()   
    giwireline_datas = GIWireline.objects.filter(giwellid =selectedwell.wellid).all()  
    giwireline_datas.order_by('giend_Date')
    x=[x1.end_Date for x1 in giwireline_datas] 
    y=[(y.post_wl_liquid-y.pre_wl_liquid) for y in giwireline_datas]
    y1=[round((y1.post_wl_liquid * (1-y1.post_wl_WC/100)-y1.pre_wl_liquid * (1-y1.pre_wl_WC/100)),2) for y1 in giwireline_datas]
    y2=[round((y2.post_wl_GOR * (y2.post_wl_liquid * (1-y2.post_wl_WC/100))/1000-y2.pre_wl_GOR * (y2.pre_wl_liquid * (1-y2.pre_wl_WC/100))/1000 ),2)  for y2 in giwireline_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'giwireline/giwireline.html', {'giwireline_datas': giwireline_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain})  
  

def create_giwireline_data(request):    
   giwireline_data = GIWireline()
   selectedwell = SelectedGasInjector.objects.first()  
   giwireline_data.fgid = selectedwell.fgid
   giwireline_data.wellid = selectedwell.wellid   
   form = GIWirelineForm(request.POST or None, instance=giwireline_data)
   if request.method =="POST":  
        form = GIWirelineForm(request.POST, request.FILES, instance=giwireline_data)       
        giwireline_data.fgid = selectedwell.fgid
        giwireline_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('giwireline:list_giwireline_data') 
   return render (request, 'giwireline/giwireline_form.html', {'form': form})

def update_giwireline_data(request, id): 
   giwireline_data = GIWireline.objects.get(id=id)  
   form = GIWirelineForm(request.POST or None, instance=giwireline_data) 
   if request.method =="POST":
        form = GIWirelineForm(request.POST, request.FILES, instance=giwireline_data)        
        if form.is_valid():
            form.save()           
            return redirect ('giwireline:list_giwireline_data')
   return render (request, 'giwireline/giwireline_form.html', {'form': form, 'giwireline_data':giwireline_data})

def delete_giwireline_data(request, id):
   giwireline_data = GIWireline.objects.get(id=id)   
   if request.method == 'POST' :
       giwireline_data.delete()
       return redirect ('giwireline:list_giwireline_data')
   return render (request, 'giwireline/giwireline_confirm_delete.html', {'giwireline_data':giwireline_data})


def detail_giwireline_data(request, id): 
    oilgain =0
    selectedwell = SelectedGasInjector.objects.first()    
    giwireline_data = GIWireline.objects.get(id=id)
    preliquid = giwireline_data.pre_wl_liquid  
    postliquid = giwireline_data.post_wl_liquid
    liquidgain = postliquid-preliquid
    prewater = giwireline_data.pre_wl_WC  
    postwater = giwireline_data.post_wl_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*giwireline_data.pre_wl_GOR)/1000
    postgas = round(postoil * giwireline_data.post_wl_GOR)/1000
    expoil = round(giwireline_data.expected_liquid *(1-giwireline_data.expected_WC/100) ,2)
    expgas = round(expoil * giwireline_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = giwireline_data.pre_wl_GOR 
    postgor = giwireline_data.post_wl_GOR
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
    dat= giwireline_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = GIWirelineForm(request.POST or None, instance=giwireline_data) 
    return render (request, 'giwireline/giwireline_detail.html', {'form': form, 'giwireline_data':giwireline_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})



