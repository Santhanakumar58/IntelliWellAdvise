from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedGasProducer.models import SelectedGasProducer
from .models import GPLeakoffTest
from .forms import  GPLeakoffTestForm


def list_gpleakoffTest(request, id): 
    selectedwell = SelectedGasProducer.objects.first()  
    gpleakoffTests = GPLeakoffTest.objects.filter(casingSize_id=id).all()
    return render (request, 'gpleakoffTests/gpleakoffTest.html', {'gpleakoffTests': gpleakoffTests, 'id':id})    

def create_gpleakoffTest(request, id):
     selectedwell = SelectedGasProducer.objects.first()
     gpleakoffTest = GPLeakoffTest()
     gpleakoffTest.gpfgid = selectedwell.fgid
     gpleakoffTest.gpwellid = selectedwell.wellid  
     gpleakoffTest.gpcasingSize_id = id
     print(id)
     form = GPLeakoffTestForm(request.POST or None, instance=gpleakoffTest)
     if request.method =="POST":
        selectedwell = SelectedGasProducer.objects.first()
        gpleakoffTest = GPLeakoffTest()
        gpleakoffTest.fgid = selectedwell.fgid
        gpleakoffTest.wellid = selectedwell.wellid
        gpleakoffTest.casingSize=request.POST.get('casingSize_id')
        gpleakoffTest.recorded_Date=request.POST.get('recorded_Date')
        gpleakoffTest.mudWeight=request.POST.get('mudWeight')
        gpleakoffTest.openholeLength = request.POST.get('openholeLength')
        form = GPLeakoffTestForm(request.POST or None, instance=gpleakoffTest)          
        if form.is_valid(): 
            form.save() 
            return redirect ('gpleakoffTests:list_gpleakoffTest', id)             
     return render (request, 'gpleakoffTests/gpleakoffTest_form.html', {'form': form, 'id':id})

def update_gpleakoffTest(request, id):
   gpleakoffTest = GPLeakoffTest.objects.get(id=id)  
   form = GPLeakoffTestForm(request.POST or None, instance=gpleakoffTest)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('gpleakoffTests:list_gpleakoffTest', id)
   return render (request, 'gpleakoffTests/gpleakoffTest_form.html', {'form': form, 'gpleakoffTest':gpleakoffTest, 'id':id})

def delete_gpleakoffTest(request, id):
   gpleakoffTest = GPLeakoffTest.objects.get(id=id)  
   if request.method == 'POST' :
       gpleakoffTest.delete()
       return redirect ('gpleakoffTests:list_gpleakoffTest', gpleakoffTest.casingSize_id)
   return render (request, 'gpleakoffTests/gpleakoffTest_confirm_delete.html', {'gpleakoffTest':gpleakoffTest})

