from django.shortcuts import redirect, render
from numpy import sort
from wigradientsurveydata.utils import get_plot
from wigradientsurveys.models import WIGradientSurvey
from selectedWaterInjector.models import SelectedWaterInjector
from .models import WIGradientSurveyData
from .forms import WIGradientSurveyDataForm
from tablib import Dataset
from django.contrib import messages
 

def list_gradientsurveydata(request, id): 
    gradientsurveyid =id  
    selectedwell = SelectedWaterInjector.objects.first()  
    gradientsurveydatas = WIGradientSurveyData.objects.filter(wiwellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
    x=[x.gauge_Pressure for x in gradientsurveydatas]
    y=[y.gauge_Depth for y in gradientsurveydatas]
    z=[z.gauge_Temperature for z in gradientsurveydatas]    
    chart = get_plot(x,y,z)
    return render (request, 'wigradientsurveydata/wigradientsurveydata.html', {'gradientsurveydatas': gradientsurveydatas, 'id':id ,'chart':chart })   

def create_gradientsurveydata(request, id):    
   gradientsurveydata = WIGradientSurveyData()
   selectedwell = SelectedWaterInjector.objects.first()  
   gradientsurveydata.wifgid = selectedwell.fgid
   gradientsurveydata.wiwellid = selectedwell.wellid   
   gradientsurveydata.gradientsurvey_id =id   
   form = WIGradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":        
        gradientsurveydata.fgid = selectedwell.fgid
        gradientsurveydata.wellid = selectedwell.wellid  
        gradientsurveydata.gradientsurvey_id =id
        form = WIGradientSurveyDataForm(request.POST, instance=gradientsurveydata)             
        if form.is_valid():       
            form.save() 
            return redirect ('wigradientsurveydata:list_wigradientsurveydata', id) 
   return render (request, 'wigradientsurveydata/wigradientsurveydata_form.html', {'form': form, 'id':id})

def update_gradientsurveydata(request, id):    
   gradientsurveydata = WIGradientSurveyData.objects.get(id=id)   
   form = WIGradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":
        form = WIGradientSurveyDataForm(request.POST, instance=gradientsurveydata)
        if form.is_valid():
            form.save()            
            return redirect ('wigradientsurveydata:list_wigradientsurveydata' , gradientsurveydata.gradientsurvey_id )
   return render (request, 'wigradientsurveydata/wigradientsurveydata_form.html', {'form': form, 'gradientsurvey':gradientsurveydata})

def delete_gradientsurveydata(request, id):
   gradientsurveydata = WIGradientSurveyData.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurveydata.delete()
       return redirect ('wigradientsurveydata:list_wigradientsurveydata', gradientsurveydata.gradientsurvey_id)
   return render (request, 'wigradientsurveydata/wigradientsurveydata_confirm_delete.html', {'gradientsurveydata':gradientsurveydata, 'id':id })


def excel_upload(request, id):  
    if request.method=='None':
        selectedwell = SelectedWaterInjector.objects.first()     
        gradientsurveydatas = WIGradientSurveyData.objects.filter(wellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
        return redirect ('wigradientsurveydata:list_wigradientsurveydata', id) 
    if request.method=="POST":
        selectedwell = SelectedWaterInjector.objects.first() 
        olddata = WIGradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id = id).all()  
        olddata.delete()      
        dataset =Dataset()
        new_gradientsurveydata = request.FILES['postedFile']
        if not new_gradientsurveydata.name.endswith('xlsx'):
            messages.info(request,'Please upload .xlsx file')
            return render(request, 'wigradientsurveydata/wigradientsurveydata_upload.html', {'id':id})
        if new_gradientsurveydata.name.endswith('xlsx'):
            imported_data = dataset.load(new_gradientsurveydata.read(), format='xlsx')       
        for data in imported_data:
            value = WIGradientSurveyData(
                gradientsurvey_id = id,
                wellid = selectedwell.wellid,
                gauge_Depth =data[1],
                gauge_Pressure = data[2],
                gauge_Temperature = data[3]
            )
            value.save()
        messages.info(request,'Successfully uploaded data')
        datas = WIGradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id =id).all().order_by('gauge_Depth')            
        return render(request, 'wigradientsurveydata/wigradientsurveydata_upload.html', {'datas':datas, 'id':id}) 
    return render(request, 'wigradientsurveydata/wigradientsurveydata_upload.html',{'id':id})

