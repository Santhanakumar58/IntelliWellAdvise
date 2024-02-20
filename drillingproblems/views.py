from django.shortcuts import render, redirect
from .models import DrillingProblems
from .forms import DrillingProblemForm
from drillingsummary.models import DrillingSummary
from selectedOilProducer.models import SelectedOilProducer

def list_drilling_problem(request): 
    selectedwell = SelectedOilProducer.objects.first()   
    drilling_problems = DrillingProblems.objects.filter(wellid = selectedwell.wellid).all()  
    return render (request, 'drillingproblems/drilling_problems.html', {'drilling_problems': drilling_problems})   
 
def create_drilling_problem(request): 
    selectedwell = SelectedOilProducer.objects.first()
    drilling_sum = DrillingSummary.objects.get(id=selectedwell.wellid)
    drilling_problem = DrillingProblems() 
    drilling_problem.drillingid =drilling_sum
    drilling_problem.fgId = drilling_sum.fgId
    drilling_problem.wellid = drilling_sum.wellid   
    form = DrillingProblemForm(request.POST or None, instance=drilling_problem)
    if request.method =="POST":  
         form = DrillingProblemForm(request.POST, request.FILES, instance=drilling_problem)       
         drilling_problem.fgId = drilling_sum.fgId
         drilling_problem.wellid = drilling_sum.wellid   
         drilling_problem.drillingid =drilling_sum                   
         if form.is_valid():
            form.save()  
            return redirect ('drillingproblems:list_drilling_problem') 
    return render (request, 'drillingproblems/drilling_problems_form.html', {'form': form})

def update_drilling_problem(request, id):  
    drilling_problem = DrillingProblems.objects.get(id=id) 
    ctid =(drilling_problem.drillingid).pk 
    form = DrillingProblemForm(request.POST or None, instance=drilling_problem)    
    if request.method =="POST":
        form = DrillingProblemForm(request.POST, request.FILES, instance=drilling_problem)        
        if form.is_valid():
            form.save() 
            ctid =(drilling_problem.drillingid).pk 
            return redirect ('drillingproblems:list_drilling_problem')
    return render (request, 'drillingproblems/drilling_problems_form.html', {'form': form, 'drilling_problem':drilling_problem, 'id':id})

def delete_drilling_problem(request, id):
    drilling_problem = DrillingProblems.objects.get(id=id)  
    ctid =(drilling_problem.drillingid).pk  
    if request.method == 'POST' :
        drilling_problem.delete()
        return redirect ('drillingproblems:list_drilling_problem')
    return render (request, 'drillingproblems/drilling_problems_confirm_delete.html', {'drilling_problem':drilling_problem, 'id':id})

