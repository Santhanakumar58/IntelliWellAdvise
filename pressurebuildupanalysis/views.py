from asyncio.windows_events import NULL
from datetime import datetime, timedelta
import os
from sqlite3 import Date
from django.shortcuts import redirect, render
from matplotlib import lines
from selectedOilProducer.models import SelectedOilProducer
from .models import PressureBuildupModel, PressureBuildupDataUploadModel
from .forms import PressureBuildupDataUploadForm, BuildupTestForm, BuildupTestUploadForm
from django.contrib import messages
import pandas as pd
import numpy as np
from . utilities import get_constabt_Rate_Buildup_plot, get_limits, get_totalplot, get_totalplot1
from django.core.files.storage import FileSystemStorage
from django.views.generic import View
from django.http import JsonResponse
import matplotlib.pyplot  as plt
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.patches as mpl_patches 
from pathlib import Path
import glob

## New Code

def list_buildup_test_data(request):
    selectedwell = SelectedOilProducer.objects.first()   
    buildup_test_datas = PressureBuildupModel.objects.filter(wellid =selectedwell.wellid).all()   
    return render (request, 'pressurebuildupanalysis/pressurebuildupanalysis.html', {'buildup_test_datas': buildup_test_datas })   
 
def create_buildup_test_data(request):    
    buildup = PressureBuildupModel()
    selectedwell = SelectedOilProducer.objects.first()  
    buildup.fgid = selectedwell.fgid
    buildup.wellid = selectedwell.wellid   
    form = BuildupTestForm(request.POST or None, instance=buildup)
    if request.method =="POST": 
        buildup.fgid = selectedwell.fgid
        buildup.wellid = selectedwell.wellid  
        form = BuildupTestForm(request.POST, request.FILES, instance=buildup)                    
        if form.is_valid(): 
            form.save()  
            file_Name = form.instance
            return redirect ('pressurebuildupanalysis:list_buildup_test_data') 
    return render (request, 'pressurebuildupanalysis/pressurebuildupanalysis_form.html', {'form': form})

def update_buildup_test_data(request, id): 
   buildup= PressureBuildupModel.objects.get(id=id)  
   form = BuildupTestForm(request.POST or None, instance=buildup) 
   if request.method =="POST":       
        form = BuildupTestForm(request.POST, request.FILES, instance=buildup)        
        if form.is_valid():
            form.save()           
            return redirect ('pressurebuildupanalysis:list_buildup_test_data')
   return render (request, 'pressurebuildupanalysis/pressurebuildupanalysis_form.html', {'form': form, 'buildup':buildup})

def delete_buildup_test_data(request, id):
   buildup = PressureBuildupModel.objects.get(id=id)   
   if request.method == 'POST' :
       buildup.delete()
       buildup.dataFile.delete()
       return redirect ('pressurebuildupanalysis:list_buildup_test_data')
   return render (request, 'pressurebuildupanalysis/pressurebuildupanalysis_confirm_delete.html', {'buildup':buildup})

def upload_buildup_test_data(request, id): 
    buildup= PressureBuildupModel.objects.get(id=id) 
    if buildup.test_Type =='Constant_Rate':
        chart =Calculate_Constant_Rate_Buildup_test(id)   
        form =BuildupTestUploadForm(request.POST or None, instance=buildup)     
        if request.method =="POST":  
            if buildup.test_Type =='Constant_Rate':     
                buildup.oil_Prod_Rate = request.POST['oil_Prod_Rate']
                buildup.guess_Value =  request.POST['guess_Value']       
                form = BuildupTestUploadForm(request.POST, request.FILES, instance=buildup)        
                if form.is_valid():
                    form.save()  
                    chart =Calculate_Constant_Rate_Buildup_test( id)        
                    return render (request, 'pressurebuildupanalysis/buildup_test_data_upload.html', {'form': form, 'chart':chart, 'buildup':buildup})
        return render (request, 'pressurebuildupanalysis/buildup_test_data_upload.html', {'form': form, 'chart':chart, 'buildup':buildup})
    elif buildup.test_Type =='Constant_Pressure':
        chart =Calculate_Constant_Rate_Buildup_test(id)   
        form = PressureBuildupDataUploadForm(request.POST or None, instance=buildup)  
        return render (request, 'pressurebuildupanalysis/buildup_test_data_upload.html', {'chart':chart})
    elif buildup.test_Type =='Multi_Rate':
        chart =Calculate_Constant_Rate_Buildup_test(id)   
        form = PressureBuildupDataUploadForm(request.POST or None, instance=buildup)  
        return render (request, 'pressurebuildupanalysis/buildup_test_data_upload.html', { 'chart':chart})

