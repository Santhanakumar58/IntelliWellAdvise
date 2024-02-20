from django.shortcuts import render, redirect
from .models import OBFishModel
from .forms import OBFishForm
from selectedObserver.models import SelectedObserver


# Create your views here.
def list_obfish(request):     
    well = SelectedObserver.objects.all().first()   
    obfishes = OBFishModel.objects.filter(obwellid=well.wellid).all()
    return render (request, 'obfish/obfish.html', {'obfishes': obfishes})

def create_obfish(request):
    obfish = OBFishModel()
    selectedwell = SelectedObserver.objects.first()  
    obfish.obfgid = selectedwell.fgid
    obfish.obwellid = selectedwell.wellid   
    form = OBFishForm(request.POST or None, instance=obfish)
    if request.method =="POST":  
        form = OBFishForm(request.POST, request.FILES, instance=obfish)       
        obfish.obfgid = selectedwell.fgid
        obfish.obwellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('obfish:list_obfish')
    return render (request, 'obfish/obfish_form.html', {'form': form})

def update_obfish(request, id):
   obfish = OBFishModel.objects.get(id=id)
   form = OBFishForm(request.POST or None, instance=obfish)
   if form.is_valid():
       form.save()
       return redirect ('obfish:list_obfish')
   return render (request, 'obfish/obfish_form.html', {'form': form, 'obfish':obfish})

def delete_obfish(request, id):
   obfish = OBFishModel.objects.get(id=id)
   
   if request.method == 'POST' :
       obfish.delete()
       return redirect ('obfish:list_obfish')
   return render (request, 'obfish/obfish_confirm_delete.html', {'obfish':obfish})


