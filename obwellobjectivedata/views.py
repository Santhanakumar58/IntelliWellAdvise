from django.shortcuts import render, redirect
from .models import OBWellobjectivedata
from  .forms import OBWellObjectivedataForm
from django.contrib import messages
from .utils import get_plot1, get_plot2
from selectedObserver.models import SelectedObserver
from IntelligentOilWell.custom_context_processors import selectedwell
from obwellobjectives.models import OBWellobjective
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage


def list_obwellobjectivedata(request, objid):    
    objective = OBWellobjective.objects.get(id=objid) 
    obwellobjectivedata = OBWellobjectivedata.objects.filter(obwellobjective=objective) 
    context = {'obwellobjectivedata': obwellobjectivedata, 'objid':objid}
    return render (request, 'obwellobjectivedata/obwellobjectivedata.html', context)

def create_obwellobjectivedata(request, objid): 
    objective = OBWellobjective.objects.get(id=objid)   
    obwellobjectivedata = OBWellobjectivedata()
    obwellobjectivedata.obwellobjective = objective   
    obwellobjectivedata.wellid = objective.wellid  
    form = OBWellObjectivedataForm(request.POST or None, instance=obwellobjectivedata)
    if request=="POST":
        form = OBWellObjectivedataForm(request.POST or None, instance=obwellobjectivedata)
        if form.is_valid():        
            form.save()
            return redirect ('obwellobjectivedata:list_obwellobjectivedata', objid)
    return render (request, 'obwellobjectivedata/obwellobjectivedata_form.html', {'form': form, 'objid':objid})

def update_obwellobjectivedata(request, id):
   obwellobjectivedata = OBWellobjectivedata.objects.get(id=id) 
   objid = obwellobjectivedata.gpwellobjective_id
   form = OBWellObjectivedataForm(request.POST or None, instance=obwellobjectivedata)  
   if form.is_valid():        
        obwellobjectivedata.save()  
        objid = obwellobjectivedata.obwellobjective_id     
        return redirect ('obwellobjectivedata:list_obwellobjectivedata', objid)
   return render (request, 'obwellobjectivedata/obwellobjectivedata_form.html', {'form': form, 'obwellobjectivedata': obwellobjectivedata, 'objid':objid})

def delete_obwellobjectivedata(request, id):
    obwellobjectivedata = OBWellobjectivedata.objects.get(id=id)    
    if request.method == 'POST' :
       obwellobjectivedata.delete()       
       return redirect ('obwellobjectivedata:list_obwellobjectivedata', obwellobjectivedata.obwellobjective_id)
    return render (request, 'obwellobjectivedata/obwellobjectivedata_confirm_delete.html', {'obwellobjectivedata':obwellobjectivedata })


def Import_Excel_pandas(request, objid):     
    objective = OBWellobjective.objects.get(id=objid) 
    olddata = OBWellobjectivedata.objects.filter(obwellobjective=objective) 
    olddata.delete()
    if request.method == 'POST' and request.FILES['myfile']: 
        obwellobjective = OBWellobjective.objects.get(id=objid)
        selectedwell = SelectedObserver.objects.first()   
        id = selectedwell.wellid
        gpdata = OBWellobjectivedata.objects.filter(gpwellid = id)
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
            obj = OBWellobjectivedata.objects.create(obwellobjective =obwellobjective, gpwellid= id, date=dbframe.date,gasrate_mmscfd=dbframe.gasrate, 
                                                     cgr_barrels_per_mmscf=dbframe.cgr, watercut_percentage=dbframe.wc )           
            obj.save()
        return redirect ('obwellobjectivedata:list_obwellobjectivedata', objid)
        # return render(request, 'gpwellobjectivedata/Import_excel.html', {
         #   'uploaded_file_url': uploaded_file_url
        # })   
    return render(request, 'obwellobjectivedata/Import_excel.html',{'objid':objid})




 
