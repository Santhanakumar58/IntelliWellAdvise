from ast import Global
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import GasProducer
from .forms import GasproducerForm
from fgis.models import FGIModel
from django.contrib.sessions.models import Session
from django.contrib  import messages
from selectedfgi.models import Selectedfgi

def list_gasproducer(request):
    gasproducers = GasProducer.objects.all()   
 
    return render (request, 'gasproducers/gasproducer.html', {'gasproducers': gasproducers})

def create_gasproducer(request): 
    selectedfgi = Selectedfgi.objects.first()
    gasproducer = GasProducer()
    gasproducer.fgid = selectedfgi.fgid
    gasproducer.is_selected = False   
    form = GasproducerForm(request.POST or None, instance=gasproducer)
    if form.is_valid():
        form.save()
        return redirect ('gasproducers:list_gasproducer')
    return render (request, 'gasproducers/gasproducer_form.html', {'form': form})

def update_gasproducer(request, id):
   gasproducer = GasProducer.objects.get(id=id)
   form = GasproducerForm(request.POST or None, instance=gasproducer)
   if form.is_valid():
        form.save()      
        return redirect ('gasproducers:list_gasproducer')
   return render (request, 'gasproducers/gasproducer_form.html', {'form': form, 'gasproducer':gasproducer})

def delete_gasproducer(request, id):
   gasproducer = GasProducer.objects.get(id=id)
   
   if request.method == 'POST' :
       gasproducer.delete()
       return redirect ('gasproducers:list_gasproducer')
   return render (request, 'gasproducers/gasproducer_confirm_delete.html', {'gasproducer':gasproducer})

