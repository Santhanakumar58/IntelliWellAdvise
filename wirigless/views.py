from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedWaterInjector.models import SelectedWaterInjector
from .models import WIRigless
from .forms import WIRiglessForm
from .utils import get_plot1, get_plot


# Create your views here.
def list_wirigless_data(request):
    selectedwell = SelectedWaterInjector.objects.first()   
    wirigless_datas = WIRigless.objects.filter(wellid =selectedwell.wellid).all()   
    x=[x1.end_Date for x1 in wirigless_datas] 
    y=[(y.post_wirigless_liquid-y.pre_wirigless_liquid) for y in wirigless_datas]
    y1=[round((y1.post_wirigless_liquid * (1-y1.post_wirigless_WC/100)-y1.pre_wirigless_liquid * (1-y1.pre_wirigless_WC/100)),2) for y1 in wirigless_datas]
    y2=[round((y2.post_wirigless_GOR * (y2.post_wirigless_liquid * (1-y2.post_wirigless_WC/100))/1000-y2.pre_wirigless_GOR * (y2.pre_wirigless_liquid * (1-y2.pre_wirigless_WC/100))/1000 ),2)  for y2 in wirigless_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'wirigless/wirigless.html', {'wirigless_datas': wirigless_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain})  

def create_wirigless_data(request):    
   wirigless_data = WIRigless()
   selectedwell = SelectedWaterInjector.objects.first()  
   wirigless_data.fgid = selectedwell.fgid
   wirigless_data.wellid = selectedwell.wellid   
   form = WIRiglessForm(request.POST or None, instance=wirigless_data)
   if request.method =="POST":  
        form = WIRiglessForm(request.POST, request.FILES, instance=wirigless_data)       
        wirigless_data.fgid = selectedwell.fgid
        wirigless_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('wirigless:list_wirigless_data') 
   return render (request, 'wirigless/wirigless_form.html', {'form': form})

def update_wirigless_data(request, id): 
   wirigless_data = WIRigless.objects.get(id=id)  
   form = WIRiglessForm(request.POST or None, instance=wirigless_data) 
   if request.method =="POST":
        form = WIRiglessForm(request.POST, request.FILES, instance=wirigless_data)        
        if form.is_valid():
            form.save()           
            return redirect ('wirigless:list_wirigless_data')
   return render (request, 'wirigless/wirigless_form.html', {'form': form, 'wirigless_data':wirigless_data})

def delete_wirigless_data(request, id):
   wirigless_data = WIRigless.objects.get(id=id)   
   if request.method == 'POST' :
       wirigless_data.delete()
       return redirect ('wirigless:list_wirigless_data')
   return render (request, 'wirigless/wirigless_confirm_delete.html', {'wirigless_data':wirigless_data})


def detail_wirigless_data(request, id): 
    oilgain =0
    selectedwell = SelectedWaterInjector.objects.first()    
    wirigless_data = WIRigless.objects.get(id=id)
    preliquid = wirigless_data.pre_wirigless_liquid  
    postliquid = wirigless_data.post_wirigless_liquid
    liquidgain = postliquid-preliquid
    prewater = wirigless_data.pre_wirigless_WC  
    postwater = wirigless_data.post_wirigless_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*wirigless_data.pre_wirigless_GOR)/1000
    postgas = round(postoil * wirigless_data.post_wirigless_GOR)/1000
    expoil = round(wirigless_data.expected_liquid *(1-wirigless_data.expected_WC/100) ,2)
    expgas = round(expoil * wirigless_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = wirigless_data.pre_wirigless_GOR 
    postgor = wirigless_data.post_wirigless_GOR
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
    dat= wirigless_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = WIRiglessForm(request.POST or None, instance=wirigless_data) 
    return render (request, 'wirigless/wirigless_detail.html', {'form': form, 'wirigless_data':wirigless_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})
