from django.shortcuts import render, redirect
from .models import FormatioPressureModel
from .forms import FormationPressureForm
from selectedOilProducer.models import SelectedOilProducer



def list_formation_Pressure(request):     
    well = SelectedOilProducer.objects.all().first()   
    pressures= FormatioPressureModel.objects.filter(wellid=well.wellid).all()
    return render (request, 'formationpressure/formationpressure.html', {'pressures': pressures})

def create_formation_Pressure(request):   
    pressure = FormatioPressureModel()
    selectedwell = SelectedOilProducer.objects.first()  
    pressure.fgid = selectedwell.fgid
    pressure.wellid = selectedwell.wellid   
    form = FormationPressureForm(request.POST or None, instance=pressure)
    if request.method =="POST":  
        form = FormationPressureForm(request.POST, request.FILES, instance=pressure)       
        pressure.fgid = selectedwell.fgid
        pressure.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('formationpressure:list_formation_Pressure')
    return render (request, 'formationpressure/formationpressure_form.html', {'form': form})

def update_formation_Pressure(request, id):
    pressure = FormatioPressureModel.objects.get(id=id)
    form = FormationPressureForm(request.POST or None, instance=pressure)
    if form.is_valid():
        form.save()
        return redirect ('formationpressure:list_formation_Pressure')
    return render (request, 'formationpressure/formationpressure_form.html', {'form': form, 'pressure':pressure})

def delete_formation_Pressure(request, id):
    pressure = FormatioPressureModel.objects.get(id=id)    
    if request.method == 'POST' :
        pressure.delete()
        return redirect ('formationpressure:list_formation_Pressure')
    return render (request, 'formationpressure/formationpressure_confirm_delete.html', {'pressure':pressure})


