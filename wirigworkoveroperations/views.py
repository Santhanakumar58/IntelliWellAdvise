from django.shortcuts import render, redirect
from selectedWaterInjector.models import SelectedWaterInjector
from wirigworkover.models import WIRigworkover
from .models import WIRigworkoverOperation
from .forms import WIRigworkoverOpsForm

def list_wirig_wor_ops_data(request, ctid):     
    selectedwell = SelectedWaterInjector.objects.first()   
    rig_wor_ops_datas = WIRigworkoverOperation.objects.filter(wiwellid = selectedwell.wellid, wirigworkover =ctid).all()  
    return render (request, 'wirigworkoveroperations/wirig_workover_ops_data.html', {'rig_wor_ops_datas': rig_wor_ops_datas,'ctid':ctid})   
 
def create_wirig_wor_ops_data(request, ctid): 
    rig_wor_data = WIRigworkover.objects.get(id=ctid)
    rig_wor_ops_data = WIRigworkoverOperation()   
    rig_wor_ops_data.wirigworkover =rig_wor_data
    rig_wor_ops_data.fgid = rig_wor_data.fgid
    rig_wor_ops_data.wellid = rig_wor_data.wellid   
    form = WIRigworkoverOpsForm(request.POST or None, instance=rig_wor_ops_data)
    if request.method =="POST":  
         form = WIRigworkoverOpsForm(request.POST, instance=rig_wor_ops_data)       
         rig_wor_ops_data.fgid = rig_wor_data.fgid
         rig_wor_ops_data.wellid = rig_wor_data.wellid   
         rig_wor_ops_data.wirigworkover =rig_wor_data                   
         if form.is_valid():
            form.save()  
            return redirect ('wirigworkoveroperations:list_wirig_wor_ops_data', ctid) 
    return render (request, 'wirigworkoveroperations/wirig_workover_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_wirig_wor_ops_data(request, id):  
    rig_wor_ops_data = WIRigworkoverOperation.objects.get(id=id) 
    ctid =(rig_wor_ops_data.wirigworkover).pk    
    form = WIRigworkoverOpsForm(request.POST or None, instance=rig_wor_ops_data)    
    if request.method =="POST":
        form = WIRigworkoverOpsForm(request.POST, request.FILES, instance=rig_wor_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('wirigworkoveroperations:list_wirig_wor_ops_data', ctid)
    return render (request, 'wirigworkoveroperations/wirig_workover_ops_data_form.html', {'form': form, 'rig_wor_ops_data':rig_wor_ops_data, 'ctid':ctid})

def delete_wirig_wor_ops_data(request, id):
    rig_wor_ops_data = WIRigworkoverOperation.objects.get(id=id)  
    ctid =(rig_wor_ops_data.wirigworkover).pk
    print(ctid) 
    if request.method == 'POST' :
        rig_wor_ops_data.delete()
        return redirect ('wirigworkoveroperations:list_wirig_wor_ops_data', ctid)
    return render (request, 'wirigworkoveroperations/wirig_workover_ops_data_confirm_delete.html', {'rig_wor_ops_data':rig_wor_ops_data, 'ctid':ctid})


