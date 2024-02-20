from django.shortcuts import render, redirect
from selectedGasProducer.models import SelectedGasProducer
from gpstimulation.models import GPStimulation
from .models import GPStimulationOperation
from .forms import GPStimulationOpsForm

def list_gpstim_ops_data(request, ctid):     
    selectedwell = SelectedGasProducer.objects.first()   
    gpstim_ops_datas = GPStimulationOperation.objects.filter(gpwellid = selectedwell.wellid, gpstimulation =ctid).all()  
    return render (request, 'gpstimulationoperations/gpstim_ops_data.html', {'gpstim_ops_datas': gpstim_ops_datas,'ctid':ctid})   
 
def create_gpstim_ops_data(request, ctid): 
    stim_data = GPStimulation.objects.get(id=ctid)
    gpstim_ops_data = GPStimulationOperation()   
    gpstim_ops_data.gpstimulation =stim_data
    gpstim_ops_data.fgid = stim_data.fgid
    gpstim_ops_data.wellid = stim_data.wellid   
    form = GPStimulationOpsForm(request.POST or None, instance=gpstim_ops_data)
    if request.method =="POST":  
         form = GPStimulationOpsForm(request.POST, instance=gpstim_ops_data)       
         gpstim_ops_data.fgid = stim_data.fgid
         gpstim_ops_data.wellid = stim_data.wellid   
         gpstim_ops_data.gpstimulation =stim_data                
         if form.is_valid():
            form.save()  
            return redirect ('gpstimulationoperations:list_gpstim_ops_data', ctid) 
    return render (request, 'gpstimulationoperations/gpstim_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_gpstim_ops_data(request, id):  
    gpstim_ops_data = GPStimulationOperation.objects.get(id=id) 
    ctid =gpstim_ops_data.gpstimulation.pk
    form = GPStimulationOpsForm(request.POST or None, instance=gpstim_ops_data)    
    if request.method =="POST":
        form = GPStimulationOpsForm(request.POST, request.FILES, instance=gpstim_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('gpstimulationoperations:list_gpstim_ops_data', ctid)
    return render (request, 'gpstimulationoperations/gpstim_ops_data_form.html', {'form': form, 'gpstim_ops_data':gpstim_ops_data, 'ctid':ctid})

def delete_gpstim_ops_data(request, id):
    gpstim_ops_data = GPStimulationOperation.objects.get(id=id)  
    ctid =(gpstim_ops_data.gpstimulation).pk 
    print(ctid) 
    if request.method == 'POST' :
        gpstim_ops_data.delete()
        return redirect ('gpstimulationoperations:list_gpstim_ops_data', ctid)
    return render (request,'gpstimulationoperations/gpstim_ops_data_confirm_delete.html', {'gpstim_ops_data':gpstim_ops_data, 'ctid':ctid})




