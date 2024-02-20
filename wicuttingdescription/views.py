from django.shortcuts import render, redirect
from .models import WICuttingDescriptionModel
from .forms import WICuttingDescriptionForm
from selectedWaterInjector.models import SelectedWaterInjector



def list_wicutting(request):     
    well = SelectedWaterInjector.objects.all().first()   
    cuttings= WICuttingDescriptionModel.objects.filter(wiwellid=well.wellid).all()
    return render (request, 'wicuttingdescription/wicuttingdescription.html', {'cuttings': cuttings})

def create_wicutting(request):   
    cutting = WICuttingDescriptionModel()
    selectedwell = SelectedWaterInjector.objects.first()  
    cutting.fgid = selectedwell.wifgid
    cutting.wellid = selectedwell.wiwellid   
    form = WICuttingDescriptionForm(request.POST or None, instance=cutting)
    if request.method =="POST":  
        form = WICuttingDescriptionForm(request.POST, request.FILES, instance=cutting)       
        cutting.fgid = selectedwell.wifgid
        cutting.wellid = selectedwell.wiwellid  
    if form.is_valid():
        form.save()
        return redirect ('wicuttingdescription:list_cutting')
    return render (request, 'wicuttingdescription/wicuttingdescription_form.html', {'form': form})

def update_wicutting(request, id):
    cutting = WICuttingDescriptionModel.objects.get(id=id)
    form = WICuttingDescriptionForm(request.POST or None, instance=cutting)
    if form.is_valid():
        form.save()
        return redirect ('wicuttingdescription:list_cutting')
    return render (request, 'wicuttingdescription/wicuttingdescription_form.html', {'form': form, 'cutting':cutting})

def delete_wicutting(request, id):
    cutting = WICuttingDescriptionModel.objects.get(id=id)    
    if request.method == 'POST' :
        cutting.delete()
        return redirect ('wicuttingdescription:list_cutting')
    return render (request, 'wicuttingdescription/wicuttingdescription_confirm_delete.html', {'cutting':cutting})


