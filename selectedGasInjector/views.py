from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import SelectedGasInjector
from .forms import SelectedGasInjectorForm
from django.contrib  import messages
from IntelligentOilWell.custom_context_processors import SelectedGasInjector


def list_selectedGasInjector(request):
    selectedGasInjectors = SelectedGasInjector.objects.all()       
    return render (request, 'selectedGasInjector/selectedGasInjector.html', {'selectedGasInjectors': selectedGasInjectors})
    
def create_selectedGasInjector(request):
   form = SelectedGasInjectorForm(request.POST or None)
   if form.is_valid():
       form.save()       
       return redirect ('selectedGasInjector:list_selectedGasInjector')    
   return render (request, 'selectedGasInjector/selectedGasInjector_form.html', {'form': form})

def update_selectedGasInjector(request, id):
   selectedGasInjector = SelectedGasInjector.objects.get(id=id)
   form = SelectedGasInjectorForm(request.POST or None, instance=selectedGasInjector)
   if form.is_valid():
       form.save()
       return redirect ('selectedGasInjector:list_selectedGasInjector')
   return render (request, 'selectedGasInjector/selectedGasInjector_form.html', {'form': form, 'selectedGasInjector':selectedGasInjector})

def delete_selectedGasInjector(request, id):
   selectedGasInjector = SelectedGasInjector.objects.get(id=id)   
   if request.method == 'POST' :
       selectedGasInjector.delete()
       return redirect ('selectedGasInjector:list_selectedGasInjector')
   return render (request, 'selectedGasInjector/selectedGasInjector_confirm_delete.html', {'selectedGasInjector':selectedGasInjector})

def addselectedgi_ajax(request):
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
      selectedGasInjectors = SelectedGasInjector.objects.all()  
      selectedGasInjectors.delete()
      selectedGasInjector = SelectedGasInjector() 
      rowdata["wellid"] = request.POST['wellid']
      selectedGasInjector.wellid = rowdata["wellid"]
      rowdata["category"] = request.POST['category']
      selectedGasInjector.category = rowdata["category"]
      rowdata["wellname"] = request.POST['wellname']
      selectedGasInjector.wellname = rowdata["wellname"]
      rowdata["fgid"] = request.POST['fgid']
      selectedGasInjector.fgid = rowdata["fgid"]
      rowdata["unit"] = request.POST['unit']
      selectedGasInjector.unit =rowdata["unit"]
      rowdata["completion"] = request.POST['completion']
      selectedGasInjector.completion = rowdata["completion"]
      rowdata["deviation"] = request.POST['deviation']
      selectedGasInjector.deviation = rowdata["deviation"]    
      rowdata["inflow"] = request.POST['inflow']
      selectedGasInjector.inflow = rowdata["inflow"]
      rowdata["station"] = request.POST['station']
      selectedGasInjector.station =  rowdata["station"]
      rowdata["header"] = request.POST['header']
      selectedGasInjector.header=  rowdata["header"]        
      selectedGasInjector.save() 
      rowdata['success'] = True
   else:
       messages.error(request, "Data Error")
   return JsonResponse(rowdata)




