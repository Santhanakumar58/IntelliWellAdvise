from token import OP
from django.shortcuts import render
from django.shortcuts import render, redirect
from selectedGasProducer.models import SelectedGasProducer
from .models import GPReservoirPressure
from .forms import GPReservoirPressureForm
from .utils import get_plot

def list_gpreservoirPressure(request):
    selectedwell = SelectedGasProducer.objects.first()   
    reservoirpressures = GPReservoirPressure.objects.filter(gpwellid =selectedwell.wellid).all()    
    x=[x.survey_Date for x in reservoirpressures]
    y=[y.datum_Pressure for y in reservoirpressures]
    chart = get_plot(x,y)
    return render (request, 'gpreservoirpressure/gpreservoirPressure.html', {'reservoirpressures': reservoirpressures, 'chart':chart})
    

def create_gpreservoirPressure(request): 
   reservoirpressure = GPReservoirPressure()
   selectedwell = SelectedGasProducer.objects.first()  
   reservoirpressure.fgid = selectedwell.fgid
   reservoirpressure.wellid = selectedwell.wellid
   form = GPReservoirPressureForm(request.POST or None, instance=reservoirpressure)
   if request.method =="POST":
        form = GPReservoirPressureForm(request.POST, instance=reservoirpressure)             
        if form.is_valid(): 
            selectedWell = SelectedGasProducer.objects.first()
            gpreservoirpressure = GPReservoirPressure()
            gpreservoirpressure.gpfgId = selectedWell.fgid
            gpreservoirpressure.gpwellid = selectedWell.wellid
            gpreservoirpressure.gpsurvey_Date =request.POST['survey_Date']
            gpreservoirpressure.gpsurvey_Type = request.POST['survey_Type']
            gpreservoirpressure.gpgauge_Depth = request.POST['gauge_Depth']
            gpreservoirpressure.gpgauge_Pressure=request.POST['gauge_Pressure']            
            gpreservoirpressure.gpdatum_Depth = request.POST['datum_Depth']
            gpreservoirpressure.gpdatum_Pressure=request.POST['datum_Pressure']
            gpreservoirpressure.gplayer_permeability=request.POST['layer_permeability']            
            gpreservoirpressure.gplayer_Thickness = request.POST['layer_Thickness']
            gpreservoirpressure.gplayer_Skin=request.POST['layer_Skin']
            gpreservoirpressure.save()  
            return redirect ('gpreservoirpressure:list_gpreservoirPressure')          
   return render (request, 'gpreservoirpressure/gpreservoirPressure_form.html', {'form': form})

def update_gpreservoirPressure(request, id):
   gpreservoirpressure = GPReservoirPressure.objects.get(id=id)
   print (gpreservoirpressure)
   selectedWell = SelectedGasProducer.objects.first()   
   gpreservoirpressure.gpfgId = selectedWell.fgid
   gpreservoirpressure.gpwellid=selectedWell.wellid
   form = GPReservoirPressureForm(request.POST or None, instance=gpreservoirpressure)
   if request.method =="POST":
        form = GPReservoirPressureForm(request.POST or None, instance=gpreservoirpressure)
        if form.is_valid():    
            form.save()    
            return redirect ('gpreservoirpressure:list_gpreservoirPressure')
   return render (request, 'gpreservoirpressure/gpreservoirPressure_form.html', {'form': form})

def delete_gpreservoirPressure(request, id):
   
   gpreservoirpressure = GPReservoirPressure.objects.get(id=id)   
   if request.method == 'POST' :
       gpreservoirpressure.delete()
       return redirect ('gpreservoirpressure:list_gpreservoirPressure')
   return render (request, 'gpreservoirpressure/gpreservoirPressure_confirm_delete.html', {'gpreservoirpressure':gpreservoirpressure})


# Create your views here.

