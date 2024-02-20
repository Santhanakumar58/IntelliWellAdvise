from token import OP
from django.shortcuts import render
from django.shortcuts import render, redirect
from selectedWaterInjector.models import SelectedWaterInjector
from .models import WIReservoirPressure
from .forms import WIReservoirPressureForm
from .utils import get_plot

def list_wireservoirPressure(request):
    selectedwell = SelectedWaterInjector.objects.first()   
    reservoirpressures = WIReservoirPressure.objects.filter(wiwellid =selectedwell.wellid).all()    
    x=[x.survey_Date for x in reservoirpressures]
    y=[y.datum_Pressure for y in reservoirpressures]
    chart = get_plot(x,y)
    return render (request, 'wireservoirpressure/wireservoirPressure.html', {'reservoirpressures': reservoirpressures, 'chart':chart})
    

def create_wireservoirPressure(request): 
   reservoirpressure = WIReservoirPressure()
   selectedwell = SelectedWaterInjector.objects.first()  
   reservoirpressure.wifgid = selectedwell.fgid
   reservoirpressure.wiwellid = selectedwell.wellid
   form = WIReservoirPressureForm(request.POST or None, instance=reservoirpressure)
   if request.method =="POST":
        form = WIReservoirPressureForm(request.POST, instance=reservoirpressure)             
        if form.is_valid(): 
            selectedWell = SelectedWaterInjector.objects.first()
            wireservoirpressure = WIReservoirPressure()
            wireservoirpressure.wifgId = selectedWell.fgid
            wireservoirpressure.wiwellid = selectedWell.wellid
            wireservoirpressure.wisurvey_Date =request.POST['survey_Date']
            wireservoirpressure.wisurvey_Type = request.POST['survey_Type']
            wireservoirpressure.wigauge_Depth = request.POST['gauge_Depth']
            wireservoirpressure.wigauge_Pressure=request.POST['gauge_Pressure']            
            wireservoirpressure.widatum_Depth = request.POST['datum_Depth']
            wireservoirpressure.widatum_Pressure=request.POST['datum_Pressure']
            wireservoirpressure.wilayer_permeability=request.POST['layer_permeability']            
            wireservoirpressure.wilayer_Thickness = request.POST['layer_Thickness']
            wireservoirpressure.wilayer_Skin=request.POST['layer_Skin']
            wireservoirpressure.save()  
            return redirect ('wireservoirpressure:list_wireservoirPressure')          
   return render (request, 'wireservoirpressure/wireservoirPressure_form.html', {'form': form})

def update_wireservoirPressure(request, id):
   wireservoirpressure = WIReservoirPressure.objects.get(id=id)
   print (wireservoirpressure)
   selectedWell = SelectedWaterInjector.objects.first()   
   wireservoirpressure.wifgId = selectedWell.fgid
   wireservoirpressure.wiwellid=selectedWell.wellid
   form = WIReservoirPressureForm(request.POST or None, instance=wireservoirpressure)
   if request.method =="POST":
        form = WIReservoirPressureForm(request.POST or None, instance=wireservoirpressure)
        if form.is_valid():    
            form.save()    
            return redirect ('wireservoirpressure:list_wireservoirPressure')
   return render (request, 'wireservoirpressure/wireservoirPressure_form.html', {'form': form})

def delete_wireservoirPressure(request, id):
   
   wireservoirpressure = WIReservoirPressure.objects.get(id=id)   
   if request.method == 'POST' :
       wireservoirpressure.delete()
       return redirect ('wireservoirpressure:list_wireservoirPressure')
   return render (request, 'wireservoirpressure/wireservoirPressure_confirm_delete.html', {'wireservoirpressure':wireservoirpressure})


# Create your views here.



