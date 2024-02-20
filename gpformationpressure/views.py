from django.shortcuts import render, redirect
from .models import GPFormatioPressureModel
from .forms import GPFormationPressureForm
from selectedGasProducer.models import SelectedGasProducer



def list_gpformation_Pressure(request):     
    well = SelectedGasProducer.objects.all().first()   
    pressures= GPFormatioPressureModel.objects.filter(gpwellid=well.wellid).all()
    return render (request, 'gpformationpressure/gpformationpressure.html', {'pressures': pressures})

def create_gpformation_Pressure(request):   
    pressure = GPFormatioPressureModel()
    selectedwell = SelectedGasProducer.objects.first()  
    pressure.fgid = selectedwell.fgid
    pressure.wellid = selectedwell.wellid   
    form = GPFormationPressureForm(request.POST or None, instance=pressure)
    if request.method =="POST":  
        form = GPFormationPressureForm(request.POST, request.FILES, instance=pressure)       
        pressure.fgid = selectedwell.fgid
        pressure.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gpformationpressure:list_gpformation_Pressure')
    return render (request, 'gpformationpressure/gpformationpressure_form.html', {'form': form})

def update_gpformation_Pressure(request, id):
    pressure = GPFormatioPressureModel.objects.get(id=id)
    form = GPFormationPressureForm(request.POST or None, instance=pressure)
    if form.is_valid():
        form.save()
        return redirect ('gpformationpressure:list_gpformation_Pressure')
    return render (request, 'gpformationpressure/gpformationpressure_form.html', {'form': form, 'pressure':pressure})

def delete_gpformation_Pressure(request, id):
    pressure = GPFormatioPressureModel.objects.get(id=id)    
    if request.method == 'POST' :
        pressure.delete()
        return redirect ('gpformationpressure:list_gpformation_Pressure')
    return render (request, 'gpformationpressure/gpformationpressure_confirm_delete.html', {'pressure':pressure})



