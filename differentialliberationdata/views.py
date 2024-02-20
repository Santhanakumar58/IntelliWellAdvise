from django.http import JsonResponse
from django.shortcuts import render, redirect
from IntelligentOilWell.custom_context_processors import selectedfgi
from django.contrib import messages
from .models import  DifferentialLiberationdata
from .forms import DiffLibDATAForm
from tablib import Dataset
from differentialliberation.models import DifferentialLiberationModel
from openpyxl import load_workbook

import numpy as np

# Create your views here.
def list_difflibdata(request, diffid):   
    Pb=0
    difflibdatas = DifferentialLiberationdata.objects.filter(ccepvt = diffid).all()   
    model = DifferentialLiberationModel.objects.get(pk=diffid)
    temp = model.temperature
    x=[]
    y=[] 
    x1=[]
    y1=[] 
    #x1=[x.pressure for x in ccepvtdatas]
    #y1=[y.relative_volume  for y in ccepvtdatas]
    #Pb= [x.pressure for x in ccepvtdatas ]
    for data in difflibdatas:
        if data.y_function !=None:
            x.append(data.pressure)
            y.append(data.y_function) 
            
    for data in difflibdatas:
        if data.relative_volume <=1:
            x1.append(data.pressure)
            y1.append(data.relative_volume) 
    for data in difflibdatas:
        if data.relative_volume ==1:
            Pb = data.pressure 
            density_Pb =data.density
            break
    m, b = np.polyfit(x, y, 1)
    m= round(m,5)
    b= round(b,5)
    print  (f"equation : y = {m}x  + {b}")  
    print  (Pb, density_Pb, temp)  
    co = calculate_co(2000, 2500,difflibdatas )
    print(co)
    #chart = get_Multiplot(x,y, x1, y1, Pb)   
    return render (request, 'differentialliberationdata/differentialliberationdata.html', {'diffid':diffid, 'difflibdatas': difflibdatas})
    
def create_difflibdata(request,diffid): 
   difflibdata = DifferentialLiberationdata.objects.get(id=diffid)
   diffid = DifferentialLiberationdata()
   difflibdata.differentialliberation = diffid
   form = DiffLibDATAForm(request.POST or None, instance=difflibdata)  
   if form.is_valid():
       form.save()       
       return redirect ('differentialliberationdata:list_difflibdata', diffid )    
   return render (request, 'differentialliberationdata/differentialliberationdata_form.html', {'form': form, 'difflibdata':difflibdata})

def update_difflibdata(request, id):
   difflibdata = DifferentialLiberationdata.objects.get(id=id)
   diffid =(difflibdata.ccepvt).pk 
   form = DiffLibDATAForm(request.POST or None, instance=difflibdata)
   if form.is_valid():
       form.save()
       return redirect ('differentialliberationdata:list_difflibdata', diffid)
   return render (request, 'differentialliberationdata/differentialliberationdata_form.html', {'form': form, 'difflibdata':difflibdata, 'id':id})

def delete_difflibdata(request, id):
   difflibdata = DifferentialLiberationdata.objects.get(id=id)  
   diffid =(difflibdata.ccepvt).pk  
   if request.method == 'POST' :
       difflibdata.delete()
       return redirect ('differentialliberationdata:list_difflibdata',diffid )
   return render (request, 'differentialliberationdata/differentialliberationdata_confirm_delete.html', {'difflibdata':difflibdata, 'id':id})

def excel_upload_difflibdata(request,diffid ):    
    print("I am in")
    if request.method=="POST":
        dataset =Dataset()
         
        new_ccedata = request.FILES['myfile']
        if not new_ccedata.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, 'differentialliberationdata/differentialliberationdata.html', diffid)
        imported_data = dataset.load(new_ccedata.read(), format='xlsx')
        print(imported_data)
        for data in imported_data:
            value = new_ccedata(
                diffid,
                data[0],
                data[1],
                data[2],
                data[3]
                         )
            value.save()
        return render(request, 'differentialliberationdata/differentialliberationdata.html', diffid)



def calculate_co(P1, P2, datas):
    v1=0
    v2=0
    p1=0
    p2=0
    for i  in range(len(datas)):        
        if i >1 and P1 >= datas[i].pressure:
            p1 = datas[i-1].pressure
            v1 = datas[i-1].relative_volume           
            break
    for i  in range(len(datas)):        
        if i >1 and P2 >= datas[i].pressure:          
            p2 = datas[i].pressure
            v2 = datas[i].relative_volume
            break
    co = (-1/v2) *(v2-v1)/(p2-p1)        
    return co
      