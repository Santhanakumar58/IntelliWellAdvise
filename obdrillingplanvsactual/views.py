from django.shortcuts import render, redirect
from obdrillingplanvsactual.utils import get_plot
from .models import OBDrillingPlanVsActual
from .forms import OBDrillingPlanForm
from obdrillingsummary.models import OBDrillingSummary
from selectedObserver.models import SelectedObserver

def list_obdrilling_plan(request): 
    selectedwell = SelectedObserver.objects.all().first()
    obdrilling_plans = OBDrillingPlanVsActual.objects.filter(obwellid = selectedwell.wellid).all()  
    x=[x.section for x in obdrilling_plans]     
    y=[y.plan_Days for y in obdrilling_plans]
    y1=[y1.actual_Days for y1 in obdrilling_plans]
    totaly = sum(y)
    totaly1 = sum(y1)
    x.append('Total')
    y.append(totaly)
    y1.append(totaly1)
    chart = get_plot(x,y,y1) 
    return render (request, 'obdrillingplanvsactual/obdrilling_plan.html', {'obdrilling_plans': obdrilling_plans,'chart':chart })   
 
def create_obdrilling_plan(request):    
    selectedwell = SelectedObserver.objects.all().first()
    obdrilling_plan = OBDrillingPlanVsActual()     
    obdrilling_plan.gpfgId = selectedwell.fgid
    obdrilling_plan.gpwellid = selectedwell.wellid   
    form = OBDrillingPlanForm(request.POST or None, instance=obdrilling_plan)
    if request.method =="POST":  
         form = OBDrillingPlanForm(request.POST, request.FILES, instance=obdrilling_plan)       
         obdrilling_plan.gpfgId = selectedwell.fgid
         obdrilling_plan.gpwellid = selectedwell.wellid  
         if form.is_valid():
            form.save()  
            return redirect ('obdrillingplanvsactual:list_obdrilling_plan') 
    return render (request, 'obdrillingplanvsactual/obdrilling_plan_form.html', {'form': form})

def update_obdrilling_plan(request, id):  
    obdrilling_plan = OBDrillingPlanVsActual.objects.get(id=id)   
    form = OBDrillingPlanForm(request.POST or None, instance=obdrilling_plan)    
    if request.method =="POST":
        form = OBDrillingPlanForm(request.POST, request.FILES, instance=obdrilling_plan)        
        if form.is_valid():
            form.save()            
            return redirect ('obdrillingplanvsactual:list_obdrilling_plan')
    return render (request, 'obdrillingplanvsactual/obdrilling_plan_form.html', {'form': form, 'obdrilling_plan':obdrilling_plan, 'id':id})

def delete_obdrilling_plan(request, id):
    obdrilling_plan = OBDrillingPlanVsActual.objects.get(id=id) 
    if request.method == 'POST' :
        obdrilling_plan.delete()
        return redirect ('obdrillingplanvsactual:list_obdrilling_plan')
    return render (request, 'obdrillingplanvsactual/obdrilling_plan_confirm_delete.html', {'obdrilling_plan':obdrilling_plan, 'id':id})



