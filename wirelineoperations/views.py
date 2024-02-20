from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from stimulation.models import Stimulation
from .models import WirelineOperation
from .forms import WirelineOpsForm

def list_wireline_ops_data(request, ctid):     
    selectedwell = SelectedOilProducer.objects.first()   
    wireline_ops_datas = WirelineOperation.objects.filter(wellid = selectedwell.wellid, wireline =ctid).all()  
    return render (request, 'wirelineoperations/wireline_ops_data.html', {'wireline_ops_datas': wireline_ops_datas,'ctid':ctid})   
 
def create_wireline_ops_data(request, ctid): 
    wireline_data = Stimulation.objects.get(id=ctid)
    wireline_ops_data = WirelineOperation()   
    wireline_ops_data.wireline =wireline_data.pk
    wireline_ops_data.fgid = wireline_data.fgid
    wireline_ops_data.wellid = wireline_data.wellid   
    form = WirelineOpsForm(request.POST or None, instance=wireline_ops_data)
    if request.method =="POST":  
         form = WirelineOpsForm(request.POST, instance=wireline_ops_data)       
         wireline_ops_data.fgid = wireline_data.fgid
         wireline_ops_data.wellid = wireline_data.wellid   
         wireline_ops_data.wireline =wireline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('wirelineoperations:list_wireline_ops_data', ctid) 
    return render (request, 'wirelineoperations/wireline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_wireline_ops_data(request, id):  
    wireline_ops_data = WirelineOperation.objects.get(id=id) 
    ctid =(wireline_ops_data.wireline).pk    
    form = WirelineOpsForm(request.POST or None, instance=wireline_ops_data)    
    if request.method =="POST":
        form = WirelineOpsForm(request.POST, request.FILES, instance=wireline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' wirelineoperations:list_wireline_ops_data', ctid)
    return render (request, ' wirelineoperations/wireline_ops_data_form.html', {'form': form, 'wireline_ops_data':wireline_ops_data, 'id':id})

def delete_wireline_ops_data(request, id):
    wireline_ops_data = WirelineOperation.objects.get(id=id)  
    ctid =(wireline_ops_data.wireline).pk
    print(ctid) 
    if request.method == 'POST' :
        wireline_ops_data.delete()
        return redirect ('wirelineoperations:list_wireline_ops_data', ctid)
    return render (request, 'wirelineoperations/wireline_ops_data_confirm_delete.html', {'wireline_ops_data':wireline_ops_data, 'id':id})




