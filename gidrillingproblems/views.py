from django.shortcuts import render, redirect
from .models import GIDrillingProblems
from .forms import GIDrillingProblemForm
from gidrillingsummary.models import GIDrillingSummary
from selectedGasProducer.models import SelectedGasProducer

def list_gidrilling_problem(request): 
    selectedwell = SelectedGasProducer.objects.first()   
    gidrilling_problems = GIDrillingProblems.objects.filter(giwellid = selectedwell.wellid).all()  
    return render (request, 'gidrillingproblems/gidrilling_problems.html', {'gidrilling_problems': gidrilling_problems})   
 
def create_gidrilling_problem(request): 
    selectedwell = SelectedGasProducer.objects.first()
    gidrilling_sum = GIDrillingSummary.objects.get(id=selectedwell.wellid)
    gidrilling_problem = GIDrillingProblems() 
    gidrilling_problem.gidrillingid =gidrilling_sum
    gidrilling_problem.fgId = gidrilling_sum.fgId
    gidrilling_problem.wellid = gidrilling_sum.wellid   
    form = GIDrillingProblemForm(request.POST or None, instance=gidrilling_problem)
    if request.method =="POST":  
         form = GIDrillingProblemForm(request.POST, request.FILES, instance=gidrilling_problem)       
         gidrilling_problem.fgId = gidrilling_sum.fgId
         gidrilling_problem.wellid = gidrilling_sum.wellid   
         gidrilling_problem.gidrillingid =gidrilling_sum                   
         if form.is_valid():
            form.save()  
            return redirect ('gidrillingproblems:list_gidrilling_problem') 
    return render (request, 'gidrillingproblems/gidrilling_problems_form.html', {'form': form})

def update_gidrilling_problem(request, id):  
    gidrilling_problem = GIDrillingProblems.objects.get(id=id) 
    ctid =(gidrilling_problem.gidrillingid).pk 
    form = GIDrillingProblemForm(request.POST or None, instance=gidrilling_problem)    
    if request.method =="POST":
        form = GIDrillingProblemForm(request.POST, request.FILES, instance=gidrilling_problem)        
        if form.is_valid():
            form.save() 
            ctid =(gidrilling_problem.gidrillingid).pk 
            return redirect ('gidrillingproblems:list_gidrilling_problem')
    return render (request, 'gidrillingproblems/gidrilling_problems_form.html', {'form': form, 'gidrilling_problem':gidrilling_problem, 'id':id})

def delete_gidrilling_problem(request, id):
    gidrilling_problem = GIDrillingProblems.objects.get(id=id)  
    ctid =(gidrilling_problem.gidrillingid).pk  
    if request.method == 'POST' :
        gidrilling_problem.delete()
        return redirect ('gidrillingproblems:list_gidrilling_problem')
    return render (request, 'gidrillingproblems/gidrilling_problems_confirm_delete.html', {'gidrilling_problem':gidrilling_problem, 'id':id})



