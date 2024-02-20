from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import GasInjector
from .forms import GasInjectorForm
from fgis.models import FGIModel
from django.contrib.sessions.models import Session
from django.contrib  import messages
from selectedfgi.models import Selectedfgi

def list_gasinjector(request):
    gasinjectors = GasInjector.objects.all()   
 
    return render (request, 'gasinjectors/gasinjector.html', {'gasinjectors': gasinjectors})

def create_gasinjector(request): 
    selectedfgi = Selectedfgi.objects.first()
    gasinjector = GasInjector()
    gasinjector.fgid = selectedfgi.fgid
    gasinjector.is_selected = False   
    form = GasInjectorForm(request.POST or None, instance=gasinjector)
    if form.is_valid():
        form.save()
        return redirect ('gasinjectors:list_gasinjector')
    return render (request, 'gasinjectors/gasinjector_form.html', {'form': form})

def update_gasinjector(request, id):
   gasinjector = GasInjector.objects.get(id=id)
   form = GasInjectorForm(request.POST or None, instance=gasinjector)
   if form.is_valid():
        form.save()      
        return redirect ('gasinjectors:list_gasinjector')
   return render (request, 'gasinjectors/gasinjector_form.html', {'form': form, 'gasinjector':gasinjector})

def delete_gasinjector(request, id):
   gasinjector = GasInjector.objects.get(id=id)
   
   if request.method == 'POST' :
       gasinjector.delete()
       return redirect ('gasinjectors:list_gasinjector')
   return render (request, 'gasinjectors/gasinjector_confirm_delete.html', {'gasinjector':gasinjector})

