from django.shortcuts import render, redirect
from .models import GIOilShowModel
from .forms import GIOilShowForm
from selectedGasInjector.models import SelectedGasInjector



def list_gioilshow(request):     
    well = SelectedGasInjector.objects.all().first()   
    shows= GIOilShowModel.objects.filter(giwellid=well.wellid).all()
    return render (request, 'gioilshows/gioilshow.html', {'shows': shows})

def create_gioilshow(request):   
    show = GIOilShowModel()
    selectedwell = SelectedGasInjector.objects.first()  
    show.fgid = selectedwell.fgid
    show.wellid = selectedwell.wellid   
    form = GIOilShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = GIOilShowForm(request.POST, request.FILES, instance=show)       
        show.fgid = selectedwell.fgid
        show.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gioilshows:list_gioilshow')
    return render (request, 'gioilshows/gioilshow_form.html', {'form': form})

def update_gioilshow(request, id):
    show = GIOilShowModel.objects.get(id=id)
    form = GIOilShowModel(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('gioilshows:list_gioilshow')
    return render (request, 'gioilshows/gioilshow_form.html', {'form': form, 'show':show})

def delete_gioilshow(request, id):
    show = GIOilShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('gioilshows:list_gioilshow')
    return render (request, 'gioilshows/gioilshow_confirm_delete.html', {'show':show})






