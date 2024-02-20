from django.shortcuts import render, redirect
from .models import GITestResultModel
from .forms import GITestResultForm
from selectedGasInjector.models import SelectedGasInjector



def list_gitestresult(request):     
    well = SelectedGasInjector.objects.all().first()   
    results= GITestResultModel.objects.filter(giwellid=well.wellid).all()
    return render (request, 'gitestresults/gitestresult.html', {'results': results})

def create_gitestresult(request):   
    result = GITestResultModel()
    selectedwell = SelectedGasInjector.objects.first()  
    result.fgid = selectedwell.fgid
    result.wellid = selectedwell.wellid   
    form = GITestResultForm(request.POST or None, instance=result)
    if request.method =="POST":  
        form = GITestResultForm(request.POST, request.FILES, instance=result)       
        result.fgid = selectedwell.fgid
        result.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gitestresults:list_gitestresult')
    return render (request, 'gitestresults/gitestresult_form.html', {'form': form})

def update_gitestresult(request, id):
    result = GITestResultModel.objects.get(id=id)
    form = GITestResultForm(request.POST or None, instance=result)
    if form.is_valid():
        form.save()
        return redirect ('gitestresults:list_gitestresult')
    return render (request, 'gitestresults/gitestresult_form.html', {'form': form, 'result':result})

def delete_gitestresult(request, id):
    result = GITestResultModel.objects.get(id=id)    
    if request.method == 'POST' :
        result.delete()
        return redirect ('gitestresults:list_gitestresult')
    return render (request, 'gitestresults/gitestresult_confirm_delete.html', {'result':result})






