from django.shortcuts import render, redirect
from .models import GPTestResultModel
from .forms import GPTestResultForm
from selectedGasProducer.models import SelectedGasProducer



def list_gptestresult(request):     
    well = SelectedGasProducer.objects.all().first()   
    results= GPTestResultModel.objects.filter(gpwellid=well.wellid).all()
    return render (request, 'gptestresults/gptestresult.html', {'results': results})

def create_gptestresult(request):   
    result = GPTestResultModel()
    selectedwell = SelectedGasProducer.objects.first()  
    result.fgid = selectedwell.fgid
    result.wellid = selectedwell.wellid   
    form = GPTestResultForm(request.POST or None, instance=result)
    if request.method =="POST":  
        form = GPTestResultForm(request.POST, request.FILES, instance=result)       
        result.fgid = selectedwell.fgid
        result.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gptestresults:list_gptestresult')
    return render (request, 'gptestresults/gptestresult_form.html', {'form': form})

def update_gptestresult(request, id):
    result = GPTestResultModel.objects.get(id=id)
    form = GPTestResultForm(request.POST or None, instance=result)
    if form.is_valid():
        form.save()
        return redirect ('gptestresults:list_gptestresult')
    return render (request, 'gptestresults/gptestresult_form.html', {'form': form, 'result':result})

def delete_gptestresult(request, id):
    result = GPTestResultModel.objects.get(id=id)    
    if request.method == 'POST' :
        result.delete()
        return redirect ('gptestresults:list_gptestresult')
    return render (request, 'gptestresults/gptestresult_confirm_delete.html', {'result':result})





