from django.shortcuts import render, redirect
from selectedGasInjector.models import SelectedGasInjector
from giwireline.models import GIWireline
from .models import GIWirelineOperation
from .forms import GIWirelineOpsForm

def list_giwireline_ops_data(request, ctid):     
    selectedwell = SelectedGasInjector.objects.first()   
    giwireline_ops_datas = GIWirelineOperation.objects.filter(wellid = selectedwell.wellid, giwireline =ctid).all()  
    return render (request, 'giwirelineoperations/giwireline_ops_data.html', {'giwireline_ops_datas': giwireline_ops_datas,'ctid':ctid})   
 
def create_giwireline_ops_data(request, ctid): 
    giwireline_data = GIWireline.objects.get(id=ctid)
    giwireline_ops_data = GIWirelineOperation()   
    giwireline_ops_data.giwireline =giwireline_data.pk
    giwireline_ops_data.fgid = giwireline_data.fgid
    giwireline_ops_data.wellid = giwireline_data.wellid   
    form = GIWirelineOpsForm(request.POST or None, instance=giwireline_ops_data)
    if request.method =="POST":  
         form = GIWirelineOpsForm(request.POST, instance=giwireline_ops_data)       
         giwireline_ops_data.fgid = giwireline_data.fgid
         giwireline_ops_data.wellid = giwireline_data.wellid   
         giwireline_ops_data.giwireline =giwireline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('giwirelineoperations:list_giwireline_ops_data', ctid) 
    return render (request, 'giwirelineoperations/giwireline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_giwireline_ops_data(request, id):  
    giwireline_ops_data = GIWirelineOperation.objects.get(id=id) 
    ctid =(giwireline_ops_data.giwireline).pk    
    form = GIWirelineOpsForm(request.POST or None, instance=giwireline_ops_data)    
    if request.method =="POST":
        form = GIWirelineOpsForm(request.POST, request.FILES, instance=giwireline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' giwirelineoperations:list_giwireline_ops_data', ctid)
    return render (request, ' giwirelineoperations/giwireline_ops_data_form.html', {'form': form, 'giwireline_ops_data':giwireline_ops_data, 'id':id})

def delete_giwireline_ops_data(request, id):
    giwireline_ops_data = GIWirelineOperation.objects.get(id=id)  
    ctid =(giwireline_ops_data.giwireline).pk
    print(ctid) 
    if request.method == 'POST' :
        giwireline_ops_data.delete()
        return redirect ('giwirelineoperations:list_giwireline_ops_data', ctid)
    return render (request, 'giwirelineoperations/giwireline_ops_data_confirm_delete.html', {'giwireline_ops_data':giwireline_ops_data, 'id':id})






