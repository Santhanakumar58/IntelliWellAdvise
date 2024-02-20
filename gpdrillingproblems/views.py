from django.shortcuts import render, redirect
from .models import GPDrillingProblems
from .forms import GPDrillingProblemForm
from gpdrillingsummaary.models import GPDrillingSummary
from selectedGasProducer.models import SelectedGasProducer

def list_gpdrilling_problem(request): 
    selectedwell = SelectedGasProducer.objects.first()   
    gpdrilling_problems = GPDrillingProblems.objects.filter(gpwellid = selectedwell.wellid).all()  
    return render (request, 'gpdrillingproblems/gpdrilling_problems.html', {'gpdrilling_problems': gpdrilling_problems})   
 
def create_gpdrilling_problem(request): 
    selectedwell = SelectedGasProducer.objects.first()
    gpdrilling_sum = GPDrillingSummary.objects.get(id=selectedwell.wellid)
    gpdrilling_problem = GPDrillingProblems() 
    gpdrilling_problem.gpdrillingid =gpdrilling_sum
    gpdrilling_problem.fgId = gpdrilling_sum.fgId
    gpdrilling_problem.wellid = gpdrilling_sum.wellid   
    form = GPDrillingProblemForm(request.POST or None, instance=gpdrilling_problem)
    if request.method =="POST":  
         form = GPDrillingProblemForm(request.POST, request.FILES, instance=gpdrilling_problem)       
         gpdrilling_problem.fgId = gpdrilling_sum.fgId
         gpdrilling_problem.wellid = gpdrilling_sum.wellid   
         gpdrilling_problem.gpdrillingid =gpdrilling_sum                   
         if form.is_valid():
            form.save()  
            return redirect ('gpdrillingproblems:list_gpdrilling_problem') 
    return render (request, 'gpdrillingproblems/gpdrilling_problems_form.html', {'form': form})

def update_gpdrilling_problem(request, id):  
    gpdrilling_problem = GPDrillingProblems.objects.get(id=id) 
    ctid =(gpdrilling_problem.gpdrillingid).pk 
    form = GPDrillingProblemForm(request.POST or None, instance=gpdrilling_problem)    
    if request.method =="POST":
        form = GPDrillingProblemForm(request.POST, request.FILES, instance=gpdrilling_problem)        
        if form.is_valid():
            form.save() 
            ctid =(gpdrilling_problem.gpdrillingid).pk 
            return redirect ('gpdrillingproblems:list_gpdrilling_problem')
    return render (request, 'gpdrillingproblems/gpdrilling_problems_form.html', {'form': form, 'gpdrilling_problem':gpdrilling_problem, 'id':id})

def delete_gpdrilling_problem(request, id):
    gpdrilling_problem = GPDrillingProblems.objects.get(id=id)  
    ctid =(gpdrilling_problem.gpdrillingid).pk  
    if request.method == 'POST' :
        gpdrilling_problem.delete()
        return redirect ('gpdrillingproblems:list_gpdrilling_problem')
    return render (request, 'gpdrillingproblems/gpdrilling_problems_confirm_delete.html', {'gpdrilling_problem':gpdrilling_problem, 'id':id})


