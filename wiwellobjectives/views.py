from django.shortcuts import render, redirect
from .models import WIWellobjective
from wiwellobjectivedata.models import WIWellobjectivedata
from selectedWaterInjector.models import SelectedWaterInjector
from .forms import WIWellObjectiveForm
from .utils import get_plot1, get_plot2
from IntelligentOilWell.custom_context_processors import selectedwell

def list_wiwellobjective(request):  
    selectedwell = SelectedWaterInjector.objects.first()     
    id1= selectedwell.wellid
    wiwellobjectives = WIWellobjective.objects.filter(wiwellid=id1).values() 
    wiwellobjectivedata = WIWellobjectivedata.objects.filter(wiwellid=id1).all()           
    x=[x.date for x in wiwellobjectivedata]
    y=[y.wat_inj_rate for y in wiwellobjectivedata]
    z=[z.wat_inj_pressure for z in wiwellobjectivedata]
    y1=[y1.tds_ppm for y1 in wiwellobjectivedata]
    y2=[y2.pH for y2 in wiwellobjectivedata]       
    chart1 = get_plot1(x,y,y1)  
    chart2 = get_plot2(x,z,y2)
    context = {'wiwellobjectives': wiwellobjectives, 'chart1':chart1,'chart2':chart2,'selectedwell':selectedwell}
    return render (request, 'wiwellobjectives/wiwellobjective.html', context) 

def create_wiwellobjective(request): 
   selectedwell = SelectedWaterInjector.objects.first()     
   id1= selectedwell.wellid     
   objective = WIWellobjective()  
   objective.wiwellid=id1   
   objective.wifgid=selectedwell.fgid   
   objective.wiwellname=selectedwell.wellname 
   form = WIWellObjectiveForm(request.POST or None, instance=objective)   
   if form.is_valid():        
       form.save()
       return redirect ('wiwellobjectives:list_wiwellobjective')
   return render (request, 'wiwellobjectives/wiwellobjective_form.html', {'form': form})

def update_wiwellobjective(request, id):
   wiwellobjective = WIWellobjective.objects.get(id=id)
   form = WIWellObjectiveForm(request.POST or None, instance=wiwellobjective)

   if form.is_valid():        
        wiwellobjective.save()       
        return redirect ('wiwellobjectives:list_wiwellobjective')
   return render (request, 'wiwellobjectives/wiwellobjective_form.html', {'form': form, 'wiwellobjective': wiwellobjective})

def delete_wiwellobjective(request, id):
    wiwellobjective = WIWellobjective.objects.get(id=id)
    if request.method == 'POST' :
       wiwellobjective.delete()       
       return redirect ('wiwellobjectives:list_wiwellobjective')
    return render (request, 'wiwellobjectives/wiwellobjective_confirm_delete.html', {'wiwellobjective':wiwellobjective })




