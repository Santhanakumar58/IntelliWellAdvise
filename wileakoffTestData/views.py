from django.shortcuts import render, redirect
from .models import WILeakoffTestData
from selectedWaterInjector.models import SelectedWaterInjector
from .forms import WILeakoffTestDataForm

# Create your views here.

def list_wileakoffTestData(request, id): 
    selectedwell = SelectedWaterInjector.objects.first()  
    wileakoffTestDatas = WILeakoffTestData.objects.filter(wileakoffTest_id = id).all()
    return render (request, 'wileakoffTestData/wileakoffTestData.html', {'wileakoffTestDatas': wileakoffTestDatas, 'id1':id})    

def create_wileakoffTestData(request, id):
    
     wileakoffTestdata = WILeakoffTestData()
     wileakoffTestdata.wileakoffTest_id = id 
     wileakoffTestdata.casingSize_id =  id  
     print(wileakoffTestdata.wileakoffTest_id)
     
     form = WILeakoffTestDataForm(request.POST or None, instance=wileakoffTestdata)
     if request.method =="POST":
        wileakoffTestdata = WILeakoffTestData()
        wileakoffTestdata.wileakoffTest = request.POST.get('wileakoffTest_id')
        wileakoffTestdata.gpcasingSize=request.POST.get('gpcasingSize_id')
        wileakoffTestdata.gptime=request.POST.get('gptime')
        wileakoffTestdata.gpvolume=request.POST.get('gpvolume')
        wileakoffTestdata.gppressure = request.POST.get('gppressure')
        form = WILeakoffTestDataForm(request.POST or None, instance=wileakoffTestdata)          
        if form.is_valid(): 
            form.save() 
            return redirect ('wileakoffTestData:list_wileakoffTestData', wileakoffTestdata.wileakoffTest_id)             
     return render (request, 'wileakoffTestData/wileakoffTestData_form.html', {'form': form})

def update_wileakoffTestData(request, id):
   wileakoffTestData = WILeakoffTestData.objects.get(id=id)
   print(wileakoffTestData)
   form = WILeakoffTestDataForm(request.POST or None, instance=wileakoffTestData)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('wileakoffTestData:list_wileakoffTestData', wileakoffTestData.wileakoffTest_id)
   return render (request, 'wileakoffTestData/wileakoffTestData_form.html', {'form': form, 'wileakoffTestData':wileakoffTestData})

def delete_wileakoffTestData(request, id):
   wileakoffTestData = WILeakoffTestData.objects.get(id=id)  
   if request.method == 'POST' :
       wileakoffTestData.delete()
       return redirect ('wileakoffTestData:list_wileakoffTestData', wileakoffTestData.wileakoffTest_id)
   return render (request, 'wileakoffTestData/wileakoffTestData_confirm_delete.html', {'wileakoffTestData':wileakoffTestData})
