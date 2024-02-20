from django.shortcuts import render, redirect
from selectedWaterInjector.models import SelectedWaterInjector
from wiwireline.models import WIWireline
from .models import WIWirelineOperation
from .forms import WIWirelineOpsForm

def list_wiwireline_ops_data(request, ctid):     
    selectedwell = SelectedWaterInjector.objects.first()   
    wiwireline_ops_datas = WIWirelineOperation.objects.filter(wiwellid = selectedwell.wellid, wiwireline =ctid).all()  
    return render (request, 'wiwirelineoperations/wiwireline_ops_data.html', {'wiwireline_ops_datas': wiwireline_ops_datas,'ctid':ctid})   
 
def create_wiwireline_ops_data(request, ctid): 
    wiwireline_data = WIWireline.objects.get(id=ctid)
    wiwireline_ops_data = WIWirelineOperation()   
    wiwireline_ops_data.wiwireline =wiwireline_data.pk
    wiwireline_ops_data.fgid = wiwireline_data.fgid
    wiwireline_ops_data.wellid = wiwireline_data.wellid   
    form = WIWirelineOpsForm(request.POST or None, instance=wiwireline_ops_data)
    if request.method =="POST":  
         form = WIWirelineOpsForm(request.POST, instance=wiwireline_ops_data)       
         wiwireline_ops_data.fgid = wiwireline_data.fgid
         wiwireline_ops_data.wellid = wiwireline_data.wellid   
         wiwireline_ops_data.wiwireline =wiwireline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('wiwirelineoperations:list_wiwireline_ops_data', ctid) 
    return render (request, 'wiwirelineoperations/wiwireline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_wiwireline_ops_data(request, id):  
    wiwireline_ops_data = WIWirelineOperation.objects.get(id=id) 
    ctid =(wiwireline_ops_data.wiwireline).pk    
    form = WIWirelineOpsForm(request.POST or None, instance=wiwireline_ops_data)    
    if request.method =="POST":
        form = WIWirelineOpsForm(request.POST, request.FILES, instance=wiwireline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' wiwirelineoperations:list_wiwireline_ops_data', ctid)
    return render (request, ' wiwirelineoperations/wiwireline_ops_data_form.html', {'form': form, 'wiwireline_ops_data':wiwireline_ops_data, 'id':id})

def delete_wiwireline_ops_data(request, id):
    wiwireline_ops_data = WIWirelineOperation.objects.get(id=id)  
    ctid =(wiwireline_ops_data.wiwireline).pk
    print(ctid) 
    if request.method == 'POST' :
        wiwireline_ops_data.delete()
        return redirect ('wiwirelineoperations:list_wiwireline_ops_data', ctid)
    return render (request, 'wiwirelineoperations/wiwireline_ops_data_confirm_delete.html', {'wiwireline_ops_data':wiwireline_ops_data, 'id':id})




