from django.shortcuts import render, redirect
from .models import PerforationModel
from .forms import PerforationForm
from selectedOilProducer.models import SelectedOilProducer

def list_perforation(request):     
    well = SelectedOilProducer.objects.all().first()   
    perfs= PerforationModel.objects.filter(wellid=well.wellid).all()
    return render (request, 'perforations/perforation.html', {'perfs': perfs})

def create_perforation(request):   
    perf = PerforationModel()
    selectedwell = SelectedOilProducer.objects.first()  
    perf.fgid = selectedwell.fgid
    perf.wellid = selectedwell.wellid   
    form = PerforationForm(request.POST or None, instance=perf)
    if request.method =="POST":  
        form = PerforationForm(request.POST, request.FILES, instance=perf)       
        perf.fgid = selectedwell.fgid
        perf.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('perforations:list_perforation')
    return render (request, 'perforations/perforation_form.html', {'form': form})

def update_perforation(request, id):
    perf = PerforationModel.objects.get(id=id)
    form = PerforationForm(request.POST or None, instance=perf)
    if form.is_valid():
        form.save()
        return redirect ('perforations:list_perforation')
    return render (request, 'perforations/perforation_form.html', {'form': form, 'perf':perf})

def delete_perforation(request, id):
    perf = PerforationModel.objects.get(id=id)    
    if request.method == 'POST' :
        perf.delete()
        return redirect ('perforations:list_perforation')
    return render (request, 'perforations/perforation_confirm_delete.html', {'perf':perf})




