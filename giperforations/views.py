from django.shortcuts import render, redirect
from .models import GIPerforationModel
from .forms import GIPerforationForm
from selectedGasInjector.models import SelectedGasInjector

def list_giperforation(request):     
    well = SelectedGasInjector.objects.all().first()   
    perfs= GIPerforationModel.objects.filter(giwellid=well.wellid).all()
    return render (request, 'giperforations/giperforation.html', {'perfs': perfs})

def create_giperforation(request):   
    perf = GIPerforationModel()
    selectedwell = SelectedGasInjector.objects.first()  
    perf.gpfgid = selectedwell.fgid
    perf.gpwellid = selectedwell.wellid   
    form = GIPerforationForm(request.POST or None, instance=perf)
    if request.method =="POST":  
        form = GIPerforationForm(request.POST, request.FILES, instance=perf)       
        perf.gpfgid = selectedwell.fgid
        perf.gpfgidwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('giperforations:list_giperforation')
    return render (request, 'giperforations/giperforation_form.html', {'form': form})

def update_giperforation(request, id):
    perf = GIPerforationModel.objects.get(id=id)
    form = GIPerforationForm(request.POST or None, instance=perf)
    if form.is_valid():
        form.save()
        return redirect ('giperforations:list_giperforation')
    return render (request, 'giperforations/giperforation_form.html', {'form': form, 'perf':perf})

def delete_giperforation(request, id):
    perf = GIPerforationModel.objects.get(id=id)    
    if request.method == 'POST' :
        perf.delete()
        return redirect ('giperforations:list_giperforation')
    return render (request, 'giperforations/giperforation_confirm_delete.html', {'perf':perf})





