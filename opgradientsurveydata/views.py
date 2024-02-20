from django.shortcuts import redirect, render
from numpy import sort
from opgradientsurveydata.utils import get_plot
from opgradientsurveys.models import GradientSurvey
from selectedOilProducer.models import SelectedOilProducer
from .models import GradientSurveyData
from .forms import GradientSurveyDataForm
from .resources import GradientSurveyDataResource
from tablib import Dataset
from django.contrib import messages
gradientsurveyid =2

def list_gradientsurveydata(request, id): 
    gradientsurveyid =id  
    selectedwell = SelectedOilProducer.objects.first()  
    gradientsurveydatas = GradientSurveyData.objects.filter(wellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
    x=[x.gauge_Pressure for x in gradientsurveydatas]
    y=[y.gauge_Depth for y in gradientsurveydatas]
    z=[z.gauge_Temperature for z in gradientsurveydatas]    
    chart = get_plot(x,y,z)
    return render (request, 'opgradientsurveydata/gradientsurveydata.html', {'gradientsurveydatas': gradientsurveydatas, 'id':id ,'chart':chart })   

def create_gradientsurveydata(request, id):    
   gradientsurveydata = GradientSurveyData()
   selectedwell = SelectedOilProducer.objects.first()  
   gradientsurveydata.fgid = selectedwell.fgid
   gradientsurveydata.wellid = selectedwell.wellid   
   gradientsurveydata.gradientsurvey_id =id   
   form = GradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":        
        gradientsurveydata.fgid = selectedwell.fgid
        gradientsurveydata.wellid = selectedwell.wellid  
        gradientsurveydata.gradientsurvey_id =id
        form = GradientSurveyDataForm(request.POST, instance=gradientsurveydata)             
        if form.is_valid():       
            form.save() 
            return redirect ('opgradientsurveydata:list_gradientsurveydata', id) 
   return render (request, 'opgradientsurveydata/gradientsurveydata_form.html', {'form': form, 'id':id})

def update_gradientsurveydata(request, id):    
   gradientsurveydata = GradientSurveyData.objects.get(id=id)   
   form = GradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":
        form = GradientSurveyDataForm(request.POST, instance=gradientsurveydata)
        if form.is_valid():
            form.save()            
            return redirect ('opgradientsurveydata:list_gradientsurveydata' , gradientsurveydata.gradientsurvey_id )
   return render (request, 'opgradientsurveydata/gradientsurveydata_form.html', {'form': form, 'gradientsurvey':gradientsurveydata})

def delete_gradientsurveydata(request, id):
   gradientsurveydata = GradientSurveyData.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurveydata.delete()
       return redirect ('opgradientsurveydata:list_gradientsurveydata', gradientsurveydata.gradientsurvey_id)
   return render (request, 'opgradientsurveydata/gradientsurveydata_confirm_delete.html', {'gradientsurveydata':gradientsurveydata, 'id':id })


def excel_upload(request, id):  
    if request.method=='None':
        selectedwell = SelectedOilProducer.objects.first()     
        gradientsurveydatas = GradientSurveyData.objects.filter(wellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
        return redirect ('opgradientsurveydata:list_gradientsurveydata', id) 
    if request.method=="POST":
        selectedwell = SelectedOilProducer.objects.first() 
        olddata = GradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id = id).all()  
        olddata.delete()
        gradientsurveydata_resources = GradientSurveyDataResource()      
        dataset =Dataset()
        new_gradientsurveydata = request.FILES['postedFile']
        if not new_gradientsurveydata.name.endswith('xlsx'):
            messages.info(request,'Please upload .xlsx file')
            return render(request, 'opgradientsurveydata/gradientsurveydata_upload.html', {'id':id})
        if new_gradientsurveydata.name.endswith('xlsx'):
            imported_data = dataset.load(new_gradientsurveydata.read(), format='xlsx')       
        for data in imported_data:
            value = GradientSurveyData(
                gradientsurvey_id = id,
                wellid = selectedwell.wellid,
                gauge_Depth =data[1],
                gauge_Pressure = data[2],
                gauge_Temperature = data[3]
            )
            value.save()
        messages.info(request,'Successfully uploaded data')
        datas = GradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id =id).all().order_by('gauge_Depth')            
        return render(request, 'opgradientsurveydata/gradientsurveydata_upload.html', {'datas':datas, 'id':id}) 
    return render(request, 'opgradientsurveydata/gradientsurveydata_upload.html',{'id':id})

