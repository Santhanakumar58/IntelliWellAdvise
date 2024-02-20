from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from selectedGasInjector.models import SelectedGasInjector
from .models import GILeakoffTest
from .forms import  GILeakoffTestForm


def list_gileakoffTest(request, id): 
    selectedwell = SelectedGasInjector.objects.first()  
    gileakoffTests = GILeakoffTest.objects.filter(gicasingSize_id=id).all()
    return render (request, 'gileakoffTests/gileakoffTest.html', {'gileakoffTests': gileakoffTests, 'id':id})    

def create_gileakoffTest(request, id):
     selectedwell = SelectedGasInjector.objects.first()
     gileakoffTest = GILeakoffTest()
     gileakoffTest.gifgid = selectedwell.fgid
     gileakoffTest.giwellid = selectedwell.wellid  
     gileakoffTest.gicasingSize_id = id
     print(id)
     form = GILeakoffTestForm(request.POST or None, instance=gileakoffTest)
     if request.method =="POST":
        selectedwell = SelectedGasInjector.objects.first()
        gileakoffTest = GILeakoffTest()
        gileakoffTest.fgid = selectedwell.fgid
        gileakoffTest.wellid = selectedwell.wellid
        gileakoffTest.casingSize=request.POST.get('casingSize_id')
        gileakoffTest.recorded_Date=request.POST.get('recorded_Date')
        gileakoffTest.mudWeight=request.POST.get('mudWeight')
        gileakoffTest.openholeLength = request.POST.get('openholeLength')
        form = GILeakoffTestForm(request.POST or None, instance=gileakoffTest)          
        if form.is_valid(): 
            form.save() 
            return redirect ('gileakoffTests:list_gileakoffTest', id)             
     return render (request, 'gileakoffTests/gileakoffTest_form.html', {'form': form, 'id':id})

def update_gileakoffTest(request, id):
   gileakoffTest = GILeakoffTest.objects.get(id=id)  
   form = GILeakoffTestForm(request.POST or None, instance=gileakoffTest)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('gileakoffTests:list_gileakoffTest', id)
   return render (request, 'gileakoffTests/gileakoffTest_form.html', {'form': form, 'gileakoffTest':gileakoffTest, 'id':id})

def delete_gileakoffTest(request, id):
   gileakoffTest = GILeakoffTest.objects.get(id=id)  
   if request.method == 'POST' :
       gileakoffTest.delete()
       return redirect ('gileakoffTests:list_gileakoffTest', gileakoffTest.casingSize_id)
   return render (request, 'gileakoffTests/gileakoffTest_confirm_delete.html', {'gileakoffTest':gileakoffTest})


