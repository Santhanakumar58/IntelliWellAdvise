from django.shortcuts import render, redirect
from selectedGasProducer.models import SelectedGasProducer
from gpwireline.models import GPWireline
from .models import GPWirelineOperation
from .forms import GPWirelineOpsForm

def list_gpwireline_ops_data(request, ctid):     
    selectedwell = SelectedGasProducer.objects.first()   
    gpwireline_ops_datas = GPWirelineOperation.objects.filter(wellid = selectedwell.wellid, gpwireline =ctid).all()  
    return render (request, 'gpwirelineoperations/gpwireline_ops_data.html', {'gpwireline_ops_datas': gpwireline_ops_datas,'ctid':ctid})   
 
def create_gpwireline_ops_data(request, ctid): 
    gpwireline_data = GPWireline.objects.get(id=ctid)
    gpwireline_ops_data = GPWirelineOperation()   
    gpwireline_ops_data.gpwireline =gpwireline_data.pk
    gpwireline_ops_data.fgid = gpwireline_data.fgid
    gpwireline_ops_data.wellid = gpwireline_data.wellid   
    form = GPWirelineOpsForm(request.POST or None, instance=gpwireline_ops_data)
    if request.method =="POST":  
         form = GPWirelineOpsForm(request.POST, instance=gpwireline_ops_data)       
         gpwireline_ops_data.fgid = gpwireline_data.fgid
         gpwireline_ops_data.wellid = gpwireline_data.wellid   
         gpwireline_ops_data.gpwireline =gpwireline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('gpwirelineoperations:list_gpwireline_ops_data', ctid) 
    return render (request, 'gpwirelineoperations/gpwireline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_gpwireline_ops_data(request, id):  
    gpwireline_ops_data = GPWirelineOperation.objects.get(id=id) 
    ctid =(gpwireline_ops_data.gpwireline).pk    
    form = GPWirelineOpsForm(request.POST or None, instance=gpwireline_ops_data)    
    if request.method =="POST":
        form = GPWirelineOpsForm(request.POST, request.FILES, instance=gpwireline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' gpwirelineoperations:list_gpwireline_ops_data', ctid)
    return render (request, ' gpwirelineoperations/gpwireline_ops_data_form.html', {'form': form, 'gpwireline_ops_data':gpwireline_ops_data, 'id':id})

def delete_gpwireline_ops_data(request, id):
    gpwireline_ops_data = GPWirelineOperation.objects.get(id=id)  
    ctid =(gpwireline_ops_data.gpwireline).pk
    print(ctid) 
    if request.method == 'POST' :
        gpwireline_ops_data.delete()
        return redirect ('gpwirelineoperations:list_gpwireline_ops_data', ctid)
    return render (request, 'gpwirelineoperations/gpwireline_ops_data_confirm_delete.html', {'gpwireline_ops_data':gpwireline_ops_data, 'id':id})





