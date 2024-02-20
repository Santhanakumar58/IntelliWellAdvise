from django.shortcuts import render, redirect
from selectedObserver.models import SelectedObserver
from obslickline.models import OBSlickline
from .models import OBSlicklineOperation
from .forms import OBSlicklineOpsForm

def list_obslickline_ops_data(request, ctid):     
    selectedwell = SelectedObserver.objects.first()   
    obslickline_ops_datas = OBSlicklineOperation.objects.filter(obwellid = selectedwell.wellid, obslickline =ctid).all()  
    return render (request, 'obslicklineoperations/obslickline_ops_data.html', {'obslickline_ops_datas': obslickline_ops_datas,'ctid':ctid})   
 
def create_obslickline_ops_data(request, ctid): 
    obslickline_data = OBSlickline.objects.get(id=ctid)
    obslickline_ops_data = OBSlicklineOperation()   
    obslickline_ops_data.obslickline =obslickline_data.pk
    obslickline_ops_data.fgid = obslickline_data.fgid
    obslickline_ops_data.wellid = obslickline_data.wellid   
    form = OBSlicklineOpsForm(request.POST or None, instance=obslickline_ops_data)
    if request.method =="POST":  
         form = OBSlicklineOpsForm(request.POST, instance=obslickline_ops_data)       
         obslickline_ops_data.fgid = obslickline_data.fgid
         obslickline_ops_data.wellid = obslickline_data.wellid   
         obslickline_ops_data.obslickline =obslickline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('obslicklineoperations:list_obslickline_ops_data', ctid) 
    return render (request, 'obslicklineoperations/obslickline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_obslickline_ops_data(request, id):  
    obslickline_ops_data = OBSlicklineOperation.objects.get(id=id) 
    ctid =(obslickline_ops_data.obslickline).pk    
    form = OBSlicklineOpsForm(request.POST or None, instance=obslickline_ops_data)    
    if request.method =="POST":
        form = OBSlicklineOpsForm(request.POST, request.FILES, instance=obslickline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' obslicklineoperations:list_ lickline_ops_data', ctid)
    return render (request, ' obslicklineoperations/ obslickline_ops_data_form.html', {'form': form, 'obslickline_ops_data':obslickline_ops_data, 'id':id})

def delete_obslickline_ops_data(request, id):
    obslickline_ops_data = OBSlicklineOperation.objects.get(id=id)  
    ctid =(obslickline_ops_data.obslickline).pk
    print(ctid) 
    if request.method == 'POST' :
        obslickline_ops_data.delete()
        return redirect ('obslicklineoperations:list_obslickline_ops_data', ctid)
    return render (request, 'obslicklineoperations/obslickline_ops_data_confirm_delete.html', {'obslickline_ops_data':obslickline_ops_data, 'id':id})




