from django.shortcuts import render, redirect
from .models import WIFormatioPressureModel
from .forms import WIFormationPressureForm
from selectedWaterInjector.models import SelectedWaterInjector



def list_wiformation_Pressure(request):     
    well = SelectedWaterInjector.objects.all().first()   
    pressures= WIFormatioPressureModel.objects.filter(wiwellid=well.wellid).all()
    return render (request, 'wiformationpressure/wiformationpressure.html', {'pressures': pressures})

def create_wiformation_Pressure(request):   
    pressure = WIFormatioPressureModel()
    selectedwell = SelectedWaterInjector.objects.first()  
    pressure.fgid = selectedwell.fgid
    pressure.wellid = selectedwell.wellid   
    form = WIFormationPressureForm(request.POST or None, instance=pressure)
    if request.method =="POST":  
        form = WIFormationPressureForm(request.POST, request.FILES, instance=pressure)       
        pressure.fgid = selectedwell.fgid
        pressure.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('wiformationpressure:list_wiformation_Pressure')
    return render (request, 'wiformationpressure/wiformationpressure_form.html', {'form': form})

def update_wiformation_Pressure(request, id):
    pressure = WIFormatioPressureModel.objects.get(id=id)
    form = WIFormationPressureForm(request.POST or None, instance=pressure)
    if form.is_valid():
        form.save()
        return redirect ('wiformationpressure:list_wiformation_Pressure')
    return render (request, 'wiformationpressure/wiformationpressure_form.html', {'form': form, 'pressure':pressure})

def delete_wiformation_Pressure(request, id):
    pressure = WIFormatioPressureModel.objects.get(id=id)    
    if request.method == 'POST' :
        pressure.delete()
        return redirect ('wiformationpressure:list_wiformation_Pressure')
    return render (request, 'wiformationpressure/wiformationpressure_confirm_delete.html', {'pressure':pressure})




