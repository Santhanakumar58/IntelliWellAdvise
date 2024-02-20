from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import SelectedObserver
from .forms import SelectedObserverForm
from django.contrib  import messages


def list_selectedObserver(request):
    selectedObservers = SelectedObserver.objects.all()       
    return render (request, 'selectedObserver/selectedObserver.html', {'selectedObservers': selectedObservers})
    
def create_selectedObserver(request):
   form = SelectedObserverForm(request.POST or None)
   if form.is_valid():
       form.save()       
       return redirect ('selectedObserver:list_selectedObserver')    
   return render (request, 'selectedObserver/selectedObserver_form.html', {'form': form})

def update_selectedObserver(request, id):
   selectedObserver = SelectedObserver.objects.get(id=id)
   form = SelectedObserverForm(request.POST or None, instance=selectedObserver)
   if form.is_valid():
       form.save()
       return redirect ('selectedObserver:list_selectedObserver')
   return render (request, 'selectedObserver/selectedObserver_form.html', {'form': form, 'selectedoilproducer':selectedObserver})

def delete_selectedObserver(request, id):
   selectedObserver = SelectedObserver.objects.get(id=id)   
   if request.method == 'POST' :
       selectedObserver.delete()
       return redirect ('selectedObserver:list_selectedObserver')
   return render (request, 'selectedObserver/selectedObserver_confirm_delete.html', {'selectedObserver':selectedObserver})

def addselectedob_ajax(request):
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
      selectedObservers = SelectedObserver.objects.all()  
      selectedObservers.delete()
      selectedObserver = SelectedObserver() 
      rowdata["wellid"] = request.POST['wellid']
      selectedObserver.wellid = rowdata["wellid"]
      rowdata["category"] = request.POST['category']
      selectedObserver.category = rowdata["category"]
      rowdata["wellname"] = request.POST['wellname']
      selectedObserver.wellname = rowdata["wellname"]
      rowdata["fgid"] = request.POST['fgid']
      selectedObserver.fgid = rowdata["fgid"]
      rowdata["unit"] = request.POST['unit']
      selectedObserver.unit =rowdata["unit"]
      rowdata["completion"] = request.POST['completion']
      selectedObserver.completion = rowdata["completion"]
      rowdata["deviation"] = request.POST['deviation']
      selectedObserver.deviation = rowdata["deviation"]
      rowdata["al"] = request.POST['al']
      selectedObserver.artificiallift = rowdata["al"]
      rowdata["inflow"] = request.POST['inflow']
      selectedObserver.inflow = rowdata["inflow"]
      rowdata["station"] = request.POST['station']
      selectedObserver.station =  rowdata["station"]
      rowdata["header"] = request.POST['header']
      selectedObserver.header=  rowdata["header"]        
      selectedObserver.save()       
      rowdata['success'] = True
   else:
       messages.error(request, "Data Error")
   return JsonResponse(rowdata)


