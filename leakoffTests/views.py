from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from .models import LeakoffTest
from .forms import  LeakoffTestForm
from selectedOilProducer.models import SelectedOilProducer

def list_leakoffTest(request, id): 
    selectedwell = SelectedOilProducer.objects.first()  
    leakoffTests = LeakoffTest.objects.filter(casingSize_id=id).all()
    return render (request, 'leakoffTests/leakoffTest.html', {'leakoffTests': leakoffTests, 'id':id})    

def create_leakoffTest(request, id):
     selectedwell = SelectedOilProducer.objects.first()
     leakoffTest = LeakoffTest()
     leakoffTest.fgid = selectedwell.fgid
     leakoffTest.wellid = selectedwell.wellid  
     leakoffTest.casingSize_id = id
     print(id)
     form = LeakoffTestForm(request.POST or None, instance=leakoffTest)
     if request.method =="POST":
        selectedwell = SelectedOilProducer.objects.first()
        leakoffTest = LeakoffTest()
        leakoffTest.fgid = selectedwell.fgid
        leakoffTest.wellid = selectedwell.wellid
        leakoffTest.casingSize=request.POST.get('casingSize_id')
        leakoffTest.recorded_Date=request.POST.get('recorded_Date')
        leakoffTest.mudWeight=request.POST.get('mudWeight')
        leakoffTest.openholeLength = request.POST.get('openholeLength')
        form = LeakoffTestForm(request.POST or None, instance=leakoffTest)          
        if form.is_valid(): 
            form.save() 
            return redirect ('leakoffTests:list_leakoffTest', id)             
     return render (request, 'leakoffTests/leakoffTest_form.html', {'form': form, 'id':id})

def update_leakoffTest(request, id):
   leakoffTest = LeakoffTest.objects.get(id=id)  
   form = LeakoffTestForm(request.POST or None, instance=leakoffTest)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('leakoffTests:list_leakoffTest', id)
   return render (request, 'leakoffTests/leakoffTest_form.html', {'form': form, 'leakoffTest':leakoffTest, 'id':id})

def delete_leakoffTest(request, id):
   leakoffTest = LeakoffTest.objects.get(id=id)  
   if request.method == 'POST' :
       leakoffTest.delete()
       return redirect ('leakoffTests:list_leakoffTest', leakoffTest.casingSize_id)
   return render (request, 'leakoffTests/leakoffTest_confirm_delete.html', {'leakoffTest':leakoffTest})

