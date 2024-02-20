from token import OP
from django.shortcuts import render
from django.shortcuts import render, redirect
from selectedObserver.models import SelectedObserver
from .models import OBReservoirPressure
from .forms import OBReservoirPressureForm
from .utils import get_plot

def list_obreservoirPressure(request):
    selectedwell = SelectedObserver.objects.first()   
    reservoirpressures = OBReservoirPressure.objects.filter(obwellid =selectedwell.wellid).all()    
    x=[x.survey_Date for x in reservoirpressures]
    y=[y.datum_Pressure for y in reservoirpressures]
    chart = get_plot(x,y)
    return render (request, 'obreservoirpressure/obreservoirPressure.html', {'reservoirpressures': reservoirpressures, 'chart':chart})
    

def create_obreservoirPressure(request): 
   reservoirpressure = OBReservoirPressure()
   selectedwell = SelectedObserver.objects.first()  
   reservoirpressure.obfgid = selectedwell.fgid
   reservoirpressure.obwellid = selectedwell.wellid
   form = OBReservoirPressureForm(request.POST or None, instance=reservoirpressure)
   if request.method =="POST":
        form = OBReservoirPressureForm(request.POST, instance=reservoirpressure)             
        if form.is_valid(): 
            selectedWell = SelectedObserver.objects.first()
            obreservoirpressure = OBReservoirPressure()
            obreservoirpressure.obfgId = selectedWell.fgid
            obreservoirpressure.obwellid = selectedWell.wellid
            obreservoirpressure.obsurvey_Date =request.POST['survey_Date']
            obreservoirpressure.obsurvey_Type = request.POST['survey_Type']
            obreservoirpressure.obgauge_Depth = request.POST['gauge_Depth']
            obreservoirpressure.obgauge_Pressure=request.POST['gauge_Pressure']            
            obreservoirpressure.obdatum_Depth = request.POST['datum_Depth']
            obreservoirpressure.obdatum_Pressure=request.POST['datum_Pressure']
            obreservoirpressure.oblayer_permeability=request.POST['layer_permeability']            
            obreservoirpressure.oblayer_Thickness = request.POST['layer_Thickness']
            obreservoirpressure.oblayer_Skin=request.POST['layer_Skin']
            obreservoirpressure.save()  
            return redirect ('obreservoirpressure:list_obreservoirPressure')          
   return render (request, 'obreservoirpressure/obreservoirPressure_form.html', {'form': form})

def update_obreservoirPressure(request, id):
   obreservoirpressure = OBReservoirPressure.objects.get(id=id)
   print (obreservoirpressure)
   selectedWell = SelectedObserver.objects.first()   
   obreservoirpressure.obfgId = selectedWell.fgid
   obreservoirpressure.obwellid=selectedWell.wellid
   form = OBReservoirPressureForm(request.POST or None, instance=obreservoirpressure)
   if request.method =="POST":
        form = OBReservoirPressureForm(request.POST or None, instance=obreservoirpressure)
        if form.is_valid():    
            form.save()    
            return redirect ('obreservoirpressure:list_obreservoirPressure')
   return render (request, 'obreservoirpressure/obreservoirPressure_form.html', {'form': form})

def delete_obreservoirPressure(request, id):
   
   obreservoirpressure = OBReservoirPressure.objects.get(id=id)   
   if request.method == 'POST' :
       obreservoirpressure.delete()
       return redirect ('obreservoirpressure:list_obreservoirPressure')
   return render (request, 'obreservoirpressure/obreservoirPressure_confirm_delete.html', {'obreservoirpressure':obreservoirpressure})


# Create your views here.


