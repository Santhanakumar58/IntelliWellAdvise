from token import OP
from django.shortcuts import render
from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from .models import OPReservoirPressure
from .forms import ReservoirPressureForm
from .utility import get_plot

def list_reservoirPressure(request):
    selectedwell = SelectedOilProducer.objects.first()   
    reservoirpressures = OPReservoirPressure.objects.filter(wellid =selectedwell.wellid).all()    
    x=[x.survey_Date for x in reservoirpressures]
    y=[y.datum_Pressure for y in reservoirpressures]
    chart = get_plot(x,y)
    return render (request, 'opreservoirpressure/opreservoirPressure.html', {'reservoirpressures': reservoirpressures, 'chart':chart})
    

def create_reservoirPressure(request): 
   reservoirpressure = OPReservoirPressure()
   selectedwell = SelectedOilProducer.objects.first()  
   reservoirpressure.fgid = selectedwell.fgid
   reservoirpressure.wellid = selectedwell.wellid
   form = ReservoirPressureForm(request.POST or None, instance=reservoirpressure)
   if request.method =="POST":
        form = ReservoirPressureForm(request.POST, instance=reservoirpressure)             
        if form.is_valid(): 
            selectedWell = SelectedOilProducer.objects.first()
            opreservoirpressure = OPReservoirPressure()
            opreservoirpressure.fgId = selectedWell.fgid
            opreservoirpressure.wellid = selectedWell.wellid
            opreservoirpressure.survey_Date =request.POST['survey_Date']
            opreservoirpressure.survey_Type = request.POST['survey_Type']
            opreservoirpressure.gauge_Depth = request.POST['gauge_Depth']
            opreservoirpressure.gauge_Pressure=request.POST['gauge_Pressure']            
            opreservoirpressure.datum_Depth = request.POST['datum_Depth']
            opreservoirpressure.datum_Pressure=request.POST['datum_Pressure']
            opreservoirpressure.layer_permeability=request.POST['layer_permeability']            
            opreservoirpressure.layer_Thickness = request.POST['layer_Thickness']
            opreservoirpressure.layer_Skin=request.POST['layer_Skin']
            opreservoirpressure.save()  
            return redirect ('opreservoirpressure:list_reservoirPressure')          
   return render (request, 'opreservoirpressure/opreservoirPressure_form.html', {'form': form})

def update_reservoirPressure(request, id):
   opreservoirpressure = OPReservoirPressure.objects.get(id=id)
   print (opreservoirpressure)
   selectedWell = SelectedOilProducer.objects.first()   
   opreservoirpressure.fgId = selectedWell.fgid
   opreservoirpressure.wellid=selectedWell.wellid
   form = ReservoirPressureForm(request.POST or None, instance=opreservoirpressure)
   if request.method =="POST":
        form = ReservoirPressureForm(request.POST or None, instance=opreservoirpressure)
        if form.is_valid():    
            form.save()    
            return redirect ('opreservoirpressure:list_reservoirPressure')
   return render (request, 'opreservoirpressure/opreservoirPressure_form.html', {'form': form, 'opreservoirpressure': opreservoirpressure})

def delete_reservoirPressure(request, id):
   
   opreservoirpressure = OPReservoirPressure.objects.get(id=id)   
   if request.method == 'POST' :
       opreservoirpressure.delete()
       return redirect ('opreservoirpressure:list_reservoirPressure')
   return render (request, 'opreservoirpressure/opreservoirPressure_confirm_delete.html', {'opreservoirpressure':opreservoirpressure})


# Create your views here.
