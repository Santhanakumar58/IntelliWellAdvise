from django.shortcuts import render, redirect
from selectedGasInjector.models import SelectedGasInjector
from gistimulation.models import GIStimulation
from .models import GIStimulationOperation
from .forms import GIStimulationOpsForm

def list_gistim_ops_data(request, ctid):     
    selectedwell = SelectedGasInjector.objects.first()   
    gistim_ops_datas = GIStimulationOperation.objects.filter(giwellid = selectedwell.wellid, gistimulation =ctid).all()  
    return render (request, 'gistimulationoperations/gistim_ops_data.html', {'gistim_ops_datas': gistim_ops_datas,'ctid':ctid})   
 
def create_gistim_ops_data(request, ctid): 
    stim_data = GIStimulation.objects.get(id=ctid)
    gistim_ops_data = GIStimulationOperation()   
    gistim_ops_data.gistimulation =stim_data
    gistim_ops_data.fgid = stim_data.fgid
    gistim_ops_data.wellid = stim_data.wellid   
    form = GIStimulationOpsForm(request.POST or None, instance=gistim_ops_data)
    if request.method =="POST":  
         form = GIStimulationOpsForm(request.POST, instance=gistim_ops_data)       
         gistim_ops_data.fgid = stim_data.fgid
         gistim_ops_data.wellid = stim_data.wellid   
         gistim_ops_data.gistimulation =stim_data                
         if form.is_valid():
            form.save()  
            return redirect ('gistimulationoperations:list_gistim_ops_data', ctid) 
    return render (request, 'gistimulationoperations/gistim_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_gistim_ops_data(request, id):  
    gistim_ops_data = GIStimulationOperation.objects.get(id=id) 
    ctid =gistim_ops_data.gistimulation.pk
    form = GIStimulationOpsForm(request.POST or None, instance=gistim_ops_data)    
    if request.method =="POST":
        form = GIStimulationOpsForm(request.POST, request.FILES, instance=gistim_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('gistimulationoperations:list_gistim_ops_data', ctid)
    return render (request, 'gistimulationoperations/gistim_ops_data_form.html', {'form': form, 'gistim_ops_data':gistim_ops_data, 'ctid':ctid})

def delete_gistim_ops_data(request, id):
    gistim_ops_data = GIStimulationOperation.objects.get(id=id)  
    ctid =(gistim_ops_data.gistimulation).pk 
    print(ctid) 
    if request.method == 'POST' :
        gistim_ops_data.delete()
        return redirect ('gistimulationoperations:list_gistim_ops_data', ctid)
    return render (request,'gistimulationoperations/gistim_ops_data_confirm_delete.html', {'gistim_ops_data':gistim_ops_data, 'ctid':ctid})





