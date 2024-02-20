from django.shortcuts import render, redirect
from .models import LeakoffTestData
from selectedOilProducer.models import SelectedOilProducer
from .forms import LeakoffTestDataForm

# Create your views here.

def list_leakoffTestData(request, id): 
    selectedwell = SelectedOilProducer.objects.first()  
    leakoffTestDatas = LeakoffTestData.objects.filter(leakoffTest_id = id).all()
    return render (request, 'leakoffTestData/leakoffTestData.html', {'leakoffTestDatas': leakoffTestDatas, 'id1':id})    

def create_leakoffTestData(request, id):
    
     leakoffTestdata = LeakoffTestData()
     leakoffTestdata.leakoffTest_id = id 
     leakoffTestdata.casingSize_id =  id  
     print(leakoffTestdata.leakoffTest_id)
     
     form = LeakoffTestDataForm(request.POST or None, instance=leakoffTestdata)
     if request.method =="POST":
        leakoffTestdata = LeakoffTestData()
        leakoffTestdata.leakoffTest = request.POST.get('leakoffTest_id')
        leakoffTestdata.casingSize=request.POST.get('casingSize_id')
        leakoffTestdata.time=request.POST.get('time')
        leakoffTestdata.volume=request.POST.get('volume')
        leakoffTestdata.pressure = request.POST.get('pressure')
        form = LeakoffTestDataForm(request.POST or None, instance=leakoffTestdata)          
        if form.is_valid(): 
            form.save() 
            return redirect ('leakoffTestData:list_leakoffTestData', leakoffTestdata.leakoffTest_id)             
     return render (request, 'leakoffTestData/leakoffTestData_form.html', {'form': form})

def update_leakoffTestData(request, id):
   leakoffTestData = LeakoffTestData.objects.get(id=id)
   print(leakoffTestData)
   form = LeakoffTestDataForm(request.POST or None, instance=leakoffTestData)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('leakoffTestData:list_leakoffTestData', leakoffTestData.leakoffTest_id)
   return render (request, 'leakoffTestData/leakoffTestData_form.html', {'form': form, 'leakoffTestData':leakoffTestData})

def delete_leakoffTestData(request, id):
   leakoffTestData = LeakoffTestData.objects.get(id=id)  
   if request.method == 'POST' :
       leakoffTestData.delete()
       return redirect ('leakoffTestData:list_leakoffTestData', leakoffTestData.leakoffTest_id)
   return render (request, 'leakoffTestData/leakoffTestData_confirm_delete.html', {'leakoffTestData':leakoffTestData})