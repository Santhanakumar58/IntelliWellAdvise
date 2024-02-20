from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedObserver.models import SelectedObserver
from .models import OBLogAnalysisModel
from .forms import OBLogAnalysisForm
 

def list_obloganalysis(request):
    selectedwell = SelectedObserver.objects.first()  
    print(selectedwell.wellid) 
    logs = OBLogAnalysisModel.objects.filter(obwellid =selectedwell.wellid).all()  
    print(logs)  
    return render (request, 'obloganalysis/obloganalysis.html', {'logs': logs })   

def create_obloganalysis(request): 
   log = OBLogAnalysisModel()
   selectedwell = SelectedObserver.objects.first()  
   log.fgid = selectedwell.fgid
   log.wellid = selectedwell.wellid    
   form = OBLogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        selectedwell = SelectedObserver.objects.first()
        log = OBLogAnalysisModel()
        log.obfgid = selectedwell.fgid
        log.obwellid = selectedwell.wellid
        log.obcasingSize=request.POST.get('casingSize')
        log.obanalyst=request.POST.get('analyst')
        log.obrecorded_date=request.POST.get('recorded_date')
        log.obinterpretation = request.POST.get('interpretation')        
        form = OBLogAnalysisForm(request.POST, request.FILES, instance=log)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance            
            return redirect ('obloganalysis:list_obloganalysis') 
        else :
             log = OBLogAnalysisModel()
             selectedwell = SelectedObserver.objects.first()  
             log.obfgid = selectedwell.fgid
             log.obwellid = selectedwell.wellid
             form = OBLogAnalysisForm(request.POST or None, instance=log)          
   return render (request, 'obloganalysis/obloganalysis_form.html', {'form': form, 'id':id})

def update_obloganalysis(request, id):   
   log = OBLogAnalysisModel.objects.get(id=id)
   form = OBLogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        form = OBLogAnalysisForm(request.POST, request.FILES, instance=log)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect ('obloganalysis:list_obloganalysis')
   return render (request, 'obloganalysis/obloganalysis_form.html', {'form': form, 'log':log})

def delete_obloganalysis(request, id):   
   log = OBLogAnalysisModel.objects.get(id=id)   
   if request.method == 'POST' :
       log.delete()
       return redirect ('obloganalysis:list_obloganalysis')
   return render (request, 'obloganalysis/obloganalysis_confirm_delete.html', {'log':log})



