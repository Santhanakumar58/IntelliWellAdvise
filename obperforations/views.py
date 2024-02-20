from django.shortcuts import render, redirect
from .models import OBPerforationModel
from .forms import OBPerforationForm
from selectedObserver.models import SelectedObserver

def list_obperforation(request):     
    well = SelectedObserver.objects.all().first()   
    perfs= OBPerforationModel.objects.filter(obwellid=well.wellid).all()
    return render (request, 'obperforations/obperforation.html', {'perfs': perfs})

def create_obperforation(request):   
    perf = OBPerforationModel()
    selectedwell = SelectedObserver.objects.first()  
    perf.obfgid = selectedwell.fgid
    perf.obwellid = selectedwell.wellid   
    form = OBPerforationForm(request.POST or None, instance=perf)
    if request.method =="POST":  
        form = OBPerforationForm(request.POST, request.FILES, instance=perf)       
        perf.obfgid = selectedwell.fgid
        perf.obfgidwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('obperforations:list_obperforation')
    return render (request, 'obperforations/obperforation_form.html', {'form': form})

def update_obperforation(request, id):
    perf = OBPerforationModel.objects.get(id=id)
    form = OBPerforationForm(request.POST or None, instance=perf)
    if form.is_valid():
        form.save()
        return redirect ('obperforations:list_obperforation')
    return render (request, 'obperforations/obperforation_form.html', {'form': form, 'perf':perf})

def delete_obperforation(request, id):
    perf = OBPerforationModel.objects.get(id=id)    
    if request.method == 'POST' :
        perf.delete()
        return redirect ('obperforations:list_obperforation')
    return render (request, 'obperforations/obperforation_confirm_delete.html', {'perf':perf})





