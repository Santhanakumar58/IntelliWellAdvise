from django.shortcuts import render, redirect
from .models import WIOilShowModel
from .forms import WIOilShowForm
from selectedOilProducer.models import SelectedOilProducer



def list_wioilshow(request):     
    well = SelectedOilProducer.objects.all().first()   
    shows= WIOilShowModel.objects.filter(wiwellid=well.wellid).all()
    return render (request, 'wioilshows/wioilshow.html', {'shows': shows})

def create_wioilshow(request):   
    show = WIOilShowModel()
    selectedwell = SelectedOilProducer.objects.first()  
    show.wifgid = selectedwell.fgid
    show.wiwellid = selectedwell.wellid   
    form = WIOilShowForm(request.POST or None, instance=show)
    if request.method =="POST":  
        form = WIOilShowForm(request.POST, request.FILES, instance=show)       
        show.wiformationfgid = selectedwell.fgid
        show.wiformationwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('wioilshows:list_wioilshow')
    return render (request, 'wioilshows/wioilshow_form.html', {'form': form})

def update_wioilshow(request, id):
    show = WIOilShowModel.objects.get(id=id)
    form = WIOilShowForm(request.POST or None, instance=show)
    if form.is_valid():
        form.save()
        return redirect ('wioilshows:list_wioilshow')
    return render (request, 'wioilshows/wioilshow_form.html', {'form': form, 'show':show})

def delete_wioilshow(request, id):
    show = WIOilShowModel.objects.get(id=id)    
    if request.method == 'POST' :
        show.delete()
        return redirect ('wioilshows:list_wioilshow')
    return render (request, 'wioilshows/wioilshow_confirm_delete.html', {'show':show})