def Calculate_Constant_Rate_Buildup_test(id): 
    buildup= PressureBuildupModel.objects.get(id=id) 
    path =buildup.dataFile  
    filename = path.name
    path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    pa = os.path.join(path1, filename)   
    q=buildup.oil_Prod_Rate  
    your_guess=0
    your_guess = buildup.guess_Value    
    df = pd.read_csv(pa)   
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df1=df.drop(index=0)
    t=df1['t'].values
    p=df1['p'].values   
    Bo = buildup.oil_FVF
    mu_oil = buildup.mu_oil
    h = buildup.layer_Thickness
    poro = buildup.layer_Porosity
    ct = buildup.total_Compressibility
    rw = buildup.wellbore_Radius
    # pi = buildup.initial_Res_Pres  
    t_since_shutin =buildup.t_since_shutin
    def permeability(q, Bo, mu_oil, h, m):        
        return (-162.6 * q * Bo * mu_oil) / (m * h)
    def skin_factor(t_since_shutin, pwf, k, poro, mu_oil, ct, rw, m, pi):   
        b = pi + m1 * np.log10(t_since_shutin + 1)
        return 1.1513 * (((pwf - b) / m1) - np.log10(k / (poro * mu_oil * ct * (rw**2))) + 3.2275)    
    def linear(x, a, b):
        return a * x + b 
    
    delta_t = (t - t[0])
    x = (t_since_shutin + delta_t) / delta_t

    x_crop1, y_crop1 = np.log10(x[-your_guess:]), p[-your_guess:]
    popt, pcov = curve_fit(linear, x_crop1, y_crop1)
    m1, c1 = popt[0], popt[1]

    pi=c1
   
    k = permeability(q, Bo, mu_oil, h, m1)
    pi=c1
    pwf=p[0]

    s = skin_factor(t_since_shutin, pwf, k, poro, mu_oil, ct, rw, m1, pi)

    chart =get_constabt_Rate_Buildup_plot(t, p, q, x, m1, c1 , k,pi,s,t_since_shutin,your_guess)
    return chart
  
def pbu_Analysis(request, id):
    buildup = PressureBuildupModel.objects.get(id=id) 
    path =buildup.dataFile  
    filename = path.name
    path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    pa = os.path.join(path1, filename)  
    p_data = pd.read_csv(pa)    
    p_data["DateTime"] = pd.to_datetime(p_data["survey_Date"] + " " + p_data["time"]) 
    print(p_data.head())  
    params_dict = {"bo": buildup.oil_FVF, "muo": buildup.mu_oil, "qo": buildup.oil_Prod_Rate, "h": buildup.layer_Thickness, "PHIE": buildup.layer_Porosity, "Pi": 5410, "ct": buildup.total_Compressibility, "rw": buildup.wellbore_Radius} 
    xy= p_data.iloc[::20]
    
    chart = get_totalplot1(p_data)
    
    #data, params_dict = prepare_data(DD_data, BU_data, params_dict, "BU")  
   
    if request.method == 'POST' :       
        data = get_limits(p_data)         
        return redirect ('pressurebuildupanalysis:list_buildup_test_data')
    return render (request, 'pressurebuildupanalysis/pressurebuildup_Analysis.html', {'chart':chart})
    

## emd of new Code
# Create your views here.
# class HomeView(View):
#     def get(self, request):
#         form = PressureBuildupDataUploadForm()
#         return render(request, 'pressurebuildupanalysis/pbudata_upload.html', context={'form':form})
# 
#     def post(self, request):
#         if request.method=='POST':
#             form = PressureBuildupDataUploadForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 return JsonResponse({'data':'Data uploaded'})
# 
#             else:
#                 return JsonResponse({'data':'Something went wrong!!'})




# def list_pressurebuildupanalysis(request):
#    selectedwell = SelectedOilProducer.objects.first()   
#    pbudata = PressureBuildupModel.objects.filter(wellid =selectedwell.wellid).all()    
#    return render (request, 'pressurebuildupanalysis/pressurebuildupanalysis.html', {'pbudata': pbudata })   #

