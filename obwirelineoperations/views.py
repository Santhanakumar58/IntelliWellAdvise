from django.shortcuts import render, redirect
from selectedObserver.models import SelectedObserver
from obwireline.models import OBWireline
from .models import OBWirelineOperation
from .forms import OBWirelineOpsForm

def list_obwireline_ops_data(request, ctid):     
    selectedwell = SelectedObserver.objects.first()   
    obwireline_ops_datas = OBWirelineOperation.objects.filter(wellid = selectedwell.wellid, obwireline =ctid).all()  
    return render (request, 'obwirelineoperations/obwireline_ops_data.html', {'obwireline_ops_datas': obwireline_ops_datas,'ctid':ctid})   
 
def create_obwireline_ops_data(request, ctid): 
    obwireline_data = OBWireline.objects.get(id=ctid)
    obwireline_ops_data = OBWirelineOperation()   
    obwireline_ops_data.obwireline =obwireline_data.pk
    obwireline_ops_data.fgid = obwireline_data.fgid
    obwireline_ops_data.wellid = obwireline_data.wellid   
    form = OBWirelineOpsForm(request.POST or None, instance=obwireline_ops_data)
    if request.method =="POST":  
         form = OBWirelineOpsForm(request.POST, instance=obwireline_ops_data)       
         obwireline_ops_data.fgid = obwireline_data.fgid
         obwireline_ops_data.wellid = obwireline_data.wellid   
         obwireline_ops_data.obwireline =obwireline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('obwirelineoperations:list_obwireline_ops_data', ctid) 
    return render (request, 'obwirelineoperations/obwireline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_obwireline_ops_data(request, id):  
    obwireline_ops_data = OBWirelineOperation.objects.get(id=id) 
    ctid =(obwireline_ops_data.obwireline).pk    
    form = OBWirelineOpsForm(request.POST or None, instance=obwireline_ops_data)    
    if request.method =="POST":
        form = OBWirelineOpsForm(request.POST, request.FILES, instance=obwireline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' obwirelineoperations:list_obwireline_ops_data', ctid)
    return render (request, ' obwirelineoperations/obwireline_ops_data_form.html', {'form': form, 'obwireline_ops_data':obwireline_ops_data, 'id':id})

def delete_obwireline_ops_data(request, id):
    obwireline_ops_data = OBWirelineOperation.objects.get(id=id)  
    ctid =(obwireline_ops_data.obwireline).pk
    print(ctid) 
    if request.method == 'POST' :
        obwireline_ops_data.delete()
        return redirect ('obwirelineoperations:list_obwireline_ops_data', ctid)
    return render (request, 'obwirelineoperations/obwireline_ops_data_confirm_delete.html', {'obwireline_ops_data':obwireline_ops_data, 'id':id})






