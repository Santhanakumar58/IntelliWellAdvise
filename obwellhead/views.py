from django.shortcuts import render
from datetime import datetime, timedelta
from sqlite3 import Date
from django.shortcuts import redirect, render
from selectedObserver.models  import SelectedObserver
from .models import OBWellhead
from .forms import OBWellheadForm

# Create your views here.
def list_obwellhead(request): 

    selectedwell=SelectedObserver.objects.all().first()
    obwellheads = OBWellhead.objects.filter(obwellid =selectedwell.wellid).all()      
    return render (request, 'obwellhead/obwellhead_data.html', {'obwellheads': obwellheads} )
  

def create_obwellhead(request): 
    selectedwell=SelectedObserver.objects.all().first()   
    obwellhead = OBWellhead()    
    obwellhead.fgid = selectedwell.fgid
    obwellhead.wellid = selectedwell.wellid   
    form = OBWellheadForm(request.POST or None, instance=obwellhead)
    if request.method =="POST":  
        form = OBWellheadForm(request.POST, request.FILES, instance=obwellhead)       
        obwellhead.fgid = selectedwell.fgid
        obwellhead.wellid = selectedwell.wellid                       
        if form.is_valid(): 
            form.save()  
            return redirect ('obwellhead:list_obwellhead') 
    return render (request, 'obwellhead/obwellhead_data_form.html', {'form': form})

def update_obwellhead(request, id): 
   obwellhead = OBWellhead.objects.get(id=id)  
   form = OBWellheadForm(request.POST or None, instance=obwellhead) 
   if request.method =="POST":
        form = OBWellheadForm(request.POST, request.FILES, instance=obwellhead)        
        if form.is_valid():
            form.save()           
            return redirect ('obwellhead:list_obwellhead')
   return render (request, 'obwellhead/obwellhead_data_form.html', {'form': form, 'obwellhead':obwellhead})

def delete_obwellhead(request, id):
   obwellhead = OBWellhead.objects.get(id=id)   
   if request.method == 'POST' :
       obwellhead.delete()
       return redirect ('obwellhead:list_obwellhead')
   return render (request, 'obwellhead/obwellhead_data_confirm_delete.html', {'obwellhead':obwellhead})


def detail_obwellhead(request, id):      
    obwellhead = OBWellhead.objects.get(id=id)    
    form = OBWellheadForm(request.POST or None, instance=obwellhead) 
    return render (request, 'wellhead/obwellhead_detail.html', {'form': form, 'obwellhead':obwellhead})



