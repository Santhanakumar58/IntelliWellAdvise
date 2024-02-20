from django.shortcuts import render, redirect
from .models import GPCementPlug, GPPumpingData
from .forms import GPCementPlugForm, GPPumpDataForm
from selectedGasProducer.models import SelectedGasProducer

plugid =0

def list_gpcement_plug(request):     
    well = SelectedGasProducer.objects.all().first()   
    gpcementplugs= GPCementPlug.objects.filter(gpwellid=well.wellid).all()
    return render (request, 'gpcementplugs/gpcement_plug.html', {'gpcementplugs': gpcementplugs})

def create_gpcement_plug(request):   
    plug = GPCementPlug()
    selectedwell = SelectedGasProducer.objects.first()  
    plug.fgid = selectedwell.fgid
    plug.wellid = selectedwell.wellid   
    form = GPCementPlugForm(request.POST or None, instance=plug)
    if request.method =="POST":  
        form = GPCementPlugForm(request.POST, request.FILES, instance=plug)       
        plug.fgid = selectedwell.fgid
        plug.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gpcementplugs:list_gpcement_plug')
    return render (request, 'gpcementplugs/gpcement_plug_form.html', {'form': form})

def update_gpcement_plug(request, id):
    plug = GPCementPlug.objects.get(id=id)
    form = GPCementPlugForm(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('gpcementplugs:list_gpcement_plug')
    return render (request, 'gpcementplugs/gpcement_plug_form.html', {'form': form, 'plug':plug})

def delete_gpcement_plug(request, id):
    plug = GPCementPlug.objects.get(id=id)    
    if request.method == 'POST' :
        plug.delete()
        return redirect ('gpcementplugs:list_gpcement_plug')
    return render (request, 'gpcementplugs/gpcement_plug_confirm_delete.html', {'plug':plug})


def list_gpcement_pumpData(request,id): 
    plugid=id    
    well = SelectedGasProducer.objects.all().first()     
    pumpdatas= GPPumpingData.objects.filter( wellid=well.wellid , gpcementplug = plugid ).all()
    return render (request, 'gpcementplugs/gpcement_plug_pumpData.html', {'pumpdatas': pumpdatas, 'plugid':plugid})

def create_gpcement_pumpData(request, plugid):   
    pumpdata = GPPumpingData()  
    selectedwell = SelectedGasProducer.objects.first()  
    pumpdata.fgid = selectedwell.fgid
    pumpdata.wellid = selectedwell.wellid   
    pumpdata.gpcementplug  = GPCementPlug.objects.get(id=plugid) 
    form = GPPumpDataForm(request.POST or None, instance=pumpdata)
    if request.method =="POST":  
        form = GPPumpDataForm(request.POST, request.FILES, instance=pumpdata)       
        pumpdata.fgid = selectedwell.fgid
        pumpdata.wellid = selectedwell.wellid  
        pumpdata.gpcementplug =GPCementPlug.objects.get(id=plugid) 
    if form.is_valid():
        form.save()
        return redirect ('gpcementplugs:list_gpcement_pumpData', plugid)
    return render (request, 'gpcementplugs/gpcement_plug_pumpData_create_form.html', {'form': form, 'id':id})

def update_gpcement_pumpData(request, id):   
    gppumpdata = GPPumpingData.objects.get(id=id)    
    form = GPPumpDataForm(request.POST or None, instance=gppumpdata)    
    gpplugid = (gppumpdata.gpcementplug).pk
    print(plugid)
    print(id)
    if form.is_valid():
        form.save()       
        return redirect ('gpcementplugs:list_gpcement_pumpData', gpplugid)
    return render (request, 'gpcementplugs/gpcement_plug_pumpData_edit_form.html', {'form': form, 'gppumpdata':gppumpdata, 'id':id})

def delete_gpcement_pumpData(request, id):    
    gppumpdata = GPPumpingData.objects.get(id=id) 
    gpplugid = (gppumpdata.gpcementplug).pk
    if request.method == 'POST' :
        gppumpdata.delete()
        gpplugid = (gppumpdata.gpcementplug).pk
        print(plugid)
        return redirect ('gpcementplugs:list_gpcement_pumpData', gpplugid)
    return render (request, 'gpcementplugs/gpcement_plug_pumpData_confirm_delete.html', {'gppumpdata':gppumpdata, 'id':id})


