from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import SelectedGasProducer
from .forms import SelectedGasProducerForm
from django.contrib  import messages


def list_selectedGasProducer(request):
    selectedGasProducers = SelectedGasProducer.objects.all()       
    return render (request, 'selectedGasProducer/selectedGasProducer.html', {'selectedGasProducers': selectedGasProducers})
    
def create_selectedGasProducer(request):
   form = SelectedGasProducerForm(request.POST or None)
   if form.is_valid():
       form.save()       
       return redirect ('selectedGasProducer:list_selectedGasProducer')    
   return render (request, 'selectedGasProducer/selectedGasProducer_form.html', {'form': form})

def update_selectedGasProducer(request, id):
   selectedGasProducer = SelectedGasProducer.objects.get(id=id)
   form = SelectedGasProducerForm(request.POST or None, instance=selectedGasProducer)
   if form.is_valid():
       form.save()
       return redirect ('selectedGasProducer:list_selectedGasProducer')
   return render (request, 'selectedGasProducer/selectedGasProducer_form.html', {'form': form, 'selectedGasProducer':selectedGasProducer})

def delete_selectedGasProducer(request, id):
   selectedGasProducer = SelectedGasProducer.objects.get(id=id)   
   if request.method == 'POST' :
       selectedGasProducer.delete()
       return redirect ('selectedGasProducer:list_selectedGasProducer')
   return render (request, 'selectedGasProducer/selectedGasProducer_confirm_delete.html', {'selectedGasProducer':selectedGasProducer})

def addselectedgp_ajax(request):
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
      selectedGasProducers = SelectedGasProducer.objects.all()  
      selectedGasProducers.delete()
      selectedGasProducer = SelectedGasProducer() 
      rowdata["wellid"] = request.POST['wellid']
      selectedGasProducer.wellid = rowdata["wellid"]
      rowdata["category"] = request.POST['category']
      selectedGasProducer.category = rowdata["category"]
      rowdata["wellname"] = request.POST['wellname']
      selectedGasProducer.wellname = rowdata["wellname"]
      rowdata["fgid"] = request.POST['fgid']
      selectedGasProducer.fgid = rowdata["fgid"]
      rowdata["unit"] = request.POST['unit']
      selectedGasProducer.unit =rowdata["unit"]
      rowdata["completion"] = request.POST['completion']
      selectedGasProducer.completion = rowdata["completion"]
      rowdata["deviation"] = request.POST['deviation']
      selectedGasProducer.deviation = rowdata["deviation"]    
      rowdata["inflow"] = request.POST['inflow']
      selectedGasProducer.inflow = rowdata["inflow"]
      rowdata["station"] = request.POST['station']
      selectedGasProducer.station =  rowdata["station"]
      rowdata["header"] = request.POST['header']
      selectedGasProducer.header=  rowdata["header"]        
      selectedGasProducer.save() 
      rowdata['success'] = True
   else:
       messages.error(request, "Data Error")
   return JsonResponse(rowdata)



