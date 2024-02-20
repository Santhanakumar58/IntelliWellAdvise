from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasProducer.models import SelectedGasProducer
from .models import GPRigless
from .forms import GPRiglessForm
from .utils import get_plot1, get_plot


# Create your views here.
def list_gprigless_data(request):
    selectedwell = SelectedGasProducer.objects.first()   
    gprigless_datas = GPRigless.objects.filter(gpwellid =selectedwell.wellid).all()   
    x=[x1.end_Date for x1 in gprigless_datas] 
    y=[(y.post_gprigless_liquid-y.pre_gprigless_liquid) for y in gprigless_datas]
    y1=[round((y1.post_gprigless_liquid * (1-y1.post_gprigless_WC/100)-y1.pre_gprigless_liquid * (1-y1.pre_gprigless_WC/100)),2) for y1 in gprigless_datas]
    y2=[round((y2.post_gprigless_GOR * (y2.post_gprigless_liquid * (1-y2.post_gprigless_WC/100))/1000-y2.pre_gprigless_GOR * (y2.pre_gprigless_liquid * (1-y2.pre_gprigless_WC/100))/1000 ),2)  for y2 in gprigless_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'gprigless/gprigless.html', {'gprigless_datas': gprigless_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain})  

def create_gprigless_data(request):    
   gprigless_data = GPRigless()
   selectedwell = SelectedGasProducer.objects.first()  
   gprigless_data.fgid = selectedwell.fgid
   gprigless_data.wellid = selectedwell.wellid   
   form = GPRiglessForm(request.POST or None, instance=gprigless_data)
   if request.method =="POST":  
        form = GPRiglessForm(request.POST, request.FILES, instance=gprigless_data)       
        gprigless_data.fgid = selectedwell.fgid
        gprigless_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('gprigless:list_gprigless_data') 
   return render (request, 'gprigless/gprigless_form.html', {'form': form})

def update_gprigless_data(request, id): 
   gprigless_data = GPRigless.objects.get(id=id)  
   form = GPRiglessForm(request.POST or None, instance=gprigless_data) 
   if request.method =="POST":
        form = GPRiglessForm(request.POST, request.FILES, instance=gprigless_data)        
        if form.is_valid():
            form.save()           
            return redirect ('gprigless:list_gprigless_data')
   return render (request, 'gprigless/gprigless_form.html', {'form': form, 'gprigless_data':gprigless_data})

def delete_gprigless_data(request, id):
   gprigless_data = GPRigless.objects.get(id=id)   
   if request.method == 'POST' :
       gprigless_data.delete()
       return redirect ('gprigless:list_gprigless_data')
   return render (request, 'gprigless/gprigless_confirm_delete.html', {'gprigless_data':gprigless_data})


def detail_gprigless_data(request, id): 
    oilgain =0
    selectedwell = SelectedGasProducer.objects.first()    
    gprigless_data = GPRigless.objects.get(id=id)
    preliquid = gprigless_data.pre_gprigless_liquid  
    postliquid = gprigless_data.post_gprigless_liquid
    liquidgain = postliquid-preliquid
    prewater = gprigless_data.pre_gprigless_WC  
    postwater = gprigless_data.post_gprigless_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*gprigless_data.pre_gprigless_GOR)/1000
    postgas = round(postoil * gprigless_data.post_gprigless_GOR)/1000
    expoil = round(gprigless_data.expected_liquid *(1-gprigless_data.expected_WC/100) ,2)
    expgas = round(expoil * gprigless_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = gprigless_data.pre_gprigless_GOR 
    postgor = gprigless_data.post_gprigless_GOR
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
    dat= gprigless_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = GPRiglessForm(request.POST or None, instance=gprigless_data) 
    return render (request, 'gprigless/gprigless_detail.html', {'form': form, 'gprigless_data':gprigless_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})
