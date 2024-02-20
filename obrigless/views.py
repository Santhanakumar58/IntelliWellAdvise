from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedObserver.models import SelectedObserver
from .models import OBRigless
from .forms import OBRiglessForm
from .utils import get_plot1, get_plot


# Create your views here.
def list_obrigless_data(request):
    selectedwell = SelectedObserver.objects.first()   
    obrigless_datas = OBRigless.objects.filter(obwellid =selectedwell.wellid).all()   
    x=[x1.end_Date for x1 in obrigless_datas] 
    y=[(y.post_obrigless_liquid-y.pre_obrigless_liquid) for y in obrigless_datas]
    y1=[round((y1.post_obrigless_liquid * (1-y1.post_obrigless_WC/100)-y1.pre_obrigless_liquid * (1-y1.pre_obrigless_WC/100)),2) for y1 in obrigless_datas]
    y2=[round((y2.post_obrigless_GOR * (y2.post_obrigless_liquid * (1-y2.post_obrigless_WC/100))/1000-y2.pre_obrigless_GOR * (y2.pre_obrigless_liquid * (1-y2.pre_obrigless_WC/100))/1000 ),2)  for y2 in obrigless_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2) 
    return render (request, 'obrigless/obrigless.html', {'obrigless_datas': obrigless_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain})  

def create_obrigless_data(request):    
   obrigless_data = OBRigless()
   selectedwell = SelectedObserver.objects.first()  
   obrigless_data.fgid = selectedwell.fgid
   obrigless_data.wellid = selectedwell.wellid   
   form = OBRiglessForm(request.POST or None, instance=obrigless_data)
   if request.method =="POST":  
        form = OBRiglessForm(request.POST, request.FILES, instance=obrigless_data)       
        obrigless_data.fgid = selectedwell.fgid
        obrigless_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('obrigless:list_obrigless_data') 
   return render (request, 'obrigless/obrigless_form.html', {'form': form})

def update_obrigless_data(request, id): 
   obrigless_data = OBRigless.objects.get(id=id)  
   form = OBRiglessForm(request.POST or None, instance=obrigless_data) 
   if request.method =="POST":
        form = OBRiglessForm(request.POST, request.FILES, instance=obrigless_data)        
        if form.is_valid():
            form.save()           
            return redirect ('obrigless:list_obrigless_data')
   return render (request, 'obrigless/obrigless_form.html', {'form': form, 'obrigless_data':obrigless_data})

def delete_obrigless_data(request, id):
   obrigless_data = OBRigless.objects.get(id=id)   
   if request.method == 'POST' :
       obrigless_data.delete()
       return redirect ('obrigless:list_obrigless_data')
   return render (request, 'obrigless/obrigless_confirm_delete.html', {'obrigless_data':obrigless_data})


def detail_obrigless_data(request, id): 
    oilgain =0
    selectedwell = SelectedObserver.objects.first()    
    obrigless_data = OBRigless.objects.get(id=id)
    preliquid = obrigless_data.pre_obrigless_liquid  
    postliquid = obrigless_data.post_obrigless_liquid
    liquidgain = postliquid-preliquid
    prewater = obrigless_data.pre_obrigless_WC  
    postwater = obrigless_data.post_obrigless_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*obrigless_data.pre_obrigless_GOR)/1000
    postgas = round(postoil * obrigless_data.post_obrigless_GOR)/1000
    expoil = round(obrigless_data.expected_liquid *(1-obrigless_data.expected_WC/100) ,2)
    expgas = round(expoil * obrigless_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)
    print(oilgain)
    pregorr = obrigless_data.pre_obrigless_GOR 
    postgor = obrigless_data.post_obrigless_GOR
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
    dat= obrigless_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = OBRiglessForm(request.POST or None, instance=obrigless_data) 
    return render (request, 'obrigless/obrigless_detail.html', {'form': form, 'obrigless_data':obrigless_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})