#def create_pressurebuildupanalysis(request):    #
#   pbudata = PressureBuildupModel()
#   selectedwell = SelectedOilProducer.objects.first()  
#   pbudata.fgid = selectedwell.fgid
#   pbudata.wellid = selectedwell.wellid   
#   form = PressureBuildupForm(request.POST or None, instance=pbudata)
#   if request.method =="POST":  
#        form = PressureBuildupForm(request.POST, request.FILES, instance=pbudata)       
#        pbudata.fgId = selectedwell.fgid
#        pbudata.wellid = selectedwell.wellid
#        old_filename = request.FILES["dataFile"] 
#        print("hello", old_filename)
#        # timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
#        # filename = "%s%s" % (timeNow, old_filename)   
#        # path = os.path.join('uploads/PBUData/', old_filename)  
#        # pbudata.dataFile= path                    
#        if form.is_valid(): 
#            print("hello", old_filename)
#            form.save()  
#            return redirect ('pressurebuildupanalysis:list_pressurebuildupanalysis') 
#   return render (request, 'pressurebuildupanalysis/pressurebuildupanalysis_form.html', {'form': form})

#def update_pressurebuildupanalysis(request, id): 
#   pbudata = PressureBuildupModel.objects.get(id=id)  
#   form = PressureBuildupForm(request.POST or None, instance=pbudata) 
#   if request.method =="POST":
#        form = PressureBuildupForm(request.POST, request.FILES, instance=pbudata) 
#        old_filename = request.FILES["dataFile"]  
#        print("hello", old_filename)        
#        if form.is_valid():
#            # fs =FileSystemStorage()
#            # fs.save(old_filename.name, old_filename)
#            form.save()           
#            return redirect ('pressurebuildupanalysis:list_pressurebuildupanalysis')
#   return render (request, 'pressurebuildupanalysis/pressurebuildupanalysis_form.html', {'form': form, 'pbudata':pbudata})

#def delete_pressurebuildupanalysis(request, id):#
#   pbudata = PressureBuildupModel.objects.get(id=id)   
#   if request.method == 'POST' :
#       pbudata.delete()
#       return redirect ('pressurebuildupanalysis:list_pressurebuildupanalysis')
#   return render (request, 'pressurebuildupanalysis/pressurebuildupanalysis_confirm_delete.html', {'pbudata':pbudata})

#def upload_PBUdata(request, id): #
#   pbudata = PressureBuildupModel.objects.get(id=id) 
#   datafile = pbudata.dataFile  
#   if datafile !="" or datafile != NULL : 
#        dateparse = lambda x: datetime.strptime(x, '%m/%d/%Y')
#        df = pd.read_csv(datafile, parse_dates=['survey_Date'], date_parser=dateparse) 
#        df_records = df.to_dict('records')
#        startrecord = df_records[0]
#        startday = int(startrecord["survey_Date"].day)
#        startyear = int(startrecord["survey_Date"].year)
#        startmonth = int(startrecord["survey_Date"].month)
#        startTime =startrecord["time"]
#        t1 = datetime.strptime(startTime, "%H:%M:%S")
#        starthour = t1.hour
#        startmin = t1.minute
#        startsec =t1.second
#        startDate = datetime(startyear, startmonth, startday, starthour, startmin, startsec)
#        models = [PressureBuildupDataUploadModel]
#        x=[]
#        y=[]
#        for record in df_records:
#            curday = record["survey_Date"].date()
#            curTime =record["time"]  
#            curday = int(record["survey_Date"].day)
#            curyear = int(record["survey_Date"].year)
#            curmonth = int(record["survey_Date"].month)
#            curTime =record["time"]
#            t2 = datetime.strptime(curTime, "%H:%M:%S")
#            curhour = t2.hour
#            curmin = t2.minute
#            cursec =t2.second
#            curDate = datetime(curyear, curmonth, curday, curhour, curmin, cursec) 
#            elapsedtime = (curDate-startDate ).total_seconds()/3600 
#            model_instances = [PressureBuildupDataUploadModel(        
#            survey_Date= record["survey_Date"].date(),  
#            time=record['time'],
#            elapsedtime = float(elapsedtime),
#            gauge_pressure=record['gauge_Pressure']
#            )]
#            gauge_pressure=float(record['gauge_Pressure'])
#            models.append(model_instances)
#            x.append(elapsedtime)
#            y.append(gauge_pressure)           
#        chart = get_plot1(x,y) 
#        plt.scatter(x, y)
#        def on_move(event):
#            if event.inaxes:
#                print(f'data coords {event.xdata} {event.ydata},',
#                f'pixel coords {event.x} {event.y}')
#        def on_click(event):
#            if event.button is MouseButton.LEFT:
#                print('disconnecting callback')
#                plt.disconnect(binding_id)
#        binding_id = plt.connect('motion_notify_event', on_move)
#        plt.connect('button_press_event', on_click)
#        chart1=plt.show() 
#        return render (request,'pressurebuildupanalysis/pbudata_upload.html',{'chart':chart}) 
#   else :            
#        form = PressureBuildupDataUploadForm(request.POST or None)          
#        return render (request, 'pressurebuildupanalysis/pbudata_upload.html', {'form': form, 'id':id})

