from django.shortcuts import render, redirect
from .models import GPOilShowModel
from .forms import GPOilShowForm
from selectedGasProducer.models import SelectedGasProducer



def list_gpoilshow(request):     
    well = SelectedGasProducer.objects.all().first()   
    shows= GPOilShowModel.objects.filter(gpwellid=well.wellid).all()
    return render (request, 'gpoilshows/gpoilshow.html', {'shows': shows})

def create_gpoilshow(request):   
    show = GPOilShowModel()
    selectedwell = SelectedGasProducer.objects.first()  
    show.fgid = selectedwell.fgid
    show.wellid = selectedwell.wellid   
    form = GPOilShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = GPOilShowForm(request.POST, request.FILES, instance=show)       
        show.fgid = selectedwell.fgid
        show.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gpoilshows:list_gpoilshow')
    return render (request, 'gpoilshows/gpoilshow_form.html', {'form': form})

def update_gpoilshow(request, id):
    show = GPOilShowModel.objects.get(id=id)
    form = GPOilShowModel(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('gpoilshows:list_gpoilshow')
    return render (request, 'gpoilshows/gpoilshow_form.html', {'form': form, 'show':show})

def delete_gpoilshow(request, id):
    show = GPOilShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('gpoilshows:list_gpoilshow')
    return render (request, 'gpoilshows/gpoilshow_confirm_delete.html', {'show':show})





