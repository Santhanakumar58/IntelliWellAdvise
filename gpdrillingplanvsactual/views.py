from django.shortcuts import render, redirect
from gpdrillingplanvsactual.utils import get_plot
from .models import GPDrillingPlanVsActual
from .forms import GPDrillingPlanForm
from gpdrillingsummaary.models import GPDrillingSummary
from selectedGasProducer.models import SelectedGasProducer

def list_gpdrilling_plan(request): 
    selectedwell = SelectedGasProducer.objects.all().first()
    gpdrilling_plans = GPDrillingPlanVsActual.objects.filter(gpwellid = selectedwell.wellid).all()  
    x=[x.section for x in gpdrilling_plans]     
    y=[y.plan_Days for y in gpdrilling_plans]
    y1=[y1.actual_Days for y1 in gpdrilling_plans]
    totaly = sum(y)
    totaly1 = sum(y1)
    x.append('Total')
    y.append(totaly)
    y1.append(totaly1)
    chart = get_plot(x,y,y1) 
    return render (request, 'gpdrillingplanvsactual/gpdrilling_plan.html', {'gpdrilling_plans': gpdrilling_plans,'chart':chart })   
 
def create_gpdrilling_plan(request):    
    selectedwell = SelectedGasProducer.objects.all().first()
    gpdrilling_plan = GPDrillingPlanVsActual()     
    gpdrilling_plan.gpfgId = selectedwell.fgid
    gpdrilling_plan.gpwellid = selectedwell.wellid   
    form = GPDrillingPlanForm(request.POST or None, instance=gpdrilling_plan)
    if request.method =="POST":  
         form = GPDrillingPlanForm(request.POST, request.FILES, instance=gpdrilling_plan)       
         gpdrilling_plan.gpfgId = selectedwell.fgid
         gpdrilling_plan.gpwellid = selectedwell.wellid  
         if form.is_valid():
            form.save()  
            return redirect ('gpdrillingplanvsactual:list_gpdrilling_plan') 
    return render (request, 'gpdrillingplanvsactual/gpdrilling_plan_form.html', {'form': form})

def update_gpdrilling_plan(request, id):  
    gpdrilling_plan = GPDrillingPlanVsActual.objects.get(id=id)   
    form = GPDrillingPlanForm(request.POST or None, instance=gpdrilling_plan)    
    if request.method =="POST":
        form = GPDrillingPlanForm(request.POST, request.FILES, instance=gpdrilling_plan)        
        if form.is_valid():
            form.save()            
            return redirect ('gpdrillingplanvsactual:list_gpdrilling_plan')
    return render (request, 'gpdrillingplanvsactual/gpdrilling_plan_form.html', {'form': form, 'gpdrilling_plan':gpdrilling_plan, 'id':id})

def delete_gpdrilling_plan(request, id):
    gpdrilling_plan = GPDrillingPlanVsActual.objects.get(id=id) 
    if request.method == 'POST' :
        gpdrilling_plan.delete()
        return redirect ('gpdrillingplanvsactual:list_gpdrilling_plan')
    return render (request, 'gpdrillingplanvsactual/gpdrilling_plan_confirm_delete.html', {'gpdrilling_plan':gpdrilling_plan, 'id':id})



