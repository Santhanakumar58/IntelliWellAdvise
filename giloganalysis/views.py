from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedGasInjector.models import SelectedGasInjector
from .models import GILogAnalysisModel
from .forms import GILogAnalysisForm
 

def list_giloganalysis(request):
    selectedwell = SelectedGasInjector.objects.first()  
    print(selectedwell.wellid) 
    logs = GILogAnalysisModel.objects.filter(giwellid =selectedwell.wellid).all()  
    print(logs)  
    return render (request, 'giloganalysis/giloganalysis.html', {'logs': logs })   

def create_giloganalysis(request): 
   log = GILogAnalysisModel()
   selectedwell = SelectedGasInjector.objects.first()  
   log.gifgid = selectedwell.fgid
   log.giwellid = selectedwell.wellid    
   form = GILogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        selectedwell = SelectedGasInjector.objects.first()
        log = GILogAnalysisModel()
        log.gifgid = selectedwell.fgid
        log.giwellid = selectedwell.wellid
        log.gicasingSize=request.POST.get('casingSize')
        log.gianalyst=request.POST.get('analyst')
        log.girecorded_date=request.POST.get('recorded_date')
        log.giinterpretation = request.POST.get('interpretation')        
        form = GILogAnalysisForm(request.POST, request.FILES, instance=log)             
        if form.is_valid():       
            form.save()
            img_obj = form.instance            
            return redirect ('giloganalysis:list_giloganalysis') 
        else :
             log = GILogAnalysisModel()
             selectedwell = SelectedGasInjector.objects.first()  
             log.gifgid = selectedwell.fgid
             log.giwellid = selectedwell.wellid
             form = GILogAnalysisForm(request.POST or None, instance=log)          
   return render (request, 'giloganalysis/giloganalysis_form.html', {'form': form, 'id':id})

def update_giloganalysis(request, id):   
   log = GILogAnalysisModel.objects.get(id=id)
   form = GILogAnalysisForm(request.POST or None, instance=log)
   if request.method =="POST":
        form = GILogAnalysisForm(request.POST, request.FILES, instance=log)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect ('giloganalysis:list_giloganalysis')
   return render (request, 'giloganalysis/giloganalysis_form.html', {'form': form, 'log':log})

def delete_giloganalysis(request, id):   
   log = GILogAnalysisModel.objects.get(id=id)   
   if request.method == 'POST' :
       log.delete()
       return redirect ('giloganalysis:list_giloganalysis')
   return render (request, 'giloganalysis/giloganalysis_confirm_delete.html', {'log':log})




