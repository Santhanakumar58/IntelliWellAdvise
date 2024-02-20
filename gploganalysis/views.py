from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedGasProducer.models import SelectedGasProducer
from .models import GPLogAnalysisModel
from .forms import GPLogAnalysisForm
 

def list_gploganalysis(request):
    selectedwell = SelectedGasProducer.objects.first()  
    print(selectedwell.wellid) 
    logs = GPLogAnalysisModel.objects.filter(gpwellid =selectedwell.wellid).all()  
    print(logs)  
    return render (request, 'gploganalysis/gploganalysis.html', {'logs': logs })   

def create_gploganalysis(request): 
   log = GPLogAnalysisModel()
   selectedwell = SelectedGasProducer.objects.first()  
   log.gpfgid = selectedwell.fgid
   log.gpwellid = selectedwell.wellid    
   form = GPLogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        selectedwell = SelectedGasProducer.objects.first()
        log = GPLogAnalysisModel()
        log.gpfgid = selectedwell.fgid
        log.gpwellid = selectedwell.wellid
        log.gpcasingSize=request.POST.get('casingSize')
        log.gpanalyst=request.POST.get('analyst')
        log.gprecorded_date=request.POST.get('recorded_date')
        log.gpinterpretation = request.POST.get('interpretation')        
        form = GPLogAnalysisForm(request.POST, request.FILES, instance=log)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance            
            return redirect ('gploganalysis:list_gploganalysis') 
        else :
             log = GPLogAnalysisModel()
             selectedwell = SelectedGasProducer.objects.first()  
             log.gpfgid = selectedwell.fgid
             log.gpwellid = selectedwell.wellid
             form = GPLogAnalysisForm(request.POST or None, instance=log)          
   return render (request, 'gploganalysis/gploganalysis_form.html', {'form': form, 'id':id})

def update_gploganalysis(request, id):   
   log = GPLogAnalysisModel.objects.get(id=id)
   form = GPLogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        form = GPLogAnalysisForm(request.POST, request.FILES, instance=log)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect ('gploganalysis:list_gploganalysis')
   return render (request, 'gploganalysis/gploganalysis_form.html', {'form': form, 'log':log})

def delete_gploganalysis(request, id):   
   log = GPLogAnalysisModel.objects.get(id=id)   
   if request.method == 'POST' :
       log.delete()
       return redirect ('gploganalysis:list_gploganalysis')
   return render (request, 'gploganalysis/gploganalysis_confirm_delete.html', {'log':log})



