from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedGasInjector.models import SelectedGasInjector
from .models import GICementBondLogModel
from .forms import GICementBondLogForm


def list_gicementbondlog(request, id):
    selectedwell = SelectedGasInjector.objects.first()   
    gicementbondlogs = GICementBondLogModel.objects.filter(wellid =selectedwell.wellid , casingSize_id = id).all()    
    return render (request, 'gicementbondlogs/gicementbondlog.html', {'gicementbondlogs': gicementbondlogs,'id':id })   

def create_gicementbondlog(request, id): 
   gicementbondlog = GICementBondLogModel()
   selectedwell = SelectedGasInjector.objects.first()  
   gicementbondlog.fgid = selectedwell.fgid
   gicementbondlog.wellid = selectedwell.wellid
   gicementbondlog.casingSize_id =id
   form = GICementBondLogForm(request.POST or None, instance=gicementbondlog)
   if request.method =="POST":
        selectedwell = SelectedGasInjector.objects.first()
        gicementbondlog = GICementBondLogModel()
        gicementbondlog.fgid = selectedwell.fgid
        gicementbondlog.wellid = selectedwell.wellid
        gicementbondlog.casingSize=request.POST.get('casingSize_id')
        gicementbondlog.analyst=request.POST.get('analyst')
        gicementbondlog.recorded_date=request.POST.get('recorded_date')
        gicementbondlog.interpretation = request.POST.get('interpretation')        
        form = GICementBondLogForm(request.POST, request.FILES, instance=gicementbondlog)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance
            id=gicementbondlog.casingSize_id
            return redirect ('gicementbondlogs:list_gicementbondlog', gicementbondlog.casingSize_id) 
        else :
             gicementbondlog = GICementBondLogModel()
             selectedwell = SelectedGasInjector.objects.first()  
             gicementbondlog.fgid = selectedwell.fgid
             gicementbondlog.wellid = selectedwell.wellid
             gicementbondlog.casingSize_id =id
             form = GICementBondLogForm(request.POST or None, instance=gicementbondlog)          
   return render (request, 'gicementbondlogs/gicementbondlog_form.html', {'form': form, 'id':id})

def update_gicementbondlog(request, id):   
   gicementbondlog = GICementBondLogModel.objects.get(id=id)
   form = GICementBondLogForm(request.POST or None, instance=gicementbondlog)
   if request.method =="POST":
        form = GICementBondLogForm(request.POST, request.FILES, instance=gicementbondlog)
        if form.is_valid():
            form.save()                        
            return redirect ('gicementbondlogs:list_gicementbondlog', gicementbondlog.casingSize_id)
   return render (request, 'gicementbondlogs/gicementbondlog_form.html', {'form': form, 'gicementbondlog':gicementbondlog, 'id': gicementbondlog.casingSize_id })

def delete_gicementbondlog(request, id):   
   gicementbondlog = GICementBondLogModel.objects.get(id=id)   
   if request.method == 'POST' :
       gicementbondlog.delete()
       return redirect ('gicementbondlogs:list_gicementbondlog', gicementbondlog.casingSize_id)
   return render (request, 'gicementbondlogs/gicementbondlog_confirm_delete.html', {'gicementbondlog':gicementbondlog})



