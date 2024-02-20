from django.shortcuts import render, redirect
from .models import GPLeakoffTestData
from selectedGasProducer.models import SelectedGasProducer
from .forms import GPLeakoffTestDataForm

# Create your views here.

def list_gpleakoffTestData(request, id): 
    selectedwell = SelectedGasProducer.objects.first()  
    gpleakoffTestDatas = GPLeakoffTestData.objects.filter(gpleakoffTest_id = id).all()
    return render (request, 'gpleakoffTestData/gpleakoffTestData.html', {'gpleakoffTestDatas': gpleakoffTestDatas, 'id1':id})    

def create_gpleakoffTestData(request, id):
    
     gpleakoffTestdata = GPLeakoffTestData()
     gpleakoffTestdata.gpleakoffTest_id = id 
     gpleakoffTestdata.casingSize_id =  id  
     print(gpleakoffTestdata.gpleakoffTest_id)
     
     form = GPLeakoffTestDataForm(request.POST or None, instance=gpleakoffTestdata)
     if request.method =="POST":
        gpleakoffTestdata = GPLeakoffTestData()
        gpleakoffTestdata.gpleakoffTest = request.POST.get('gpleakoffTest_id')
        gpleakoffTestdata.gpcasingSize=request.POST.get('gpcasingSize_id')
        gpleakoffTestdata.gptime=request.POST.get('gptime')
        gpleakoffTestdata.gpvolume=request.POST.get('gpvolume')
        gpleakoffTestdata.gppressure = request.POST.get('gppressure')
        form = GPLeakoffTestDataForm(request.POST or None, instance=gpleakoffTestdata)          
        if form.is_valid(): 
            form.save() 
            return redirect ('gpleakoffTestData:list_gpleakoffTestData', gpleakoffTestdata.gpleakoffTest_id)             
     return render (request, 'gpleakoffTestData/gpleakoffTestData_form.html', {'form': form})

def update_gpleakoffTestData(request, id):
   gpleakoffTestData = GPLeakoffTestData.objects.get(id=id)
   print(gpleakoffTestData)
   form = GPLeakoffTestDataForm(request.POST or None, instance=gpleakoffTestData)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('gpleakoffTestData:list_gpleakoffTestData', gpleakoffTestData.gpleakoffTest_id)
   return render (request, 'gpleakoffTestData/gpleakoffTestData_form.html', {'form': form, 'gpleakoffTestData':gpleakoffTestData})

def delete_gpleakoffTestData(request, id):
   gpleakoffTestData = GPLeakoffTestData.objects.get(id=id)  
   if request.method == 'POST' :
       gpleakoffTestData.delete()
       return redirect ('gpleakoffTestData:list_gpleakoffTestData', gpleakoffTestData.gpleakoffTest_id)
   return render (request, 'gpleakoffTestData/gpleakoffTestData_confirm_delete.html', {'gpleakoffTestData':gpleakoffTestData})