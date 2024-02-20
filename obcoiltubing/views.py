from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedObserver.models import SelectedObserver
from .forms import OBCoiltubingForm
from .utils import get_plot, get_plot1
from .models import OBCoiltubing


# Create your views here.
def list_obcoil_tubing_data(request):
    selectedwell = SelectedObserver.objects.first()   
    obcoil_tubing_datas = OBCoiltubing.objects.filter(obwellid =selectedwell.wellid).all()    
    x=[x1.end_Date for x1 in obcoil_tubing_datas] 
    y=[(y.post_ct_liquid-y.pre_ct_liquid) for y in obcoil_tubing_datas]
    y1=[round((y1.post_ct_liquid * (1-y1.post_ct_WC/100)-y1.pre_ct_liquid * (1-y1.pre_ct_WC/100)),2) for y1 in obcoil_tubing_datas]
    y2=[round((y2.post_ct_GOR * (y2.post_ct_liquid * (1-y2.post_ct_WC/100))/1000-y2.pre_ct_GOR * (y2.pre_ct_liquid * (1-y2.pre_ct_WC/100))/1000 ),2)  for y2 in obcoil_tubing_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'obcoiltubing/obcoil_tubing_data.html', {'obcoil_tubing_datas': obcoil_tubing_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain  })   
 
def create_obcoil_tubing_data(request):    
   obcoil_tubing_data = OBCoiltubing()
   selectedwell = SelectedObserver.objects.first()  
   obcoil_tubing_data.fgid = selectedwell.fgid
   obcoil_tubing_data.wellid = selectedwell.wellid   
   form = OBCoiltubingForm(request.POST or None, instance=obcoil_tubing_data)
   if request.method =="POST":  
        form = OBCoiltubingForm(request.POST, request.FILES, instance=obcoil_tubing_data)       
        obcoil_tubing_data.fgid = selectedwell.fgid
        obcoil_tubing_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('obcoiltubing:list_obcoil_tubing_data') 
   return render (request, 'obcoiltubing/obcoil_tubing_data_form.html', {'form': form})

def update_obcoil_tubing_data(request, id): 
   obcoil_tubing_data = OBCoiltubing.objects.get(id=id)  
   form = OBCoiltubingForm(request.POST or None, instance=obcoil_tubing_data) 
   if request.method =="POST":
        form = OBCoiltubingForm(request.POST, request.FILES, instance=obcoil_tubing_data)        
        if form.is_valid():
            form.save()           
            return redirect ('obcoiltubing:list_obcoil_tubing_data')
   return render (request, 'obcoiltubing/obcoil_tubing_data_form.html', {'form': form, 'obcoil_tubing_data':obcoil_tubing_data})

def delete_obcoil_tubing_data(request, id):
   obcoil_tubing_data = OBCoiltubing.objects.get(id=id)   
   if request.method == 'POST' :
       obcoil_tubing_data.delete()
       return redirect ('obcoiltubing:list_obcoil_tubing_data')
   return render (request, 'obcoiltubing/obcoil_tubing_data_confirm_delete.html', {'obcoil_tubing_data':obcoil_tubing_data})

def detail_obcoil_tubing_data(request, id): 
    oilgain =0
    selectedwell = SelectedObserver.objects.first()    
    obcoil_tubing_data = OBCoiltubing.objects.get(id=id)
    preliquid = obcoil_tubing_data.pre_ct_liquid  
    postliquid = obcoil_tubing_data.post_ct_liquid
    liquidgain = postliquid-preliquid
    prewater = obcoil_tubing_data.pre_ct_WC  
    postwater = obcoil_tubing_data.post_ct_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*obcoil_tubing_data.pre_ct_GOR)/1000
    postgas = round(postoil * obcoil_tubing_data.post_ct_GOR)/1000
    expoil = round(obcoil_tubing_data.expected_liquid *(1-obcoil_tubing_data.expected_WC/100) ,2)
    expgas = round(expoil * obcoil_tubing_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = obcoil_tubing_data.pre_ct_GOR 
    postgor = obcoil_tubing_data.post_ct_GOR
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
    dat= obcoil_tubing_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = OBCoiltubingForm(request.POST or None, instance=obcoil_tubing_data) 
    return render (request, 'obcoiltubing/obcoil_tubing_data_detail.html', {'form': form, 'obcoil_tubing_data':obcoil_tubing_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})

   


