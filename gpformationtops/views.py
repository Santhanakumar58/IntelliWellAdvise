from django.shortcuts import render, redirect
from .models import GPFormatioTopsModel
from .forms import GPFormationTopsForm
from selectedGasProducer.models import SelectedGasProducer



def list_gpformationtops(request):     
    well = SelectedGasProducer.objects.all().first()   
    formationtops= GPFormatioTopsModel.objects.filter(gpwellid=well.wellid).all()
    return render (request, 'gpformationtops/gpformationtops.html', {'formationtops': formationtops})

def create_gpformationtops(request):   
    formationtop = GPFormatioTopsModel()
    selectedwell = SelectedGasProducer.objects.first()  
    formationtop.fgid = selectedwell.fgid
    formationtop.wellid = selectedwell.wellid   
    form = GPFormationTopsForm(request.POST or None, instance=formationtop)
    if request.method =="POST":  
        form = GPFormationTopsForm(request.POST, request.FILES, instance=formationtop)       
        formationtop.fgid = selectedwell.fgid
        formationtop.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gpformationtops:list_gpformationtops')
    return render (request, 'gpformationtops/gpformationtops_form.html', {'form': form})

def update_gpformationtops(request, id):
    formationtop = GPFormatioTopsModel.objects.get(id=id)
    form = GPFormationTopsForm(request.POST or None, instance=formationtop)
    if form.is_valid():
        form.save()
        return redirect ('gpformationtops:list_gpformationtops')
    return render (request, 'gpformationtops/gpformationtops_form.html', {'form': form, 'formationtop':formationtop})

def delete_gpformationtops(request, id):
    formationtop = GPFormatioTopsModel.objects.get(id=id)    
    if request.method == 'POST' :
        formationtop.delete()
        return redirect ('gpformationtops:list_gpformationtops')
    return render (request, 'gpformationtops/gpformationtops_confirm_delete.html', {'formationtop':formationtop})



