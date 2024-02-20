from django.shortcuts import render, redirect
from selectedObserver.models import SelectedObserver
from obrigworkover.models import OBRigworkover
from .models import OBRigworkoverOperation
from .forms import OBRigworkoverOpsForm

def list_obrig_wor_ops_data(request, ctid):     
    selectedwell = SelectedObserver.objects.first()   
    obrig_wor_ops_datas = OBRigworkoverOperation.objects.filter(wellid = selectedwell.wellid, obrigworkover =ctid).all()  
    return render (request, 'obrigworkover1operations/obrig_workover_ops_data.html', {'obrig_wor_ops_datas': obrig_wor_ops_datas,'ctid':ctid})   
 
def create_obrig_wor_ops_data(request, ctid): 
    obrig_wor_data = OBRigworkover.objects.get(id=ctid)
    obrig_wor_ops_data = OBRigworkoverOperation()   
    obrig_wor_ops_data.obrigworkover =obrig_wor_data
    obrig_wor_ops_data.fgid = obrig_wor_data.fgid
    obrig_wor_ops_data.wellid = obrig_wor_data.wellid   
    form = OBRigworkoverOpsForm(request.POST or None, instance=obrig_wor_ops_data)
    if request.method =="POST":  
         form = OBRigworkoverOpsForm(request.POST, instance=obrig_wor_ops_data)       
         obrig_wor_ops_data.fgid = obrig_wor_data.fgid
         obrig_wor_ops_data.wellid = obrig_wor_data.wellid   
         obrig_wor_ops_data.obrigworkover =obrig_wor_data                   
         if form.is_valid():
            form.save()  
            return redirect ('obrigworkover1operations:list_obrig_wor_ops_data', ctid) 
    return render (request, 'obrigworkover1operations/obrig_workover_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_obrig_wor_ops_data(request, id):  
    obrig_wor_ops_data = OBRigworkoverOperation.objects.get(id=id) 
    ctid =(obrig_wor_ops_data.obrigworkover).pk    
    form = OBRigworkoverOpsForm(request.POST or None, instance=obrig_wor_ops_data)    
    if request.method =="POST":
        form = OBRigworkoverOpsForm(request.POST, request.FILES, instance=obrig_wor_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('obrigworkover1operations:list_obrig_wor_ops_data', ctid)
    return render (request, 'obrigworkover1operations/obrig_workover_ops_data_form.html', {'form': form, 'obrig_wor_ops_data':obrig_wor_ops_data, 'ctid':ctid})

def delete_obrig_wor_ops_data(request, id):
    obrig_wor_ops_data = OBRigworkoverOperation.objects.get(id=id)  
    ctid =(obrig_wor_ops_data.obrigworkover).pk
    print(ctid) 
    if request.method == 'POST' :
        obrig_wor_ops_data.delete()
        return redirect ('obrigworkover1operations:list_obrig_wor_ops_data', ctid)
    return render (request, 'obrigworkover1operations/obrig_workover_ops_data_confirm_delete.html', {'obrig_wor_ops_data':obrig_wor_ops_data, 'ctid':ctid})


