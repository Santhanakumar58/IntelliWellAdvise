from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from .models import LeakoffTest
from .forms import  LeakoffTestForm
from casings.models import CasingModel
from selectedOilProducer.models import SelectedOilProducer

def list_leakoffTest(request, cid):    
    leakoffTests = LeakoffTest.objects.filter(casingModelid = cid)    
    return render (request, 'leakoffTests/leakoffTest.html', {'leakoffTests': leakoffTests, 'cid':cid})    

def create_leakoffTest(request, cid):
     print(cid)
     selectedwell = SelectedOilProducer.objects.first()
     leakoffTest = LeakoffTest()
     leakoffTest.fgid = selectedwell.fgid
     leakoffTest.wellid = selectedwell.wellid  
     leakoffTest.casingModelid = cid     
     form = LeakoffTestForm(request.POST or None, instance=leakoffTest)
     if request.method =="POST":
        selectedwell = SelectedOilProducer.objects.first()
        leakoffTest = LeakoffTest()
        leakoffTest.fgid = selectedwell.fgid
        leakoffTest.wellid = selectedwell.wellid
        leakoffTest.casingModelid = cid  
        leakoffTest.casingSize=request.POST.get('casingSize_id')
        leakoffTest.recorded_Date=request.POST.get('recorded_Date')
        leakoffTest.mudWeight=request.POST.get('mudWeight')
        leakoffTest.openholeLength = request.POST.get('openholeLength')
        form = LeakoffTestForm(request.POST or None, instance=leakoffTest)          
        if form.is_valid(): 
            form.save() 
            return redirect ('leakoffTests:list_leakoffTest', cid)             
     return render (request, 'leakoffTests/leakoffTest_form.html', {'form': form, 'cid':cid})

def update_leakoffTest(request, id):   
   leakoffTest = LeakoffTest.objects.get(id=id)  
   cid = leakoffTest.casingModelid 
   selectedcasing = CasingModel.objects.filter(casingSize_id = leakoffTest.casingSize_id)   

   form = LeakoffTestForm(request.POST or None, instance=leakoffTest)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('leakoffTests:list_leakoffTest', cid)
   return render (request, 'leakoffTests/leakoffTest_form.html', {'form': form, 'leakoffTest':leakoffTest, 'id':id})

def delete_leakoffTest(request, id):
   leakoffTest = LeakoffTest.objects.get(id=id)  
   if request.method == 'POST' :
       leakoffTest.delete()
       return redirect ('leakoffTests:list_leakoffTest', leakoffTest.casingModelid)
   return render (request, 'leakoffTests/leakoffTest_confirm_delete.html', {'leakoffTest':leakoffTest})

