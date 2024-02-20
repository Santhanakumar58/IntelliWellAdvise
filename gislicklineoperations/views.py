from django.shortcuts import render, redirect
from selectedGasInjector.models import SelectedGasInjector
from gislickline.models import GISlickline
from .models import GISlicklineOperation
from .forms import GISlicklineOpsForm

def list_gislickline_ops_data(request, ctid):     
    selectedwell = SelectedGasInjector.objects.first()   
    gislickline_ops_datas = GISlicklineOperation.objects.filter(giwellid = selectedwell.wellid, gislickline =ctid).all()  
    return render (request, 'gislicklineoperations/gislickline_ops_data.html', {'gislickline_ops_datas': gislickline_ops_datas,'ctid':ctid})   
 
def create_gislickline_ops_data(request, ctid): 
    gislickline_data = GISlickline.objects.get(id=ctid)
    gislickline_ops_data = GISlicklineOperation()   
    gislickline_ops_data.gislickline =gislickline_data.pk
    gislickline_ops_data.fgid = gislickline_data.fgid
    gislickline_ops_data.wellid = gislickline_data.wellid   
    form = GISlicklineOpsForm(request.POST or None, instance=gislickline_ops_data)
    if request.method =="POST":  
         form = GISlicklineOpsForm(request.POST, instance=gislickline_ops_data)       
         gislickline_ops_data.fgid = gislickline_data.fgid
         gislickline_ops_data.wellid = gislickline_data.wellid   
         gislickline_ops_data.gislickline =gislickline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('gislicklineoperations:list_gislickline_ops_data', ctid) 
    return render (request, 'gislicklineoperations/gislickline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_gislickline_ops_data(request, id):  
    gislickline_ops_data = GISlicklineOperation.objects.get(id=id) 
    ctid =(gislickline_ops_data.gislickline).pk    
    form = GISlicklineOpsForm(request.POST or None, instance=gislickline_ops_data)    
    if request.method =="POST":
        form = GISlicklineOpsForm(request.POST, request.FILES, instance=gislickline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' gislicklineoperations:list_ lickline_ops_data', ctid)
    return render (request, ' gislicklineoperations/ gislickline_ops_data_form.html', {'form': form, 'gislickline_ops_data':gislickline_ops_data, 'id':id})

def delete_gislickline_ops_data(request, id):
    gislickline_ops_data = GISlicklineOperation.objects.get(id=id)  
    ctid =(gislickline_ops_data.gislickline).pk
    print(ctid) 
    if request.method == 'POST' :
        gislickline_ops_data.delete()
        return redirect ('gislicklineoperations:list_gislickline_ops_data', ctid)
    return render (request, 'gislicklineoperations/gislickline_ops_data_confirm_delete.html', {'gislickline_ops_data':gislickline_ops_data, 'id':id})




