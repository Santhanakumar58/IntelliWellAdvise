from django.shortcuts import render, redirect
from .models import WITestResultModel
from .forms import WITestResultForm
from selectedWaterInjector.models import SelectedWaterInjector



def list_witestresult(request):     
    well = SelectedWaterInjector.objects.all().first()   
    results= WITestResultModel.objects.filter(wiwellid=well.wellid).all()
    return render (request, 'witestresults/witestresult.html', {'results': results})

def create_witestresult(request):   
    result = WITestResultModel()
    selectedwell = SelectedWaterInjector.objects.first()  
    result.fgid = selectedwell.fgid
    result.wellid = selectedwell.wellid   
    form = WITestResultForm(request.POST or None, instance=result)
    if request.method =="POST":  
        form = WITestResultForm(request.POST, request.FILES, instance=result)       
        result.fgid = selectedwell.fgid
        result.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('witestresults:list_witestresult')
    return render (request, 'witestresults/witestresult_form.html', {'form': form})

def update_witestresult(request, id):
    result = WITestResultModel.objects.get(id=id)
    form = WITestResultForm(request.POST or None, instance=result)
    if form.is_valid():
        form.save()
        return redirect ('witestresults:list_witestresult')
    return render (request, 'witestresults/witestresult_form.html', {'form': form, 'result':result})

def delete_witestresult(request, id):
    result = WITestResultModel.objects.get(id=id)    
    if request.method == 'POST' :
        result.delete()
        return redirect ('witestresults:list_witestresult')
    return render (request, 'witestresults/witestresult_confirm_delete.html', {'result':result})





