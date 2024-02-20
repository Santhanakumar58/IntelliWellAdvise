from django.shortcuts import render, redirect
from .models import WIDrillingProblems
from .forms import WIDrillingProblemForm
from widrillingsummary.models import WIDrillingSummary
from selectedWaterInjector.models import SelectedWaterInjector

def list_widrilling_problem(request): 
    selectedwell = SelectedWaterInjector.objects.first()   
    widrilling_problems = WIDrillingProblems.objects.filter(wiwellid = selectedwell.wellid).all()  
    return render (request, 'widrillingproblems/widrilling_problems.html', {'widrilling_problems': widrilling_problems})   
 
def create_widrilling_problem(request): 
    selectedwell = SelectedWaterInjector.objects.first()
    widrilling_sum = WIDrillingSummary.objects.get(id=selectedwell.wellid)
    widrilling_problem = WIDrillingProblems() 
    widrilling_problem.widrillingid =widrilling_sum
    widrilling_problem.fgId = widrilling_sum.fgId
    widrilling_problem.wellid = widrilling_sum.wellid   
    form = WIDrillingProblemForm(request.POST or None, instance=widrilling_problem)
    if request.method =="POST":  
         form = WIDrillingProblemForm(request.POST, request.FILES, instance=widrilling_problem)       
         widrilling_problem.fgId = widrilling_sum.fgId
         widrilling_problem.wellid = widrilling_sum.wellid   
         widrilling_problem.widrillingid =widrilling_sum                   
         if form.is_valid():
            form.save()  
            return redirect ('widrillingproblems:list_widrilling_problem') 
    return render (request, 'widrillingproblems/widrilling_problems_form.html', {'form': form})

def update_widrilling_problem(request, id):  
    widrilling_problem = WIDrillingProblems.objects.get(id=id) 
    ctid =(widrilling_problem.widrillingid).pk 
    form = WIDrillingProblemForm(request.POST or None, instance=widrilling_problem)    
    if request.method =="POST":
        form = WIDrillingProblemForm(request.POST, request.FILES, instance=widrilling_problem)        
        if form.is_valid():
            form.save() 
            ctid =(widrilling_problem.widrillingid).pk 
            return redirect ('widrillingproblems:list_widrilling_problem')
    return render (request, 'widrillingproblems/widrilling_problems_form.html', {'form': form, 'widrilling_problem':widrilling_problem, 'id':id})

def delete_widrilling_problem(request, id):
    widrilling_problem = WIDrillingProblems.objects.get(id=id)  
    ctid =(widrilling_problem.widrillingid).pk  
    if request.method == 'POST' :
        widrilling_problem.delete()
        return redirect ('widrillingproblems:list_widrilling_problem')
    return render (request, 'widrillingproblems/widrilling_problems_confirm_delete.html', {'widrilling_problem':widrilling_problem, 'id':id})



