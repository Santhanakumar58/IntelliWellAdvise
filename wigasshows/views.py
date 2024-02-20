from django.shortcuts import render, redirect
from .models import WIGasShowModel
from .forms import WIGasShowForm
from selectedWaterInjector.models import SelectedWaterInjector



def list_wigasshow(request):     
    well = SelectedWaterInjector.objects.all().first()   
    shows= WIGasShowModel.objects.filter(wiwellid=well.wellid).all()
    return render (request, 'wigasshows/wigasshow.html', {'shows': shows})

def create_wigasshow(request):   
    show = WIGasShowModel()
    selectedwell = SelectedWaterInjector.objects.first()  
    show.fgid = selectedwell.fgid
    show.wellid = selectedwell.wellid   
    form = WIGasShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = WIGasShowForm(request.POST, request.FILES, instance=show)       
        show.fgid = selectedwell.fgid
        show.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('wigasshows:list_wigasshow')
    return render (request, 'wigasshows/wigasshow_form.html', {'form': form})

def update_wigasshow(request, id):
    show = WIGasShowModel.objects.get(id=id)
    form = WIGasShowForm(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('wigasshows:list_wigasshow')
    return render (request, 'wigasshows/wigasshow_form.html', {'form': form, 'show':show})

def delete_wigasshow(request, id):
    show = WIGasShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('wigasshows:list_wigasshow')
    return render (request, 'wigasshows/wigasshow_confirm_delete.html', {'show':show})





