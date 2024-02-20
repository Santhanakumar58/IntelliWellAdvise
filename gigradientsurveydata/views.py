from django.shortcuts import redirect, render
from numpy import sort
from .utils import get_plot
from selectedGasInjector.models import SelectedGasInjector
from .models import GIGradientSurveyData
from .forms import GIGradientSurveyDataForm
from .resources import GIGradientSurveyDataResource
from tablib import Dataset
from django.contrib import messages
 

def list_gigradientsurveydata(request, id): 
    gradientsurveyid =id  
    selectedwell = SelectedGasInjector.objects.first()  
    gradientsurveydatas = GIGradientSurveyData.objects.filter(giwellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
    x=[x.gauge_Pressure for x in gradientsurveydatas]
    y=[y.gauge_Depth for y in gradientsurveydatas]
    z=[z.gauge_Temperature for z in gradientsurveydatas]    
    chart = get_plot(x,y,z)
    return render (request, 'gigradientsurveydata/gigradientsurveydata.html', {'gradientsurveydatas': gradientsurveydatas, 'id':id ,'chart':chart })   

def create_gigradientsurveydata(request, id):    
   gradientsurveydata = GIGradientSurveyData()
   selectedwell = SelectedGasInjector.objects.first()  
   gradientsurveydata.gifgid = selectedwell.fgid
   gradientsurveydata.giwellid = selectedwell.wellid   
   gradientsurveydata.gradientsurvey_id =id   
   form = GIGradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":        
        gradientsurveydata.fgid = selectedwell.fgid
        gradientsurveydata.wellid = selectedwell.wellid  
        gradientsurveydata.gradientsurvey_id =id
        form = GIGradientSurveyDataForm(request.POST, instance=gradientsurveydata)             
        if form.is_valid():       
            form.save() 
            return redirect ('gigradientsurveydata:list_gigradientsurveydata', id) 
   return render (request, 'gigradientsurveydata/gigradientsurveydata_form.html', {'form': form, 'id':id})

def update_gigradientsurveydata(request, id):    
   gradientsurveydata = GIGradientSurveyData.objects.get(id=id)   
   form = GIGradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":
        form = GIGradientSurveyDataForm(request.POST, instance=gradientsurveydata)
        if form.is_valid():
            form.save()            
            return redirect ('gigradientsurveydata:list_gigradientsurveydata' , gradientsurveydata.gradientsurvey_id )
   return render (request, 'gigradientsurveydata/gigradientsurveydata_form.html', {'form': form, 'gradientsurvey':gradientsurveydata})

def delete_gigradientsurveydata(request, id):
   gradientsurveydata = GIGradientSurveyData.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurveydata.delete()
       return redirect ('gigradientsurveydata:list_gigradientsurveydata', gradientsurveydata.gradientsurvey_id)
   return render (request, 'gigradientsurveydata/gigradientsurveydata_confirm_delete.html', {'gradientsurveydata':gradientsurveydata, 'id':id })


def excel_upload(request, id):  
    if request.method=='None':
        selectedwell = SelectedGasInjector.objects.first()     
        gradientsurveydatas = GIGradientSurveyData.objects.filter(wellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
        return redirect ('gigradientsurveydata:list_gigradientsurveydata', id) 
    if request.method=="POST":
        selectedwell = SelectedGasInjector.objects.first() 
        olddata = GIGradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id = id).all()  
        olddata.delete()
        gradientsurveydata_resources = GIGradientSurveyDataResource()      
        dataset =Dataset()
        new_gradientsurveydata = request.FILES['postedFile']
        if not new_gradientsurveydata.name.endsgith('xlsx'):
            messages.info(request,'Please upload .xlsx file')
            return render(request, 'gigradientsurveydata/gigradientsurveydata_upload.html', {'id':id})
        if new_gradientsurveydata.name.endsgith('xlsx'):
            imported_data = dataset.load(new_gradientsurveydata.read(), format='xlsx')       
        for data in imported_data:
            value = GIGradientSurveyData(
                gradientsurvey_id = id,
                wellid = selectedwell.wellid,
                gauge_Depth =data[1],
                gauge_Pressure = data[2],
                gauge_Temperature = data[3]
            )
            value.save()
        messages.info(request,'Successfully uploaded data')
        datas = GIGradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id =id).all().order_by('gauge_Depth')            
        return render(request, 'gigradientsurveydata/gigradientsurveydata_upload.html', {'datas':datas, 'id':id}) 
    return render(request, 'gigradientsurveydata/gigradientsurveydata_upload.html',{'id':id})


