from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from rigless.models import Rigless
from .models import RiglessOperation
from .forms import RiglessOpsForm

def list_rigless_ops_data(request, ctid):     
    selectedwell = SelectedOilProducer.objects.first()   
    rigless_ops_datas = RiglessOperation.objects.filter(wellid = selectedwell.wellid, rigless =ctid).all()  
    return render (request, 'riglessoperations/rigless_ops_data.html', {'rigless_ops_datas': rigless_ops_datas,'ctid':ctid})   
 
def create_rigless_ops_data(request, ctid): 
    print(ctid)
    rigless_data = Rigless.objects.get(id=ctid)
    rigless_ops_data = RiglessOperation()   
    rigless_ops_data.rigless =rigless_data
    rigless_ops_data.fgid = rigless_data.fgid
    rigless_ops_data.wellid = rigless_data.wellid   
    form = RiglessOpsForm(request.POST or None, instance=rigless_ops_data)
    if request.method =="POST":  
         form = RiglessOpsForm(request.POST, instance=rigless_ops_data)       
         rigless_ops_data.fgid = rigless_data.fgid
         rigless_ops_data.wellid = rigless_data.wellid   
         rigless_ops_data.rigless =rigless_data                  
         if form.is_valid():
            form.save()  
            return redirect ('riglessoperations:list_rigless_ops_data', ctid) 
    return render (request, 'riglessoperations/rigless_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_rigless_ops_data(request, id):  
    rigless_ops_data = RiglessOperation.objects.get(id=id) 
    ctid =(rigless_ops_data.rigless).pk    
    form = RiglessOpsForm(request.POST or None, instance=rigless_ops_data)    
    if request.method =="POST":
        form = RiglessOpsForm(request.POST, request.FILES, instance=rigless_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('riglessoperations:list_rigless_ops_data', ctid)
    return render (request, 'riglessoperations/rigless_ops_data_form.html', {'form': form, 'rigless_ops_data':rigless_ops_data, 'id':id})

def delete_rigless_ops_data(request, id):
    rigless_ops_data = RiglessOperation.objects.get(id=id)  
    ctid =(rigless_ops_data.rigless).pk
    print(ctid) 
    if request.method == 'POST' :
        rigless_ops_data.delete()
        return redirect ('riglessoperations:list_rigless_ops_data', ctid)
    return render (request, 'riglessoperations/rigless_ops_data_confirm_delete.html', {'rigless_ops_data':rigless_ops_data, 'id':id})


