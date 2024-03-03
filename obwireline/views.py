from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedObserver.models import SelectedObserver
from .models import OBWireline
from .forms import OBWirelineForm
from .utils import get_plot, get_plot1

# Create your views here.
def list_obwireline_data(request):
    selectedwell = SelectedObserver.objects.first()   
    obwireline_datas = OBWireline.objects.filter(obwellid =selectedwell.wellid).all()  
    obwireline_datas.order_by('obend_Date')
    x=[x1.end_Date for x1 in obwireline_datas] 
    y=[(y.post_wl_liquid-y.pre_wl_liquid) for y in obwireline_datas]
    y1=[round((y1.post_wl_liquid * (1-y1.post_wl_WC/100)-y1.pre_wl_liquid * (1-y1.pre_wl_WC/100)),2) for y1 in obwireline_datas]
    y2=[round((y2.post_wl_GOR * (y2.post_wl_liquid * (1-y2.post_wl_WC/100))/1000-y2.pre_wl_GOR * (y2.pre_wl_liquid * (1-y2.pre_wl_WC/100))/1000 ),2)  for y2 in obwireline_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'obwireline/obwireline.html', {'obwireline_datas': obwireline_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain})  
  

def create_obwireline_data(request):    
   obwireline_data = OBWireline()
   selectedwell = SelectedObserver.objects.first()  
   obwireline_data.fgid = selectedwell.fgid
   obwireline_data.wellid = selectedwell.wellid   
   form = OBWirelineForm(request.POST or None, instance=obwireline_data)
   if request.method =="POST":  
        form = OBWirelineForm(request.POST, request.FILES, instance=obwireline_data)       
        obwireline_data.fgid = selectedwell.fgid
        obwireline_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('obwireline:list_obwireline_data') 
   return render (request, 'obwireline/obwireline_form.html', {'form': form})

def update_obwireline_data(request, id): 
   obwireline_data = OBWireline.objects.get(id=id)  
   form = OBWirelineForm(request.POST or None, instance=obwireline_data) 
   if request.method =="POST":
        form = OBWirelineForm(request.POST, request.FILES, instance=obwireline_data)        
        if form.is_valid():
            form.save()           
            return redirect ('obwireline:list_obwireline_data')
   return render (request, 'obwireline/obwireline_form.html', {'form': form, 'obwireline_data':obwireline_data})

def delete_obwireline_data(request, id):
   obwireline_data = OBWireline.objects.get(id=id)   
   if request.method == 'POST' :
       obwireline_data.delete()
       return redirect ('obwireline:list_obwireline_data')
   return render (request, 'obwireline/obwireline_confirm_delete.html', {'obwireline_data':obwireline_data})


def detail_obwireline_data(request, id): 
    oilgain =0
    selectedwell = SelectedObserver.objects.first()    
    obwireline_data = OBWireline.objects.get(id=id)
    preliquid = obwireline_data.pre_wl_liquid  
    postliquid = obwireline_data.post_wl_liquid
    liquidgain = postliquid-preliquid
    prewater = obwireline_data.pre_wl_WC  
    postwater = obwireline_data.post_wl_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*obwireline_data.pre_wl_GOR)/1000
    postgas = round(postoil * obwireline_data.post_wl_GOR)/1000
    expoil = round(obwireline_data.expected_liquid *(1-obwireline_data.expected_WC/100) ,2)
    expgas = round(expoil * obwireline_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = obwireline_data.pre_wl_GOR 
    postgor = obwireline_data.post_wl_GOR
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
    dat= obwireline_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = OBWirelineForm(request.POST or None, instance=obwireline_data) 
    return render (request, 'obwireline/obwireline_detail.html', {'form': form, 'obwireline_data':obwireline_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})


