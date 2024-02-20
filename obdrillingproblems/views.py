from django.shortcuts import render, redirect
from .models import OBDrillingProblems
from .forms import OBDrillingProblemForm
from obdrillingsummary.models import OBDrillingSummary
from selectedObserver.models import SelectedObserver

def list_obdrilling_problem(request): 
    selectedwell = SelectedObserver.objects.first()   
    obdrilling_problems = OBDrillingProblems.objects.filter(obwellid = selectedwell.wellid).all()  
    return render (request, 'obdrillingproblems/obdrilling_problems.html', {'obdrilling_problems': obdrilling_problems})   
 
def create_obdrilling_problem(request): 
    selectedwell = SelectedObserver.objects.first()
    obdrilling_sum = OBDrillingSummary.objects.get(id=selectedwell.wellid)
    obdrilling_problem = OBDrillingProblems() 
    obdrilling_problem.obdrillingid =obdrilling_sum
    obdrilling_problem.obfgId = obdrilling_sum.fgId
    obdrilling_problem.obwellid = obdrilling_sum.wellid   
    form = OBDrillingProblemForm(request.POST or None, instance=obdrilling_problem)
    if request.method =="POST":  
         form = OBDrillingProblemForm(request.POST, request.FILES, instance=obdrilling_problem)       
         obdrilling_problem.obfgId = obdrilling_sum.fgId
         obdrilling_problem.obwellid = obdrilling_sum.wellid   
         obdrilling_problem.obdrillingid =obdrilling_sum                   
         if form.is_valid():
            form.save()  
            return redirect ('obdrillingproblems:list_obdrilling_problem') 
    return render (request, 'obdrillingproblems/obdrilling_problems_form.html', {'form': form})

def update_obdrilling_problem(request, id):  
    obdrilling_problem = OBDrillingProblems.objects.get(id=id) 
    ctid =(obdrilling_problem.obdrillingid).pk 
    form = OBDrillingProblemForm(request.POST or None, instance=obdrilling_problem)    
    if request.method =="POST":
        form = OBDrillingProblemForm(request.POST, request.FILES, instance=obdrilling_problem)        
        if form.is_valid():
            form.save() 
            ctid =(obdrilling_problem.obdrillingid).pk 
            return redirect ('obdrillingproblems:list_obdrilling_problem')
    return render (request, 'obdrillingproblems/obdrilling_problems_form.html', {'form': form, 'obdrilling_problem':obdrilling_problem, 'id':id})

def delete_obdrilling_problem(request, id):
    obdrilling_problem = OBDrillingProblems.objects.get(id=id)  
    ctid =(obdrilling_problem.obdrillingid).pk  
    if request.method == 'POST' :
        obdrilling_problem.delete()
        return redirect ('obdrillingproblems:list_obdrilling_problem')
    return render (request, 'obdrillingproblems/obdrilling_problems_confirm_delete.html', {'obdrilling_problem':obdrilling_problem, 'id':id})



