from django.shortcuts import render, redirect
from .models import OBFormatioPressureModel
from .forms import OBFormationPressureForm
from selectedGasProducer.models import SelectedGasProducer



def list_obformation_Pressure(request):     
    well = SelectedGasProducer.objects.all().first()   
    pressures= OBFormatioPressureModel.objects.filter(obwellid=well.wellid).all()
    return render (request, 'obformationpressure/obformationpressure.html', {'pressures': pressures})

def create_obformation_Pressure(request):   
    pressure = OBFormatioPressureModel()
    selectedwell = SelectedGasProducer.objects.first()  
    pressure.fgid = selectedwell.fgid
    pressure.wellid = selectedwell.wellid   
    form = OBFormationPressureForm(request.POST or None, instance=pressure)
    if request.method =="POST":  
        form = OBFormationPressureForm(request.POST, request.FILES, instance=pressure)       
        pressure.fgid = selectedwell.fgid
        pressure.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('obformationpressure:list_obformation_Pressure')
    return render (request, 'obformationpressure/obformationpressure_form.html', {'form': form})

def update_obformation_Pressure(request, id):
    pressure = OBFormatioPressureModel.objects.get(id=id)
    form = OBFormationPressureForm(request.POST or None, instance=pressure)
    if form.is_valid():
        form.save()
        return redirect ('obformationpressure:list_obformation_Pressure')
    return render (request, 'obformationpressure/obformationpressure_form.html', {'form': form, 'pressure':pressure})

def delete_obformation_Pressure(request, id):
    pressure = OBFormatioPressureModel.objects.get(id=id)    
    if request.method == 'POST' :
        pressure.delete()
        return redirect ('obformationpressure:list_obformation_Pressure')
    return render (request, 'obformationpressure/obformationpressure_confirm_delete.html', {'pressure':pressure})