#def pbudata_upload(request, id):#
#     
#    return render(request, 'pressurebuildupanalysis/pbudata_upload.html')

#def pbu_chart(request,id):#
#    labels = []
#    data = []
#    pbudata = PressureBuildupModel.objects.get(id=id) 
#    file = pbudata.dataFile  
#    if file !="" or file != NULL : 
#        dateparse = lambda x: datetime.strptime(x, '%m/%d/%Y')
#        df = pd.read_csv(file, parse_dates=['survey_Date'], date_parser=dateparse) 
#        df_records = df.to_dict('records')
#        startrecord = df_records[0]
#        startday = int(startrecord["survey_Date"].day)
#        startyear = int(startrecord["survey_Date"].year)
#        startmonth = int(startrecord["survey_Date"].month)
#        startTime =startrecord["time"]
#        t1 = datetime.strptime(startTime, "%H:%M:%S")
#        starthour = t1.hour
#        startmin = t1.minute
#        startsec =t1.second
#        startDate = datetime(startyear, startmonth, startday, starthour, startmin, startsec)
#        models = [PressureBuildupDataUploadModel] 
#        for record in df_records:
#            curday = record["survey_Date"].date()
#            curTime =record["time"]  
#            curday = int(record["survey_Date"].day)
#            curyear = int(record["survey_Date"].year)
#            curmonth = int(record["survey_Date"].month)
#            curTime =record["time"]
#            t2 = datetime.strptime(curTime, "%H:%M:%S")
#            curhour = t2.hour
#            curmin = t2.minute
#            cursec =t2.second
#            curDate = datetime(curyear, curmonth, curday, curhour, curmin, cursec) 
#            elapsedtime = (curDate-startDate ).total_seconds()/3600 
#            model_instances = [PressureBuildupDataUploadModel(        
#            survey_Date= record["survey_Date"].date(),  
#            time=record['time'],
#            elapsedtime = float(elapsedtime),
#            gauge_pressure=record['gauge_Pressure']
#            )]
#            gauge_pressure=float(record['gauge_Pressure'])
#            models.append(model_instances)
#            labels.append(elapsedtime*1000)
#            data.append(record['gauge_Pressure']*1000)
#            print (data)
#        return JsonResponse(data={'labels': labels,'data': data})

# def fileUpload(request, id):
#    selectedwell = SelectedOilProducer.objects.first()  
#    datafiles = FileUploadModel.objects.filter(pressureBuildupModel =id).all() 
#    model = FileUploadModel()
#    model.pressureBuildupModel = id
#    model.survey_Date = datetime.today()
#    model.upload_Date = datetime.today()
#    form = FileUploadForm(request.POST or None,instance=model )
#    if request.method == 'POST':         
#        datafile = request.FILES['postedFile']
#        print (datafile, datafile.name, datafile.size)
#        form = FileUploadForm(request.POST, request.FILES, instance=model)        
#        if not datafile.name.endswith('csv'):
#            messages.info(request,'The uploaded file extension is not .csv')
#            return render(request, 'pressurebuildupanalysis/data_Upload.html', {'id':id, 'datafiles':datafiles })
#        elif datafile.name.endswith('csv'):            
#            fs=FileSystemStorage()
#            fs.save(datafile.name, datafile)
#            if form.is_valid():
#                print ("hello1", model.survey_Date)
#                fs=FileSystemStorage()
#                fs.save(datafile.name, datafile)
#                print ("hello")
#                form.save()
#                pbudatafiles = FileUploadModel.objects.filter(pressureBuildupModel =id).all()
#                return render(request, 'pressurebuildupanalysis/data_Upload.html', {'id':id, 'pbudatafiles':pbudatafiles })        
#    return render(request, 'pressurebuildupanalysis/data_Upload.html', {'id':id, 'model':model})
