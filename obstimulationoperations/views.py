from django.shortcuts import render, redirect
from selectedObserver.models import SelectedObserver
from obstimulation.models import OBStimulation
from .models import OBStimulationOperation
from .forms import OBStimulationOpsForm

def list_obstim_ops_data(request, ctid):     
    selectedwell = SelectedObserver.objects.first()   
    obstim_ops_datas = OBStimulationOperation.objects.filter(obwellid = selectedwell.wellid, obstimulation =ctid).all()  
    return render (request, 'obstimulationoperations/obstim_ops_data.html', {'obstim_ops_datas': obstim_ops_datas,'ctid':ctid})   
 
def create_obstim_ops_data(request, ctid): 
    stim_data = OBStimulation.objects.get(id=ctid)
    obstim_ops_data = OBStimulationOperation()   
    obstim_ops_data.obstimulation =stim_data
    obstim_ops_data.fgid = stim_data.fgid
    obstim_ops_data.wellid = stim_data.wellid   
    form = OBStimulationOpsForm(request.POST or None, instance=obstim_ops_data)
    if request.method =="POST":  
         form = OBStimulationOpsForm(request.POST, instance=obstim_ops_data)       
         obstim_ops_data.fgid = stim_data.fgid
         obstim_ops_data.wellid = stim_data.wellid   
         obstim_ops_data.obstimulation =stim_data                
         if form.is_valid():
            form.save()  
            return redirect ('obstimulationoperations:list_obstim_ops_data', ctid) 
    return render (request, 'obstimulationoperations/obstim_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_obstim_ops_data(request, id):  
    obstim_ops_data = OBStimulationOperation.objects.get(id=id) 
    ctid =obstim_ops_data.obstimulation.pk
    form = OBStimulationOpsForm(request.POST or None, instance=obstim_ops_data)    
    if request.method =="POST":
        form = OBStimulationOpsForm(request.POST, request.FILES, instance=obstim_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('obstimulationoperations:list_obstim_ops_data', ctid)
    return render (request, 'obstimulationoperations/obstim_ops_data_form.html', {'form': form, 'obstim_ops_data':obstim_ops_data, 'ctid':ctid})

def delete_obstim_ops_data(request, id):
    obstim_ops_data = OBStimulationOperation.objects.get(id=id)  
    ctid =(obstim_ops_data.obstimulation).pk 
    print(ctid) 
    if request.method == 'POST' :
        obstim_ops_data.delete()
        return redirect ('obstimulationoperations:list_obstim_ops_data', ctid)
    return render (request,'obstimulationoperations/obstim_ops_data_confirm_delete.html', {'obstim_ops_data':obstim_ops_data, 'ctid':ctid})





