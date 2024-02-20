from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from rigworkover.models import Rigworkover
from .models import RigworkoverOperation
from .forms import RigworkoverOpsForm

def list_rig_wor_ops_data(request, ctid):     
    selectedwell = SelectedOilProducer.objects.first()   
    rig_wor_ops_datas = RigworkoverOperation.objects.filter(wellid = selectedwell.wellid, rigworkover =ctid).all()  
    return render (request, 'rigworkoveroperations/rig_workover_ops_data.html', {'rig_wor_ops_datas': rig_wor_ops_datas,'ctid':ctid})   
 
def create_rig_wor_ops_data(request, ctid): 
    rig_wor_data = Rigworkover.objects.get(id=ctid)
    rig_wor_ops_data = RigworkoverOperation()   
    rig_wor_ops_data.rigworkover =rig_wor_data
    rig_wor_ops_data.fgid = rig_wor_data.fgid
    rig_wor_ops_data.wellid = rig_wor_data.wellid   
    form = RigworkoverOpsForm(request.POST or None, instance=rig_wor_ops_data)
    if request.method =="POST":  
         form = RigworkoverOpsForm(request.POST, instance=rig_wor_ops_data)       
         rig_wor_ops_data.fgid = rig_wor_data.fgid
         rig_wor_ops_data.wellid = rig_wor_data.wellid   
         rig_wor_ops_data.rigworkover =rig_wor_data                   
         if form.is_valid():
            form.save()  
            return redirect ('rigworkoveroperations:list_rig_wor_ops_data', ctid) 
    return render (request, 'rigworkoveroperations/rig_workover_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_rig_wor_ops_data(request, id):  
    rig_wor_ops_data = RigworkoverOperation.objects.get(id=id) 
    ctid =(rig_wor_ops_data.rigworkover).pk    
    form = RigworkoverOpsForm(request.POST or None, instance=rig_wor_ops_data)    
    if request.method =="POST":
        form = RigworkoverOpsForm(request.POST, request.FILES, instance=rig_wor_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('rigworkoveroperations:list_rig_wor_ops_data', ctid)
    return render (request, 'rigworkoveroperations/rig_workover_ops_data_form.html', {'form': form, 'rig_wor_ops_data':rig_wor_ops_data, 'ctid':ctid})

def delete_rig_wor_ops_data(request, id):
    rig_wor_ops_data = RigworkoverOperation.objects.get(id=id)  
    ctid =(rig_wor_ops_data.rigworkover).pk
    print(ctid) 
    if request.method == 'POST' :
        rig_wor_ops_data.delete()
        return redirect ('rigworkoveroperations:list_rig_wor_ops_data', ctid)
    return render (request, 'rigworkoveroperations/rig_workover_ops_data_confirm_delete.html', {'rig_wor_ops_data':rig_wor_ops_data, 'ctid':ctid})


