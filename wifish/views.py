from django.shortcuts import render, redirect
from .models import WIFishModel
from .forms import WIFishForm
from selectedWaterInjector.models import SelectedWaterInjector

 


# Create your views here.
def list_wifish(request):     
    well = SelectedWaterInjector.objects.all().first()   
    wifishes = WIFishModel.objects.filter(wiwellid=well.wellid).all()
    return render (request, 'wifish/wifish.html', {'wifishes': wifishes})

def create_wifish(request):
    wifish = WIFishModel()
    selectedwell = SelectedWaterInjector.objects.first()  
    wifish.gpfgid = selectedwell.fgid
    wifish.gpwellid = selectedwell.wellid   
    form = WIFishForm(request.POST or None, instance=wifish)
    if request.method =="POST":  
        form = WIFishForm(request.POST, request.FILES, instance=wifish)       
        wifish.gpfgid = selectedwell.fgid
        wifish.gpwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('wifish:list_wifish')
    return render (request, 'wifish/wifish_form.html', {'form': form})

def update_wifish(request, id):
   wifish = WIFishModel.objects.get(id=id)
   form = WIFishForm(request.POST or None, instance=wifish)
   if form.is_valid():
       form.save()
       return redirect ('wifish:list_wifish')
   return render (request, 'wifish/wifish_form.html', {'form': form, 'wifish':wifish})

def delete_wifish(request, id):
   wifish = WIFishModel.objects.get(id=id)
   
   if request.method == 'POST' :
       wifish.delete()
       return redirect ('wifish:list_wifish')
   return render (request, 'wifish/wifish_confirm_delete.html', {'wifish':wifish})


