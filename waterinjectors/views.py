from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import WaterInjector
from .forms import WaterInjectorForm
from fgis.models import FGIModel
from django.contrib.sessions.models import Session
from django.contrib  import messages
from selectedfgi.models import Selectedfgi

def list_waterinjector(request):
    waterinjectors = WaterInjector.objects.all()   
 
    return render (request, 'waterinjectors/waterinjector.html', {'waterinjectors': waterinjectors})

def create_waterinjector(request): 
    selectedfgi = Selectedfgi.objects.first()
    waterinjector = WaterInjector()
    waterinjector.fgid = selectedfgi.fgid
    waterinjector.is_selected = False  
    form = WaterInjectorForm(request.POST or None, instance=waterinjector)
    if form.is_valid():
        form.save()
        return redirect ('waterinjectors:list_waterinjector')
    return render (request, 'waterinjectors/waterinjector_form.html', {'form': form})

def update_waterinjector(request, id):
   waterinjector = WaterInjector.objects.get(id=id)
   form = WaterInjectorForm(request.POST or None, instance=waterinjector)
   if form.is_valid():
        form.save()      
        return redirect ('waterinjectors:list_waterinjector')
   return render (request, 'waterinjectors/waterinjector_form.html', {'form': form, 'waterinjector':waterinjector})

def delete_waterinjector(request, id):
   waterinjector = WaterInjector.objects.get(id=id)
   
   if request.method == 'POST' :
       waterinjector.delete()
       return redirect ('waterinjectors:list_waterinjector')
   return render (request, 'waterinjectors/waterinjector_confirm_delete.html', {'waterinjector':waterinjector})

