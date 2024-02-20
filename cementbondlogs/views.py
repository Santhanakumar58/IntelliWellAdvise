from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from .models import CementBondLogModel
from .forms import CementBondLogForm
from selectedOilProducer.models import SelectedOilProducer

def list_cementbondlog(request, id):
    selectedwell = SelectedOilProducer.objects.first()   
    cementbondlogs = CementBondLogModel.objects.filter(wellid =selectedwell.wellid , casingSize_id = id).all()    
    return render (request, 'cementbondlogs/cementbondlog.html', {'cementbondlogs': cementbondlogs,'id':id })   

def create_cementbondlog(request, id): 
   cementbondlog = CementBondLogModel()
   selectedwell = SelectedOilProducer.objects.first()  
   cementbondlog.fgid = selectedwell.fgid
   cementbondlog.wellid = selectedwell.wellid
   cementbondlog.casingSize_id =id
   form = CementBondLogForm(request.POST or None, instance=cementbondlog)
   if request.method =="POST":
        selectedwell = SelectedOilProducer.objects.first()
        cementbondlog = CementBondLogModel()
        cementbondlog.fgid = selectedwell.fgid
        cementbondlog.wellid = selectedwell.wellid
        cementbondlog.casingSize=request.POST.get('casingSize_id')
        cementbondlog.analyst=request.POST.get('analyst')
        cementbondlog.recorded_date=request.POST.get('recorded_date')
        cementbondlog.interpretation = request.POST.get('interpretation')        
        form = CementBondLogForm(request.POST, request.FILES, instance=cementbondlog)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance
            id=cementbondlog.casingSize_id
            return redirect ('cementbondlogs:list_cementbondlog', cementbondlog.casingSize_id) 
        else :
             cementbondlog = CementBondLogModel()
             selectedwell = SelectedOilProducer.objects.first()  
             cementbondlog.fgid = selectedwell.fgid
             cementbondlog.wellid = selectedwell.wellid
             cementbondlog.casingSize_id =id
             form = CementBondLogForm(request.POST or None, instance=cementbondlog)          
   return render (request, 'cementbondlogs/cementbondlog_form.html', {'form': form, 'id':id})

def update_cementbondlog(request, id):   
   cementbondlog = CementBondLogModel.objects.get(id=id)
   form = CementBondLogForm(request.POST or None, instance=cementbondlog)
   if request.method =="POST":
        form = CementBondLogForm(request.POST, request.FILES, instance=cementbondlog)
        if form.is_valid():
            form.save()                        
            return redirect ('cementbondlogs:list_cementbondlog', cementbondlog.casingSize_id)
   return render (request, 'cementbondlogs/cementbondlog_form.html', {'form': form, 'cementbondlog':cementbondlog, 'id': cementbondlog.casingSize_id })

def delete_cementbondlog(request, id):   
   cementbondlog = CementBondLogModel.objects.get(id=id)   
   if request.method == 'POST' :
       cementbondlog.delete()
       return redirect ('cementbondlogs:list_cementbondlog', cementbondlog.casingSize_id)
   return render (request, 'cementbondlogs/cementbondlog_confirm_delete.html', {'cementbondlog':cementbondlog})

