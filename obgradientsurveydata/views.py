from django.shortcuts import redirect, render
from numpy import sort
from obgradientsurveydata.utils import get_plot
from obgradientsurveys.models import OBGradientSurvey
from selectedObserver.models import SelectedObserver
from .models import OBGradientSurveyData
from .forms import OBGradientSurveyDataForm
from tablib import Dataset
from django.contrib import messages
 

def list_obgradientsurveydata(request, id): 
    gradientsurveyid =id  
    selectedwell = SelectedObserver.objects.first()  
    gradientsurveydatas = OBGradientSurveyData.objects.filter(obwellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
    x=[x.gauge_Pressure for x in gradientsurveydatas]
    y=[y.gauge_Depth for y in gradientsurveydatas]
    z=[z.gauge_Temperature for z in gradientsurveydatas]    
    chart = get_plot(x,y,z)
    return render (request, 'obgradientsurveydata/obgradientsurveydata.html', {'gradientsurveydatas': gradientsurveydatas, 'id':id ,'chart':chart })   

def create_obgradientsurveydata(request, id):    
   gradientsurveydata = OBGradientSurveyData()
   selectedwell = SelectedObserver.objects.first()  
   gradientsurveydata.obfgid = selectedwell.fgid
   gradientsurveydata.obwellid = selectedwell.wellid   
   gradientsurveydata.gradientsurvey_id =id   
   form = OBGradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":        
        gradientsurveydata.fgid = selectedwell.fgid
        gradientsurveydata.wellid = selectedwell.wellid  
        gradientsurveydata.gradientsurvey_id =id
        form =OBGradientSurveyDataForm(request.POST, instance=gradientsurveydata)             
        if form.is_valid():       
            form.save() 
            return redirect ('obgradientsurveydata:list_obgradientsurveydata', id) 
   return render (request, 'obgradientsurveydata/obgradientsurveydata_form.html', {'form': form, 'id':id})

def update_obgradientsurveydata(request, id):    
   gradientsurveydata = OBGradientSurveyData.objects.get(id=id)   
   form = OBGradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":
        form = OBGradientSurveyDataForm(request.POST, instance=gradientsurveydata)
        if form.is_valid():
            form.save()            
            return redirect ('obgradientsurveydata:list_obgradientsurveydata' , gradientsurveydata.gradientsurvey_id )
   return render (request, 'obgradientsurveydata/obgradientsurveydata_form.html', {'form': form, 'gradientsurvey':gradientsurveydata})

def delete_obgradientsurveydata(request, id):
   gradientsurveydata = OBGradientSurveyData.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurveydata.delete()
       return redirect ('obgradientsurveydata:list_obgradientsurveydata', gradientsurveydata.gradientsurvey_id)
   return render (request, 'obgradientsurveydata/obgradientsurveydata_confirm_delete.html', {'gradientsurveydata':gradientsurveydata, 'id':id })


def excel_upload(request, id):  
    if request.method=='None':
        selectedwell = SelectedObserver.objects.first()     
        gradientsurveydatas = OBGradientSurveyData.objects.filter(wellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
        return redirect ('obgradientsurveydata:list_obgradientsurveydata', id) 
    if request.method=="POST":
        selectedwell = SelectedObserver.objects.first() 
        olddata = OBGradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id = id).all()  
        olddata.delete()     
        dataset =Dataset()
        new_gradientsurveydata = request.FILES['postedFile']
        if not new_gradientsurveydata.name.endsobth('xlsx'):
            messages.info(request,'Please upload .xlsx file')
            return render(request, 'obgradientsurveydata/obgradientsurveydata_upload.html', {'id':id})
        if new_gradientsurveydata.name.endsobth('xlsx'):
            imported_data = dataset.load(new_gradientsurveydata.read(), format='xlsx')       
        for data in imported_data:
            value = OBGradientSurveyData(
                gradientsurvey_id = id,
                wellid = selectedwell.wellid,
                gauge_Depth =data[1],
                gauge_Pressure = data[2],
                gauge_Temperature = data[3]
            )
            value.save()
        messages.info(request,'Successfully uploaded data')
        datas = OBGradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id =id).all().order_by('gauge_Depth')            
        return render(request, 'obgradientsurveydata/obgradientsurveydata_upload.html', {'datas':datas, 'id':id}) 
    return render(request, 'obgradientsurveydata/obgradientsurveydata_upload.html',{'id':id})


