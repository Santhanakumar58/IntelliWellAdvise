from django.shortcuts import render, redirect
from .models import GPCuttingDescriptionModel
from .forms import GPCuttingDescriptionForm
from selectedGasProducer.models import SelectedGasProducer



def list_gpcutting(request):     
    well = SelectedGasProducer.objects.all().first()   
    cuttings= GPCuttingDescriptionModel.objects.filter(gpwellid=well.wellid).all()
    return render (request, 'gpcuttingdescription/gpcuttingdescription.html', {'cuttings': cuttings})

def create_gpcutting(request):   
    cutting = GPCuttingDescriptionModel()
    selectedwell = SelectedGasProducer.objects.first()  
    cutting.fgid = selectedwell.gpfgid
    cutting.wellid = selectedwell.gpwellid   
    form = GPCuttingDescriptionForm(request.POST or None, instance=cutting)
    if request.method =="POST":  
        form = GPCuttingDescriptionForm(request.POST, request.FILES, instance=cutting)       
        cutting.fgid = selectedwell.gpfgid
        cutting.wellid = selectedwell.gpwellid  
    if form.is_valid():
        form.save()
        return redirect ('gpcuttingdescription:list_cutting')
    return render (request, 'gpcuttingdescription/gpcuttingdescription_form.html', {'form': form})

def update_gpcutting(request, id):
    cutting = GPCuttingDescriptionModel.objects.get(id=id)
    form = GPCuttingDescriptionForm(request.POST or None, instance=cutting)
    if form.is_valid():
        form.save()
        return redirect ('gpcuttingdescription:list_cutting')
    return render (request, 'gpcuttingdescription/gpcuttingdescription_form.html', {'form': form, 'cutting':cutting})

def delete_gpcutting(request, id):
    cutting = GPCuttingDescriptionModel.objects.get(id=id)    
    if request.method == 'POST' :
        cutting.delete()
        return redirect ('gpcuttingdescription:list_cutting')
    return render (request, 'gpcuttingdescription/gpcuttingdescription_confirm_delete.html', {'cutting':cutting})

