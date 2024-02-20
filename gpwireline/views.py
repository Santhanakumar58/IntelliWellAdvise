from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasProducer.models import SelectedGasProducer
from .models import GPWireline
from .forms import GPWirelineForm
from .utils import get_plot, get_plot1

# Create your views here.
def list_gpwireline_data(request):
    selectedwell = SelectedGasProducer.objects.first()   
    gpwireline_datas = GPWireline.objects.filter(gpwellid =selectedwell.wellid).all()  
    gpwireline_datas.order_by('gpend_Date')
    x=[x1.end_Date for x1 in gpwireline_datas] 
    y=[(y.post_wl_liquid-y.pre_wl_liquid) for y in gpwireline_datas]
    y1=[round((y1.post_wl_liquid * (1-y1.post_wl_WC/100)-y1.pre_wl_liquid * (1-y1.pre_wl_WC/100)),2) for y1 in gpwireline_datas]
    y2=[round((y2.post_wl_GOR * (y2.post_wl_liquid * (1-y2.post_wl_WC/100))/1000-y2.pre_wl_GOR * (y2.pre_wl_liquid * (1-y2.pre_wl_WC/100))/1000 ),2)  for y2 in gpwireline_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'gpwireline/gpwireline.html', {'gpwireline_datas': gpwireline_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain})  
  

def create_gpwireline_data(request):    
   gpwireline_data = GPWireline()
   selectedwell = SelectedGasProducer.objects.first()  
   gpwireline_data.fgid = selectedwell.fgid
   gpwireline_data.wellid = selectedwell.wellid   
   form = GPWirelineForm(request.POST or None, instance=gpwireline_data)
   if request.method =="POST":  
        form = GPWirelineForm(request.POST, request.FILES, instance=gpwireline_data)       
        gpwireline_data.fgid = selectedwell.fgid
        gpwireline_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('gpwireline:list_gpwireline_data') 
   return render (request, 'gpwireline/gpwireline_form.html', {'form': form})

def update_gpwireline_data(request, id): 
   gpwireline_data = GPWireline.objects.get(id=id)  
   form = GPWirelineForm(request.POST or None, instance=gpwireline_data) 
   if request.method =="POST":
        form = GPWirelineForm(request.POST, request.FILES, instance=gpwireline_data)        
        if form.is_valid():
            form.save()           
            return redirect ('gpwireline:list_gpwireline_data')
   return render (request, 'gpwireline/gpwireline_form.html', {'form': form, 'gpwireline_data':gpwireline_data})

def delete_gpwireline_data(request, id):
   gpwireline_data = GPWireline.objects.get(id=id)   
   if request.method == 'POST' :
       gpwireline_data.delete()
       return redirect ('gpwireline:list_gpwireline_data')
   return render (request, 'gpwireline/gpwireline_confirm_delete.html', {'gpwireline_data':gpwireline_data})


def detail_gpwireline_data(request, id): 
    oilgain =0
    selectedwell = SelectedGasProducer.objects.first()    
    gpwireline_data = GPWireline.objects.get(id=id)
    preliquid = gpwireline_data.pre_wl_liquid  
    postliquid = gpwireline_data.post_wl_liquid
    liquidgain = postliquid-preliquid
    prewater = gpwireline_data.pre_wl_WC  
    postwater = gpwireline_data.post_wl_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*gpwireline_data.pre_wl_GOR)/1000
    postgas = round(postoil * gpwireline_data.post_wl_GOR)/1000
    expoil = round(gpwireline_data.expected_liquid *(1-gpwireline_data.expected_WC/100) ,2)
    expgas = round(expoil * gpwireline_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = gpwireline_data.pre_wl_GOR 
    postgor = gpwireline_data.post_wl_GOR
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
    dat= gpwireline_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = GPWirelineForm(request.POST or None, instance=gpwireline_data) 
    return render (request, 'gpwireline/gpwireline_detail.html', {'form': form, 'gpwireline_data':gpwireline_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})


