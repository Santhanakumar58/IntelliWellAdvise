from django.shortcuts import render, redirect
from .models import GIWellobjective
from giwellobjectivedata.models import GIWellobjectivedata
from selectedGasProducer.models import SelectedGasProducer
from .forms import GIWellObjectiveForm
from .utils import get_plot1, get_plot2
from IntelligentOilWell.custom_context_processors import selectedwell

def list_giwellobjective(request):  
    selectedwell = SelectedGasProducer.objects.first()     
    id1= selectedwell.wellid
    giwellobjectives = GIWellobjective.objects.filter(giwellid=id1).values() 
    giwellobjectivedata = GIWellobjectivedata.objects.filter(giwellid=id1).all()           
    x=[x.date for x in giwellobjectivedata]
    y=[y.gasrate_mmscfd for y in giwellobjectivedata]
    z=[z.cgr_barrels_per_mmscf for z in giwellobjectivedata]
    y1=[y1.condensaterate for y1 in giwellobjectivedata]
    y2=[y2.waterate for y2 in giwellobjectivedata]
    y3=[y3.liquidrate for y3 in giwellobjectivedata]
    y4=[y4.watercut_percentage for y4 in giwellobjectivedata]    
    chart1 = get_plot1(x,y,y1)  
    chart2 = get_plot2(x,z,y2)
    context = {'giwellobjectives': giwellobjectives, 'chart1':chart1,'chart2':chart2,'selectedwell':selectedwell}
    return render (request, 'giwellobjectives/giwellobjective.html', context) 

def create_giwellobjective(request): 
   selectedwell = SelectedGasProducer.objects.first()     
   id1= selectedwell.wellid    
   objective = GIWellobjective()  
   objective.gpwellid=id1   
   objective.gpfgid=selectedwell.fgid   
   objective.gpwellname=selectedwell.wellname 
   form = GIWellObjectiveForm(request.POST or None, instance=objective)   
   if form.is_valid():        
       form.save()
       return redirect ('giwellobjectives:list_giwellobjective')
   return render (request, 'giwellobjectives/giwellobjective_form.html', {'form': form})

def update_giwellobjective(request, id):
   giwellobjective = GIWellobjective.objects.get(id=id)
   form = GIWellObjectiveForm(request.POST or None, instance=giwellobjective)

   if form.is_valid():        
        giwellobjective.save()       
        return redirect ('giwellobjectives:list_giwellobjective')
   return render (request, 'giwellobjectives/giwellobjective_form.html', {'form': form, 'giwellobjective': giwellobjective})

def delete_giwellobjective(request, id):
    giwellobjective = GIWellobjective.objects.get(id=id)
    if request.method == 'POST' :
       giwellobjective.delete()       
       return redirect ('giwellobjectives:list_giwellobjective')
    return render (request, 'giwellobjectives/giwellobjective_confirm_delete.html', {'giwellobjective':giwellobjective })



