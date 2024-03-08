from django.shortcuts import render, redirect
from .models import CementPlug, PumpingData
from .forms import CementPlugForm, PumpDataForm
from selectedOilProducer.models import SelectedOilProducer

plugid =0

def list_cement_plug(request):     
    well = SelectedOilProducer.objects.all().first()   
    cementplugs= CementPlug.objects.filter(wellid=well.wellid).all()
    return render (request, 'cementplugs/cement_plug.html', {'cementplugs': cementplugs})

def create_cement_plug(request):   
    plug = CementPlug()
    selectedwell = SelectedOilProducer.objects.first()  
    plug.fgid = selectedwell.fgid
    plug.wellid = selectedwell.wellid   
    form = CementPlugForm(request.POST or None, instance=plug)
    if request.method =="POST":  
        form = CementPlugForm(request.POST, request.FILES, instance=plug)       
        plug.fgid = selectedwell.fgid
        plug.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('cementplugs:list_cement_plug')
    return render (request, 'cementplugs/cement_plug_form.html', {'form': form})

def update_cement_plug(request, id):
    plug = CementPlug.objects.get(id=id)
    form = CementPlugForm(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('cementplugs:list_cement_plug')
    return render (request, 'cementplugs/cement_plug_form.html', {'form': form, 'plug':plug})

def delete_cement_plug(request, id):
    plug = CementPlug.objects.get(id=id)    
    if request.method == 'POST' :
        plug.delete()
        return redirect ('cementplugs:list_cement_plug')
    return render (request, 'cementplugs/cement_plug_confirm_delete.html', {'plug':plug})


def list_cement_pumpData(request,plugid):   
    well = SelectedOilProducer.objects.all().first()     
    pumpdatas= PumpingData.objects.filter( wellid=well.wellid , cementplug = plugid ).all()
    return render (request, 'cementplugs/cement_plug_pumpData.html', {'pumpdatas': pumpdatas, 'plugid':plugid})

def create_cement_pumpData(request, plugid):   
    pumpdata = PumpingData()  
    selectedwell = SelectedOilProducer.objects.first()  
    pumpdata.fgid = selectedwell.fgid
    pumpdata.wellid = selectedwell.wellid   
    pumpdata.cementplug  = CementPlug.objects.get(id=plugid) 
    form = PumpDataForm(request.POST or None, instance=pumpdata)
    if request.method =="POST":  
        form = PumpDataForm(request.POST, request.FILES, instance=pumpdata)       
        pumpdata.fgid = selectedwell.fgid
        pumpdata.wellid = selectedwell.wellid  
        pumpdata.cementplug =CementPlug.objects.get(id=plugid) 
    if form.is_valid():
        form.save()
        return redirect ('cementplugs:list_cement_pumpData', plugid)
    return render (request, 'cementplugs/cement_plug_pumpData_create_form.html', {'form': form, 'plugid':plugid})

def update_cement_pumpData(request, id):   
    pumpdata = PumpingData.objects.get(id=id)    
    form = PumpDataForm(request.POST or None, instance=pumpdata)    
    plugid = (pumpdata.cementplug).pk
    print(plugid)
    print(id)
    if form.is_valid():
        form.save()       
        return redirect ('cementplugs:list_cement_pumpData', plugid)
    return render (request, 'cementplugs/cement_plug_pumpData_edit_form.html', {'form': form, 'pumpdata':pumpdata, 'id':id})

def delete_cement_pumpData(request, id):    
    pumpdata = PumpingData.objects.get(id=id) 
    plugid = (pumpdata.cementplug).pk
    if request.method == 'POST' :
        pumpdata.delete()
        plugid = (pumpdata.cementplug).pk
        print(plugid)
        return redirect ('cementplugs:list_cement_pumpData', plugid)
    return render (request, 'cementplugs/cement_plug_pumpData_confirm_delete.html', {'pumpdata':pumpdata, 'id':id})

