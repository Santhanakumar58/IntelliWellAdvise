from django.shortcuts import render, redirect
from .models import GICuttingDescriptionModel
from .forms import GICuttingDescriptionForm
from selectedGasInjector.models import SelectedGasInjector



def list_gicutting(request):     
    well = SelectedGasInjector.objects.all().first()   
    cuttings= GICuttingDescriptionModel.objects.filter(giwellid=well.wellid).all()
    return render (request, 'gicuttingdescription/gicuttingdescription.html', {'cuttings': cuttings})

def create_gicutting(request):   
    cutting = GICuttingDescriptionModel()
    selectedwell = SelectedGasInjector.objects.first()  
    cutting.fgid = selectedwell.gifgid
    cutting.wellid = selectedwell.giwellid   
    form = GICuttingDescriptionForm(request.POST or None, instance=cutting)
    if request.method =="POST":  
        form = GICuttingDescriptionForm(request.POST, request.FILES, instance=cutting)       
        cutting.fgid = selectedwell.gifgid
        cutting.wellid = selectedwell.giwellid  
    if form.is_valid():
        form.save()
        return redirect ('gicuttingdescription:list_cutting')
    return render (request, 'gicuttingdescription/gicuttingdescription_form.html', {'form': form})

def update_gicutting(request, id):
    cutting = GICuttingDescriptionModel.objects.get(id=id)
    form = GICuttingDescriptionForm(request.POST or None, instance=cutting)
    if form.is_valid():
        form.save()
        return redirect ('gicuttingdescription:list_cutting')
    return render (request, 'gicuttingdescription/gicuttingdescription_form.html', {'form': form, 'cutting':cutting})

def delete_gicutting(request, id):
    cutting = GICuttingDescriptionModel.objects.get(id=id)    
    if request.method == 'POST' :
        cutting.delete()
        return redirect ('gicuttingdescription:list_cutting')
    return render (request, 'gicuttingdescription/gicuttingdescription_confirm_delete.html', {'cutting':cutting})


