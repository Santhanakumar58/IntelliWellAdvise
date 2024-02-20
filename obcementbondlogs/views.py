from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedGasProducer.models import SelectedGasProducer
from .models import OBCementBondLogModel
from .forms import OBCementBondLogForm


def list_obcementbondlog(request, id):
    selectedwell = SelectedGasProducer.objects.first()   
    obcementbondlogs = OBCementBondLogModel.objects.filter(obwellid =selectedwell.wellid , casingSize_id = id).all()    
    return render (request, 'obcementbondlogs/obcementbondlog.html', {'obcementbondlogs': obcementbondlogs,'id':id })   

def create_obcementbondlog(request, id): 
   obcementbondlog = OBCementBondLogModel()
   selectedwell = SelectedGasProducer.objects.first()  
   obcementbondlog.fgid = selectedwell.fgid
   obcementbondlog.wellid = selectedwell.wellid
   obcementbondlog.casingSize_id =id
   form = OBCementBondLogForm(request.POST or None, instance=obcementbondlog)
   if request.method =="POST":
        selectedwell = SelectedGasProducer.objects.first()
        obcementbondlog = OBCementBondLogModel()
        obcementbondlog.fgid = selectedwell.fgid
        obcementbondlog.wellid = selectedwell.wellid
        obcementbondlog.casingSize=request.POST.get('casingSize_id')
        obcementbondlog.analyst=request.POST.get('analyst')
        obcementbondlog.recorded_date=request.POST.get('recorded_date')
        obcementbondlog.interpretation = request.POST.get('interpretation')        
        form = OBCementBondLogForm(request.POST, request.FILES, instance=obcementbondlog)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance
            id=obcementbondlog.casingSize_id
            return redirect ('obcementbondlogs:list_obcementbondlog', obcementbondlog.casingSize_id) 
        else :
             obcementbondlog = OBCementBondLogModel()
             selectedwell = SelectedGasProducer.objects.first()  
             obcementbondlog.fgid = selectedwell.fgid
             obcementbondlog.wellid = selectedwell.wellid
             obcementbondlog.casingSize_id =id
             form = OBCementBondLogForm(request.POST or None, instance=obcementbondlog)          
   return render (request, 'obcementbondlogs/obcementbondlog_form.html', {'form': form, 'id':id})

def update_obcementbondlog(request, id):   
   obcementbondlog = OBCementBondLogModel.objects.get(id=id)
   form = OBCementBondLogForm(request.POST or None, instance=obcementbondlog)
   if request.method =="POST":
        form = OBCementBondLogForm(request.POST, request.FILES, instance=obcementbondlog)
        if form.is_valid():
            form.save()                        
            return redirect ('obcementbondlogs:list_obcementbondlog', obcementbondlog.casingSize_id)
   return render (request, 'obcementbondlogs/obcementbondlog_form.html', {'form': form, 'obcementbondlog':obcementbondlog, 'id': obcementbondlog.casingSize_id })

def delete_obcementbondlog(request, id):   
   obcementbondlog = OBCementBondLogModel.objects.get(id=id)   
   if request.method == 'POST' :
       obcementbondlog.delete()
       return redirect ('obcementbondlogs:list_obcementbondlog', obcementbondlog.casingSize_id)
   return render (request, 'obcementbondlogs/obcementbondlog_confirm_delete.html', {'obcementbondlog':obcementbondlog})



