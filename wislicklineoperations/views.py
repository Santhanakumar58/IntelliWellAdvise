from django.shortcuts import render, redirect
from selectedWaterInjector.models import SelectedWaterInjector
from wislickline.models import WISlickline
from .models import WISlicklineOperation
from .forms import WISlicklineOpsForm

def list_wislickline_ops_data(request, ctid):     
    selectedwell = SelectedWaterInjector.objects.first()   
    wislickline_ops_datas = WISlicklineOperation.objects.filter(wellid = selectedwell.wellid, wislickline =ctid).all()  
    return render (request, 'wislicklineoperations/wislickline_ops_data.html', {'wislickline_ops_datas': wislickline_ops_datas,'ctid':ctid})   
 
def create_wislickline_ops_data(request, ctid): 
    wislickline_data = WISlickline.objects.get(id=ctid)
    wislickline_ops_data = WISlicklineOperation()   
    wislickline_ops_data.wislickline =wislickline_data.pk
    wislickline_ops_data.fgid = wislickline_data.fgid
    wislickline_ops_data.wellid = wislickline_data.wellid   
    form = WISlicklineOpsForm(request.POST or None, instance=wislickline_ops_data)
    if request.method =="POST":  
         form = WISlicklineOpsForm(request.POST, instance=wislickline_ops_data)       
         wislickline_ops_data.fgid = wislickline_data.fgid
         wislickline_ops_data.wellid = wislickline_data.wellid   
         wislickline_ops_data.wislickline =wislickline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('wislicklineoperations:list_wislickline_ops_data', ctid) 
    return render (request, 'wislicklineoperations/wislickline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_wislickline_ops_data(request, id):  
    wislickline_ops_data = WISlicklineOperation.objects.get(id=id) 
    ctid =(wislickline_ops_data.wislickline).pk    
    form = WISlicklineOpsForm(request.POST or None, instance=wislickline_ops_data)    
    if request.method =="POST":
        form = WISlicklineOpsForm(request.POST, request.FILES, instance=wislickline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' wislicklineoperations:list_ lickline_ops_data', ctid)
    return render (request, ' wislicklineoperations/ wislickline_ops_data_form.html', {'form': form, 'wislickline_ops_data':wislickline_ops_data, 'id':id})

def delete_wislickline_ops_data(request, id):
    wislickline_ops_data = WISlicklineOperation.objects.get(id=id)  
    ctid =(wislickline_ops_data.wislickline).pk
    print(ctid) 
    if request.method == 'POST' :
        wislickline_ops_data.delete()
        return redirect ('wislicklineoperations:list_wislickline_ops_data', ctid)
    return render (request, 'wislicklineoperations/wislickline_ops_data_confirm_delete.html', {'wislickline_ops_data':wislickline_ops_data, 'id':id})



