from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedWaterInjector.models import SelectedWaterInjector
from .models import WICementBondLogModel
from .forms import WICementBondLogForm


def list_wicementbondlog(request, id):
    selectedwell = SelectedWaterInjector.objects.first()   
    wicementbondlogs = WICementBondLogModel.objects.filter(wellid =selectedwell.wellid , casingSize_id = id).all()    
    return render (request, 'wicementbondlogs/wicementbondlog.html', {'wicementbondlogs': wicementbondlogs,'id':id })   

def create_wicementbondlog(request, id): 
   wicementbondlog = WICementBondLogModel()
   selectedwell = SelectedWaterInjector.objects.first()  
   wicementbondlog.fgid = selectedwell.fgid
   wicementbondlog.wellid = selectedwell.wellid
   wicementbondlog.casingSize_id =id
   form = WICementBondLogForm(request.POST or None, instance=wicementbondlog)
   if request.method =="POST":
        selectedwell = SelectedWaterInjector.objects.first()
        wicementbondlog = WICementBondLogModel()
        wicementbondlog.fgid = selectedwell.fgid
        wicementbondlog.wellid = selectedwell.wellid
        wicementbondlog.casingSize=request.POST.get('casingSize_id')
        wicementbondlog.analyst=request.POST.get('analyst')
        wicementbondlog.recorded_date=request.POST.get('recorded_date')
        wicementbondlog.interpretation = request.POST.get('interpretation')        
        form = WICementBondLogForm(request.POST, request.FILES, instance=wicementbondlog)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance
            id=wicementbondlog.casingSize_id
            return redirect ('wicementbondlogs:list_wicementbondlog', wicementbondlog.casingSize_id) 
        else :
             wicementbondlog = WICementBondLogModel()
             selectedwell = SelectedWaterInjector.objects.first()  
             wicementbondlog.fgid = selectedwell.fgid
             wicementbondlog.wellid = selectedwell.wellid
             wicementbondlog.casingSize_id =id
             form = WICementBondLogForm(request.POST or None, instance=wicementbondlog)          
   return render (request, 'wicementbondlogs/wicementbondlog_form.html', {'form': form, 'id':id})

def update_wicementbondlog(request, id):   
   wicementbondlog = WICementBondLogModel.objects.get(id=id)
   form = WICementBondLogForm(request.POST or None, instance=wicementbondlog)
   if request.method =="POST":
        form = WICementBondLogForm(request.POST, request.FILES, instance=wicementbondlog)
        if form.is_valid():
            form.save()                        
            return redirect ('wicementbondlogs:list_wicementbondlog', wicementbondlog.casingSize_id)
   return render (request, 'wicementbondlogs/wicementbondlog_form.html', {'form': form, 'wicementbondlog':wicementbondlog, 'id': wicementbondlog.casingSize_id })

def delete_wicementbondlog(request, id):   
   wicementbondlog = WICementBondLogModel.objects.get(id=id)   
   if request.method == 'POST' :
       wicementbondlog.delete()
       return redirect ('wicementbondlogs:list_wicementbondlog', wicementbondlog.casingSize_id)
   return render (request, 'wicementbondlogs/wicementbondlog_confirm_delete.html', {'wicementbondlog':wicementbondlog})



