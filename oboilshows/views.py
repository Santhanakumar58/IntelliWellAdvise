from django.shortcuts import render, redirect
from .models import OBOilShowModel
from .forms import OBOilShowForm
from selectedObserver.models import SelectedObserver



def list_oboilshow(request):     
    well = SelectedObserver.objects.all().first()   
    shows= OBOilShowModel.objects.filter(obwellid=well.wellid).all()
    return render (request, 'oboilshows/oboilshow.html', {'shows': shows})

def create_oboilshow(request):   
    show = OBOilShowModel()
    selectedwell = SelectedObserver.objects.first()  
    show.fgid = selectedwell.fgid
    show.wellid = selectedwell.wellid   
    form = OBOilShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = OBOilShowForm(request.POST, request.FILES, instance=show)       
        show.fgid = selectedwell.fgid
        show.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('oboilshows:list_oboilshow')
    return render (request, 'oboilshows/oboilshow_form.html', {'form': form})

def update_oboilshow(request, id):
    show = OBOilShowModel.objects.get(id=id)
    form = OBOilShowModel(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('oboilshows:list_oboilshow')
    return render (request, 'oboilshows/oboilshow_form.html', {'form': form, 'show':show})

def delete_oboilshow(request, id):
    show = OBOilShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('oboilshows:list_oboilshow')
    return render (request, 'oboilshows/oboilshow_confirm_delete.html', {'show':show})





