from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedWaterInjector.models import SelectedWaterInjector
from .models import WILogAnalysisModel
from .forms import WILogAnalysisForm
 

def list_wiloganalysis(request):
    selectedwell = SelectedWaterInjector.objects.first()  
    print(selectedwell.wellid) 
    logs = WILogAnalysisModel.objects.filter(wiwellid =selectedwell.wellid).all()  
    print(logs)  
    return render (request, 'wiloganalysis/wiloganalysis.html', {'logs': logs })   

def create_wiloganalysis(request): 
   log = WILogAnalysisModel()
   selectedwell = SelectedWaterInjector.objects.first()  
   log.wifgid = selectedwell.fgid
   log.wiwellid = selectedwell.wellid    
   form = WILogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        selectedwell = SelectedWaterInjector.objects.first()
        log = WILogAnalysisModel()
        log.wifgid = selectedwell.fgid
        log.wiwellid = selectedwell.wellid
        log.wicasingSize=request.POST.get('casingSize')
        log.wianalyst=request.POST.get('analyst')
        log.wirecorded_date=request.POST.get('recorded_date')
        log.wiinterpretation = request.POST.get('interpretation')        
        form = WILogAnalysisForm(request.POST, request.FILES, instance=log)             
        if form.is_valid():       
            form.save()
            img_wij = form.instance            
            return redirect ('wiloganalysis:list_wiloganalysis') 
        else :
             log = WILogAnalysisModel()
             selectedwell = SelectedWaterInjector.objects.first()  
             log.wifgid = selectedwell.fgid
             log.wiwellid = selectedwell.wellid
             form = WILogAnalysisForm(request.POST or None, instance=log)          
   return render (request, 'wiloganalysis/wiloganalysis_form.html', {'form': form, 'id':id})

def update_wiloganalysis(request, id):   
   log = WILogAnalysisModel.objects.get(id=id)
   form = WILogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        form = WILogAnalysisForm(request.POST, request.FILES, instance=log)
        if form.is_valid():
            form.save()
            img_wij = form.instance
            return redirect ('wiloganalysis:list_wiloganalysis')
   return render (request, 'wiloganalysis/wiloganalysis_form.html', {'form': form, 'log':log})

def delete_wiloganalysis(request, id):   
   log = WILogAnalysisModel.objects.get(id=id)   
   if request.method == 'POST' :
       log.delete()
       return redirect ('wiloganalysis:list_wiloganalysis')
   return render (request, 'wiloganalysis/wiloganalysis_confirm_delete.html', {'log':log})




