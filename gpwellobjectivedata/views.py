from django.shortcuts import render, redirect
from .models import GPWellobjectivedata
from  .forms import GPWellObjectivedataForm
from django.contrib import messages
from .utils import get_plot1, get_plot2
from selectedGasProducer.models import SelectedGasProducer
from IntelligentOilWell.custom_context_processors import selectedwell
from gpwellobjectives.models import GPWellobjective
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage


def list_gpwellobjectivedata(request, objid):    
    objective = GPWellobjective.objects.get(id=objid) 
    gpwellobjectivedata = GPWellobjectivedata.objects.filter(gpwellobjective=objective)            
    x=[x.date for x in gpwellobjectivedata]
    y=[y.gasrate_mmscfd for y in gpwellobjectivedata]
    z=[z.cgr_barrels_per_mmscf for z in gpwellobjectivedata]
    y1=[y1.condensaterate for y1 in gpwellobjectivedata]
    y2=[y2.waterate for y2 in gpwellobjectivedata]
    y3=[y3.liquidrate for y3 in gpwellobjectivedata]
    y4=[y4.watercut_percentage for y4 in gpwellobjectivedata]  
    chart1 = get_plot1(x,y, y1)    
    chart2 = get_plot2(x,z,y2)
    context = {'gpwellobjectivedata': gpwellobjectivedata, 'chart1': chart1,'chart2': chart2, 'objid':objid}
    return render (request, 'gpwellobjectivedata/gpwellobjectivedata.html', context)

def create_gpwellobjectivedata(request, objid): 
    objective = GPWellobjective.objects.get(id=objid)   
    gpwellobjectivedata = GPWellobjectivedata()
    gpwellobjectivedata.gpwellobjective = objective   
    gpwellobjectivedata.wellid = objective.wellid  
    form = GPWellObjectivedataForm(request.POST or None, instance=gpwellobjectivedata)
    if request=="POST":
        form = GPWellObjectivedataForm(request.POST or None, instance=gpwellobjectivedata)
        if form.is_valid():        
            form.save()
            return redirect ('gpwellobjectivedata:list_gpwellobjectivedata', objid)
    return render (request, 'gpwellobjectivedata/gpwellobjectivedata_form.html', {'form': form, 'objid':objid})

def update_gpwellobjectivedata(request, id):
   gpwellobjectivedata = GPWellobjectivedata.objects.get(id=id) 
   objid = gpwellobjectivedata.gpwellobjective_id
   form = GPWellObjectivedataForm(request.POST or None, instance=gpwellobjectivedata)  
   if form.is_valid():        
        gpwellobjectivedata.save()  
        objid = gpwellobjectivedata.gpwellobjective_id     
        return redirect ('gpwellobjectivedata:list_gpwellobjectivedata', objid)
   return render (request, 'gpwellobjectivedata/gpwellobjectivedata_form.html', {'form': form, 'gpwellobjectivedata': gpwellobjectivedata, 'objid':objid})

def delete_gpwellobjectivedata(request, id):
    gpwellobjectivedata = GPWellobjectivedata.objects.get(id=id)    
    if request.method == 'POST' :
       gpwellobjectivedata.delete()       
       return redirect ('gpwellobjectivedata:list_gpwellobjectivedata', gpwellobjectivedata.gpwellobjective_id)
    return render (request, 'gpwellobjectivedata/gpwellobjectivedata_confirm_delete.html', {'gpwellobjectivedata':gpwellobjectivedata })


def Import_Excel_pandas(request, objid):     
    objective = GPWellobjective.objects.get(id=objid) 
    olddata = GPWellobjectivedata.objects.filter(gpwellobjective=objective) 
    olddata.delete()
    if request.method == 'POST' and request.FILES['myfile']: 
        gpwellobjective = GPWellobjective.objects.get(id=objid)
        selectedwell = SelectedGasProducer.objects.first()   
        id = selectedwell.wellid
        gpdata = GPWellobjectivedata.objects.filter(gpwellid = id)
        gpdata.delete()
        myfile = request.FILES['myfile']       
        fs = FileSystemStorage()
        filename = fs.save('profiledata/'+myfile.name, myfile)
        uploaded_file_url = fs.url(filename)   
        d = os.getcwd()  
        filepath = d+'\media\\'+ filename   
        print(filepath)   
        empexceldata = pd.read_excel(filepath)       
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = GPWellobjectivedata.objects.create(gpwellobjective =gpwellobjective, gpwellid= id, date=dbframe.date,gasrate_mmscfd=dbframe.gasrate, 
                                                     cgr_barrels_per_mmscf=dbframe.cgr, watercut_percentage=dbframe.wc )           
            obj.save()
        return redirect ('gpwellobjectivedata:list_gpwellobjectivedata', objid)
        # return render(request, 'gpwellobjectivedata/Import_excel.html', {
         #   'uploaded_file_url': uploaded_file_url
        # })   
    return render(request, 'gpwellobjectivedata/Import_excel.html',{'objid':objid})




 
