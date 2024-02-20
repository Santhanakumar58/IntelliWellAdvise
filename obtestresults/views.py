from django.shortcuts import render, redirect
from .models import OBTestResultModel
from .forms import OBTestResultForm
from selectedObserver.models import SelectedObserver



def list_obtestresult(request):     
    well = SelectedObserver.objects.all().first()   
    results= OBTestResultModel.objects.filter(obwellid=well.wellid).all()
    return render (request, 'obtestresults/obtestresult.html', {'results': results})

def create_obtestresult(request):   
    result = OBTestResultModel()
    selectedwell = SelectedObserver.objects.first()  
    result.obfgid = selectedwell.fgid
    result.obwellid = selectedwell.wellid   
    form = OBTestResultForm(request.POST or None, instance=result)
    if request.method =="POST":  
        form = OBTestResultForm(request.POST, request.FILES, instance=result)       
        result.fgid = selectedwell.fgid
        result.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('obtestresults:list_obtestresult')
    return render (request, 'obtestresults/obtestresult_form.html', {'form': form})

def update_obtestresult(request, id):
    result = OBTestResultModel.objects.get(id=id)
    form = OBTestResultForm(request.POST or None, instance=result)
    if form.is_valid():
        form.save()
        return redirect ('obtestresults:list_obtestresult')
    return render (request, 'obtestresults/obtestresult_form.html', {'form': form, 'result':result})

def delete_obtestresult(request, id):
    result = OBTestResultModel.objects.get(id=id)    
    if request.method == 'POST' :
        result.delete()
        return redirect ('obtestresults:list_obtestresult')
    return render (request, 'obtestresults/obtestresult_confirm_delete.html', {'result':result})





