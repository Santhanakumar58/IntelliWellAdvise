from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedOilProducer.models import SelectedOilProducer
from .models import Stimulation
from .forms import StimulationForm
from .utils import get_plot, get_plot1

# Create your views here.
def list_stimulation_data(request):
    selectedwell = SelectedOilProducer.objects.first()   
    stim_datas = Stimulation.objects.filter(wellid =selectedwell.wellid).all()     
    x=[x1.end_Date for x1 in stim_datas] 
    y=[(y.post_stim_liquid-y.pre_stim_liquid) for y in stim_datas]
    y1=[round((y1.post_stim_liquid * (1-y1.post_stim_WC/100)-y1.pre_stim_liquid * (1-y1.pre_stim_WC/100)),2) for y1 in stim_datas]
    y2=[round((y2.post_stim_GOR * (y2.post_stim_liquid * (1-y2.post_stim_WC/100))/1000-y2.pre_stim_GOR * (y2.pre_stim_liquid * (1-y2.pre_stim_WC/100))/1000 ),2)  for y2 in stim_datas]    
    avgliqgain = 0
    avgoilgain =0
    if y :
        avgliqgain=round(sum(y)/len(y),2)   
    if y1:
        avgoilgain = round(sum(y1)/len(y1),2)
    chart = get_plot(x,y,y1,y2)    
    chart = get_plot(x,y,y1,y2)  
    return render (request, 'stimulation/stimulation.html', {'stim_datas': stim_datas,'chart':chart, 'avgliqgain':avgliqgain,'avgoilgain':avgoilgain  })   

def create_stimulation_data(request):    
   stim_data = Stimulation()
   selectedwell = SelectedOilProducer.objects.first()  
   stim_data.fgid = selectedwell.fgid
   stim_data.wellid = selectedwell.wellid   
   form = StimulationForm(request.POST or None, instance=stim_data)
   if request.method =="POST":  
        form = StimulationForm(request.POST, request.FILES, instance=stim_data)       
        stim_data.fgid = selectedwell.fgid
        stim_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('stimulation:list_stimulation_data') 
   return render (request, 'stimulation/stimulation_form.html', {'form': form})

def update_stimulation_data(request, id): 
   stim_data = Stimulation.objects.get(id=id)  
   form = StimulationForm(request.POST or None, instance=stim_data) 
   if request.method =="POST":
        form = StimulationForm(request.POST, request.FILES, instance=stim_data)        
        if form.is_valid():
            form.save()           
            return redirect ('stimulation:list_stimulation_data')
   return render (request, 'stimulation/stimulation_form.html', {'form': form, 'stim_data':stim_data})

def delete_stimulation_data(request, id):
   stim_data = Stimulation.objects.get(id=id)   
   if request.method == 'POST' :
       stim_data.delete()
       return redirect ('stimulation:list_stimulation_data')
   return render (request, 'stimulation/stimulation_confirm_delete.html', {'stim_data':stim_data})


def detail_stimulation_data(request, id): 
    oilgain =0
    selectedwell = SelectedOilProducer.objects.first()    
    stim_data = Stimulation.objects.get(id=id)
    preliquid = stim_data.pre_stim_liquid  
    postliquid = stim_data.post_stim_liquid
    liquidgain = postliquid-preliquid
    prewater = stim_data.pre_stim_WC  
    postwater = stim_data.post_stim_WC
    watergain = postwater-prewater
    preoil =  round(preliquid*(1.0-prewater/100) ,2)
    postoil = round(postliquid *(1.0-postwater/100) ,2)
    pregas =  round(preoil*stim_data.pre_stim_GOR)/1000
    postgas = round(postoil * stim_data.post_stim_GOR)/1000
    expoil = round(stim_data.expected_liquid *(1-stim_data.expected_WC/100) ,2)
    expgas = round(expoil * stim_data.expected_GOR)/1000
    oilgain = round(postoil-preoil,2)
    gasgain = round(postgas-pregas,2)    
    pregorr = stim_data.pre_stim_GOR 
    postgor = stim_data.post_stim_GOR
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
    dat= stim_data.end_Date
    chart = get_plot1(dat, x1, x2,x3,y1,y2,y3)  
    form = StimulationForm(request.POST or None, instance=stim_data) 
    return render (request, 'stimulation/stimulation_data_detail.html', {'form': form, 'stim_data':stim_data, 
    'liquidgain': liquidgain,'watergain':watergain, 'gorgain': gorgain, 'status':status, 'status1':status1, 'status2':status2, 
    'preoil': preoil, 'postoil': postoil, 'oilgain' :oilgain, 'pregas':pregas, 'postgas': postgas, 'expoil' : expoil, 'expgas': expgas,
    'gasgain':gasgain,'status3':status3, 'status4':status4, 'chart':chart})

