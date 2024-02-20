from django.shortcuts import render, redirect
from .models import GPWellobjective
from gpwellobjectivedata.models import GPWellobjectivedata
from selectedGasProducer.models import SelectedGasProducer
from .forms import GPWellObjectiveForm
from .utils import get_plot1, get_plot2
from IntelligentOilWell.custom_context_processors import selectedgpwell


def list_gpwellobjective(request):  
    selectedwell = SelectedGasProducer.objects.first()  
    id1= selectedwell.wellid
    gpwellobjectives = GPWellobjective.objects.filter(gpwellid=id1).values() 
    gpwellobjectivedata = GPWellobjectivedata.objects.filter(gpwellid=id1).all()           
    x=[x.date for x in gpwellobjectivedata]
    y=[y.gasrate_mmscfd for y in gpwellobjectivedata]
    z=[z.cgr_barrels_per_mmscf for z in gpwellobjectivedata]
    y1=[y1.condensaterate for y1 in gpwellobjectivedata]
    y2=[y2.waterate for y2 in gpwellobjectivedata]
    y3=[y3.liquidrate for y3 in gpwellobjectivedata]
    y4=[y4.watercut_percentage for y4 in gpwellobjectivedata]    
    chart1 = get_plot1(x,y,y1)  
    chart2 = get_plot2(x,z,y2)
    context = {'gpwellobjectives': gpwellobjectives, 'chart1':chart1,'chart2':chart2,'selectedwell':selectedwell}
    return render (request, 'gpwellobjectives/gpwellobjective.html', context) 

def create_gpwellobjective(request): 
   selectedwell = SelectedGasProducer.objects.first()     
   id1= selectedwell.wellid  
   print(id1, selectedwell.wellname, selectedwell.fgid)
   objective = GPWellobjective()  
   objective.gpwellid=id1   
   objective.gpfgid=selectedwell.fgid   
   objective.gpwellname=selectedwell.wellname 
   form = GPWellObjectiveForm(request.POST or None, instance=objective)   
   if form.is_valid():        
       form.save()
       return redirect ('gpwellobjectives:list_gpwellobjective')
   return render (request, 'gpwellobjectives/gpwellobjective_form.html', {'form': form})

def update_gpwellobjective(request, id):
   gpwellobjective = GPWellobjective.objects.get(id=id)
   form = GPWellObjectiveForm(request.POST or None, instance=gpwellobjective)

   if form.is_valid():        
        gpwellobjective.save()       
        return redirect ('gpwellobjectives:list_gpwellobjective')
   return render (request, 'gpwellobjectives/gpwellobjective_form.html', {'form': form, 'gpwellobjective': gpwellobjective})

def delete_gpwellobjective(request, id):
    gpwellobjective = GPWellobjective.objects.get(id=id)
    if request.method == 'POST' :
       gpwellobjective.delete()       
       return redirect ('gpwellobjectives:list_gpwellobjective')
    return render (request, 'gpwellobjectives/gpwellobjective_confirm_delete.html', {'gpwellobjective':gpwellobjective })



