from django.shortcuts import render, redirect
from .models import GIWellobjectivedata
from  .forms import GIWellObjectivedataForm
from django.contrib import messages
from .utils import get_plot1, get_plot2
from selectedGasInjector.models import SelectedGasInjector
from IntelligentOilWell.custom_context_processors import selectedwell
from giwellobjectives.models import GIWellobjective
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage


def list_giwellobjectivedata(request, objid):    
    objective = GIWellobjective.objects.get(id=objid) 
    giwellobjectivedata = GIWellobjectivedata.objects.filter(giwellobjective=objective)            
    x=[x.date for x in giwellobjectivedata]
    y=[y.gasrate_mmscfd for y in giwellobjectivedata]
    z=[z.cgr_barrels_per_mmscf for z in giwellobjectivedata]
    y1=[y1.condensaterate for y1 in giwellobjectivedata]
    y2=[y2.waterate for y2 in giwellobjectivedata]
    y3=[y3.liquidrate for y3 in giwellobjectivedata]
    y4=[y4.watercut_percentage for y4 in giwellobjectivedata]  
    chart1 = get_plot1(x,y, y1)    
    chart2 = get_plot2(x,z,y2)
    context = {'giwellobjectivedata': giwellobjectivedata, 'chart1': chart1,'chart2': chart2, 'objid':objid}
    return render (request, 'giwellobjectivedata/giwellobjectivedata.html', context)

def create_giwellobjectivedata(request, objid): 
    objective = GIWellobjective.objects.get(id=objid)   
    giwellobjectivedata = GIWellobjectivedata()
    giwellobjectivedata.giwellobjective = objective   
    giwellobjectivedata.wellid = objective.wellid  
    form = GIWellObjectivedataForm(request.POST or None, instance=giwellobjectivedata)
    if request=="POST":
        form = GIWellObjectivedataForm(request.POST or None, instance=giwellobjectivedata)
        if form.is_valid():        
            form.save()
            return redirect ('giwellobjectivedata:list_giwellobjectivedata', objid)
    return render (request, 'giwellobjectivedata/giwellobjectivedata_form.html', {'form': form, 'objid':objid})

def update_giwellobjectivedata(request, id):
   giwellobjectivedata = GIWellobjectivedata.objects.get(id=id) 
   objid = giwellobjectivedata.giwellobjective_id
   form = GIWellObjectivedataForm(request.POST or None, instance=giwellobjectivedata)  
   if form.is_valid():        
        giwellobjectivedata.save()  
        objid = giwellobjectivedata.giwellobjective_id     
        return redirect ('giwellobjectivedata:list_giwellobjectivedata', objid)
   return render (request, 'giwellobjectivedata/giwellobjectivedata_form.html', {'form': form, 'giwellobjectivedata': giwellobjectivedata, 'objid':objid})

def delete_giwellobjectivedata(request, id):
    giwellobjectivedata = GIWellobjectivedata.objects.get(id=id)    
    if request.method == 'POST' :
       giwellobjectivedata.delete()       
       return redirect ('giwellobjectivedata:list_giwellobjectivedata', giwellobjectivedata.giwellobjectivedata)
    return render (request, 'giwellobjectivedata/giwellobjectivedata_confirm_delete.html', {'giwellobjectivedata':giwellobjectivedata })


def Import_Excel_pandas(request, objid):     
    objective = GIWellobjective.objects.get(id=objid) 
    olddata = GIWellobjectivedata.objects.filter(giwellobjective=objective) 
    olddata.delete()
    if request.method == 'POST' and request.FILES['myfile']: 
        giwellobjective = GIWellobjective.objects.get(id=objid)
        selectedwell = SelectedGasInjector.objects.first()   
        id = selectedwell.wellid
        gpdata = GIWellobjectivedata.objects.filter(giwellid = id)
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
            obj = GIWellobjectivedata.objects.create(giwellobjective =giwellobjective, giwellid= id, date=dbframe.date,gasrate_mmscfd=dbframe.gasrate, 
                                                     cgr_barrels_per_mmscf=dbframe.cgr, watercut_percentage=dbframe.wc )           
            obj.save()
        return redirect ('gpwellobjectivedata:list_giwellobjectivedata', objid)
        # return render(request, 'giwellobjectivedata/Import_excel.html', {
         #   'uploaded_file_url': uploaded_file_url
        # })   
    return render(request, 'giwellobjectivedata/Import_excel.html',{'objid':objid})




 

