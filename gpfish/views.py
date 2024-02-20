from django.shortcuts import render, redirect
from .models import GPFishModel
from .forms import GPFishForm
from selectedGasProducer.models import SelectedGasProducer

 


# Create your views here.
def list_gpfish(request):     
    well = SelectedGasProducer.objects.all().first()   
    gpfishes = GPFishModel.objects.filter(gpwellid=well.wellid).all()
    return render (request, 'gpfish/gpfish.html', {'gpfishes': gpfishes})

def create_gpfish(request):
    gpfish = GPFishModel()
    selectedwell = SelectedGasProducer.objects.first()  
    gpfish.gpfgid = selectedwell.fgid
    gpfish.gpwellid = selectedwell.wellid   
    form = GPFishForm(request.POST or None, instance=gpfish)
    if request.method =="POST":  
        form = GPFishForm(request.POST, request.FILES, instance=gpfish)       
        gpfish.gpfgid = selectedwell.fgid
        gpfish.gpwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gpfish:list_gpfish')
    return render (request, 'gpfish/gpfish_form.html', {'form': form})

def update_gpfish(request, id):
   gpfish = GPFishModel.objects.get(id=id)
   form = GPFishForm(request.POST or None, instance=gpfish)
   if form.is_valid():
       form.save()
       return redirect ('gpfish:list_gpfish')
   return render (request, 'gpfish/gpfish_form.html', {'form': form, 'gpfish':gpfish})

def delete_gpfish(request, id):
   gpfish = GPFishModel.objects.get(id=id)
   
   if request.method == 'POST' :
       gpfish.delete()
       return redirect ('gpfish:list_gpfish')
   return render (request, 'gpfish/gpfish_confirm_delete.html', {'gpfish':gpfish})

