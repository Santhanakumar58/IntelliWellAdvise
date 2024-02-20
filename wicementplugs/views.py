from django.shortcuts import render, redirect
from .models import WICementPlug, WIPumpingData
from .forms import WICementPlugForm, WIPumpDataForm
from selectedWaterInjector.models import SelectedWaterInjector

plugid =0

def list_wicement_plug(request):     
    well = SelectedWaterInjector.objects.all().first()   
    wicementplugs= WICementPlug.objects.filter(wiwellid=well.wellid).all()
    return render (request, 'wicementplugs/wicement_plug.html', {'wicementplugs': wicementplugs})

def create_wicement_plug(request):   
    plug = WICementPlug()
    selectedwell = SelectedWaterInjector.objects.first()  
    plug.fgid = selectedwell.fgid
    plug.wellid = selectedwell.wellid   
    form = WICementPlugForm(request.POST or None, instance=plug)
    if request.method =="POST":  
        form = WICementPlugForm(request.POST, request.FILES, instance=plug)       
        plug.fgid = selectedwell.fgid
        plug.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('wicementplugs:list_wicement_plug')
    return render (request, 'wicementplugs/wicement_plug_form.html', {'form': form})

def update_wicement_plug(request, id):
    plug = WICementPlug.objects.get(id=id)
    form = WICementPlugForm(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('wicementplugs:list_wicement_plug')
    return render (request, 'wicementplugs/wicement_plug_form.html', {'form': form, 'plug':plug})

def delete_wicement_plug(request, id):
    plug = WICementPlug.objects.get(id=id)    
    if request.method == 'POST' :
        plug.delete()
        return redirect ('wicementplugs:list_wicement_plug')
    return render (request, 'wicementplugs/wicement_plug_confirm_delete.html', {'plug':plug})


def list_wicement_pumpData(request,id): 
    plugid=id    
    well = SelectedWaterInjector.objects.all().first()     
    pumpdatas= WIPumpingData.objects.filter( wiwellid=well.wellid , wicementplug = plugid ).all()
    return render (request, 'wicementplugs/wicement_plug_pumpData.html', {'pumpdatas': pumpdatas, 'plugid':plugid})

def create_wicement_pumpData(request, plugid):   
    pumpdata = WIPumpingData()  
    selectedwell = SelectedWaterInjector.objects.first()  
    pumpdata.fgid = selectedwell.fgid
    pumpdata.wellid = selectedwell.wellid   
    pumpdata.wicementplug  = WICementPlug.objects.get(id=plugid) 
    form = WIPumpDataForm(request.POST or None, instance=pumpdata)
    if request.method =="POST":  
        form = WIPumpDataForm(request.POST, request.FILES, instance=pumpdata)       
        pumpdata.fgid = selectedwell.fgid
        pumpdata.wellid = selectedwell.wellid  
        pumpdata.wicementplug =WICementPlug.objects.get(id=plugid) 
    if form.is_valid():
        form.save()
        return redirect ('wicementplugs:list_wicement_pumpData', plugid)
    return render (request, 'wicementplugs/wicement_plug_pumpData_create_form.html', {'form': form, 'id':id})

def update_wicement_pumpData(request, id):   
    gppumpdata = WIPumpingData.objects.get(id=id)    
    form = WIPumpDataForm(request.POST or None, instance=gppumpdata)    
    gpplugid = (gppumpdata.wicementplug).pk
    print(plugid)
    print(id)
    if form.is_valid():
        form.save()       
        return redirect ('wicementplugs:list_wicement_pumpData', gpplugid)
    return render (request, 'wicementplugs/wicement_plug_pumpData_edit_form.html', {'form': form, 'gppumpdata':gppumpdata, 'id':id})

def delete_wicement_pumpData(request, id):    
    gppumpdata = WIPumpingData.objects.get(id=id) 
    gpplugid = (gppumpdata.wicementplug).pk
    if request.method == 'POST' :
        gppumpdata.delete()
        gpplugid = (gppumpdata.wicementplug).pk
        print(plugid)
        return redirect ('wicementplugs:list_wicement_pumpData', gpplugid)
    return render (request, 'wicementplugs/wicement_plug_pumpData_confirm_delete.html', {'gppumpdata':gppumpdata, 'id':id})



