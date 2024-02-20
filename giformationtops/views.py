from django.shortcuts import render, redirect
from .models import GIFormatioTopsModel
from .forms import GIFormationTopsForm
from selectedGasInjector.models import SelectedGasInjector



def list_giformationtops(request):     
    well = SelectedGasInjector.objects.all().first()   
    giformationtops= GIFormatioTopsModel.objects.filter(giwellid=well.wellid).all()
    return render (request, 'giformationtops/giformationtops.html', {'giformationtops': giformationtops})

def create_giformationtops(request):   
    formationtop = GIFormatioTopsModel()
    selectedwell = SelectedGasInjector.objects.first()  
    formationtop.fgid = selectedwell.fgid
    formationtop.wellid = selectedwell.wellid   
    form = GIFormationTopsForm(request.POST or None, instance=formationtop)
    if request.method =="POST":  
        form = GIFormationTopsForm(request.POST, request.FILES, instance=formationtop)       
        formationtop.fgid = selectedwell.fgid
        formationtop.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('giformationtops:list_gigiformationtops')
    return render (request, 'giformationtops/giformationtops_form.html', {'form': form})

def update_giformationtops(request, id):
    formationtop = GIFormatioTopsModel.objects.get(id=id)
    form = GIFormationTopsForm(request.POST or None, instance=formationtop)
    if form.is_valid():
        form.save()
        return redirect ('giformationtops:list_gigiformationtops')
    return render (request, 'giformationtops/giformationtops_form.html', {'form': form, 'formationtop':formationtop})

def delete_giformationtops(request, id):
    formationtop = GIFormatioTopsModel.objects.get(id=id)    
    if request.method == 'POST' :
        formationtop.delete()
        return redirect ('giformationtops:list_gigiformationtops')
    return render (request, 'giformationtops/giformationtops_confirm_delete.html', {'formationtop':formationtop})




