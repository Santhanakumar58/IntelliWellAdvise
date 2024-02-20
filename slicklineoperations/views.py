from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from slickline.models import Slickline
from .models import SlicklineOperation
from .forms import SlicklineOpsForm

def list_slickline_ops_data(request, ctid):     
    selectedwell = SelectedOilProducer.objects.first()   
    slickline_ops_datas = SlicklineOperation.objects.filter(wellid = selectedwell.wellid, slickline =ctid).all()  
    return render (request, 'slicklineoperations/slickline_ops_data.html', {'slickline_ops_datas': slickline_ops_datas,'ctid':ctid})   
 
def create_slickline_ops_data(request, ctid): 
    slickline_data = Slickline.objects.get(id=ctid)
    slickline_ops_data = SlicklineOperation()   
    slickline_ops_data.slickline =slickline_data.pk
    slickline_ops_data.fgid = slickline_data.fgid
    slickline_ops_data.wellid = slickline_data.wellid   
    form = SlicklineOpsForm(request.POST or None, instance=slickline_ops_data)
    if request.method =="POST":  
         form = SlicklineOpsForm(request.POST, instance=slickline_ops_data)       
         slickline_ops_data.fgid = slickline_data.fgid
         slickline_ops_data.wellid = slickline_data.wellid   
         slickline_ops_data.slickline =slickline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('slicklineoperations:list_slickline_ops_data', ctid) 
    return render (request, 'slicklineoperations/slickline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_slickline_ops_data(request, id):  
    slickline_ops_data = SlicklineOperation.objects.get(id=id) 
    ctid =(slickline_ops_data.slickline).pk    
    form = SlicklineOpsForm(request.POST or None, instance=slickline_ops_data)    
    if request.method =="POST":
        form = SlicklineOpsForm(request.POST, request.FILES, instance=slickline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' slicklineoperations:list_ lickline_ops_data', ctid)
    return render (request, ' slicklineoperations/ slickline_ops_data_form.html', {'form': form, 'slickline_ops_data':slickline_ops_data, 'id':id})

def delete_slickline_ops_data(request, id):
    slickline_ops_data = SlicklineOperation.objects.get(id=id)  
    ctid =(slickline_ops_data.slickline).pk
    print(ctid) 
    if request.method == 'POST' :
        slickline_ops_data.delete()
        return redirect ('slicklineoperations:list_slickline_ops_data', ctid)
    return render (request, 'slicklineoperations/slickline_ops_data_confirm_delete.html', {'slickline_ops_data':slickline_ops_data, 'id':id})


