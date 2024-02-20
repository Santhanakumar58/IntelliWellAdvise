from django.shortcuts import render, redirect
from .models import WIBridgePlug
from .forms import WIBridgePlugForm
from selectedWaterInjector.models import SelectedWaterInjector

def list_wibridgeplug(request):
    selectedwell = SelectedWaterInjector.objects.first()
    wiplugs = WIBridgePlug.objects.filter(wiwellid = selectedwell.wellid).all()    
    return render (request, 'wibridgeplugs/wibridge_plug.html', {'wiplugs': wiplugs})

def create_wibridgeplug(request): 
    selectedwell = SelectedWaterInjector.objects.first()
    plug = WIBridgePlug()
    plug.wifgid = selectedwell.fgid
    plug.wiwellid =selectedwell.fgid     
    form = WIBridgePlug(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('wibridgeplugs:list_wibridgeplug')
    return render (request, 'wibridgeplugs/wibridge_plug_form.html', {'form': form})

def update_wibridgeplug(request, id):
   plug = WIBridgePlug.objects.get(id=id)
   form = WIBridgePlugForm(request.POST or None, instance=plug)
   if form.is_valid():
        form.save()      
        return redirect ('wibridgeplugs:list_wibridgeplug')
   return render (request, 'wibridgeplugs/wibridge_plug_form.html', {'form': form, 'plug':plug})

def delete_wibridgeplug(request, id):
   plug = WIBridgePlug.objects.get(id=id)
   
   if request.method == 'POST' :
       plug.delete()
       return redirect ('wibridgeplugs:list_wibridgeplug')
   return render (request, 'wibridgeplugs/wibridge_plug_confirm_delete.html', {'plug':plug})



