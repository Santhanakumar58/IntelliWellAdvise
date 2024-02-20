from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from IntelligentOilWell.custom_context_processors import selectedfgi
from django.contrib import messages
from .models import CCEPVT 
from .forms import CCEPVTForm 
from selectedfgi.models import Selectedfgi
from sublayers.models import Sublayer
from tablib import Dataset
from .resources import CCEPVTdataResource
from .utils import get_plot





def list_ccepvt(request):
    selectedfgi = Selectedfgi.objects.first()
    ccepvts = CCEPVT.objects.filter(fgId = selectedfgi.fgid)   
    chart=get_plot()
    return render (request, 'constantcompositionexpansion/ccePVT.html', {'ccepvts': ccepvts, 'chart':chart})
    
def create_ccepvt(request):  
   selectedfgi = Selectedfgi.objects.first()   
   ccepvt = CCEPVT()
   ccepvt.fgId = selectedfgi.fgid 
   sublayer = Sublayer.objects.get(sublayername=selectedfgi.selectedsublayername)
   ccepvt.subLayer = sublayer
    
   
   form = CCEPVTForm(request.POST or None, instance=ccepvt)  
   if form.is_valid():
       form.save()       
       return redirect ('constantcompositionexpansion:list_ccepvt')    
   return render (request, 'constantcompositionexpansion/ccePVT_form.html', {'form': form})

def update_ccepvt(request, id):
   ccepvt = CCEPVT.objects.get(id=id)
   if ccepvt.subLayer == "" or ccepvt.subLayer == None:
       selectedfgi = Selectedfgi.objects.first()   
       sublayer = Sublayer.objects.get(sublayername=selectedfgi.selectedsublayername)
       ccepvt.subLayer = sublayer   
   form = CCEPVTForm(request.POST or None, instance=ccepvt)
   if form.is_valid():
       form.save()
       return redirect ('constantcompositionexpansion:list_ccepvt')
   return render (request, 'constantcompositionexpansion/ccePVT_form.html', {'form': form, 'ccepvt':ccepvt})

def delete_ccepvt(request, id):
   ccepvt = CCEPVT.objects.get(id=id)   
   if request.method == 'POST' :
       ccepvt.delete()
       return redirect ('constantcompositionexpansion:list_ccepvt')
   return render (request, 'constantcompositionexpansion/ccePVT_confirm_delete.html', {'ccepvt':ccepvt})



