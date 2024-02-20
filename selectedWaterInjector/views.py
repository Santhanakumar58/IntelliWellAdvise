from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import SelectedWaterInjector
from .forms import SelectedWaterInjectorForm
from django.contrib  import messages


def list_selectedWaterInjector(request):
    selectedWaterInjectors = SelectedWaterInjector.objects.all()       
    return render (request, 'selectedWaterInjector/selectedWaterInjector.html', {'selectedWaterInjectors': selectedWaterInjectors})
    
def create_selectedWaterInjector(request):
   form = SelectedWaterInjectorForm(request.POST or None)
   if form.is_valid():
       form.save()       
       return redirect ('selectedWaterInjector:list_selectedWaterInjector')    
   return render (request, 'selectedWaterInjector/selectedWaterInjector_form.html', {'form': form})

def update_selectedWaterInjector(request, id):
   selectedWaterInjector = SelectedWaterInjector.objects.get(id=id)
   form = SelectedWaterInjectorForm(request.POST or None, instance=selectedWaterInjector)
   if form.is_valid():
       form.save()
       return redirect ('selectedWaterInjector:list_selectedWaterInjector')
   return render (request, 'selectedWaterInjector/selectedWaterInjector_form.html', {'form': form, 'selectedoilproducer':selectedWaterInjector})

def delete_selectedWaterInjector(request, id):
   selectedWaterInjector = SelectedWaterInjector.objects.get(id=id)   
   if request.method == 'POST' :
       selectedWaterInjector.delete()
       return redirect ('selectedWaterInjector:list_selectedWaterInjector')
   return render (request, 'selectedWaterInjector/selectedWaterInjector_confirm_delete.html', {'selectedWaterInjector':selectedWaterInjector})

def addselectedwi_ajax(request):
   rowdata = {
     'success': False,
     'wellid': None,
     'category': None,
     'wellname': None,
     'fgid': None,
     'unit': None,
     'completion': None,
     'deviation': None,     
     'inflow': None,
     'station': None,
     'header': None
     }
  
   if request.method=='POST':
      selectedWaterInjectors = SelectedWaterInjector.objects.all()  
      selectedWaterInjectors.delete()
      selectedWaterInjector = SelectedWaterInjector() 
      rowdata["wellid"] = request.POST['wellid']
      selectedWaterInjector.wellid = rowdata["wellid"]
      rowdata["category"] = request.POST['category']
      selectedWaterInjector.category = rowdata["category"]
      rowdata["wellname"] = request.POST['wellname']
      selectedWaterInjector.wellname = rowdata["wellname"]
      rowdata["fgid"] = request.POST['fgid']
      selectedWaterInjector.fgid = rowdata["fgid"]
      rowdata["unit"] = request.POST['unit']
      selectedWaterInjector.unit =rowdata["unit"]
      rowdata["completion"] = request.POST['completion']
      selectedWaterInjector.completion = rowdata["completion"]
      rowdata["deviation"] = request.POST['deviation']
      selectedWaterInjector.deviation = rowdata["deviation"]     
      rowdata["inflow"] = request.POST['inflow']
      selectedWaterInjector.inflow = rowdata["inflow"]
      rowdata["station"] = request.POST['station']
      selectedWaterInjector.station =  rowdata["station"]
      rowdata["header"] = request.POST['header']
      selectedWaterInjector.header=  rowdata["header"]        
      selectedWaterInjector.save()       
      rowdata['success'] = True
   else:
       messages.error(request, "Data Error")
   return JsonResponse(rowdata)



