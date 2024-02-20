from django.shortcuts import render, redirect
from gidrillingplanvsactual.utils import get_plot
from .models import GIDrillingPlanVsActual
from .forms import GIDrillingPlanForm
from gidrillingsummary.models import GIDrillingSummary
from selectedGasInjector.models import SelectedGasInjector

def list_gidrilling_plan(request): 
    selectedwell = SelectedGasInjector.objects.all().first()
    gidrilling_plans = GIDrillingPlanVsActual.objects.filter(giwellid = selectedwell.wellid).all()  
    x=[x.section for x in gidrilling_plans]     
    y=[y.plan_Days for y in gidrilling_plans]
    y1=[y1.actual_Days for y1 in gidrilling_plans]
    totaly = sum(y)
    totaly1 = sum(y1)
    x.append('Total')
    y.append(totaly)
    y1.append(totaly1)
    chart = get_plot(x,y,y1) 
    return render (request, 'gidrillingplanvsactual/gidrilling_plan.html', {'gidrilling_plans': gidrilling_plans,'chart':chart })   
 
def create_gidrilling_plan(request):    
    selectedwell = SelectedGasInjector.objects.all().first()
    gidrilling_plan = GIDrillingPlanVsActual()     
    gidrilling_plan.gpfgId = selectedwell.fgid
    gidrilling_plan.gpwellid = selectedwell.wellid   
    form = GIDrillingPlanForm(request.POST or None, instance=gidrilling_plan)
    if request.method =="POST":  
         form = GIDrillingPlanForm(request.POST, request.FILES, instance=gidrilling_plan)       
         gidrilling_plan.gpfgId = selectedwell.fgid
         gidrilling_plan.gpwellid = selectedwell.wellid  
         if form.is_valid():
            form.save()  
            return redirect ('gidrillingplanvsactual:list_gidrilling_plan') 
    return render (request, 'gidrillingplanvsactual/gidrilling_plan_form.html', {'form': form})

def update_gidrilling_plan(request, id):  
    gidrilling_plan = GIDrillingPlanVsActual.objects.get(id=id)   
    form = GIDrillingPlanForm(request.POST or None, instance=gidrilling_plan)    
    if request.method =="POST":
        form = GIDrillingPlanForm(request.POST, request.FILES, instance=gidrilling_plan)        
        if form.is_valid():
            form.save()            
            return redirect ('gidrillingplanvsactual:list_gidrilling_plan')
    return render (request, 'gidrillingplanvsactual/gidrilling_plan_form.html', {'form': form, 'gidrilling_plan':gidrilling_plan, 'id':id})

def delete_gidrilling_plan(request, id):
    gidrilling_plan = GIDrillingPlanVsActual.objects.get(id=id) 
    if request.method == 'POST' :
        gidrilling_plan.delete()
        return redirect ('gidrillingplanvsactual:list_gidrilling_plan')
    return render (request, 'gidrillingplanvsactual/gidrilling_plan_confirm_delete.html', {'gidrilling_plan':gidrilling_plan, 'id':id})




