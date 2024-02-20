from django.shortcuts import render, redirect
from .models import OBBridgePlug
from .forms import OBBridgePlugForm
from selectedObserver.models import SelectedObserver

def list_obbridgeplug(request):
    selectedwell = SelectedObserver.objects.first()
    gpplugs = OBBridgePlug.objects.filter(obwellid = selectedwell.wellid).all()    
    return render (request, 'obbridgeplugs/obbridge_plug.html', {'gpplugs': gpplugs})

def create_obbridgeplug(request): 
    selectedwell = SelectedObserver.objects.first()
    plug = OBBridgePlug()
    plug.obfgid = selectedwell.fgid
    plug.obwellid =selectedwell.fgid     
    form = OBBridgePlug(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('obbridgeplugs:list_obbridgeplug')
    return render (request, 'obbridgeplugs/obbridge_plug_form.html', {'form': form})

def update_obbridgeplug(request, id):
   plug = OBBridgePlug.objects.get(id=id)
   form = OBBridgePlugForm(request.POST or None, instance=plug)
   if form.is_valid():
        form.save()      
        return redirect ('obbridgeplugs:list_obbridgeplug')
   return render (request, 'obbridgeplugs/obbridge_plug_form.html', {'form': form, 'plug':plug})

def delete_obbridgeplug(request, id):
   plug = OBBridgePlug.objects.get(id=id)
   
   if request.method == 'POST' :
       plug.delete()
       return redirect ('obbridgeplugs:list_obbridgeplug')
   return render (request, 'obbridgeplugs/obbridge_plug_confirm_delete.html', {'plug':plug})



