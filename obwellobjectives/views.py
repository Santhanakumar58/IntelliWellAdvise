from django.shortcuts import render, redirect
from .models import OBWellobjective
from obwellobjectivedata.models import OBWellobjectivedata
from selectedObserver.models import SelectedObserver
from .forms import OBWellObjectiveForm
from IntelligentOilWell.custom_context_processors import selectedwell

def list_obwellobjective(request):  
    selectedwell = SelectedObserver.objects.first()     
    id1= selectedwell.wellid
    obwellobjectives = OBWellobjective.objects.filter(obwellid=id1).values()             
    context = {'obwellobjectives': obwellobjectives, 'selectedwell':selectedwell}
    return render (request, 'obwellobjectives/obwellobjective.html', context) 

def create_obwellobjective(request): 
   selectedwell = SelectedObserver.objects.first()     
   id1= selectedwell.wellid  
   print(id1, selectedwell.wellname, selectedwell.fgid)
   objective = OBWellobjective()  
   objective.obwellid=id1   
   objective.obfgid=selectedwell.fgid   
   objective.obwellname=selectedwell.wellname 
   form = OBWellObjectiveForm(request.POST or None, instance=objective)   
   if form.is_valid():        
       form.save()
       return redirect ('obwellobjectives:list_obwellobjective')
   return render (request, 'obwellobjectives/obwellobjective_form.html', {'form': form})

def update_obwellobjective(request, id):
   obwellobjective = OBWellobjective.objects.get(id=id)
   form = OBWellObjectiveForm(request.POST or None, instance=obwellobjective)

   if form.is_valid():        
        obwellobjective.save()       
        return redirect ('obwellobjectives:list_obwellobjective')
   return render (request, 'obwellobjectives/obwellobjective_form.html', {'form': form, 'obwellobjective': obwellobjective})

def delete_obwellobjective(request, id):
    obwellobjective = OBWellobjective.objects.get(id=id)
    if request.method == 'POST' :
       obwellobjective.delete()       
       return redirect ('obwellobjectives:list_obwellobjective')
    return render (request, 'obwellobjectives/obwellobjective_confirm_delete.html', {'obwellobjective':obwellobjective })




