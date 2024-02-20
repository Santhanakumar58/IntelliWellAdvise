from django.shortcuts import render
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasInjector.models import SelectedGasInjector
from .models import GISlickline
from .forms import GISlicklineForm
from .utils import get_plot, get_plot1

# Create your views here.
def list_gislickline_data(request):
    selectedwell = SelectedGasInjector.objects.first()   
    slick_datas = GISlickline.objects.filter(giwellid =selectedwell.wellid).all()   
    print (slick_datas)  
    x=[x.start_Date for x in slick_datas] 
    y=[(y.post_slick_liquid-y.pre_slick_liquid) for y in slick_datas]
    y1=[round((y1.post_slick_liquid * (1-y1.post_slick_WC/100)-y1.pre_slick_liquid * (1-y1.pre_slick_WC/100)),2) for y1 in slick_datas]
    y2=[round((y2.post_slick_GOR * (y2.post_slick_liquid * (1-y2.post_slick_WC/100))/1000-y2.pre_slick_GOR * (y2.pre_slick_liquid * (1-y2.pre_slick_WC/100))/1000 ),2)  for y2 in slick_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2)    
    
    return render (request, 'gislickline/gislickline.html', {'slick_datas': slick_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain  })   

def create_gislickline_data(request):    
   slick_data = GISlickline()
   selectedwell = SelectedGasInjector.objects.first()  
   slick_data.fgid = selectedwell.fgid
   slick_data.wellid = selectedwell.wellid   
   form = GISlicklineForm(request.POST or None, instance=slick_data)
   if request.method =="POST":  
        form = GISlicklineForm(request.POST, request.FILES, instance=slick_data)       
        slick_data.fgid = selectedwell.fgid
        slick_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('gislickline:list_gislickline_data') 
   return render (request, 'gislickline/gislickline_form.html', {'form': form})

def update_gislickline_data(request, id): 
   slick_data = GISlickline.objects.get(id=id)  
   form = GISlicklineForm(request.POST or None, instance=slick_data) 
   if request.method =="POST":
        form = GISlicklineForm(request.POST, request.FILES, instance=slick_data)        
        if form.is_valid():
            form.save()           
            return redirect ('gislickline:list_gislickline_data')
   return render (request, 'gislickline/gislickline_form.html', {'form': form, 'slick_data':slick_data})

def delete_gislickline_data(request, id):
   slick_data = GISlickline.objects.get(id=id)   
   if request.method == 'POST' :
       slick_data.delete()
       return redirect ('gislickline:list_gislickline_data')
   return render (request, 'gislickline/gislickline_confirm_delete.html', {'slick_data':slick_data})


def detail_gislickline_data(request, id): 
    oilgain =0
    selectedwell = SelectedGasInjector.objects.first()    
    slick_data = GISlickline.objects.get(id=id)
    preliquid = slick_data.pre_slick_liquid  
    postliquid = slick_data.post_slick_liquid
    liquidgain = postliquid-preliquid
    prewater = slick_data.pre_slick_WC  
    postwater = slick_data.post_slick_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*slick_data.pre_slick_GOR)/1000
    postgas = round(postoil * slick_data.post_slick_GOR)/1000
    expoil = round(slick_data.expected_liquid *(1-slick_data.expected_WC/100) ,2)
    expgas = round(expoil * slick_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)    
    pregorr = slick_data.pre_slick_GOR 
    postgor = slick_data.post_slick_GOR
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
    dat= slick_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = GISlicklineForm(request.POST or None, instance=slick_data) 
    return render (request, 'gislickline/gislickline_data_detail.html', {'form': form, 'slick_data':slick_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})


