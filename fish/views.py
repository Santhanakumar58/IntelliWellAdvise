from django.shortcuts import render, redirect
from .models import FishModel
from .forms import FishForm
from selectedOilProducer.models import SelectedOilProducer

 


# Create your views here.
def list_fish(request):     
    well = SelectedOilProducer.objects.all().first()   
    fishes = FishModel.objects.filter(wellid=well.wellid).all()
    return render (request, 'fish/fish.html', {'fishes': fishes})

def create_fish(request):
    fish = FishModel()
    selectedwell = SelectedOilProducer.objects.first()  
    fish.fgid = selectedwell.fgid
    fish.wellid = selectedwell.wellid   
    form = FishForm(request.POST or None, instance=fish)
    if request.method =="POST":  
        form = FishForm(request.POST, request.FILES, instance=fish)       
        fish.fgid = selectedwell.fgid
        fish.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('fish:list_fish')
    return render (request, 'fish/fish_form.html', {'form': form})

def update_fish(request, id):
   fish = FishModel.objects.get(id=id)
   form = FishForm(request.POST or None, instance=fish)
   if form.is_valid():
       form.save()
       return redirect ('fish:list_fish')
   return render (request, 'fish/fish_form.html', {'form': form, 'fish':fish})

def delete_fish(request, id):
   fish = FishModel.objects.get(id=id)
   
   if request.method == 'POST' :
       fish.delete()
       return redirect ('fish:list_fish')
   return render (request, 'fish/fish_confirm_delete.html', {'fish':fish})

