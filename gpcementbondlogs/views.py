from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedGasProducer.models import SelectedGasProducer
from .models import GPCementBondLogModel
from .forms import GPCementBondLogForm


def list_gpcementbondlog(request, id):
    selectedwell = SelectedGasProducer.objects.first()   
    gpcementbondlogs = GPCementBondLogModel.objects.filter(wellid =selectedwell.wellid , casingSize_id = id).all()    
    return render (request, 'gpcementbondlogs/gpcementbondlog.html', {'gpcementbondlogs': gpcementbondlogs,'id':id })   

def create_gpcementbondlog(request, id): 
   gpcementbondlog = GPCementBondLogModel()
   selectedwell = SelectedGasProducer.objects.first()  
   gpcementbondlog.fgid = selectedwell.fgid
   gpcementbondlog.wellid = selectedwell.wellid
   gpcementbondlog.casingSize_id =id
   form = GPCementBondLogForm(request.POST or None, instance=gpcementbondlog)
   if request.method =="POST":
        selectedwell = SelectedGasProducer.objects.first()
        gpcementbondlog = GPCementBondLogModel()
        gpcementbondlog.fgid = selectedwell.fgid
        gpcementbondlog.wellid = selectedwell.wellid
        gpcementbondlog.casingSize=request.POST.get('casingSize_id')
        gpcementbondlog.analyst=request.POST.get('analyst')
        gpcementbondlog.recorded_date=request.POST.get('recorded_date')
        gpcementbondlog.interpretation = request.POST.get('interpretation')        
        form = GPCementBondLogForm(request.POST, request.FILES, instance=gpcementbondlog)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance
            id=gpcementbondlog.casingSize_id
            return redirect ('gpcementbondlogs:list_gpcementbondlog', gpcementbondlog.casingSize_id) 
        else :
             gpcementbondlog = GPCementBondLogModel()
             selectedwell = SelectedGasProducer.objects.first()  
             gpcementbondlog.fgid = selectedwell.fgid
             gpcementbondlog.wellid = selectedwell.wellid
             gpcementbondlog.casingSize_id =id
             form = GPCementBondLogForm(request.POST or None, instance=gpcementbondlog)          
   return render (request, 'gpcementbondlogs/gpcementbondlog_form.html', {'form': form, 'id':id})

def update_gpcementbondlog(request, id):   
   gpcementbondlog = GPCementBondLogModel.objects.get(id=id)
   form = GPCementBondLogForm(request.POST or None, instance=gpcementbondlog)
   if request.method =="POST":
        form = GPCementBondLogForm(request.POST, request.FILES, instance=gpcementbondlog)
        if form.is_valid():
            form.save()                        
            return redirect ('gpcementbondlogs:list_gpcementbondlog', gpcementbondlog.casingSize_id)
   return render (request, 'gpcementbondlogs/gpcementbondlog_form.html', {'form': form, 'gpcementbondlog':gpcementbondlog, 'id': gpcementbondlog.casingSize_id })

def delete_gpcementbondlog(request, id):   
   gpcementbondlog = GPCementBondLogModel.objects.get(id=id)   
   if request.method == 'POST' :
       gpcementbondlog.delete()
       return redirect ('gpcementbondlogs:list_gpcementbondlog', gpcementbondlog.casingSize_id)
   return render (request, 'gpcementbondlogs/gpcementbondlog_confirm_delete.html', {'gpcementbondlog':gpcementbondlog})


