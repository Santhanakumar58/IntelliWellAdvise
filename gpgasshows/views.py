from django.shortcuts import render, redirect
from .models import GPGasShowModel
from .forms import GPGasShowForm
from selectedGasProducer.models import SelectedGasProducer



def list_gpgasshow(request):     
    well = SelectedGasProducer.objects.all().first()   
    shows= GPGasShowModel.objects.filter(gpwellid=well.wellid).all()
    return render (request, 'gpgasshows/gpgasshow.html', {'shows': shows})

def create_gpgasshow(request):   
    show = GPGasShowModel()
    selectedwell = SelectedGasProducer.objects.first()  
    show.fgid = selectedwell.fgid
    show.wellid = selectedwell.wellid   
    form = GPGasShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = GPGasShowForm(request.POST, request.FILES, instance=show)       
        show.fgid = selectedwell.fgid
        show.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gpgasshows:list_gpgasshow')
    return render (request, 'gpgasshows/gpgasshow_form.html', {'form': form})

def update_gpgasshow(request, id):
    show = GPGasShowModel.objects.get(id=id)
    form = GPGasShowForm(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('gpgasshows:list_gpgasshow')
    return render (request, 'gpgasshows/gpgasshow_form.html', {'form': form, 'show':show})

def delete_gpgasshow(request, id):
    show = GPGasShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('gpgasshows:list_gpgasshow')
    return render (request, 'gpgasshows/gpgasshow_confirm_delete.html', {'show':show})




