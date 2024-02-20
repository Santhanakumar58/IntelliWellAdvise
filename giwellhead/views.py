from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasInjector.models  import SelectedGasInjector
from .models import GIWellhead
from .forms import GIWellheadForm

# Create your views here.
def list_giwellhead(request): 

    selectedwell=SelectedGasInjector.objects.all().first()
    giwellheads = GIWellhead.objects.filter(giwellid =selectedwell.wellid).all()      
    return render (request, 'giwellhead/giwellhead_data.html', {'giwellheads': giwellheads} )
  

def create_giwellhead(request): 
    selectedwell=SelectedGasInjector.objects.all().first()   
    giwellhead = GIWellhead()    
    giwellhead.fgid = selectedwell.fgid
    giwellhead.wellid = selectedwell.wellid   
    form = GIWellheadForm(request.POST or None, instance=giwellhead)
    if request.method =="POST":  
        form = GIWellheadForm(request.POST, request.FILES, instance=giwellhead)       
        giwellhead.fgid = selectedwell.fgid
        giwellhead.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('giwellhead:list_giwellhead') 
    return render (request, 'giwellhead/giwellhead_data_form.html', {'form': form})

def update_giwellhead(request, id): 
   giwellhead = GIWellhead.objects.get(id=id)  
   form = GIWellheadForm(request.POST or None, instance=giwellhead) 
   if request.method =="POST":
        form = GIWellheadForm(request.POST, request.FILES, instance=giwellhead)        
        if form.is_valid():
            form.save()           
            return redirect ('giwellhead:list_giwellhead')
   return render (request, 'giwellhead/giwellhead_data_form.html', {'form': form, 'giwellhead':giwellhead})

def delete_giwellhead(request, id):
   giwellhead = GIWellhead.objects.get(id=id)   
   if request.method == 'POST' :
       giwellhead.delete()
       return redirect ('giwellhead:list_giwellhead')
   return render (request, 'giwellhead/giwellhead_data_confirm_delete.html', {'giwellhead':giwellhead})


def detail_giwellhead(request, id):      
    giwellhead = GIWellhead.objects.get(id=id)    
    form = GIWellheadForm(request.POST or None, instance=giwellhead) 
    return render (request, 'wellhead/giwellhead_detail.html', {'form': form, 'giwellhead':giwellhead})



