from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedWaterInjector.models  import SelectedWaterInjector
from .models import WIWellhead
from .forms import WIWellheadForm

# Create your views here.
def list_wiwellhead(request): 
    selectedwell=SelectedWaterInjector.objects.all().first()
    wiwellheads = WIWellhead.objects.filter(wiwellid =selectedwell.wellid).all()      
    return render (request, 'wiwellhead/wiwellhead_data.html', {'wiwellheads': wiwellheads} )
  

def create_wiwellhead(request): 
    selectedwell=SelectedWaterInjector.objects.all().first()   
    wiwellhead = WIWellhead()    
    wiwellhead.fgid = selectedwell.fgid
    wiwellhead.wellid = selectedwell.wellid   
    form = WIWellheadForm(request.POST or None, instance=wiwellhead)
    if request.method =="POST":  
        form = WIWellheadForm(request.POST, request.FILES, instance=wiwellhead)       
        wiwellhead.fgid = selectedwell.fgid
        wiwellhead.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('wiwellhead:list_wiwellhead') 
    return render (request, 'wiwellhead/wiwellhead_data_form.html', {'form': form})

def update_wiwellhead(request, id): 
   wiwellhead = WIWellhead.objects.get(id=id)  
   form = WIWellheadForm(request.POST or None, instance=wiwellhead) 
   if request.method =="POST":
        form = WIWellheadForm(request.POST, request.FILES, instance=wiwellhead)        
        if form.is_valid():
            form.save()           
            return redirect ('wiwellhead:list_wiwellhead')
   return render (request, 'wiwellhead/wiwellhead_data_form.html', {'form': form, 'wiwellhead':wiwellhead})

def delete_wiwellhead(request, id):
   wiwellhead = WIWellhead.objects.get(id=id)   
   if request.method == 'POST' :
       wiwellhead.delete()
       return redirect ('wiwellhead:list_wiwellhead')
   return render (request, 'wiwellhead/wiwellhead_data_confirm_delete.html', {'wiwellhead':wiwellhead})


def detail_wiwellhead(request, id):      
    wiwellhead = WIWellhead.objects.get(id=id)    
    form = WIWellheadForm(request.POST or None, instance=wiwellhead) 
    return render (request, 'wellhead/wiwellhead_detail.html', {'form': form, 'wiwellhead':wiwellhead})




