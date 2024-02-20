from django.shortcuts import render, redirect
from .models import OBCementPlug, OBPumpingData
from .forms import OBCementPlugForm, OBPumpDataForm
from selectedObserver.models import SelectedObserver

plugid =0

def list_obcement_plug(request):     
    well = SelectedObserver.objects.all().first()   
    obcementplugs= OBCementPlug.objects.filter(obwellid=well.wellid).all()
    return render (request, 'obcementplugs/obcement_plug.html', {'obcementplugs': obcementplugs})

def create_obcement_plug(request):   
    plug = OBCementPlug()
    selectedwell = SelectedObserver.objects.first()  
    plug.fgid = selectedwell.fgid
    plug.wellid = selectedwell.wellid   
    form = OBCementPlugForm(request.POST or None, instance=plug)
    if request.method =="POST":  
        form = OBCementPlugForm(request.POST, request.FILES, instance=plug)       
        plug.fgid = selectedwell.fgid
        plug.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('obcementplugs:list_obcement_plug')
    return render (request, 'obcementplugs/obcement_plug_form.html', {'form': form})

def update_obcement_plug(request, id):
    plug = OBCementPlug.objects.get(id=id)
    form = OBCementPlugForm(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('obcementplugs:list_obcement_plug')
    return render (request, 'obcementplugs/obcement_plug_form.html', {'form': form, 'plug':plug})

def delete_obcement_plug(request, id):
    plug = OBCementPlug.objects.get(id=id)    
    if request.method == 'POST' :
        plug.delete()
        return redirect ('obcementplugs:list_obcement_plug')
    return render (request, 'obcementplugs/obcement_plug_confirm_delete.html', {'plug':plug})


def list_obcement_pumpData(request,id): 
    plugid=id    
    well = SelectedObserver.objects.all().first()     
    pumpdatas= OBPumpingData.objects.filter( wellid=well.wellid , obcementplug = plugid ).all()
    return render (request, 'obcementplugs/obcement_plug_pumpData.html', {'pumpdatas': pumpdatas, 'plugid':plugid})

def create_obcement_pumpData(request, plugid):   
    pumpdata = OBPumpingData()  
    selectedwell = SelectedObserver.objects.first()  
    pumpdata.fgid = selectedwell.fgid
    pumpdata.wellid = selectedwell.wellid   
    pumpdata.obcementplug  = OBCementPlug.objects.get(id=plugid) 
    form = OBPumpDataForm(request.POST or None, instance=pumpdata)
    if request.method =="POST":  
        form = OBPumpDataForm(request.POST, request.FILES, instance=pumpdata)       
        pumpdata.fgid = selectedwell.fgid
        pumpdata.wellid = selectedwell.wellid  
        pumpdata.obcementplug =OBCementPlug.objects.get(id=plugid) 
    if form.is_valid():
        form.save()
        return redirect ('obcementplugs:list_obcement_pumpData', plugid)
    return render (request, 'obcementplugs/obcement_plug_pumpData_create_form.html', {'form': form, 'id':id})

def update_obcement_pumpData(request, id):   
    gppumpdata = OBPumpingData.objects.get(id=id)    
    form = OBPumpDataForm(request.POST or None, instance=gppumpdata)    
    gpplugid = (gppumpdata.obcementplug).pk
    print(plugid)
    print(id)
    if form.is_valid():
        form.save()       
        return redirect ('obcementplugs:list_obcement_pumpData', gpplugid)
    return render (request, 'obcementplugs/obcement_plug_pumpData_edit_form.html', {'form': form, 'gppumpdata':gppumpdata, 'id':id})

def delete_obcement_pumpData(request, id):    
    gppumpdata = OBPumpingData.objects.get(id=id) 
    gpplugid = (gppumpdata.obcementplug).pk
    if request.method == 'POST' :
        gppumpdata.delete()
        gpplugid = (gppumpdata.obcementplug).pk
        print(plugid)
        return redirect ('obcementplugs:list_obcement_pumpData', gpplugid)
    return render (request, 'obcementplugs/obcement_plug_pumpData_confirm_delete.html', {'gppumpdata':gppumpdata, 'id':id})



