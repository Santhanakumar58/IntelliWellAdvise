from django.shortcuts import render, redirect
from .models import GIGasShowModel
from .forms import GIGasShowForm
from selectedGasInjector.models import SelectedGasInjector



def list_gigasshow(request):     
    well =SelectedGasInjector.objects.all().first()   
    shows= GIGasShowModel.objects.filter(giwellid=well.wellid).all()
    return render (request, 'gigasshows/gigasshow.html', {'shows': shows})

def create_gigasshow(request):   
    show = GIGasShowModel()
    selectedwell = SelectedGasInjector.objects.first()  
    show.fgid = selectedwell.fgid
    show.wellid = selectedwell.wellid   
    form = GIGasShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = GIGasShowForm(request.POST, request.FILES, instance=show)       
        show.fgid = selectedwell.fgid
        show.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gigasshows:list_gigasshow')
    return render (request, 'gigasshows/gigasshow_form.html', {'form': form})

def update_gigasshow(request, id):
    show = GIGasShowModel.objects.get(id=id)
    form = GIGasShowForm(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('gigasshows:list_gigasshow')
    return render (request, 'gigasshows/gigasshow_form.html', {'form': form, 'show':show})

def delete_gigasshow(request, id):
    show = GIGasShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('gigasshows:list_gigasshow')
    return render (request, 'gigasshows/gigasshow_confirm_delete.html', {'show':show})





