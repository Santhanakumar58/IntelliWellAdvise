from django.shortcuts import render, redirect
from selectedGasInjector.models import SelectedGasInjector
from girigless.models import GIRigless
from .models import GIRiglessOperation
from .forms import GIRiglessOpsForm

def list_girigless_ops_data(request, ctid):     
    selectedwell = SelectedGasInjector.objects.first()   
    girigless_ops_datas = GIRiglessOperation.objects.filter(wellid = selectedwell.wellid, girigless =ctid).all()  
    return render (request, 'giriglessoperations/girigless_ops_data.html', {'girigless_ops_datas': girigless_ops_datas,'ctid':ctid})   
 
def create_girigless_ops_data(request, ctid): 
    print(ctid)
    girigless_data = GIRigless.objects.get(id=ctid)
    girigless_ops_data = GIRiglessOperation()   
    girigless_ops_data.girigless =girigless_data
    girigless_ops_data.fgid = girigless_data.fgid
    girigless_ops_data.wellid = girigless_data.wellid   
    form = GIRiglessOpsForm(request.POST or None, instance=girigless_ops_data)
    if request.method =="POST":  
         form = GIRiglessOpsForm(request.POST, instance=girigless_ops_data)       
         girigless_ops_data.fgid = girigless_data.fgid
         girigless_ops_data.wellid = girigless_data.wellid   
         girigless_ops_data.girigless =girigless_data                  
         if form.is_valid():
            form.save()  
            return redirect ('giriglessoperations:list_girigless_ops_data', ctid) 
    return render (request, 'giriglessoperations/girigless_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_girigless_ops_data(request, id):  
    girigless_ops_data = GIRiglessOperation.objects.get(id=id) 
    ctid =(girigless_ops_data.girigless).pk    
    form = GIRiglessOpsForm(request.POST or None, instance=girigless_ops_data)    
    if request.method =="POST":
        form = GIRiglessOpsForm(request.POST, request.FILES, instance=girigless_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('giriglessoperations:list_girigless_ops_data', ctid)
    return render (request, 'giriglessoperations/girigless_ops_data_form.html', {'form': form, 'girigless_ops_data':girigless_ops_data, 'id':id})

def delete_girigless_ops_data(request, id):
    girigless_ops_data = GIRiglessOperation.objects.get(id=id)  
    ctid =(girigless_ops_data.girigless).pk
    print(ctid) 
    if request.method == 'POST' :
        girigless_ops_data.delete()
        return redirect ('giriglessoperations:list_girigless_ops_data', ctid)
    return render (request, 'giriglessoperations/girigless_ops_data_confirm_delete.html', {'girigless_ops_data':girigless_ops_data, 'id':id})




