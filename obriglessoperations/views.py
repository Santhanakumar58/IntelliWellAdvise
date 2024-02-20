from django.shortcuts import render, redirect
from selectedObserver.models import SelectedObserver
from obrigless.models import OBRigless
from .models import OBRiglessOperation
from .forms import OBRiglessOpsForm

def list_obrigless_ops_data(request, ctid):     
    selectedwell = SelectedObserver.objects.first()   
    obrigless_ops_datas = OBRiglessOperation.objects.filter(wellid = selectedwell.wellid, obrigless =ctid).all()  
    return render (request, 'obriglessoperations/obrigless_ops_data.html', {'obrigless_ops_datas': obrigless_ops_datas,'ctid':ctid})   
 
def create_obrigless_ops_data(request, ctid): 
    print(ctid)
    obrigless_data = OBRigless.objects.get(id=ctid)
    obrigless_ops_data = OBRiglessOperation()   
    obrigless_ops_data.obrigless =obrigless_data
    obrigless_ops_data.fgid = obrigless_data.fgid
    obrigless_ops_data.wellid = obrigless_data.wellid   
    form = OBRiglessOpsForm(request.POST or None, instance=obrigless_ops_data)
    if request.method =="POST":  
         form = OBRiglessOpsForm(request.POST, instance=obrigless_ops_data)       
         obrigless_ops_data.fgid = obrigless_data.fgid
         obrigless_ops_data.wellid = obrigless_data.wellid   
         obrigless_ops_data.obrigless =obrigless_data                  
         if form.is_valid():
            form.save()  
            return redirect ('obriglessoperations:list_obrigless_ops_data', ctid) 
    return render (request, 'obriglessoperations/obrigless_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_obrigless_ops_data(request, id):  
    obrigless_ops_data = OBRiglessOperation.objects.get(id=id) 
    ctid =(obrigless_ops_data.obrigless).pk    
    form = OBRiglessOpsForm(request.POST or None, instance=obrigless_ops_data)    
    if request.method =="POST":
        form = OBRiglessOpsForm(request.POST, request.FILES, instance=obrigless_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('obriglessoperations:list_obrigless_ops_data', ctid)
    return render (request, 'obriglessoperations/obrigless_ops_data_form.html', {'form': form, 'obrigless_ops_data':obrigless_ops_data, 'id':id})

def delete_obrigless_ops_data(request, id):
    obrigless_ops_data = OBRiglessOperation.objects.get(id=id)  
    ctid =(obrigless_ops_data.obrigless).pk
    print(ctid) 
    if request.method == 'POST' :
        obrigless_ops_data.delete()
        return redirect ('obriglessoperations:list_obrigless_ops_data', ctid)
    return render (request, 'obriglessoperations/obrigless_ops_data_confirm_delete.html', {'obrigless_ops_data':obrigless_ops_data, 'id':id})




