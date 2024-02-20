from django.shortcuts import render, redirect
from selectedGasInjector.models import SelectedGasInjector
from girigworkover.models import GIRigworkover
from .models import GIRigworkoverOperation
from .forms import GIRigworkoverOpsForm

def list_girig_wor_ops_data(request, ctid):     
    selectedwell = SelectedGasInjector.objects.first()   
    girig_wor_ops_datas = GIRigworkoverOperation.objects.filter(wellid = selectedwell.wellid, girigworkover =ctid).all()  
    return render (request, 'girigworkover1operations/girig_workover_ops_data.html', {'girig_wor_ops_datas': girig_wor_ops_datas,'ctid':ctid})   
 
def create_girig_wor_ops_data(request, ctid): 
    girig_wor_data = GIRigworkover.objects.get(id=ctid)
    girig_wor_ops_data = GIRigworkoverOperation()   
    girig_wor_ops_data.girigworkover =girig_wor_data
    girig_wor_ops_data.fgid = girig_wor_data.fgid
    girig_wor_ops_data.wellid = girig_wor_data.wellid   
    form = GIRigworkoverOpsForm(request.POST or None, instance=girig_wor_ops_data)
    if request.method =="POST":  
         form = GIRigworkoverOpsForm(request.POST, instance=girig_wor_ops_data)       
         girig_wor_ops_data.fgid = girig_wor_data.fgid
         girig_wor_ops_data.wellid = girig_wor_data.wellid   
         girig_wor_ops_data.girigworkover =girig_wor_data                   
         if form.is_valid():
            form.save()  
            return redirect ('girigworkover1operations:list_girig_wor_ops_data', ctid) 
    return render (request, 'girigworkover1operations/girig_workover_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_girig_wor_ops_data(request, id):  
    girig_wor_ops_data = GIRigworkoverOperation.objects.get(id=id) 
    ctid =(girig_wor_ops_data.girigworkover).pk    
    form = GIRigworkoverOpsForm(request.POST or None, instance=girig_wor_ops_data)    
    if request.method =="POST":
        form = GIRigworkoverOpsForm(request.POST, request.FILES, instance=girig_wor_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('girigworkover1operations:list_girig_wor_ops_data', ctid)
    return render (request, 'girigworkover1operations/girig_workover_ops_data_form.html', {'form': form, 'girig_wor_ops_data':girig_wor_ops_data, 'ctid':ctid})

def delete_girig_wor_ops_data(request, id):
    girig_wor_ops_data = GIRigworkoverOperation.objects.get(id=id)  
    ctid =(girig_wor_ops_data.girigworkover).pk
    print(ctid) 
    if request.method == 'POST' :
        girig_wor_ops_data.delete()
        return redirect ('girigworkover1operations:list_girig_wor_ops_data', ctid)
    return render (request, 'girigworkover1operations/girig_workover_ops_data_confirm_delete.html', {'girig_wor_ops_data':girig_wor_ops_data, 'ctid':ctid})


