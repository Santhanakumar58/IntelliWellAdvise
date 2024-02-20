from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from .models import LogAnalysisModel
from .forms import LogAnalysisForm
from selectedOilProducer.models import SelectedOilProducer

def list_loganalysis(request):
    selectedwell = SelectedOilProducer.objects.first()  
    print(selectedwell.wellid) 
    logs = LogAnalysisModel.objects.filter(wellid =selectedwell.wellid).all()  
    print(logs)  
    return render (request, 'loganalysis/loganalysis.html', {'logs': logs })   

def create_loganalysis(request): 
   log = LogAnalysisModel()
   selectedwell = SelectedOilProducer.objects.first()  
   log.fgid = selectedwell.fgid
   log.wellid = selectedwell.wellid    
   form = LogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        selectedwell = SelectedOilProducer.objects.first()
        log = LogAnalysisModel()
        log.fgid = selectedwell.fgid
        log.wellid = selectedwell.wellid
        log.casingSize=request.POST.get('casingSize')
        log.analyst=request.POST.get('analyst')
        log.recorded_date=request.POST.get('recorded_date')
        log.interpretation = request.POST.get('interpretation')        
        form = LogAnalysisForm(request.POST, request.FILES, instance=log)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance            
            return redirect ('loganalysis:list_loganalysis') 
        else :
             log = LogAnalysisModel()
             selectedwell = SelectedOilProducer.objects.first()  
             log.fgid = selectedwell.fgid
             log.wellid = selectedwell.wellid
             form = LogAnalysisForm(request.POST or None, instance=log)          
   return render (request, 'loganalysis/loganalysis_form.html', {'form': form, 'id':id})

def update_loganalysis(request, id):   
   log = LogAnalysisModel.objects.get(id=id)
   form = LogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        form = LogAnalysisForm(request.POST, request.FILES, instance=log)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect ('loganalysis:list_loganalysis')
   return render (request, 'loganalysis/loganalysis_form.html', {'form': form, 'log':log})

def delete_loganalysis(request, id):   
   log = LogAnalysisModel.objects.get(id=id)   
   if request.method == 'POST' :
       log.delete()
       return redirect ('loganalysis:list_loganalysis')
   return render (request, 'loganalysis/loganalysis_confirm_delete.html', {'log':log})


