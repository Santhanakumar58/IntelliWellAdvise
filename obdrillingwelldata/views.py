from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import OBDrillingWellData
from .forms import OBDrillingWellDataForm
from selectedObserver.models import SelectedObserver

def list_obdrillingwelldata(request):
    selectedwell = SelectedObserver.objects.all().first()
    obdrillingwelldatas = OBDrillingWellData.objects.filter(obwellid = selectedwell.wellid).all()    
   
    return render (request, 'obdrillingwelldata/obdrillingwelldata.html', {'obdrillingwelldatas': obdrillingwelldatas})
    
def create_obdrillingwelldata(request):  
   selctedoilproducer = SelectedObserver.objects.all().first()   
   obdrillingwelldata = OBDrillingWellData()   
   obdrillingwelldata.fgId = selctedoilproducer.fgid
   obdrillingwelldata.wellid= selctedoilproducer.wellid
   form = OBDrillingWellDataForm(request.POST or None, instance=obdrillingwelldata)  
   if form.is_valid():
       form.save()       
       return redirect ('obdrillingwelldata:list_obdrillingwelldata')    
   return render (request, 'obdrillingwelldata/obdrillingwelldata_form.html', {'form': form})

def update_obdrillingwelldata(request, id):
   obdrillingwelldata = OBDrillingWellData.objects.get(id=id)
   form = OBDrillingWellDataForm(request.POST or None, instance=obdrillingwelldata)
   if form.is_valid():
       form.save()
       return redirect ('obdrillingwelldata:list_obdrillingwelldata')
   return render (request, 'obdrillingwelldata/obdrillingwelldata_form.html', {'form': form, 'obdrillingwelldata':obdrillingwelldata})

def delete_obdrillingwelldata(request, id):
   obdrillingwelldata = OBDrillingWellData.objects.get(id=id)   
   if request.method == 'POST' :
       obdrillingwelldata.delete()
       return redirect ('obdrillingwelldata:list_obdrillingwelldata')
   return render (request, 'obdrillingwelldata/obdrillingwelldata_confirm_delete.html', {'obdrillingwelldata':obdrillingwelldata})



