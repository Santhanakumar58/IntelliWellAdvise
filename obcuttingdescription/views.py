from django.shortcuts import render, redirect
from .models import OBCuttingDescriptionModel
from .forms import OBCuttingDescriptionForm
from selectedObserver.models import SelectedObserver



def list_obcutting(request):     
    well = SelectedObserver.objects.all().first()   
    cuttings= OBCuttingDescriptionModel.objects.filter(obwellid=well.wellid).all()
    return render (request, 'obcuttingdescription/obcuttingdescription.html', {'cuttings': cuttings})

def create_obcutting(request):   
    cutting = OBCuttingDescriptionModel()
    selectedwell = SelectedObserver.objects.first()  
    cutting.fgid = selectedwell.obfgid
    cutting.wellid = selectedwell.obwellid   
    form = OBCuttingDescriptionForm(request.POST or None, instance=cutting)
    if request.method =="POST":  
        form = OBCuttingDescriptionForm(request.POST, request.FILES, instance=cutting)       
        cutting.fgid = selectedwell.obfgid
        cutting.wellid = selectedwell.obwellid  
    if form.is_valid():
        form.save()
        return redirect ('obcuttingdescription:list_cutting')
    return render (request, 'obcuttingdescription/obcuttingdescription_form.html', {'form': form})

def update_obcutting(request, id):
    cutting = OBCuttingDescriptionModel.objects.get(id=id)
    form = OBCuttingDescriptionForm(request.POST or None, instance=cutting)
    if form.is_valid():
        form.save()
        return redirect ('obcuttingdescription:list_cutting')
    return render (request, 'obcuttingdescription/obcuttingdescription_form.html', {'form': form, 'cutting':cutting})

def delete_obcutting(request, id):
    cutting = OBCuttingDescriptionModel.objects.get(id=id)    
    if request.method == 'POST' :
        cutting.delete()
        return redirect ('obcuttingdescription:list_cutting')
    return render (request, 'obcuttingdescription/obcuttingdescription_confirm_delete.html', {'cutting':cutting})


