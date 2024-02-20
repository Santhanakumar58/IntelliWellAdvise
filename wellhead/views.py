from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedOilProducer.models  import SelectedOilProducer
from .models import Wellhead
from .forms import WellheadForm

# Create your views here.
def list_wh_data(request): 

    selectedwell=SelectedOilProducer.objects.all().first()
    wh_datas = Wellhead.objects.filter(wellid =selectedwell.wellid).all()      
    return render (request, 'wellhead/wellhead_data.html', {'wh_datas': wh_datas} )
  

def create_wh_data(request): 
    selectedwell=SelectedOilProducer.objects.all().first()   
    wh_data = Wellhead()    
    wh_data.fgid = selectedwell.fgid
    wh_data.wellid = selectedwell.wellid   
    form = WellheadForm(request.POST or None, instance=wh_data)
    if request.method =="POST":  
        form = WellheadForm(request.POST, request.FILES, instance=wh_data)       
        wh_data.fgid = selectedwell.fgid
        wh_data.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('wellhead:list_wh_data') 
    return render (request, 'wellhead/wellhead_data_form.html', {'form': form})

def update_wh_data(request, id): 
   wh_data = Wellhead.objects.get(id=id)  
   form = WellheadForm(request.POST or None, instance=wh_data) 
   if request.method =="POST":
        form = WellheadForm(request.POST, request.FILES, instance=wh_data)        
        if form.is_valid():
            form.save()           
            return redirect ('wellhead:list_wh_data')
   return render (request, 'wellhead/wellhead_data_form.html', {'form': form, 'wh_data':wh_data})

def delete_wh_data(request, id):
   wh_data = Wellhead.objects.get(id=id)   
   if request.method == 'POST' :
       wh_data.delete()
       return redirect ('wellhead:list_wh_data')
   return render (request, 'wellhead/wellhead_data_confirm_delete.html', {'wh_data':wh_data})


def detail_wh_data(request, id):      
    wh_data = Wellhead.objects.get(id=id)    
    form = WellheadForm(request.POST or None, instance=wh_data) 
    return render (request, 'wellhead/wellhead_detail.html', {'form': form, 'wh_data':wh_data})



