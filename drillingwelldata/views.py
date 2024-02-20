from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import DrillingWellData
from .forms import DrillingWellDataForm
from selectedOilProducer.models import SelectedOilProducer

def list_drillingwelldata(request):
    selectedwell = SelectedOilProducer.objects.all().first()
    drillingwelldata = DrillingWellData.objects.filter(wellid = selectedwell.wellid).all()   
    
    print(drillingwelldata)
    return render (request, 'drillingwelldata/drillingwelldata.html', {'drillingwelldata': drillingwelldata})
    
def create_drillingwelldata(request):  
   selctedoilproducer = SelectedOilProducer.objects.all().first()   
   drillingwelldata = DrillingWellData()   
   drillingwelldata.fgId = selctedoilproducer.fgid
   drillingwelldata.wellid= selctedoilproducer.wellid
   form = DrillingWellDataForm(request.POST or None, instance=drillingwelldata)  
   if form.is_valid():
       form.save()       
       return redirect ('drillingwelldata:list_drillingwelldata')    
   return render (request, 'drillingwelldata/drillingwelldata_form.html', {'form': form})

def update_drillingwelldata(request, id):
   drillingwelldata = DrillingWellData.objects.get(id=id)
   form = DrillingWellDataForm(request.POST or None, instance=drillingwelldata)
   if form.is_valid():
       form.save()
       return redirect ('drillingwelldata:list_drillingwelldata')
   return render (request, 'drillingwelldata/drillingwelldata_form.html', {'form': form, 'drillingwelldata':drillingwelldata})

def delete_drillingwelldata(request, id):
   drillingwelldata = DrillingWellData.objects.get(id=id)   
   if request.method == 'POST' :
       drillingwelldata.delete()
       return redirect ('drillingwelldata:list_drillingwelldata')
   return render (request, 'drillingwelldata/drillingwelldata_confirm_delete.html', {'drillingwelldata':drillingwelldata})


