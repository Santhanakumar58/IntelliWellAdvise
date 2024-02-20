from django.shortcuts import render, redirect
from .models import OilShowModel
from .forms import OilShowForm
from selectedOilProducer.models import SelectedOilProducer



def list_oilshow(request):     
    well = SelectedOilProducer.objects.all().first()   
    shows= OilShowModel.objects.filter(wellid=well.wellid).all()
    return render (request, 'oilshows/oilshow.html', {'shows': shows})

def create_oilshow(request):   
    show = OilShowModel()
    selectedwell = SelectedOilProducer.objects.first()  
    show.fgid = selectedwell.fgid
    show.wellid = selectedwell.wellid   
    form = OilShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = OilShowForm(request.POST, request.FILES, instance=show)       
        show.fgid = selectedwell.fgid
        show.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('oilshows:list_oilshow')
    return render (request, 'oilshows/oilshow_form.html', {'form': form})

def update_oilshow(request, id):
    show = OilShowModel.objects.get(id=id)
    form = OilShowModel(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('oilshows:list_oilshow')
    return render (request, 'oilshows/oilshow_form.html', {'form': form, 'show':show})

def delete_oilshow(request, id):
    show = OilShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('oilshows:list_oilshow')
    return render (request, 'oilshows/oilshow_confirm_delete.html', {'show':show})




