from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Observer
from .forms import ObserverForm
from fgis.models import FGIModel
from django.contrib.sessions.models import Session
from django.contrib  import messages
from selectedfgi.models import Selectedfgi
from selectedObserver.models import SelectedObserver
from .models import Observer

def list_observer(request):
    observers = Observer.objects.all()  
    return render (request, 'observers/observer.html', {'observers': observers})

def create_observer(request): 
    selectedfgi = Selectedfgi.objects.first()
    observer = Observer()
    observer.fgid = selectedfgi.fgid
    observer.is_selected = False   
    print (selectedfgi) 
    form = ObserverForm(request.POST or None, instance=observer)
    if form.is_valid():
        form.save()
        return redirect ('observers:list_observer')
    return render (request, 'observers/observer_form.html', {'form': form})

def update_observer(request, id):
   observer = Observer.objects.get(id=id)
   form = ObserverForm(request.POST or None, instance=observer)
   if form.is_valid():
        form.save()      
        return redirect ('observers:list_observer')
   return render (request, 'observers/observer_form.html', {'form': form, 'observer':observer})

def delete_observer(request, id):
   observer = Observer.objects.get(id=id)
   
   if request.method == 'POST' :
       observer.delete()
       return redirect ('observers:list_observer')
   return render (request, 'observers/observer_confirm_delete.html', {'observer':observer})


