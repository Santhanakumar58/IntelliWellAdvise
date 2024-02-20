from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedObserver.models import SelectedObserver
from .models import OBLeakoffTest
from .forms import  OBLeakoffTestForm


def list_obleakoffTest(request, id): 
    selectedwell = SelectedObserver.objects.first()  
    obleakoffTests = OBLeakoffTest.objects.filter(casingSize_id=id).all()
    return render (request, 'obleakoffTests/obleakoffTest.html', {'obleakoffTests': obleakoffTests, 'id':id})    

def create_obleakoffTest(request, id):
     selectedwell = SelectedObserver.objects.first()
     obleakoffTest = OBLeakoffTest()
     obleakoffTest.gpfgid = selectedwell.fgid
     obleakoffTest.gpwellid = selectedwell.wellid  
     obleakoffTest.gpcasingSize_id = id
     print(id)
     form = OBLeakoffTestForm(request.POST or None, instance=obleakoffTest)
     if request.method =="POST":
        selectedwell = SelectedObserver.objects.first()
        obleakoffTest = OBLeakoffTest()
        obleakoffTest.fgid = selectedwell.fgid
        obleakoffTest.wellid = selectedwell.wellid
        obleakoffTest.casingSize=request.POST.get('casingSize_id')
        obleakoffTest.recorded_Date=request.POST.get('recorded_Date')
        obleakoffTest.mudWeight=request.POST.get('mudWeight')
        obleakoffTest.openholeLength = request.POST.get('openholeLength')
        form = OBLeakoffTestForm(request.POST or None, instance=obleakoffTest)          
        if form.is_valid(): 
            form.save() 
            return redirect ('obleakoffTests:list_obleakoffTest', id)             
     return render (request, 'obleakoffTests/obleakoffTest_form.html', {'form': form, 'id':id})

def update_obleakoffTest(request, id):
   obleakoffTest = OBLeakoffTest.objects.get(id=id)  
   form = OBLeakoffTestForm(request.POST or None, instance=obleakoffTest)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('obleakoffTests:list_obleakoffTest', id)
   return render (request, 'obleakoffTests/obleakoffTest_form.html', {'form': form, 'obleakoffTest':obleakoffTest, 'id':id})

def delete_obleakoffTest(request, id):
   obleakoffTest = OBLeakoffTest.objects.get(id=id)  
   if request.method == 'POST' :
       obleakoffTest.delete()
       return redirect ('obleakoffTests:list_obleakoffTest', obleakoffTest.casingSize_id)
   return render (request, 'obleakoffTests/obleakoffTest_confirm_delete.html', {'obleakoffTest':obleakoffTest})

