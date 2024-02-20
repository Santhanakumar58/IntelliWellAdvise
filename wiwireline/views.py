from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedWaterInjector.models import SelectedWaterInjector
from .models import WIWireline
from .forms import WIWirelineForm
from .utils import get_plot, get_plot1

# Create your views here.
def list_wiwireline_data(request):
    selectedwell = SelectedWaterInjector.objects.first()   
    wiwireline_datas = WIWireline.objects.filter(wellid =selectedwell.wellid).all()  
    wiwireline_datas.order_by('end_Date')
    x=[x1.end_Date for x1 in wiwireline_datas] 
    y=[(y.post_wl_liquid-y.pre_wl_liquid) for y in wiwireline_datas]
    y1=[round((y1.post_wl_liquid * (1-y1.post_wl_WC/100)-y1.pre_wl_liquid * (1-y1.pre_wl_WC/100)),2) for y1 in wiwireline_datas]
    y2=[round((y2.post_wl_GOR * (y2.post_wl_liquid * (1-y2.post_wl_WC/100))/1000-y2.pre_wl_GOR * (y2.pre_wl_liquid * (1-y2.pre_wl_WC/100))/1000 ),2)  for y2 in wiwireline_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'wiwireline/wiwireline.html', {'wiwireline_datas': wiwireline_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain})  
  

def create_wiwireline_data(request):    
   wiwireline_data = WIWireline()
   selectedwell = SelectedWaterInjector.objects.first()  
   wiwireline_data.fgid = selectedwell.fgid
   wiwireline_data.wellid = selectedwell.wellid   
   form = WIWirelineForm(request.POST or None, instance=wiwireline_data)
   if request.method =="POST":  
        form = WIWirelineForm(request.POST, request.FILES, instance=wiwireline_data)       
        wiwireline_data.fgid = selectedwell.fgid
        wiwireline_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('wiwireline:list_wiwireline_data') 
   return render (request, 'wiwireline/wiwireline_form.html', {'form': form})

def update_wiwireline_data(request, id): 
   wiwireline_data = WIWireline.objects.get(id=id)  
   form = WIWirelineForm(request.POST or None, instance=wiwireline_data) 
   if request.method =="POST":
        form = WIWirelineForm(request.POST, request.FILES, instance=wiwireline_data)        
        if form.is_valid():
            form.save()           
            return redirect ('wiwireline:list_wiwireline_data')
   return render (request, 'wiwireline/wiwireline_form.html', {'form': form, 'wiwireline_data':wiwireline_data})

def delete_wiwireline_data(request, id):
   wiwireline_data = WIWireline.objects.get(id=id)   
   if request.method == 'POST' :
       wiwireline_data.delete()
       return redirect ('wiwireline:list_wiwireline_data')
   return render (request, 'wiwireline/wiwireline_confirm_delete.html', {'wiwireline_data':wiwireline_data})


def detail_wiwireline_data(request, id): 
    oilgain =0
    selectedwell = SelectedWaterInjector.objects.first()    
    wiwireline_data = WIWireline.objects.get(id=id)
    preliquid = wiwireline_data.pre_wl_liquid  
    postliquid = wiwireline_data.post_wl_liquid
    liquidgain = postliquid-preliquid
    prewater = wiwireline_data.pre_wl_WC  
    postwater = wiwireline_data.post_wl_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*wiwireline_data.pre_wl_GOR)/1000
    postgas = round(postoil * wiwireline_data.post_wl_GOR)/1000
    expoil = round(wiwireline_data.expected_liquid *(1-wiwireline_data.expected_WC/100) ,2)
    expgas = round(expoil * wiwireline_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = wiwireline_data.pre_wl_GOR 
    postgor = wiwireline_data.post_wl_GOR
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
    dat= wiwireline_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = WIWirelineForm(request.POST or None, instance=wiwireline_data) 
    return render (request, 'wiwireline/wiwireline_detail.html', {'form': form, 'wiwireline_data':wiwireline_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})



