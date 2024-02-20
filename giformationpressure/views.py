from django.shortcuts import render, redirect
from .models import GIFormatioPressureModel
from .forms import GIFormationPressureForm
from selectedGasInjector.models import SelectedGasInjector



def list_giformation_Pressure(request):     
    well = SelectedGasInjector.objects.all().first()   
    pressures= GIFormatioPressureModel.objects.filter(giwellid=well.wellid).all()
    return render (request, 'giformationpressure/giformationpressure.html', {'pressures': pressures})

def create_giformation_Pressure(request):   
    pressure = GIFormatioPressureModel()
    selectedwell = SelectedGasInjector.objects.first()  
    pressure.fgid = selectedwell.fgid
    pressure.wellid = selectedwell.wellid   
    form = GIFormationPressureForm(request.POST or None, instance=pressure)
    if request.method =="POST":  
        form = GIFormationPressureForm(request.POST, request.FILES, instance=pressure)       
        pressure.fgid = selectedwell.fgid
        pressure.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('giformationpressure:list_giformation_Pressure')
    return render (request, 'giformationpressure/giformationpressure_form.html', {'form': form})

def update_giformation_Pressure(request, id):
    pressure = GIFormatioPressureModel.objects.get(id=id)
    form = GIFormationPressureForm(request.POST or None, instance=pressure)
    if form.is_valid():
        form.save()
        return redirect ('giformationpressure:list_giformation_Pressure')
    return render (request, 'giformationpressure/giformationpressure_form.html', {'form': form, 'pressure':pressure})

def delete_giformation_Pressure(request, id):
    pressure = GIFormatioPressureModel.objects.get(id=id)    
    if request.method == 'POST' :
        pressure.delete()
        return redirect ('giformationpressure:list_giformation_Pressure')
    return render (request, 'giformationpressure/giformationpressure_confirm_delete.html', {'pressure':pressure})




