from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from IntelligentOilWell.custom_context_processors import selectedfgi
from django.contrib import messages
from .models import DifferentialLiberationModel 
from .forms import DiffLibForm 
from selectedfgi.models import Selectedfgi
from sublayers.models import Sublayer
from tablib import Dataset

def list_difflib(request):
    selectedfgi = Selectedfgi.objects.first()
    difflibs = DifferentialLiberationModel.objects.filter(fgId = selectedfgi.fgid)   
    return render (request, 'differentialliberation/differentialliberation.html', {'difflibs': difflibs})
    
def create_difflib(request):  
   selectedfgi = Selectedfgi.objects.first()   
   difflib = DifferentialLiberationModel()
   difflib.fgId = selectedfgi.fgid 
   sublayer = Sublayer.objects.get(sublayername=selectedfgi.selectedsublayername)
   difflib.subLayer = sublayer  
   form = DiffLibForm(request.POST or None, instance=difflib)  
   if form.is_valid():
       form.save()       
       return redirect ('differentialliberation:list_difflib')    
   return render (request, 'differentialliberation/differentialliberation_form.html', {'form': form})

def update_difflib(request, id):
   difflib = DifferentialLiberationModel.objects.get(id=id)
   if difflib.subLayer == "" or difflib.subLayer == None:
       selectedfgi = Selectedfgi.objects.first()   
       sublayer = Sublayer.objects.get(sublayername=selectedfgi.selectedsublayername)
       difflib.subLayer = sublayer   
   form = DiffLibForm(request.POST or None, instance=difflib)
   if form.is_valid():
       form.save()
       return redirect ('differentialliberation:list_difflib')
   return render (request, 'differentialliberation/differentialliberation_form.html', {'form': form, 'difflib':difflib})

def delete_difflib(request, id):
   difflib = DifferentialLiberationModel.objects.get(id=id)   
   if request.method == 'POST' :
       difflib.delete()
       return redirect ('differentialliberation:list_difflib')
   return render (request, 'differentialliberation/differentialliberation_confirm_delete.html', {'difflib':difflib})



