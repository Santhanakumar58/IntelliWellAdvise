from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import WIDrillingWellData
from .forms import WIDrillingWellDataForm
from selectedWaterInjector.models import SelectedWaterInjector

def list_widrillingwelldata(request):
    selectedwell = SelectedWaterInjector.objects.all().first()
    widrillingwelldatas = WIDrillingWellData.objects.filter(wiwellid = selectedwell.wellid).all()    
   
    return render (request, 'widrillingwelldata/widrillingwelldata.html', {'widrillingwelldatas': widrillingwelldatas})
    
def create_widrillingwelldata(request):  
   selctedoilproducer = SelectedWaterInjector.objects.all().first()   
   widrillingwelldata = WIDrillingWellData()   
   widrillingwelldata.fgId = selctedoilproducer.fgid
   widrillingwelldata.wellid= selctedoilproducer.wellid
   form = WIDrillingWellDataForm(request.POST or None, instance=widrillingwelldata)  
   if form.is_valid():
       form.save()       
       return redirect ('widrillingwelldata:list_widrillingwelldata')    
   return render (request, 'widrillingwelldata/widrillingwelldata_form.html', {'form': form})

def update_widrillingwelldata(request, id):
   widrillingwelldata = WIDrillingWellData.objects.get(id=id)
   form = WIDrillingWellDataForm(request.POST or None, instance=widrillingwelldata)
   if form.is_valid():
       form.save()
       return redirect ('widrillingwelldata:list_widrillingwelldata')
   return render (request, 'widrillingwelldata/widrillingwelldata_form.html', {'form': form, 'widrillingwelldata':widrillingwelldata})

def delete_widrillingwelldata(request, id):
   widrillingwelldata = WIDrillingWellData.objects.get(id=id)   
   if request.method == 'POST' :
       widrillingwelldata.delete()
       return redirect ('widrillingwelldata:list_widrillingwelldata')
   return render (request, 'widrillingwelldata/widrillingwelldata_confirm_delete.html', {'widrillingwelldata':widrillingwelldata})



