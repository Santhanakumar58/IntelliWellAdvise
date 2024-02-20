from django.shortcuts import render, redirect
from .models import CuttingDescriptionModel
from .forms import CuttingDescriptionForm
from selectedOilProducer.models import SelectedOilProducer



def list_cutting(request):     
    well = SelectedOilProducer.objects.all().first()   
    cuttings= CuttingDescriptionModel.objects.filter(wellid=well.wellid).all()
    return render (request, 'cuttingdescription/cuttingdescription.html', {'cuttings': cuttings})

def create_cutting(request):   
    cutting = CuttingDescriptionModel()
    selectedwell = SelectedOilProducer.objects.first()  
    cutting.fgid = selectedwell.fgid
    cutting.wellid = selectedwell.wellid   
    form = CuttingDescriptionForm(request.POST or None, instance=cutting)
    if request.method =="POST":  
        form = CuttingDescriptionForm(request.POST, request.FILES, instance=cutting)       
        cutting.fgid = selectedwell.fgid
        cutting.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('cuttingdescription:list_cutting')
    return render (request, 'cuttingdescription/cuttingdescription_form.html', {'form': form})

def update_cutting(request, id):
    cutting = CuttingDescriptionModel.objects.get(id=id)
    form = CuttingDescriptionForm(request.POST or None, instance=cutting)
    if form.is_valid():
        form.save()
        return redirect ('cuttingdescription:list_cutting')
    return render (request, 'cuttingdescription/cuttingdescription_form.html', {'form': form, 'cutting':cutting})

def delete_cutting(request, id):
    cutting = CuttingDescriptionModel.objects.get(id=id)    
    if request.method == 'POST' :
        cutting.delete()
        return redirect ('cuttingdescription:list_cutting')
    return render (request, 'cuttingdescription/cuttingdescription_confirm_delete.html', {'cutting':cutting})

