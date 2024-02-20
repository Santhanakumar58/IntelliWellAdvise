from django.shortcuts import render, redirect
from .models import GasShowModel
from .forms import GasShowForm
from selectedOilProducer.models import SelectedOilProducer



def list_gasshow(request):     
    well = SelectedOilProducer.objects.all().first()   
    shows= GasShowModel.objects.filter(wellid=well.wellid).all()
    return render (request, 'gasshows/gasshow.html', {'shows': shows})

def create_gasshow(request):   
    show = GasShowModel()
    selectedwell = SelectedOilProducer.objects.first()  
    show.fgid = selectedwell.fgid
    show.wellid = selectedwell.wellid   
    form = GasShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = GasShowForm(request.POST, request.FILES, instance=show)       
        show.fgid = selectedwell.fgid
        show.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gasshows:list_gasshow')
    return render (request, 'gasshows/gasshow_form.html', {'form': form})

def update_gasshow(request, id):
    show = GasShowModel.objects.get(id=id)
    form = GasShowForm(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('gasshows:list_gasshow')
    return render (request, 'gasshows/gasshow_form.html', {'form': form, 'show':show})

def delete_gasshow(request, id):
    show = GasShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('gasshows:list_gasshow')
    return render (request, 'gasshows/gasshow_confirm_delete.html', {'show':show})



