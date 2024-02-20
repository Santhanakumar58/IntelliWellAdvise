from django.shortcuts import render, redirect
from selectedGasProducer.models import SelectedGasProducer
from gprigworkover1.models import GPRigworkover
from .models import GPRigworkoverOperation
from .forms import GPRigworkoverOpsForm

def list_gprig_wor_ops_data(request, ctid):     
    selectedwell = SelectedGasProducer.objects.first()   
    gprig_wor_ops_datas = GPRigworkoverOperation.objects.filter(wellid = selectedwell.wellid, gprigworkover =ctid).all()  
    return render (request, 'gprigworkover1operations/gprig_workover_ops_data.html', {'gprig_wor_ops_datas': gprig_wor_ops_datas,'ctid':ctid})   
 
def create_gprig_wor_ops_data(request, ctid): 
    gprig_wor_data = GPRigworkover.objects.get(id=ctid)
    gprig_wor_ops_data = GPRigworkoverOperation()   
    gprig_wor_ops_data.gprigworkover =gprig_wor_data
    gprig_wor_ops_data.fgid = gprig_wor_data.fgid
    gprig_wor_ops_data.wellid = gprig_wor_data.wellid   
    form = GPRigworkoverOpsForm(request.POST or None, instance=gprig_wor_ops_data)
    if request.method =="POST":  
         form = GPRigworkoverOpsForm(request.POST, instance=gprig_wor_ops_data)       
         gprig_wor_ops_data.fgid = gprig_wor_data.fgid
         gprig_wor_ops_data.wellid = gprig_wor_data.wellid   
         gprig_wor_ops_data.gprigworkover =gprig_wor_data                   
         if form.is_valid():
            form.save()  
            return redirect ('gprigworkover1operations:list_gprig_wor_ops_data', ctid) 
    return render (request, 'gprigworkover1operations/gprig_workover_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_gprig_wor_ops_data(request, id):  
    gprig_wor_ops_data = GPRigworkoverOperation.objects.get(id=id) 
    ctid =(gprig_wor_ops_data.gprigworkover).pk    
    form = GPRigworkoverOpsForm(request.POST or None, instance=gprig_wor_ops_data)    
    if request.method =="POST":
        form = GPRigworkoverOpsForm(request.POST, request.FILES, instance=gprig_wor_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('gprigworkover1operations:list_gprig_wor_ops_data', ctid)
    return render (request, 'gprigworkover1operations/gprig_workover_ops_data_form.html', {'form': form, 'gprig_wor_ops_data':gprig_wor_ops_data, 'ctid':ctid})

def delete_gprig_wor_ops_data(request, id):
    gprig_wor_ops_data = GPRigworkoverOperation.objects.get(id=id)  
    ctid =(gprig_wor_ops_data.gprigworkover).pk
    print(ctid) 
    if request.method == 'POST' :
        gprig_wor_ops_data.delete()
        return redirect ('gprigworkover1operations:list_gprig_wor_ops_data', ctid)
    return render (request, 'gprigworkover1operations/gprig_workover_ops_data_confirm_delete.html', {'gprig_wor_ops_data':gprig_wor_ops_data, 'ctid':ctid})


