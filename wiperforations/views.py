from django.shortcuts import render, redirect
from .models import WIPerforationModel
from .forms import WIPerforationForm
from selectedWaterInjector.models import SelectedWaterInjector

def list_wiperforation(request):     
    well = SelectedWaterInjector.objects.all().first()   
    perfs= WIPerforationModel.objects.filter(wiwellid=well.wellid).all()
    return render (request, 'wiperforations/wiperforation.html', {'perfs': perfs})

def create_wiperforation(request):   
    perf = WIPerforationModel()
    selectedwell = SelectedWaterInjector.objects.first()  
    perf.wifgid = selectedwell.fgid
    perf.wiwellid = selectedwell.wellid   
    form = WIPerforationForm(request.POST or None, instance=perf)
    if request.method =="POST":  
        form = WIPerforationForm(request.POST, request.FILES, instance=perf)       
        perf.gpfgid = selectedwell.fgid
        perf.gpfgidwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('wiperforations:list_wiperforation')
    return render (request, 'wiperforations/wiperforation_form.html', {'form': form})

def update_wiperforation(request, id):
    perf = WIPerforationModel.objects.get(id=id)
    form = WIPerforationForm(request.POST or None, instance=perf)
    if form.is_valid():
        form.save()
        return redirect ('wiperforations:list_wiperforation')
    return render (request, 'wiperforations/wiperforation_form.html', {'form': form, 'perf':perf})

def delete_wiperforation(request, id):
    perf = WIPerforationModel.objects.get(id=id)    
    if request.method == 'POST' :
        perf.delete()
        return redirect ('wiperforations:list_wiperforation')
    return render (request, 'wiperforations/wiperforation_confirm_delete.html', {'perf':perf})





