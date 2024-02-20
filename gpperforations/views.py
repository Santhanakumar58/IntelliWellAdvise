from django.shortcuts import render, redirect
from .models import GPPerforationModel
from .forms import GPPerforationForm
from selectedGasProducer.models import SelectedGasProducer

def list_gpperforation(request):     
    well = SelectedGasProducer.objects.all().first()   
    perfs= GPPerforationModel.objects.filter(gpwellid=well.wellid).all()
    return render (request, 'gpperforations/gpperforation.html', {'perfs': perfs})

def create_gpperforation(request):   
    perf = GPPerforationModel()
    selectedwell = SelectedGasProducer.objects.first()  
    perf.gpfgid = selectedwell.fgid
    perf.gpwellid = selectedwell.wellid   
    form = GPPerforationForm(request.POST or None, instance=perf)
    if request.method =="POST":  
        form = GPPerforationForm(request.POST, request.FILES, instance=perf)       
        perf.gpfgid = selectedwell.fgid
        perf.gpfgidwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gpperforations:list_gpperforation')
    return render (request, 'gpperforations/gpperforation_form.html', {'form': form})

def update_gpperforation(request, id):
    perf = GPPerforationModel.objects.get(id=id)
    form = GPPerforationForm(request.POST or None, instance=perf)
    if form.is_valid():
        form.save()
        return redirect ('gpperforations:list_gpperforation')
    return render (request, 'gpperforations/gpperforation_form.html', {'form': form, 'perf':perf})

def delete_gpperforation(request, id):
    perf = GPPerforationModel.objects.get(id=id)    
    if request.method == 'POST' :
        perf.delete()
        return redirect ('gpperforations:list_gpperforation')
    return render (request, 'gpperforations/gpperforation_confirm_delete.html', {'perf':perf})




