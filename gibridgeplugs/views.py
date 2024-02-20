from django.shortcuts import render, redirect
from .models import GIBridgePlug
from .forms import GIBridgePlugForm
from selectedGasInjector.models import SelectedGasInjector

def list_gibridgeplug(request):
    selectedwell = SelectedGasInjector.objects.first()
    gpplugs = GIBridgePlug.objects.filter(giwellid = selectedwell.wellid).all()    
    return render (request, 'gibridgeplugs/gibridge_plug.html', {'gpplugs': gpplugs})

def create_gibridgeplug(request): 
    selectedwell = SelectedGasInjector.objects.first()
    plug = GIBridgePlug()
    plug.gifgid = selectedwell.fgid
    plug.giwellid =selectedwell.fgid     
    form = GIBridgePlug(request.POST or None, instance=plug)
    if form.is_valid():
        form.save()
        return redirect ('gibridgeplugs:list_gibridgeplug')
    return render (request, 'gibridgeplugs/gibridge_plug_form.html', {'form': form})

def update_gibridgeplug(request, id):
   plug = GIBridgePlug.objects.get(id=id)
   form = GIBridgePlugForm(request.POST or None, instance=plug)
   if form.is_valid():
        form.save()      
        return redirect ('gibridgeplugs:list_gibridgeplug')
   return render (request, 'gibridgeplugs/gibridge_plug_form.html', {'form': form, 'plug':plug})

def delete_gibridgeplug(request, id):
   plug = GIBridgePlug.objects.get(id=id)
   
   if request.method == 'POST' :
       plug.delete()
       return redirect ('gibridgeplugs:list_gibridgeplug')
   return render (request, 'gibridgeplugs/gibridge_plug_confirm_delete.html', {'plug':plug})



