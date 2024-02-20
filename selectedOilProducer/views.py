from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import SelectedOilProducer
from .forms import SelectedOilProducerForm
from django.contrib  import messages


def list_selectedOilProducer(request):
    selectedOilProducers = SelectedOilProducer.objects.all()       
    return render (request, 'selectedOilProducer/selectedOilProducer.html', {'selectedOilProducers': selectedOilProducers})
    
def create_selectedOilProducer(request):
   form = SelectedOilProducerForm(request.POST or None)
   if form.is_valid():
       form.save()       
       return redirect ('selectedOilProducer:list_selectedOilProducer')    
   return render (request, 'selectedOilProducer/selectedOilProducer_form.html', {'form': form})

def update_selectedOilProducer(request, id):
   selectedOilProducer = SelectedOilProducer.objects.get(id=id)
   form = SelectedOilProducerForm(request.POST or None, instance=selectedOilProducer)
   if form.is_valid():
       form.save()
       return redirect ('selectedOilProducer:list_selectedOilProducer')
   return render (request, 'selectedOilProducer/selectedOilProducer_form.html', {'form': form, 'selectedoilproducer':selectedOilProducer})

def delete_selectedOilProducer(request, id):
   selectedOilProducer = SelectedOilProducer.objects.get(id=id)   
   if request.method == 'POST' :
       selectedOilProducer.delete()
       return redirect ('selectedOilProducer:list_selectedOilProducer')
   return render (request, 'selectedOilProducer/selectedOilProducer_confirm_delete.html', {'selectedOilProducer':selectedOilProducer})

def addselectedop_ajax(request):
   rowdata = {
     'success': False,
     'wellid': None,
     'category': None,
     'wellname': None,
     'fgid': None,
     'unit': None,
     'completion': None,
     'deviation': None,
     'artificiallift': None,
     'inflow': None,
     'station': None,
     'header': None
     }
  
   if request.method=='POST':
      selectedOilProducers = SelectedOilProducer.objects.all()  
      selectedOilProducers.delete()
      selectedOilProducer = SelectedOilProducer() 
      rowdata["wellid"] = request.POST['wellid']
      selectedOilProducer.wellid = rowdata["wellid"]
      rowdata["category"] = request.POST['category']
      selectedOilProducer.category = rowdata["category"]
      rowdata["wellname"] = request.POST['wellname']
      selectedOilProducer.wellname = rowdata["wellname"]
      rowdata["fgid"] = request.POST['fgid']
      selectedOilProducer.fgid = rowdata["fgid"]
      rowdata["unit"] = request.POST['unit']
      selectedOilProducer.unit =rowdata["unit"]
      rowdata["completion"] = request.POST['completion']
      selectedOilProducer.completion = rowdata["completion"]
      rowdata["deviation"] = request.POST['deviation']
      selectedOilProducer.deviation = rowdata["deviation"]
      rowdata["al"] = request.POST['al']
      selectedOilProducer.artificiallift = rowdata["al"]
      rowdata["inflow"] = request.POST['inflow']
      selectedOilProducer.inflow = rowdata["inflow"]
      rowdata["station"] = request.POST['station']
      selectedOilProducer.station =  rowdata["station"]
      rowdata["header"] = request.POST['header']
      selectedOilProducer.header=  rowdata["header"]        
      selectedOilProducer.save()      
      rowdata['success'] = True
   else:
       messages.error(request, "Data Error")
   return JsonResponse(rowdata)


