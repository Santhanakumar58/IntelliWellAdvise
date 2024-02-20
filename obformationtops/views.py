from django.shortcuts import render, redirect
from .models import OBFormatioTopsModel
from .forms import OBFormationTopsForm
from selectedObserver.models import SelectedObserver



def list_obformationtops(request):     
    well = SelectedObserver.objects.all().first()   
    formationtops= OBFormatioTopsModel.objects.filter(obwellid=well.wellid).all()
    return render (request, 'obformationtops/obformationtops.html', {'formationtops': formationtops})

def create_obformationtops(request):   
    formationtop = OBFormatioTopsModel()
    selectedwell = SelectedObserver.objects.first()  
    formationtop.fgid = selectedwell.fgid
    formationtop.wellid = selectedwell.wellid   
    form = OBFormationTopsForm(request.POST or None, instance=formationtop)
    if request.method =="POST":  
        form = OBFormationTopsForm(request.POST, request.FILES, instance=formationtop)       
        formationtop.fgid = selectedwell.fgid
        formationtop.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('obformationtops:list_obformationtops')
    return render (request, 'obformationtops/obformationtops_form.html', {'form': form})

def update_obformationtops(request, id):
    formationtop = OBFormatioTopsModel.objects.get(id=id)
    form = OBFormationTopsForm(request.POST or None, instance=formationtop)
    if form.is_valid():
        form.save()
        return redirect ('obformationtops:list_obformationtops')
    return render (request, 'obformationtops/obformationtops_form.html', {'form': form, 'formationtop':formationtop})

def delete_obformationtops(request, id):
    formationtop = OBFormatioTopsModel.objects.get(id=id)    
    if request.method == 'POST' :
        formationtop.delete()
        return redirect ('obformationtops:list_obformationtops')
    return render (request, 'obformationtops/obformationtops_confirm_delete.html', {'formationtop':formationtop})



