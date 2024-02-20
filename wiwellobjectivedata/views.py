from django.shortcuts import render, redirect
from .models import WIWellobjectivedata
from  .forms import WIWellObjectivedataForm
from django.contrib import messages
from .utils import get_plot1, get_plot2
from selectedWaterInjector.models import SelectedWaterInjector
from IntelligentOilWell.custom_context_processors import selectedwell
from wiwellobjectives.models import WIWellobjective
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage


def list_wiwellobjectivedata(request, objid):    
    objective = WIWellobjective.objects.get(id=objid) 
    wiwellobjectivedata = WIWellobjectivedata.objects.filter(wiwellobjective=objective)            
    x=[x.date for x in wiwellobjectivedata]
    y=[y.gasrate_mmscfd for y in wiwellobjectivedata]
    z=[z.cgr_barrels_per_mmscf for z in wiwellobjectivedata]
    y1=[y1.condensaterate for y1 in wiwellobjectivedata]
    y2=[y2.waterate for y2 in wiwellobjectivedata]
    y3=[y3.liquidrate for y3 in wiwellobjectivedata]
    y4=[y4.watercut_percentage for y4 in wiwellobjectivedata]  
    chart1 = get_plot1(x,y, y1)    
    chart2 = get_plot2(x,z,y2)
    context = {'wiwellobjectivedata': wiwellobjectivedata, 'chart1': chart1,'chart2': chart2, 'objid':objid}
    return render (request, 'wiwellobjectivedata/wiwellobjectivedata.html', context)

def create_wiwellobjectivedata(request, objid): 
    objective = WIWellobjective.objects.get(id=objid)   
    wiwellobjectivedata = WIWellobjectivedata()
    wiwellobjectivedata.wiwellobjective = objective   
    wiwellobjectivedata.wellid = objective.wellid  
    form = WIWellObjectivedataForm(request.POST or None, instance=wiwellobjectivedata)
    if request=="POST":
        form = WIWellObjectivedataForm(request.POST or None, instance=wiwellobjectivedata)
        if form.is_valid():        
            form.save()
            return redirect ('wiwellobjectivedata:list_wiwellobjectivedata', objid)
    return render (request, 'wiwellobjectivedata/wiwellobjectivedata_form.html', {'form': form, 'objid':objid})

def update_wiwellobjectivedata(request, id):
   wiwellobjectivedata = WIWellobjectivedata.objects.get(id=id) 
   objid = wiwellobjectivedata.giwellobjective_id
   form = WIWellObjectivedataForm(request.POST or None, instance=wiwellobjectivedata)  
   if form.is_valid():        
        wiwellobjectivedata.save()  
        objid = wiwellobjectivedata.giwellobjective_id     
        return redirect ('wiwellobjectivedata:list_wiwellobjectivedata', objid)
   return render (request, 'wiwellobjectivedata/wiwellobjectivedata_form.html', {'form': form, 'wiwellobjectivedata': wiwellobjectivedata, 'objid':objid})

def delete_wiwellobjectivedata(request, id):
    wiwellobjectivedata = WIWellobjectivedata.objects.get(id=id)    
    if request.method == 'POST' :
       wiwellobjectivedata.delete()       
       return redirect ('wiwellobjectivedata:list_wiwellobjectivedata', wiwellobjectivedata.wiwellobjectivedata)
    return render (request, 'wiwellobjectivedata/wiwellobjectivedata_confirm_delete.html', {'giwellobjectivedata':wiwellobjectivedata })


def Import_Excel_pandas(request, objid):     
    objective = WIWellobjective.objects.get(id=objid) 
    olddata = WIWellobjectivedata.objects.filter(wiwellobjective=objective) 
    olddata.delete()
    if request.method == 'POST' and request.FILES['myfile']: 
        wiwellobjective = WIWellobjective.objects.get(id=objid)
        selectedwell = SelectedWaterInjector.objects.first()   
        id = selectedwell.wellid
        widata = WIWellobjectivedata.objects.filter(giwellid = id)
        widata.delete()
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
            obj = WIWellobjectivedata.objects.create(wiwellobjective =wiwellobjective, wiwellid= id, date=dbframe.date,gasrate_mmscfd=dbframe.gasrate, 
                                                     cgr_barrels_per_mmscf=dbframe.cgr, watercut_percentage=dbframe.wc )           
            obj.save()
        return redirect ('wiwellobjectivedata:list_wiwellobjectivedata', objid)
        # return render(request, 'giwellobjectivedata/Import_excel.html', {
         #   'uploaded_file_url': uploaded_file_url
        # })   
    return render(request, 'wiwellobjectivedata/Import_excel.html',{'objid':objid})





