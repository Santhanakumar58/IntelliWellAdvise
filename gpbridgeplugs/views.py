from django.shortcuts import render, redirect
from .models import GPBridgePlug
from .forms import GPBridgePlugForm
from selectedGasProducer.models import SelectedGasProducer

def list_gpbridgeplug(request):
    selectedwell = SelectedGasProducer.objects.first()
    gpplugs = GPBridgePlug.objects.filter(gpwellid = selectedwell.wellid).all()    
    return render (request, 'gpbridgeplugs/gpbridge_plug.html', {'gpplugs': gpplugs})

def create_gpbridgeplug(request): 
    selectedwell = SelectedGasProducer.objects.first()
    plug = GPBridgePlug()
    plug.gpfgid = selectedwell.fgid
    plug.gpwellid =selectedwell.fgid     
    form = GPBridgePlug(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('gpbridgeplugs:list_gpbridgeplug')
    return render (request, 'gpbridgeplugs/gpbridge_plug_form.html', {'form': form})

def update_gpbridgeplug(request, id):
   plug = GPBridgePlug.objects.get(id=id)
   form = GPBridgePlugForm(request.POST or None, instance=plug)
   if form.is_valid():
        form.save()      
        return redirect ('gpbridgeplugs:list_gpbridgeplug')
   return render (request, 'gpbridgeplugs/gpbridge_plug_form.html', {'form': form, 'plug':plug})

def delete_gpbridgeplug(request, id):
   plug = GPBridgePlug.objects.get(id=id)
   
   if request.method == 'POST' :
       plug.delete()
       return redirect ('gpbridgeplugs:list_gpbridgeplug')
   return render (request, 'gpbridgeplugs/gpbridge_plug_confirm_delete.html', {'plug':plug})


