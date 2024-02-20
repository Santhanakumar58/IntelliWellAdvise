from django.shortcuts import render, redirect
from widrillingplanvsactual.utils import get_plot
from .models import WIDrillingPlanVsActual
from .forms import WIDrillingPlanForm
from widrillingsummary.models import WIDrillingSummary
from selectedWaterInjector.models import SelectedWaterInjector

def list_widrilling_plan(request): 
    selectedwell = SelectedWaterInjector.objects.all().first()
    widrilling_plans = WIDrillingPlanVsActual.objects.filter(wiwellid = selectedwell.wellid).all()  
    x=[x.section for x in widrilling_plans]     
    y=[y.plan_Days for y in widrilling_plans]
    y1=[y1.actual_Days for y1 in widrilling_plans]
    totaly = sum(y)
    totaly1 = sum(y1)
    x.append('Total')
    y.append(totaly)
    y1.append(totaly1)
    chart = get_plot(x,y,y1) 
    return render (request, 'widrillingplanvsactual/widrilling_plan.html', {'widrilling_plans': widrilling_plans,'chart':chart })   
 
def create_widrilling_plan(request):    
    selectedwell = SelectedWaterInjector.objects.all().first()
    widrilling_plan = WIDrillingPlanVsActual()     
    widrilling_plan.gpfgId = selectedwell.fgid
    widrilling_plan.gpwellid = selectedwell.wellid   
    form = WIDrillingPlanForm(request.POST or None, instance=widrilling_plan)
    if request.method =="POST":  
         form = WIDrillingPlanForm(request.POST, request.FILES, instance=widrilling_plan)       
         widrilling_plan.gpfgId = selectedwell.fgid
         widrilling_plan.gpwellid = selectedwell.wellid  
         if form.is_valid():
            form.save()  
            return redirect ('widrillingplanvsactual:list_widrilling_plan') 
    return render (request, 'widrillingplanvsactual/widrilling_plan_form.html', {'form': form})

def update_widrilling_plan(request, id):  
    widrilling_plan = WIDrillingPlanVsActual.objects.get(id=id)   
    form = WIDrillingPlanForm(request.POST or None, instance=widrilling_plan)    
    if request.method =="POST":
        form = WIDrillingPlanForm(request.POST, request.FILES, instance=widrilling_plan)        
        if form.is_valid():
            form.save()            
            return redirect ('widrillingplanvsactual:list_widrilling_plan')
    return render (request, 'widrillingplanvsactual/widrilling_plan_form.html', {'form': form, 'widrilling_plan':widrilling_plan, 'id':id})

def delete_widrilling_plan(request, id):
    widrilling_plan = WIDrillingPlanFormDrillingPlanVsActual.objects.get(id=id) 
    if request.method == 'POST' :
        widrilling_plan.delete()
        return redirect ('widrillingplanvsactual:list_widrilling_plan')
    return render (request, 'widrillingplanvsactual/widrilling_plan_confirm_delete.html', {'widrilling_plan':widrilling_plan, 'id':id})




