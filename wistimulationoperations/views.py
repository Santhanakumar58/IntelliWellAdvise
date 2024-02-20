from django.shortcuts import render, redirect
from selectedWaterInjector.models import SelectedWaterInjector
from wistimulation.models import WIStimulation
from .models import WIStimulationOperation
from .forms import WIStimulationOpsForm

def list_wistim_ops_data(request, ctid):     
    selectedwell = SelectedWaterInjector.objects.first()   
    stim_ops_datas = WIStimulationOperation.objects.filter(wiwellid = selectedwell.wellid, wistimulation =ctid).all()  
    return render (request, 'wistimulationoperations/wistim_ops_data.html', {'stim_ops_datas': stim_ops_datas,'ctid':ctid})   
 
def create_wistim_ops_data(request, ctid): 
    stim_data = WIStimulation.objects.get(id=ctid)
    stim_ops_data = WIStimulationOperation()   
    stim_ops_data.wistimulation =stim_data
    stim_ops_data.fgid = stim_data.fgid
    stim_ops_data.wellid = stim_data.wellid   
    form = WIStimulationOpsForm(request.POST or None, instance=stim_ops_data)
    if request.method =="POST":  
         form = WIStimulationOpsForm(request.POST, instance=stim_ops_data)       
         stim_ops_data.fgid = stim_data.fgid
         stim_ops_data.wellid = stim_data.wellid   
         stim_ops_data.wistimulation =stim_data                
         if form.is_valid():
            form.save()  
            return redirect ('wistimulationoperations:list_wistim_ops_data', ctid) 
    return render (request, 'wistimulationoperations/wistim_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_wistim_ops_data(request, id):  
    stim_ops_data = WIStimulationOperation.objects.get(id=id) 
    ctid =stim_ops_data.wistimulation.pk
    form = WIStimulationOpsForm(request.POST or None, instance=stim_ops_data)    
    if request.method =="POST":
        form = WIStimulationOpsForm(request.POST, request.FILES, instance=stim_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('wistimulationoperations:list_wistim_ops_data', ctid)
    return render (request, 'wistimulationoperations/wistim_ops_data_form.html', {'form': form, 'stim_ops_data':stim_ops_data, 'ctid':ctid})

def delete_wistim_ops_data(request, id):
    stim_ops_data = WIStimulationOperation.objects.get(id=id)  
    ctid =(stim_ops_data.wistimulation).pk 
    print(ctid) 
    if request.method == 'POST' :
        stim_ops_data.delete()
        return redirect ('wistimulationoperations:list_wistim_ops_data', ctid)
    return render (request,'wistimulationoperations/wistim_ops_data_confirm_delete.html', {'stim_ops_data':stim_ops_data, 'ctid':ctid})




