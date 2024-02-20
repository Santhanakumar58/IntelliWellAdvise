from token import OP
from django.shortcuts import render
from django.shortcuts import render, redirect
from selectedGasInjector.models import SelectedGasInjector
from .models import GIReservoirPressure
from .forms import GIReservoirPressureForm
from .utils import get_plot

def list_gireservoirPressure(request):
    selectedwell = SelectedGasInjector.objects.first()   
    reservoirpressures = GIReservoirPressure.objects.filter(giwellid =selectedwell.wellid).all()    
    x=[x.survey_Date for x in reservoirpressures]
    y=[y.datum_Pressure for y in reservoirpressures]
    chart = get_plot(x,y)
    return render (request, 'gireservoirpressure/gireservoirPressure.html', {'reservoirpressures': reservoirpressures, 'chart':chart})
    

def create_gireservoirPressure(request): 
   reservoirpressure = GIReservoirPressure()
   selectedwell = SelectedGasInjector.objects.first()  
   reservoirpressure.fgid = selectedwell.fgid
   reservoirpressure.wellid = selectedwell.wellid
   form = GIReservoirPressureForm(request.POST or None, instance=reservoirpressure)
   if request.method =="POST":
        form = GIReservoirPressureForm(request.POST, instance=reservoirpressure)             
        if form.is_valid(): 
            selectedWell = SelectedGasInjector.objects.first()
            gireservoirpressure = GIReservoirPressure()
            gireservoirpressure.gifgId = selectedWell.fgid
            gireservoirpressure.giwellid = selectedWell.wellid
            gireservoirpressure.gisurvey_Date =request.POST['survey_Date']
            gireservoirpressure.gisurvey_Type = request.POST['survey_Type']
            gireservoirpressure.gigauge_Depth = request.POST['gauge_Depth']
            gireservoirpressure.gigauge_Pressure=request.POST['gauge_Pressure']            
            gireservoirpressure.gidatum_Depth = request.POST['datum_Depth']
            gireservoirpressure.gidatum_Pressure=request.POST['datum_Pressure']
            gireservoirpressure.gilayer_permeability=request.POST['layer_permeability']            
            gireservoirpressure.gilayer_Thickness = request.POST['layer_Thickness']
            gireservoirpressure.gilayer_Skin=request.POST['layer_Skin']
            gireservoirpressure.save()  
            return redirect ('gireservoirpressure:list_gireservoirPressure')          
   return render (request, 'gireservoirpressure/gireservoirPressure_form.html', {'form': form})

def update_gireservoirPressure(request, id):
   gireservoirpressure = GIReservoirPressure.objects.get(id=id)
   print (gireservoirpressure)
   selectedWell = SelectedGasInjector.objects.first()   
   gireservoirpressure.gifgId = selectedWell.fgid
   gireservoirpressure.giwellid=selectedWell.wellid
   form = GIReservoirPressureForm(request.POST or None, instance=gireservoirpressure)
   if request.method =="POST":
        form = GIReservoirPressureForm(request.POST or None, instance=gireservoirpressure)
        if form.is_valid():    
            form.save()    
            return redirect ('gireservoirpressure:list_gireservoirPressure')
   return render (request, 'gireservoirpressure/gireservoirPressure_form.html', {'form': form})

def delete_gireservoirPressure(request, id):
   
   gireservoirpressure = GIReservoirPressure.objects.get(id=id)   
   if request.method == 'POST' :
       gireservoirpressure.delete()
       return redirect ('gireservoirpressure:list_gireservoirPressure')
   return render (request, 'gireservoirpressure/gireservoirPressure_confirm_delete.html', {'gireservoirpressure':gireservoirpressure})


# Create your views here.


