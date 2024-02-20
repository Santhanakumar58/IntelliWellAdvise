from ast import Global
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import OilProducer
from .forms import OilproducerForm
from fgis.models import FGIModel
from django.contrib.sessions.models import Session
from django.contrib  import messages
from selectedfgi.models import Selectedfgi

def list_oilproducer(request):
    oilproducers = OilProducer.objects.all()  
    return render (request, 'oilproducers/oilproducer.html', {'oilproducers': oilproducers})

def create_oilproducer(request): 
    selectedfgi = Selectedfgi.objects.first()
    oilproducer = OilProducer()
    oilproducer.fgid = selectedfgi.fgid
    oilproducer.is_selected = False       
    form = OilproducerForm(request.POST or None, instance=oilproducer)
    if form.is_valid():
        form.save()
        return redirect ('oilproducers:list_oilproducer')
    return render (request, 'oilproducers/oilproducer_form.html', {'form': form})

def update_oilproducer(request, id):
   oilproducer = OilProducer.objects.get(id=id)
   form = OilproducerForm(request.POST or None, instance=oilproducer)
   if form.is_valid():
        form.save()      
        return redirect ('oilproducers:list_oilproducer')
   return render (request, 'oilproducers/oilproducer_form.html', {'form': form, 'oilproducer':oilproducer})

def delete_oilproducer(request, id):
   oilproducer = OilProducer.objects.get(id=id)
   
   if request.method == 'POST' :
       oilproducer.delete()
       return redirect ('oilproducers:list_oilproducer')
   return render (request, 'oilproducers/oilproducer_confirm_delete.html', {'oilproducer':oilproducer})
