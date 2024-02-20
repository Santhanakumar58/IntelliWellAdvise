from django.shortcuts import render, redirect
from selectedWaterInjector.models import SelectedWaterInjector
from wirigless.models import WIRigless
from .models import WIRiglessOperation
from .forms import WIRiglessOpsForm

def list_wirigless_ops_data(request, ctid):     
    selectedwell = SelectedWaterInjector.objects.first()   
    wirigless_ops_datas = WIRiglessOperation.objects.filter(wellid = selectedwell.wellid, wirigless =ctid).all()  
    return render (request, 'wiriglessoperations/wirigless_ops_data.html', {'wirigless_ops_datas': wirigless_ops_datas,'ctid':ctid})   
 
def create_wirigless_ops_data(request, ctid): 
    print(ctid)
    wirigless_data = WIRigless.objects.get(id=ctid)
    wirigless_ops_data = WIRiglessOperation()   
    wirigless_ops_data.wirigless =wirigless_data
    wirigless_ops_data.fgid = wirigless_data.fgid
    wirigless_ops_data.wellid = wirigless_data.wellid   
    form = WIRiglessOpsForm(request.POST or None, instance=wirigless_ops_data)
    if request.method =="POST":  
         form = WIRiglessOpsForm(request.POST, instance=wirigless_ops_data)       
         wirigless_ops_data.fgid = wirigless_data.fgid
         wirigless_ops_data.wellid = wirigless_data.wellid   
         wirigless_ops_data.wirigless =wirigless_data                  
         if form.is_valid():
            form.save()  
            return redirect ('wiriglessoperations:list_wirigless_ops_data', ctid) 
    return render (request, 'wiriglessoperations/wirigless_ops_data_form.html', {'form': form, 'ctid':ctid})

def update_wirigless_ops_data(request, id):  
    wirigless_ops_data = WIRiglessOperation.objects.get(id=id) 
    ctid =(wirigless_ops_data.wirigless).pk    
    form = WIRiglessOpsForm(request.POST or None, instance=wirigless_ops_data)    
    if request.method =="POST":
        form = WIRiglessOpsForm(request.POST, request.FILES, instance=wirigless_ops_data)        
        if form.is_valid():
            form.save() 
            return redirect ('wiriglessoperations:list_wirigless_ops_data', ctid)
    return render (request, 'wiriglessoperations/wirigless_ops_data_form.html', {'form': form, 'wirigless_ops_data':wirigless_ops_data, 'id':id})

def delete_wirigless_ops_data(request, id):
    wirigless_ops_data = WIRiglessOperation.objects.get(id=id)  
    ctid =(wirigless_ops_data.wirigless).pk
    print(ctid) 
    if request.method == 'POST' :
        wirigless_ops_data.delete()
        return redirect ('wiriglessoperations:list_wirigless_ops_data', ctid)
    return render (request, 'wiriglessoperations/wirigless_ops_data_confirm_delete.html', {'wirigless_ops_data':wirigless_ops_data, 'id':id})



