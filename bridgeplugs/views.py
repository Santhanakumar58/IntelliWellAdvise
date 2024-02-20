from django.shortcuts import render, redirect
from .models import BridgePlug
from .forms import BridgePlugForm
from selectedGasProducer.models import SelectedGasProducer

def list_bridgeplug(request):
    selectedwell = SelectedGasProducer.objects.first()
    plugs = BridgePlug.objects.filter(wellid = selectedwell.wellid).all()    
    return render (request, 'bridgeplugs/bridge_plug.html', {'plugs': plugs})

def create_bridgeplug(request): 
    selectedwell = SelectedGasProducer.objects.first()
    plug = BridgePlug()
    plug.fgid = selectedwell.fgid
    plug.wellid =selectedwell.fgid     
    form = BridgePlugForm(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('bridgeplugs:list_bridgeplug')
    return render (request, 'bridgeplugs/bridge_plug_form.html', {'form': form})

def update_bridgeplug(request, id):
   plug = BridgePlug.objects.get(id=id)
   form = BridgePlugForm(request.POST or None, instance=plug)
   if form.is_valid():
        form.save()      
        return redirect ('bridgeplugs:list_bridgeplug')
   return render (request, 'bridgeplugs/bridge_plug_form.html', {'form': form, 'plug':plug})

def delete_bridgeplug(request, id):
   plug = BridgePlug.objects.get(id=id)
   
   if request.method == 'POST' :
       plug.delete()
       return redirect ('bridgeplugs:list_bridgeplug')
   return render (request, 'bridgeplugs/bridge_plug_confirm_delete.html', {'plug':plug})


