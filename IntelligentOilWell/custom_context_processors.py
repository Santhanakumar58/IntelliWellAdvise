from django.shortcuts import render
from selectedOilProducer.models import SelectedOilProducer
from selectedGasProducer.models import SelectedGasProducer
from selectedWaterInjector.models import SelectedWaterInjector
from selectedGasInjector.models import SelectedGasInjector
from selectedObserver.models import SelectedObserver
from selectedfgi.models import Selectedfgi
from blackoilpvt.models import BlackoilPVT


def selectedfgi(request):   
    return {'selectedfgi': Selectedfgi.objects.first() }


def selectedwell(request): 
    selectedwell = SelectedOilProducer.objects.all().first()      
    return  {'selectedwell': selectedwell}

def selectedgpwell(request): 
    selectedgpwell = SelectedGasProducer.objects.all().first()      
    return  {'selectedgpwell': selectedgpwell}

def selectedwiwell(request): 
    selectedwiwell = SelectedWaterInjector.objects.all().first()      
    return  {'selectedwiwell': selectedwiwell}

def selectedgiwell(request): 
    selectedgiwell = SelectedGasInjector.objects.all().first()      
    return  {'selectedgiwell': selectedgiwell}

def selectedobwell(request): 
    selectedobwell = SelectedObserver.objects.all().first()      
    return  {'selectedobwell': selectedobwell}

def  PVTwells(request):     
    fgi =Selectedfgi.objects.first()   
    pvt_wells = BlackoilPVT.objects.filter(fgid = fgi.fgid).all()  
    return  {'pvt_wells': pvt_wells}

 