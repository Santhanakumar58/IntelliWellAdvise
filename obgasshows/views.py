from django.shortcuts import render, redirect
from .models import OBGasShowModel
from .forms import OBGasShowForm
from selectedObserver.models import SelectedObserver



def list_obgasshow(request):     
    well = SelectedObserver.objects.all().first()   
    shows= OBGasShowModel.objects.filter(obwellid=well.wellid).all()
    return render (request, 'obgasshows/obgasshow.html', {'shows': shows})

def create_obgasshow(request):   
    show = OBGasShowModel()
    selectedwell = SelectedObserver.objects.first()  
    show.obfgid = selectedwell.fgid
    show.obwellid = selectedwell.wellid   
    form = OBGasShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = OBGasShowForm(request.POST, request.FILES, instance=show)       
        show.obfgid = selectedwell.fgid
        show.obwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('obgasshows:list_obgasshow')
    return render (request, 'obgasshows/obgasshow_form.html', {'form': form})

def update_obgasshow(request, id):
    show = OBGasShowModel.objects.get(id=id)
    form = OBGasShowForm(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('obgasshows:list_obgasshow')
    return render (request, 'obgasshows/obgasshow_form.html', {'form': form, 'show':show})

def delete_obgasshow(request, id):
    show = OBGasShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('obgasshows:list_obgasshow')
    return render (request, 'obgasshows/obgasshow_confirm_delete.html', {'show':show})





