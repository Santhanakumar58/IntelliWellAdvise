from django.shortcuts import render, redirect
from selectedGasProducer.models import SelectedGasProducer
from gprigless.models import GPRigless
from .models import GPRiglessOperation
from .forms import GPRiglessOpsForm

def list_gprigless_ops_data(request, ctid):     
    selectedwell = SelectedGasProducer.objects.first()   
    gprigless_ops_datas = GPRiglessOperation.objects.filter(wellid = selectedwell.wellid, gprigless =ctid).all()  
    return render (request, 'gpriglessoperations/gprigless_ops_data.html', {'gprigless_ops_datas': gprigless_ops_datas,'ctid':ctid})   
 
def create_gprigless_ops_data(request, ctid): 
    print(ctid)
    gprigless_data = GPRigless.objects.get(id=ctid)
    gprigless_ops_data = GPRiglessOperation()   
    gprigless_ops_data.gprigless =gprigless_data
    gprigless_ops_data.fgid = gprigless_data.fgid
    gprigless_ops_data.wellid = gprigless_data.wellid   
    form = GPRiglessOpsForm(request.POST or None, instance=gprigless_ops_data)
    if request.method =="POST":  
         form = GPRiglessOpsForm(request.POST, instance=gprigless_ops_data)       
         gprigless_ops_data.fgid = gprigless_data.fgid
         gprigless_ops_data.wellid = gprigless_data.wellid   
         gprigless_ops_data.gprigless =gprigless_data                  
         if form.is_valid():
            form.save()  
            return redirect ('gpriglessoperations:list_gprigless_ops_data', ctid) 
    return render (request, 'gpriglessoperations/gprigless_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_gprigless_ops_data(request, id):  
    gprigless_ops_data = GPRiglessOperation.objects.get(id=id) 
    ctid =(gprigless_ops_data.gprigless).pk    
    form = GPRiglessOpsForm(request.POST or None, instance=gprigless_ops_data)    
    if request.method =="POST":
        form = GPRiglessOpsForm(request.POST, request.FILES, instance=gprigless_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('gpriglessoperations:list_gprigless_ops_data', ctid)
    return render (request, 'gpriglessoperations/gprigless_ops_data_form.html', {'form': form, 'gprigless_ops_data':gprigless_ops_data, 'id':id})

def delete_gprigless_ops_data(request, id):
    gprigless_ops_data = GPRiglessOperation.objects.get(id=id)  
    ctid =(gprigless_ops_data.gprigless).pk
    print(ctid) 
    if request.method == 'POST' :
        gprigless_ops_data.delete()
        return redirect ('gpriglessoperations:list_gprigless_ops_data', ctid)
    return render (request, 'gpriglessoperations/gprigless_ops_data_confirm_delete.html', {'gprigless_ops_data':gprigless_ops_data, 'id':id})



