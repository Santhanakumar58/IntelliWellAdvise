from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import GIDrillingWellData
from .forms import GIDrillingWellDataForm
from selectedGasInjector.models import SelectedGasInjector

def list_gidrillingwelldata(request):
    selectedwell = SelectedGasInjector.objects.all().first()
    gidrillingwelldatas = GIDrillingWellData.objects.filter(giwellid = selectedwell.wellid).all()    
   
    return render (request, 'gidrillingwelldata/gidrillingwelldata.html', {'gidrillingwelldatas': gidrillingwelldatas})
    
def create_gidrillingwelldata(request):  
   selctedoilproducer = SelectedGasInjector.objects.all().first()   
   gidrillingwelldata = GIDrillingWellData()   
   gidrillingwelldata.fgId = selctedoilproducer.fgid
   gidrillingwelldata.wellid= selctedoilproducer.wellid
   form = GIDrillingWellDataForm(request.POST or None, instance=gidrillingwelldata)  
   if form.is_valid():
       form.save()       
       return redirect ('gidrillingwelldata:list_gidrillingwelldata')    
   return render (request, 'gidrillingwelldata/gidrillingwelldata_form.html', {'form': form})

def update_gidrillingwelldata(request, id):
   gidrillingwelldata = GIDrillingWellData.objects.get(id=id)
   form = GIDrillingWellDataForm(request.POST or None, instance=gidrillingwelldata)
   if form.is_valid():
       form.save()
       return redirect ('gidrillingwelldata:list_gidrillingwelldata')
   return render (request, 'gidrillingwelldata/gidrillingwelldata_form.html', {'form': form, 'gidrillingwelldata':gidrillingwelldata})

def delete_gidrillingwelldata(request, id):
   gidrillingwelldata = GIDrillingWellData.objects.get(id=id)   
   if request.method == 'POST' :
       gidrillingwelldata.delete()
       return redirect ('gidrillingwelldata:list_gidrillingwelldata')
   return render (request, 'gidrillingwelldata/gidrillingwelldata_confirm_delete.html', {'gidrillingwelldata':gidrillingwelldata})


