from django.shortcuts import render, redirect
from .models import OPWellobjectivedata
from  .forms import OPWellObjectivedataForm
from django.contrib import messages
from .utils import get_plot
from selectedOilProducer.models import SelectedOilProducer
from IntelligentOilWell.custom_context_processors import selectedwell
from opwellobjectives.models import OPWellobjective
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage



def list_opwellobjectivedata(request, objid):    
    objective = OPWellobjective.objects.get(id=objid) 
    opwellobjectivedata = OPWellobjectivedata.objects.filter(opwellobjective=objective)            
    x=[x.date for x in opwellobjectivedata]
    y=[y.gasrate/1000 for y in opwellobjectivedata]
    z=[z.gasoilratio for z in opwellobjectivedata]
    y1=[y1.oilrate for y1 in opwellobjectivedata]
    y2=[y2.waterate for y2 in opwellobjectivedata]
    y3=[y3.liquidrate for y3 in opwellobjectivedata] 
    chart = get_plot(x,y,z,y1, y2, y3)
    context = {'opwellobjectivedata': opwellobjectivedata, 'chart': chart, 'objid':objid}
    return render (request, 'opwellobjectivedata/opwellobjectivedata.html', context)

def create_opwellobjectivedata(request, objid): 
    objective = OPWellobjective.objects.get(id=objid)   
    opwellobjectivedata = OPWellobjectivedata()
    opwellobjectivedata.opwellobjective = objective   
    opwellobjectivedata.wellid = objective.wellid  
    form = OPWellObjectivedataForm(request.POST or None, instance=opwellobjectivedata)
    if request=="POST":
        form = OPWellObjectivedataForm(request.POST or None, instance=opwellobjectivedata)
        if form.is_valid():        
            form.save()
            return redirect ('opwellobjectivedata:list_opwellobjectivedata', objid)
    return render (request, 'opwellobjectivedata/opwellobjectivedata_form.html', {'form': form, 'objid':objid})

def update_opwellobjectivedata(request, id):
   opwellobjectivedata = OPWellobjectivedata.objects.get(id=id) 
   objid = opwellobjectivedata.opwellobjective_id
   form = OPWellObjectivedataForm(request.POST or None, instance=opwellobjectivedata)  
   if form.is_valid():        
        opwellobjectivedata.save()  
        objid = opwellobjectivedata.opwellobjective_id     
        return redirect ('opwellobjectivedata:list_opwellobjectivedata', objid)
   return render (request, 'opwellobjectivedata/opwellobjectivedata_form.html', {'form': form, 'opwellobjectivedata': opwellobjectivedata, 'objid':objid})

def delete_opwellobjectivedata(request, id):
    opwellobjectivedata = OPWellobjectivedata.objects.get(id=id)    
    if request.method == 'POST' :
       opwellobjectivedata.delete()       
       return redirect ('opwellobjectivedata:list_opwellobjectivedata', opwellobjectivedata.opwellobjective_id)
    return render (request, 'opwellobjectivedata/opwellobjectivedata_confirm_delete.html', {'opwellobjectivedata':opwellobjectivedata })


def Import_Excel_pandas(request, objid):     
    if request.method == 'POST' and request.FILES['myfile']: 
        opwellobjective = OPWellobjective.objects.get(id=objid)
        selectedwell = SelectedOilProducer.objects.first()   
        id = selectedwell.wellid
        opdata = OPWellobjectivedata.objects.filter(wellid = id)
        opdata.delete()
        myfile = request.FILES['myfile']       
        fs = FileSystemStorage()
        filename = fs.save('profiledata/'+myfile.name, myfile)
        uploaded_file_url = fs.url(filename)   
        d = os.getcwd()  
        filepath = d+'\media\\'+ filename      
        empexceldata = pd.read_excel(filepath)       
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = OPWellobjectivedata.objects.create(opwellobjective =opwellobjective, wellid= id, date=dbframe.date,liquidrate=dbframe.liquidrate, watercut=dbframe.watercut,
                                            gasoilratio=dbframe.gasoilratio )           
            obj.save()
        return render(request, 'opwellobjectivedata/Import_excel.html', {
            'uploaded_file_url': uploaded_file_url
        })   
    return render(request, 'opwellobjectivedata/Import_excel.html',{'objid':objid})




 