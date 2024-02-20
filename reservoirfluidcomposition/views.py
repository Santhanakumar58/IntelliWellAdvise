from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from IntelligentOilWell.custom_context_processors import selectedfgi
from django.contrib import messages
from .models import FluidComposition 
from .forms import FluidCompositionForm
from selectedfgi.models import Selectedfgi
from sublayers.models import Sublayer
from tablib import Dataset
 
def list_fluid_composition(request):
    selectedfgi = Selectedfgi.objects.first()
    fcs = FluidComposition.objects.filter(fgId = selectedfgi.fgid)   
    return render (request, 'reservoirfluidcomposition/fluid_composition.html', {'fcs': fcs})
    
def create_fluid_composition(request):  
   selectedfgi = Selectedfgi.objects.first()   
   fc = FluidComposition()
   fc.fgId = selectedfgi.fgid 
   sublayer = Sublayer.objects.get(sublayername=selectedfgi.selectedsublayername)
   fc.subLayer = sublayer 
   form = FluidCompositionForm(request.POST or None, instance=fc)  
   if request.method =="POST": 
        form = FluidCompositionForm(request.POST, instance=fc)  
        if form.is_valid():
            form.save()       
            return redirect ('reservoirfluidcomposition:list_fluid_composition')    
   return render (request, 'reservoirfluidcomposition/fluid_composition_form.html', {'form': form})

def update_fluid_composition(request, id):
   fc = FluidComposition.objects.get(id=id)
   if fc.subLayer == "" or fc.subLayer == None:
       selectedfgi = Selectedfgi.objects.first()   
       sublayer = Sublayer.objects.get(sublayername=selectedfgi.selectedsublayername)
       fc.subLayer = sublayer   
   form = FluidCompositionForm(request.POST or None, instance=fc)
   if form.is_valid():
       form.save()
       return redirect ('reservoirfluidcomposition:list_fluid_composition')
   return render (request, 'reservoirfluidcomposition/fluid_composition_form.html', {'form': form, 'fc':fc})

def delete_fluid_composition(request, id):
   fc = FluidComposition.objects.get(id=id)   
   if request.method == 'POST' :
       fc.delete()
       return redirect ('reservoirfluidcomposition:list_fluid_composition')
   return render (request, 'reservoirfluidcomposition/fluid_composition_confirm_delete.html', {'fc':fc})


