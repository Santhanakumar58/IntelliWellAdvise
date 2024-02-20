from django.shortcuts import render, redirect
from .models import TestResultModel
from .forms import TestResultForm
from selectedOilProducer.models import SelectedOilProducer



def list_testresult(request):     
    well = SelectedOilProducer.objects.all().first()   
    results= TestResultModel.objects.filter(wellid=well.wellid).all()
    return render (request, 'testresults/testresult.html', {'results': results})

def create_testresult(request):   
    result = TestResultModel()
    selectedwell = SelectedOilProducer.objects.first()  
    result.fgid = selectedwell.fgid
    result.wellid = selectedwell.wellid   
    form = TestResultForm(request.POST or None, instance=result)
    if request.method =="POST":  
        form = TestResultForm(request.POST, request.FILES, instance=result)       
        result.fgid = selectedwell.fgid
        result.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('testresults:list_testresult')
    return render (request, 'testresults/testresult_form.html', {'form': form})

def update_testresult(request, id):
    result = TestResultModel.objects.get(id=id)
    form = TestResultForm(request.POST or None, instance=result)
    if form.is_valid():
        form.save()
        return redirect ('testresults:list_testresult')
    return render (request, 'testresults/testresult_form.html', {'form': form, 'result':result})

def delete_testresult(request, id):
    result = TestResultModel.objects.get(id=id)    
    if request.method == 'POST' :
        result.delete()
        return redirect ('testresults:list_testresult')
    return render (request, 'testresults/testresult_confirm_delete.html', {'result':result})




