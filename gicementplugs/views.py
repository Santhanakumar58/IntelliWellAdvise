from django.shortcuts import render, redirect
from .models import GICementPlug, GIPumpingData
from .forms import GICementPlugForm, GIPumpDataForm
from selectedGasInjector.models import SelectedGasInjector

plugid =0

def list_gicement_plug(request):     
    well = SelectedGasInjector.objects.all().first()   
    gicementplugs= GICementPlug.objects.filter(giwellid=well.wellid).all()
    return render (request, 'gicementplugs/gicement_plug.html', {'gicementplugs': gicementplugs})

def create_gicement_plug(request):   
    plug = GICementPlug()
    selectedwell = SelectedGasInjector.objects.first()  
    plug.fgid = selectedwell.fgid
    plug.wellid = selectedwell.wellid   
    form = GICementPlugForm(request.POST or None, instance=plug)
    if request.method =="POST":  
        form = GICementPlugForm(request.POST, request.FILES, instance=plug)       
        plug.fgid = selectedwell.fgid
        plug.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gicementplugs:list_gicement_plug')
    return render (request, 'gicementplugs/gicement_plug_form.html', {'form': form})

def update_gicement_plug(request, id):
    plug = GICementPlug.objects.get(id=id)
    form = GICementPlugForm(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('gicementplugs:list_gicement_plug')
    return render (request, 'gicementplugs/gicement_plug_form.html', {'form': form, 'plug':plug})

def delete_gicement_plug(request, id):
    plug = GICementPlug.objects.get(id=id)    
    if request.method == 'POST' :
        plug.delete()
        return redirect ('gicementplugs:list_gicement_plug')
    return render (request, 'gicementplugs/gicement_plug_confirm_delete.html', {'plug':plug})


def list_gicement_pumpData(request,id): 
    plugid=id    
    well = SelectedGasInjector.objects.all().first()     
    pumpdatas= GIPumpingData.objects.filter( wellid=well.wellid , gicementplug = plugid ).all()
    return render (request, 'gicementplugs/gicement_plug_pumpData.html', {'pumpdatas': pumpdatas, 'plugid':plugid})

def create_gicement_pumpData(request, plugid):   
    pumpdata = GIPumpingData()  
    selectedwell = SelectedGasInjector.objects.first()  
    pumpdata.fgid = selectedwell.fgid
    pumpdata.wellid = selectedwell.wellid   
    pumpdata.gicementplug  = GICementPlug.objects.get(id=plugid) 
    form = GIPumpDataForm(request.POST or None, instance=pumpdata)
    if request.method =="POST":  
        form = GIPumpDataForm(request.POST, request.FILES, instance=pumpdata)       
        pumpdata.fgid = selectedwell.fgid
        pumpdata.wellid = selectedwell.wellid  
        pumpdata.gicementplug =GICementPlug.objects.get(id=plugid) 
    if form.is_valid():
        form.save()
        return redirect ('gicementplugs:list_gicement_pumpData', plugid)
    return render (request, 'gicementplugs/gicement_plug_pumpData_create_form.html', {'form': form, 'id':id})

def update_gicement_pumpData(request, id):   
    gipumpdata = GIPumpingData.objects.get(id=id)    
    form = GIPumpDataForm(request.POST or None, instance=gipumpdata)    
    giplugid = (gipumpdata.gicementplug).pk
    print(plugid)
    print(id)
    if form.is_valid():
        form.save()       
        return redirect ('gicementplugs:list_gicement_pumpData', giplugid)
    return render (request, 'gicementplugs/gicement_plug_pumpData_edit_form.html', {'form': form, 'gppumpdata':gipumpdata, 'id':id})

def delete_gicement_pumpData(request, id):    
    gppumpdata = GIPumpingData.objects.get(id=id) 
    gpplugid = (gppumpdata.gicementplug).pk
    if request.method == 'POST' :
        gppumpdata.delete()
        gpplugid = (gppumpdata.gicementplug).pk
        print(plugid)
        return redirect ('gicementplugs:list_gicement_pumpData', gpplugid)
    return render (request, 'gicementplugs/gicement_plug_pumpData_confirm_delete.html', {'gppumpdata':gppumpdata, 'id':id})



