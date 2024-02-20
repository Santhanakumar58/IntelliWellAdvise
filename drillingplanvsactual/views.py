from django.shortcuts import render, redirect
from drillingplanvsactual.utils import get_plot
from .models import DrillingPlanVsActual
from .forms import DrillingPlanForm
from drillingsummary.models import DrillingSummary
from selectedOilProducer.models import SelectedOilProducer

def list_drilling_plan(request): 
    selectedwell = SelectedOilProducer.objects.all().first()
    drilling_plans = DrillingPlanVsActual.objects.filter(wellid = selectedwell.wellid).all()  
    x=[x.section for x in drilling_plans]     
    y=[y.plan_Days for y in drilling_plans]
    y1=[y1.actual_Days for y1 in drilling_plans]
    totaly = sum(y)
    totaly1 = sum(y1)
    x.append('Total')
    y.append(totaly)
    y1.append(totaly1)
    chart = get_plot(x,y,y1) 
    return render (request, 'drillingplanvsactual/drilling_plan.html', {'drilling_plans': drilling_plans,'chart':chart })   
 
def create_drilling_plan(request):    
    selectedwell = SelectedOilProducer.objects.all().first()
    drilling_plan = DrillingPlanVsActual()     
    drilling_plan.fgId = selectedwell.fgid
    drilling_plan.wellid = selectedwell.wellid   
    form = DrillingPlanForm(request.POST or None, instance=drilling_plan)
    if request.method =="POST":  
         form = DrillingPlanForm(request.POST, request.FILES, instance=drilling_plan)       
         drilling_plan.fgId = selectedwell.fgid
         drilling_plan.wellid = selectedwell.wellid  
         if form.is_valid():
            form.save()  
            return redirect ('drillingplanvsactual:list_drilling_plan') 
    return render (request, 'drillingplanvsactual/drilling_plan_form.html', {'form': form})

def update_drilling_plan(request, id):  
    drilling_plan = DrillingPlanVsActual.objects.get(id=id)   
    form = DrillingPlanForm(request.POST or None, instance=drilling_plan)    
    if request.method =="POST":
        form = DrillingPlanForm(request.POST, request.FILES, instance=drilling_plan)        
        if form.is_valid():
            form.save()            
            return redirect ('drillingplanvsactual:list_drilling_plan')
    return render (request, 'drillingplanvsactual/drilling_plan_form.html', {'form': form, 'drilling_plan':drilling_plan, 'id':id})

def delete_drilling_plan(request, id):
    drilling_plan = DrillingPlanVsActual.objects.get(id=id) 
    if request.method == 'POST' :
        drilling_plan.delete()
        return redirect ('drillingplanvsactual:list_drilling_plan')
    return render (request, 'drillingplanvsactual/drilling_plan_confirm_delete.html', {'drilling_plan':drilling_plan, 'id':id})


