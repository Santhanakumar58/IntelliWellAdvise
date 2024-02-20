from django.shortcuts import render, redirect
from .models import OPWellobjective
from opwellobjectivedata.models import OPWellobjectivedata
from selectedOilProducer.models import SelectedOilProducer
from .forms import OPWellObjectiveForm
from .utils import get_plot
from IntelligentOilWell.custom_context_processors import selectedwell

def list_opwellobjective(request):  
    selectedwell = SelectedOilProducer.objects.first()     
    id1= selectedwell.wellid
    opwellobjectives = OPWellobjective.objects.filter(wellid=id1).values() 
    opwellobjectivedata = OPWellobjectivedata.objects.filter(wellid=id1).all()           
    x=[x.date for x in opwellobjectivedata]
    y=[y.gasrate/1000 for y in opwellobjectivedata]
    z=[z.gasoilratio for z in opwellobjectivedata]
    y1=[y1.oilrate for y1 in opwellobjectivedata]
    y2=[y2.waterate for y2 in opwellobjectivedata]
    y3=[y3.liquidrate for y3 in opwellobjectivedata]
    y4=[y4.watercut for y4 in opwellobjectivedata]  
    chart = get_plot(x,y,z,y1,y2, y3,y4)      
    context = {'opwellobjectives': opwellobjectives, 'chart':chart, 'selectedwell':selectedwell}
    return render (request, 'opwellobjectives/opwellobjective.html', context) 

def create_opwellobjective(request): 
   selectedwell = SelectedOilProducer.objects.first()     
   id1= selectedwell.wellid  
   objective = OPWellobjective()  
   objective.wellid=id1   
   objective.opfgid=selectedwell.fgid   
   objective.opwellname=selectedwell.wellname 
   form = OPWellObjectiveForm(request.POST or None, instance=objective)   
   if form.is_valid():        
       form.save()
       return redirect ('opwellobjectives:list_opwellobjective')
   return render (request, 'opwellobjectives/opwellobjective_form.html', {'form': form})

def update_opwellobjective(request, id):
   opwellobjective = OPWellobjective.objects.get(id=id)
   form = OPWellObjectiveForm(request.POST or None, instance=opwellobjective)

   if form.is_valid():        
        opwellobjective.save()       
        return redirect ('opwellobjectives:list_opwellobjective')
   return render (request, 'opwellobjectives/opwellobjective_form.html', {'form': form, 'opwellobjective': opwellobjective})

def delete_opwellobjective(request, id):
    opwellobjective = OPWellobjective.objects.get(id=id)
    if request.method == 'POST' :
       opwellobjective.delete()       
       return redirect ('opwellobjectives:list_opwellobjective')
    return render (request, 'opwellobjectives/opwellobjective_confirm_delete.html', {'opwellobjective':opwellobjective })


