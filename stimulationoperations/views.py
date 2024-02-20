from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from stimulation.models import Stimulation
from .models import StimulationOperation
from .forms import StimulationOpsForm

def list_stim_ops_data(request, ctid):     
    selectedwell = SelectedOilProducer.objects.first()   
    stim_ops_datas = StimulationOperation.objects.filter(wellid = selectedwell.wellid, stimulation =ctid).all()  
    return render (request, 'stimulationoperations/stim_ops_data.html', {'stim_ops_datas': stim_ops_datas,'ctid':ctid})   
 
def create_stim_ops_data(request, ctid): 
    stim_data = Stimulation.objects.get(id=ctid)
    stim_ops_data = StimulationOperation()   
    stim_ops_data.stimulation =stim_data
    stim_ops_data.fgid = stim_data.fgid
    stim_ops_data.wellid = stim_data.wellid   
    form = StimulationOpsForm(request.POST or None, instance=stim_ops_data)
    if request.method =="POST":  
         form = StimulationOpsForm(request.POST, instance=stim_ops_data)       
         stim_ops_data.fgid = stim_data.fgid
         stim_ops_data.wellid = stim_data.wellid   
         stim_ops_data.stimulation =stim_data                
         if form.is_valid():
            form.save()  
            return redirect ('stimulationoperations:list_stim_ops_data', ctid) 
    return render (request, 'stimulationoperations/stim_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_stim_ops_data(request, id):  
    stim_ops_data = StimulationOperation.objects.get(id=id) 
    ctid =stim_ops_data.stimulation.pk
    form = StimulationOpsForm(request.POST or None, instance=stim_ops_data)    
    if request.method =="POST":
        form = StimulationOpsForm(request.POST, request.FILES, instance=stim_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('stimulationoperations:list_stim_ops_data', ctid)
    return render (request, 'stimulationoperations/stim_ops_data_form.html', {'form': form, 'stim_ops_data':stim_ops_data, 'ctid':ctid})

def delete_stim_ops_data(request, id):
    stim_ops_data = StimulationOperation.objects.get(id=id)  
    ctid =(stim_ops_data.stimulation).pk 
    print(ctid) 
    if request.method == 'POST' :
        stim_ops_data.delete()
        return redirect ('stimulationoperations:list_stim_ops_data', ctid)
    return render (request,'stimulationoperations/stim_ops_data_confirm_delete.html', {'stim_ops_data':stim_ops_data, 'ctid':ctid})



