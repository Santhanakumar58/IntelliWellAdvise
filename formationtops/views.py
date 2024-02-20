from django.shortcuts import render, redirect
from .models import FormatioTopsModel
from .forms import FormationTopsForm
from selectedOilProducer.models import SelectedOilProducer



def list_formationTops(request):     
    well = SelectedOilProducer.objects.all().first()   
    formationtops= FormatioTopsModel.objects.filter(wellid=well.wellid).all()
    return render (request, 'formationtops/formationtops.html', {'formationtops': formationtops})

def create_formationTops(request):   
    formationtop = FormatioTopsModel()
    selectedwell = SelectedOilProducer.objects.first()  
    formationtop.fgid = selectedwell.fgid
    formationtop.wellid = selectedwell.wellid   
    form = FormationTopsForm(request.POST or None, instance=formationtop)
    if request.method =="POST":  
        form = FormationTopsForm(request.POST, request.FILES, instance=formationtop)       
        formationtop.fgid = selectedwell.fgid
        formationtop.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('formationtops:list_formationTops')
    return render (request, 'formationtops/formationtops_form.html', {'form': form})

def update_formationTops(request, id):
    formationtop = FormatioTopsModel.objects.get(id=id)
    form = FormationTopsForm(request.POST or None, instance=formationtop)
    if form.is_valid():
        form.save()
        return redirect ('formationtops:list_formationTops')
    return render (request, 'formationtops/formationtops_form.html', {'form': form, 'formationtop':formationtop})

def delete_formationTops(request, id):
    formationtop = FormatioTopsModel.objects.get(id=id)    
    if request.method == 'POST' :
        formationtop.delete()
        return redirect ('formationtops:list_formationTops')
    return render (request, 'formationtops/formationtops_confirm_delete.html', {'formationtop':formationtop})


