from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from .models import CementBondLogModel
from .forms import CementBondLogForm
from casings.models import CasingModel, CasingSizeModel
from selectedOilProducer.models import SelectedOilProducer

def list_cementbondlog(request, cid):      
    print(cid) 
    cementbondlogs = CementBondLogModel.objects.filter(casingModelid= cid)       
    return render (request, 'cementbondlogs/cementbondlog.html', {'cementbondlogs': cementbondlogs,'cid':cid })   

def create_cementbondlog(request, cid): 
   print(cid)
   cementbondlog = CementBondLogModel()
   selectedcasing = CasingModel.objects.get(id=cid) 
   cementbondlog.fgid = selectedcasing.fgid
   cementbondlog.wellid = selectedcasing.wellid
   cementbondlog.casingSize_id =selectedcasing.casingSize_id
   cementbondlog.casingModelid =cid
   form = CementBondLogForm(request.POST or None, instance=cementbondlog)
   if request.method =="POST":
        selectedwell = SelectedOilProducer.objects.first()
        cementbondlog = CementBondLogModel()
        cementbondlog.fgid = selectedwell.fgid
        cementbondlog.wellid = selectedwell.wellid
        cementbondlog.casingModelid =cid
        cementbondlog.casingSize=request.POST.get('casingSize_id')
        cementbondlog.analyst=request.POST.get('analyst')
        cementbondlog.recorded_date=request.POST.get('recorded_date')
        cementbondlog.interpretation = request.POST.get('interpretation') 
        cementbondlog.cblImage = request.POST.get('cblImage') 
        print(cementbondlog.cblImage)       
        form = CementBondLogForm(request.POST, request.FILES, instance=cementbondlog)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance
            id=cementbondlog.casingSize_id
            return redirect ('cementbondlogs:list_cementbondlog', cid) 
        else :
             cementbondlog = CementBondLogModel()
             selectedwell = SelectedOilProducer.objects.first()  
             cementbondlog.fgid = selectedwell.fgid
             cementbondlog.wellid = selectedwell.wellid
             cementbondlog.casingSize_id =id
             form = CementBondLogForm(request.POST or None, instance=cementbondlog)          
   return render (request, 'cementbondlogs/cementbondlog_form.html', {'form': form, 'cid':cid})

def update_cementbondlog(request, id):   
   cementbondlog = CementBondLogModel.objects.get(id=id)
   cid = cementbondlog.casingModelid
   form = CementBondLogForm(request.POST or None, instance=cementbondlog)
   if request.method =="POST":
        form = CementBondLogForm(request.POST, request.FILES, instance=cementbondlog)
        if form.is_valid():
            cid = form.casingModelid
            form.save()                        
            return redirect ('cementbondlogs:list_cementbondlog', cid)
   return render (request, 'cementbondlogs/cementbondlog_form.html', {'form': form, 'cementbondlog':cementbondlog, 'id': id})

def delete_cementbondlog(request, id):   
   cementbondlog = CementBondLogModel.objects.get(id=id)   
   if request.method == 'POST' :
       cid = cementbondlog.casingModelid
       cementbondlog.delete()
       return redirect ('cementbondlogs:list_cementbondlog', cid)
   return render (request, 'cementbondlogs/cementbondlog_confirm_delete.html', {'cementbondlog':cementbondlog})

