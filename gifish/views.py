from django.shortcuts import render, redirect
from .models import GIFishModel
from .forms import GIFishForm
from selectedGasInjector.models import SelectedGasInjector

 


# Create your views here.
def list_gifish(request):     
    well = SelectedGasInjector.objects.all().first()   
    gifishes = GIFishModel.objects.filter(giwellid=well.wellid).all()
    return render (request, 'gifish/gifish.html', {'gifishes': gifishes})

def create_gifish(request):
    gifish = GIFishModel()
    selectedwell = SelectedGasInjector.objects.first()  
    gifish.gpfgid = selectedwell.fgid
    gifish.gpwellid = selectedwell.wellid   
    form = GIFishForm(request.POST or None, instance=gifish)
    if request.method =="POST":  
        form = GIFishForm(request.POST, request.FILES, instance=gifish)       
        gifish.gpfgid = selectedwell.fgid
        gifish.gpwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gifish:list_gifish')
    return render (request, 'gifish/gifish_form.html', {'form': form})

def update_gifish(request, id):
   gifish = GIFishModel.objects.get(id=id)
   form = GIFishForm(request.POST or None, instance=gifish)
   if form.is_valid():
       form.save()
       return redirect ('gifish:list_gifish')
   return render (request, 'gifish/gifish_form.html', {'form': form, 'gifish':gifish})

def delete_gifish(request, id):
   gifish = GIFishModel.objects.get(id=id)
   
   if request.method == 'POST' :
       gifish.delete()
       return redirect ('gifish:list_gifish')
   return render (request, 'gifish/gifish_confirm_delete.html', {'gifish':gifish})

