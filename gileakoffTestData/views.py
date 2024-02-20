from django.shortcuts import render, redirect
from .models import GILeakoffTestData
from selectedGasInjector.models import SelectedGasInjector
from .forms import GILeakoffTestDataForm

# Create your views here.

def list_gileakoffTestData(request, id): 
    selectedwell = SelectedGasInjector.objects.first()  
    gileakoffTestDatas = GILeakoffTestData.objects.filter(gileakoffTest_id = id).all()
    return render (request, 'gileakoffTestData/gileakoffTestData.html', {'gileakoffTestDatas': gileakoffTestDatas, 'id1':id})    

def create_gileakoffTestData(request, id):
    
     gileakoffTestdata = GILeakoffTestData()
     gileakoffTestdata.gileakoffTest_id = id 
     gileakoffTestdata.casingSize_id =  id  
     print(gileakoffTestdata.gileakoffTest_id)
     
     form = GILeakoffTestDataForm(request.POST or None, instance=gileakoffTestdata)
     if request.method =="POST":
        gileakoffTestdata = GILeakoffTestData()
        gileakoffTestdata.gileakoffTest = request.POST.get('gileakoffTest_id')
        gileakoffTestdata.gpcasingSize=request.POST.get('gpcasingSize_id')
        gileakoffTestdata.gptime=request.POST.get('gptime')
        gileakoffTestdata.gpvolume=request.POST.get('gpvolume')
        gileakoffTestdata.gppressure = request.POST.get('gppressure')
        form = GILeakoffTestDataForm(request.POST or None, instance=gileakoffTestdata)          
        if form.is_valid(): 
            form.save() 
            return redirect ('gileakoffTestData:list_gileakoffTestData', gileakoffTestdata.gileakoffTest_id)             
     return render (request, 'gileakoffTestData/gileakoffTestData_form.html', {'form': form})

def update_gileakoffTestData(request, id):
   gileakoffTestData = GILeakoffTestData.objects.get(id=id)
   print(gileakoffTestData)
   form = GILeakoffTestDataForm(request.POST or None, instance=gileakoffTestData)
   if request.method =="POST":        
        if form.is_valid():
            form.save()
            return redirect ('gileakoffTestData:list_gileakoffTestData', gileakoffTestData.gileakoffTest_id)
   return render (request, 'gileakoffTestData/gileakoffTestData_form.html', {'form': form, 'gileakoffTestData':gileakoffTestData})

def delete_gileakoffTestData(request, id):
   gileakoffTestData = GILeakoffTestData.objects.get(id=id)  
   if request.method == 'POST' :
       gileakoffTestData.delete()
       return redirect ('gileakoffTestData:list_gileakoffTestData', gileakoffTestData.gileakoffTest_id)
   return render (request, 'gileakoffTestData/gileakoffTestData_confirm_delete.html', {'gileakoffTestData':gileakoffTestData})
