from django.shortcuts import render, redirect
from .models import OBLeakoffTestData
from selectedObserver.models import SelectedObserver
from .forms import OBLeakoffTestDataForm

# Create your views here.

def list_obleakoffTestData(request, id): 
    selectedwell = SelectedObserver.objects.first()  
    obleakoffTestDatas = OBLeakoffTestData.objects.filter(obleakoffTest_id = id).all()
    return render (request, 'obleakoffTestData/obleakoffTestData.html', {'obleakoffTestDatas': obleakoffTestDatas, 'id1':id})    

def create_obleakoffTestData(request, id):
    
     obleakoffTestdata = OBLeakoffTestData()
     obleakoffTestdata.obleakoffTest_id = id 
     obleakoffTestdata.casingSize_id =  id  
     print(obleakoffTestdata.obleakoffTest_id)
     
     form = OBLeakoffTestDataForm(request.POST or None, instance=obleakoffTestdata)
     if request.method =="POST":
        obleakoffTestdata = OBLeakoffTestData()
        obleakoffTestdata.obleakoffTest = request.POST.get('obleakoffTest_id')
        obleakoffTestdata.gpcasingSize=request.POST.get('gpcasingSize_id')
        obleakoffTestdata.gptime=request.POST.get('gptime')
        obleakoffTestdata.gpvolume=request.POST.get('gpvolume')
        obleakoffTestdata.gppressure = request.POST.get('gppressure')
        form = OBLeakoffTestDataForm(request.POST or None, instance=obleakoffTestdata)          
        if form.is_valid(): 
            form.save() 
            return redirect ('obleakoffTestData:list_obleakoffTestData', obleakoffTestdata.obleakoffTest_id)             
     return render (request, 'obleakoffTestData/obleakoffTestData_form.html', {'form': form})

def update_obleakoffTestData(request, id):
   obleakoffTestData = OBLeakoffTestData.objects.get(id=id)
   print(obleakoffTestData)
   form = OBLeakoffTestDataForm(request.POST or None, instance=obleakoffTestData)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('obleakoffTestData:list_obleakoffTestData', obleakoffTestData.obleakoffTest_id)
   return render (request, 'obleakoffTestData/obleakoffTestData_form.html', {'form': form, 'obleakoffTestData':obleakoffTestData})

def delete_obleakoffTestData(request, id):
   obleakoffTestData = OBLeakoffTestData.objects.get(id=id)  
   if request.method == 'POST' :
       obleakoffTestData.delete()
       return redirect ('obleakoffTestData:list_obleakoffTestData', obleakoffTestData.obleakoffTest_id)
   return render (request, 'obleakoffTestData/obleakoffTestData_confirm_delete.html', {'obleakoffTestData':obleakoffTestData})
