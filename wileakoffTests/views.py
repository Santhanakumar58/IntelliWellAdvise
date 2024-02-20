from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedWaterInjector.models import SelectedWaterInjector
from .models import WILeakoffTest
from .forms import  WILeakoffTestForm


def list_wileakoffTest(request, id): 
    selectedwell = SelectedWaterInjector.objects.first()  
    wileakoffTests = WILeakoffTest.objects.filter(casingSize_id=id).all()
    return render (request, 'wileakoffTests/wileakoffTest.html', {'wileakoffTests': wileakoffTests, 'id':id})    

def create_wileakoffTest(request, id):
     selectedwell = SelectedWaterInjector.objects.first()
     wileakoffTest = WILeakoffTest()
     wileakoffTest.gpfgid = selectedwell.fgid
     wileakoffTest.gpwellid = selectedwell.wellid  
     wileakoffTest.gpcasingSize_id = id
     print(id)
     form = WILeakoffTestForm(request.POST or None, instance=wileakoffTest)
     if request.method =="POST":
        selectedwell = SelectedWaterInjector.objects.first()
        wileakoffTest = WILeakoffTest()
        wileakoffTest.fgid = selectedwell.fgid
        wileakoffTest.wellid = selectedwell.wellid
        wileakoffTest.casingSize=request.POST.get('casingSize_id')
        wileakoffTest.recorded_Date=request.POST.get('recorded_Date')
        wileakoffTest.mudWeight=request.POST.get('mudWeight')
        wileakoffTest.openholeLength = request.POST.get('openholeLength')
        form = WILeakoffTestForm(request.POST or None, instance=wileakoffTest)          
        if form.is_valid(): 
            form.save() 
            return redirect ('wileakoffTests:list_wileakoffTest', id)             
     return render (request, 'wileakoffTests/wileakoffTest_form.html', {'form': form, 'id':id})

def update_wileakoffTest(request, id):
   wileakoffTest = WILeakoffTest.objects.get(id=id)  
   form = WILeakoffTestForm(request.POST or None, instance=wileakoffTest)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('wileakoffTests:list_wileakoffTest', id)
   return render (request, 'wileakoffTests/wileakoffTest_form.html', {'form': form, 'wileakoffTest':wileakoffTest, 'id':id})

def delete_wileakoffTest(request, id):
   wileakoffTest = WILeakoffTest.objects.get(id=id)  
   if request.method == 'POST' :
       wileakoffTest.delete()
       return redirect ('wileakoffTests:list_wileakoffTest', wileakoffTest.casingSize_id)
   return render (request, 'wileakoffTests/wileakoffTest_confirm_delete.html', {'wileakoffTest':wileakoffTest})


