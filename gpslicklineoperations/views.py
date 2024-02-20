from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from gpslickline.models import GPSlickline
from .models import GPSlicklineOperation
from .forms import GPSlicklineOpsForm

def list_gpslickline_ops_data(request, ctid):     
    selectedwell = SelectedOilProducer.objects.first()   
    gpslickline_ops_datas = GPSlicklineOperation.objects.filter(gpwellid = selectedwell.wellid, gpslickline =ctid).all()  
    return render (request, 'gpslicklineoperations/gpslickline_ops_data.html', {'gpslickline_ops_datas': gpslickline_ops_datas,'ctid':ctid})   
 
def create_gpslickline_ops_data(request, ctid): 
    gpslickline_data = GPSlickline.objects.get(id=ctid)
    gpslickline_ops_data = GPSlicklineOperation()   
    gpslickline_ops_data.gpslickline =gpslickline_data.pk
    gpslickline_ops_data.fgid = gpslickline_data.fgid
    gpslickline_ops_data.wellid = gpslickline_data.wellid   
    form = GPSlicklineOpsForm(request.POST or None, instance=gpslickline_ops_data)
    if request.method =="POST":  
         form = GPSlicklineOpsForm(request.POST, instance=gpslickline_ops_data)       
         gpslickline_ops_data.fgid = gpslickline_data.fgid
         gpslickline_ops_data.wellid = gpslickline_data.wellid   
         gpslickline_ops_data.gpslickline =gpslickline_data.pk                   
         if form.is_valid():
            form.save()  
            return redirect ('gpslicklineoperations:list_gpslickline_ops_data', ctid) 
    return render (request, 'gpslicklineoperations/gpslickline_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_gpslickline_ops_data(request, id):  
    gpslickline_ops_data = GPSlicklineOperation.objects.get(id=id) 
    ctid =(gpslickline_ops_data.gpslickline).pk    
    form = GPSlicklineOpsForm(request.POST or None, instance=gpslickline_ops_data)    
    if request.method =="POST":
        form = GPSlicklineOpsForm(request.POST, request.FILES, instance=gpslickline_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect (' gpslicklineoperations:list_ lickline_ops_data', ctid)
    return render (request, ' gpslicklineoperations/ gpslickline_ops_data_form.html', {'form': form, 'gpslickline_ops_data':gpslickline_ops_data, 'id':id})

def delete_gpslickline_ops_data(request, id):
    gpslickline_ops_data = GPSlicklineOperation.objects.get(id=id)  
    ctid =(gpslickline_ops_data.gpslickline).pk
    print(ctid) 
    if request.method == 'POST' :
        gpslickline_ops_data.delete()
        return redirect ('gpslicklineoperations:list_gpslickline_ops_data', ctid)
    return render (request, 'gpslicklineoperations/gpslickline_ops_data_confirm_delete.html', {'gpslickline_ops_data':gpslickline_ops_data, 'id':id})



