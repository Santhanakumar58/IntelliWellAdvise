from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import GPDrillingWellData
from .forms import GPDrillingWellDataForm
from selectedGasProducer.models import SelectedGasProducer

def list_gpdrillingwelldata(request):
    selectedwell = SelectedGasProducer.objects.all().first()
    gpdrillingwelldatas = GPDrillingWellData.objects.filter(gpwellid = selectedwell.wellid).all()    
   
    return render (request, 'gpdrillingwelldata/gpdrillingwelldata.html', {'gpdrillingwelldatas': gpdrillingwelldatas})
    
def create_gpdrillingwelldata(request):  
   selctedoilproducer = SelectedGasProducer.objects.all().first()   
   gpdrillingwelldata = GPDrillingWellData()   
   gpdrillingwelldata.fgId = selctedoilproducer.fgid
   gpdrillingwelldata.wellid= selctedoilproducer.wellid
   form = GPDrillingWellDataForm(request.POST or None, instance=gpdrillingwelldata)  
   if form.is_valid():
       form.save()       
       return redirect ('gpdrillingwelldata:list_gpdrillingwelldata')    
   return render (request, 'gpdrillingwelldata/gpdrillingwelldata_form.html', {'form': form})

def update_gpdrillingwelldata(request, id):
   gpdrillingwelldata = GPDrillingWellData.objects.get(id=id)
   form = GPDrillingWellDataForm(request.POST or None, instance=gpdrillingwelldata)
   if form.is_valid():
       form.save()
       return redirect ('gpdrillingwelldata:list_gpdrillingwelldata')
   return render (request, 'gpdrillingwelldata/gpdrillingwelldata_form.html', {'form': form, 'gpdrillingwelldata':gpdrillingwelldata})

def delete_gpdrillingwelldata(request, id):
   gpdrillingwelldata = GPDrillingWellData.objects.get(id=id)   
   if request.method == 'POST' :
       gpdrillingwelldata.delete()
       return redirect ('gpdrillingwelldata:list_gpdrillingwelldata')
   return render (request, 'gpdrillingwelldata/gpdrillingwelldata_confirm_delete.html', {'gpdrillingwelldata':gpdrillingwelldata})


