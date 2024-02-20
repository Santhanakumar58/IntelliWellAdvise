from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Selectedfgi
from .forms import SelectedfgiForm
from fgis.models import FGIModel
from blocks.models import Block
from assets.models import Asset

def list_selectedfgi(request):
    selectedfgis = Selectedfgi.objects.all()
    if selectedfgis :
       selectedfgis =selectedfgis
    else:
       fgis = FGIModel.objects.all()
       selectedfgis= fgis    
    return render (request, 'selectedfgi/selectedfgi.html', {'selectedfgis': selectedfgis})
  
def create_selectedfgi(request):
   form = SelectedfgiForm(request.POST or None)
   if form.is_valid():       
       form.save()
       return JsonResponse({'status':"Saved"})
   else:
        JsonResponse({'status':"Failed"})      
   return render (request, 'selectedfgi/selectedfgi_form.html', {'form': form})

def update_selectedfgi(request, id):
   selectedfgi = Selectedfgi.objects.get(id=id)
   form = SelectedfgiForm(request.POST or None, instance=selectedfgi)

   if form.is_valid():
       form.save()
       return redirect ('selectedfgi:list_selectedfgi')
   return render (request, 'selectedfgi/selectedfgi_form.html', {'form': form, 'selectedfgi':selectedfgi})

def delete_selectedfgi(request, id):
   selectedfgi = Selectedfgi.objects.get(id=id)
   
   if request.method == 'POST' :
       selectedfgi.delete()
       return redirect ('selectedfgi:list_selectedfgi')
   return render (request, 'selectedfgi/selectedfgi_confirm_delete.html', {'selectedfgi':selectedfgi})

def addselectedfgi_ajax(request):
   data ={'success':False}
   if request.method=='POST':       
      selectedfgis= Selectedfgi.objects.all()
      selectedfgis.delete()
      selectedfgi = Selectedfgi()   
      selectedfgi.fgid = request.POST.get("fgid")
      selectedfgi.selectedassetname = request.POST.get("asset")  
      selectedfgi.selectedblockname = request.POST.get("block")
      selectedfgi.selectedfieldname = request.POST.get("field")
      selectedfgi.selectedlayername =request.POST.get("layer") 
      selectedfgi.selectedsublayername = request.POST.get("sublayer")
      selectedfgi.save()     
   else:
       messages.error(request, "Data Error")
   return JsonResponse(data)

def addselectedfgi_ajax1(request):
   rowdata = {
     'success': False,
     'fgid': None,
     'asset': None,
     'block': None,
     'oilfield': None,
     'layer': None,
     'sublayer': None}
   
   if request.method=='POST':       
      selectedfgis= Selectedfgi.objects.all()
      selectedfgis.delete()
      selectedfgi = Selectedfgi()      
      rowdata['fgid'] = request.POST.get("fgid")
      selectedfgi.fgid = rowdata['fgid']      
      rowdata['asset'] = request.POST.get("asset")
      selectedfgi.selectedassetname = rowdata['asset']
      rowdata['block'] = request.POST.get("block")
      selectedfgi.selectedblockname = rowdata['block']
      rowdata['oilfield'] = request.POST.get("oilfield")
      selectedfgi.selectedfieldname = rowdata['oilfield']
      rowdata['layer'] = request.POST.get("layer")
      selectedfgi.selectedlayername = rowdata['layer']
      rowdata['sublayer'] = request.POST.get("sublayer")
      selectedfgi.selectedsublayername = rowdata['sublayer']    
      selectedfgi.save()  
   else:
       messages.error(request, "Data Error")
   return JsonResponse(rowdata)
