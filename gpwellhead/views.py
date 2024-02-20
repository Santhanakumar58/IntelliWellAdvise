from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedGasProducer.models  import SelectedGasProducer
from .models import GPWellhead
from .forms import GPWellheadForm

# Create your views here.
def list_gpwellhead(request): 

    selectedwell=SelectedGasProducer.objects.all().first()
    gpwellheads = GPWellhead.objects.filter(gpwellid =selectedwell.wellid).all()      
    return render (request, 'gpwellhead/gpwellhead_data.html', {'gpwellheads': gpwellheads} )
  

def create_gpwellhead(request): 
    selectedwell=SelectedGasProducer.objects.all().first()   
    gpwellhead = GPWellhead()    
    gpwellhead.fgid = selectedwell.fgid
    gpwellhead.wellid = selectedwell.wellid   
    form = GPWellheadForm(request.POST or None, instance=gpwellhead)
    if request.method =="POST":  
        form = GPWellheadForm(request.POST, request.FILES, instance=gpwellhead)       
        gpwellhead.fgid = selectedwell.fgid
        gpwellhead.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('gpwellhead:list_gpwellhead') 
    return render (request, 'gpwellhead/gpwellhead_data_form.html', {'form': form})

def update_gpwellhead(request, id): 
   gpwellhead = GPWellhead.objects.get(id=id)  
   form = GPWellheadForm(request.POST or None, instance=gpwellhead) 
   if request.method =="POST":
        form = GPWellheadForm(request.POST, request.FILES, instance=gpwellhead)        
        if form.is_valid():
            form.save()           
            return redirect ('gpwellhead:list_gpwellhead')
   return render (request, 'gpwellhead/gpwellhead_data_form.html', {'form': form, 'gpwellhead':gpwellhead})

def delete_gpwellhead(request, id):
   gpwellhead = GPWellhead.objects.get(id=id)   
   if request.method == 'POST' :
       gpwellhead.delete()
       return redirect ('gpwellhead:list_gpwellhead')
   return render (request, 'gpwellhead/gpwellhead_data_confirm_delete.html', {'gpwellhead':gpwellhead})


def detail_gpwellhead(request, id):      
    gpwellhead = GPWellhead.objects.get(id=id)    
    form = GPWellheadForm(request.POST or None, instance=gpwellhead) 
    return render (request, 'wellhead/gpwellhead_detail.html', {'form': form, 'gpwellhead':gpwellhead})



