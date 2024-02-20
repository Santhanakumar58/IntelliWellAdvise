from django.shortcuts import redirect, render
from numpy import sort
from gpgradientsurveydata.utils import get_plot
from gpgradientsurveys.models import GPGradientSurvey
from selectedGasProducer.models import SelectedGasProducer
from .models import GPGradientSurveyData
from .forms import GPGradientSurveyDataForm
from tablib import Dataset
from django.contrib import messages
 

def list_gpgradientsurveydata(request, id): 
    gradientsurveyid =id  
    selectedwell = SelectedGasProducer.objects.first()  
    gradientsurveydatas = GPGradientSurveyData.objects.filter(gpwellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
    x=[x.gauge_Pressure for x in gradientsurveydatas]
    y=[y.gauge_Depth for y in gradientsurveydatas]
    z=[z.gauge_Temperature for z in gradientsurveydatas]    
    chart = get_plot(x,y,z)
    return render (request, 'gpgradientsurveydata/gpgradientsurveydata.html', {'gradientsurveydatas': gradientsurveydatas, 'id':id ,'chart':chart })   

def create_gpgradientsurveydata(request, id):    
   gradientsurveydata = GPGradientSurveyData()
   selectedwell = SelectedGasProducer.objects.first()  
   gradientsurveydata.gpfgid = selectedwell.fgid
   gradientsurveydata.gpwellid = selectedwell.wellid   
   gradientsurveydata.gradientsurvey_id =id   
   form = GPGradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":        
        gradientsurveydata.fgid = selectedwell.fgid
        gradientsurveydata.wellid = selectedwell.wellid  
        gradientsurveydata.gradientsurvey_id =id
        form = GPGradientSurveyDataForm(request.POST, instance=gradientsurveydata)             
        if form.is_valid():       
            form.save() 
            return redirect ('gpgradientsurveydata:list_gpgradientsurveydata', id) 
   return render (request, 'gpgradientsurveydata/gpgradientsurveydata_form.html', {'form': form, 'id':id})

def update_gpgradientsurveydata(request, id):    
   gradientsurveydata = GPGradientSurveyData.objects.get(id=id)   
   form = GPGradientSurveyDataForm(request.POST or None, instance=gradientsurveydata)
   if request.method =="POST":
        form = GPGradientSurveyDataForm(request.POST, instance=gradientsurveydata)
        if form.is_valid():
            form.save()            
            return redirect ('gpgradientsurveydata:list_gpgradientsurveydata' , gradientsurveydata.gradientsurvey_id )
   return render (request, 'gpgradientsurveydata/gpgradientsurveydata_form.html', {'form': form, 'gradientsurvey':gradientsurveydata})

def delete_gpgradientsurveydata(request, id):
   gradientsurveydata = GPGradientSurveyData.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurveydata.delete()
       return redirect ('gpgradientsurveydata:list_gpgradientsurveydata', gradientsurveydata.gradientsurvey_id)
   return render (request, 'gpgradientsurveydata/gpgradientsurveydata_confirm_delete.html', {'gradientsurveydata':gradientsurveydata, 'id':id })


def excel_upload(request, id):  
    if request.method=='None':
        selectedwell = SelectedGasProducer.objects.first()     
        gradientsurveydatas = GPGradientSurveyData.objects.filter(wellid =selectedwell.wellid, gradientsurvey_id=id).all().order_by('gauge_Depth')   
        return redirect ('gpgradientsurveydata:list_gpgradientsurveydata', id) 
    if request.method=="POST":
        selectedwell = SelectedGasProducer.objects.first() 
        olddata = GPGradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id = id).all()  
        olddata.delete()     
        dataset =Dataset()
        new_gradientsurveydata = request.FILES['postedFile']
        if not new_gradientsurveydata.name.endsgpth('xlsx'):
            messages.info(request,'Please upload .xlsx file')
            return render(request, 'gpgradientsurveydata/gpgradientsurveydata_upload.html', {'id':id})
        if new_gradientsurveydata.name.endsgpth('xlsx'):
            imported_data = dataset.load(new_gradientsurveydata.read(), format='xlsx')       
        for data in imported_data:
            value = GPGradientSurveyData(
                gradientsurvey_id = id,
                wellid = selectedwell.wellid,
                gauge_Depth =data[1],
                gauge_Pressure = data[2],
                gauge_Temperature = data[3]
            )
            value.save()
        messages.info(request,'Successfully uploaded data')
        datas = GPGradientSurveyData.objects.filter(wellid=selectedwell.wellid, gradientsurvey_id =id).all().order_by('gauge_Depth')            
        return render(request, 'gpgradientsurveydata/gpgradientsurveydata_upload.html', {'datas':datas, 'id':id}) 
    return render(request, 'gpgradientsurveydata/gpgradientsurveydata_upload.html',{'id':id})


