from django.shortcuts import render, redirect
from .models import WIFormatioTopsModel
from .forms import WIFormationTopsForm
from selectedWaterInjector.models import SelectedWaterInjector



def list_wiformationtops(request):     
    well = SelectedWaterInjector.objects.all().first()   
    formationtops= WIFormatioTopsModel.objects.filter(wiwellid=well.wellid).all()
    return render (request, 'wiformationtops/wiformationtops.html', {'formationtops': formationtops})

def create_wiformationtops(request):   
    formationtop = WIFormatioTopsModel()
    selectedwell = SelectedWaterInjector.objects.first()  
    formationtop.fgid = selectedwell.fgid
    formationtop.wellid = selectedwell.wellid   
    form = WIFormationTopsForm(request.POST or None, instance=formationtop)
    if request.method =="POST":  
        form = WIFormationTopsForm(request.POST, request.FILES, instance=formationtop)       
        formationtop.fgid = selectedwell.fgid
        formationtop.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('wiformationtops:list_wiformationtops')
    return render (request, 'wiformationtops/wiformationtops_form.html', {'form': form})

def update_wiformationtops(request, id):
    formationtop = WIFormatioTopsModel.objects.get(id=id)
    form = WIFormationTopsForm(request.POST or None, instance=formationtop)
    if form.is_valid():
        form.save()
        return redirect ('wiformationtops:list_wiformationtops')
    return render (request, 'wiformationtops/wiformationtops_form.html', {'form': form, 'formationtop':formationtop})

def delete_wiformationtops(request, id):
    formationtop = WIFormatioTopsModel.objects.get(id=id)    
    if request.method == 'POST' :
        formationtop.delete()
        return redirect ('wiformationtops:list_wiformationtops')
    return render (request, 'wiformationtops/wiformationtops_confirm_delete.html', {'formationtop':formationtop})




