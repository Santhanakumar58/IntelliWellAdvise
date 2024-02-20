from decimal import Decimal
import math
from django.shortcuts import render, redirect
from .utils import get_plot
from .forms import OBDeviationSurveyDataForm
from selectedObserver.models import SelectedObserver
from obdrillingwelldata.models import OBDrillingWellData
from obdeviationsurveydata.models import OBDeviationsurveydata
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage

def list_obdeviationsurvey(request):
    selectedwell= SelectedObserver.objects.all().first()
    obdeviationsurveys = OBDeviationsurveydata.objects.filter(obwellid = selectedwell.wellid) 
    obdrillingwelldata = OBDrillingWellData.objects.filter(obwellid=selectedwell.wellid).first()
    sortedmodels = obdeviationsurveys.order_by('obmeasuredDepth')   
    x=[x.northSouth for x in sortedmodels]
    y=[y.eastWest for y in sortedmodels]
    z=[-z.tvd for z in sortedmodels]
    chart = get_plot(x,y,z)
    return render (request, 'obdeviationsurveydata/obdeviationsurvey.html', {'obdeviationsurveys': sortedmodels,'chart':chart })

def create_obdeviationsurvey(request):
    selctedoilproducer = SelectedObserver.objects.all().first()
    previousmodel = OBDeviationsurveydata.objects.all().last()
    obdeviationsurvey = OBDeviationsurveydata()   
    obdeviationsurvey.fgId = selctedoilproducer.fgid
    obdeviationsurvey.wellid= selctedoilproducer.wellid
    form = OBDeviationSurveyDataForm(request.POST or None, instance=obdeviationsurvey) 
    if request.method == "POST":       
        curdepth = float(request.POST["measuredDepth"])
        curangle = float(request.POST["angle"])
        curazimuth = float(request.POST["azimuth"])
        premodel =OBDeviationsurveydata()
        obdeviationsurveys = OBDeviationsurveydata.objects.filter(wellid =selctedoilproducer.wellid)
        if float(curdepth) > previousmodel.measuredDepth:
           premodel = previousmodel
        else:
            for data in obdeviationsurveys:
                if float(curdepth) > data.measuredDepth:
                    premodel = data
                    break
        prevdepth = premodel.measuredDepth  
        prevangle = premodel.angle  
        prevazimuth = premodel.azimuth      
        north =calculate_North(prevdepth, prevangle, prevazimuth,curdepth, curangle, curazimuth)
        obdeviationsurvey.northSouth = north + premodel.northSouth
        east = calculate_East(prevdepth, prevangle, prevazimuth,curdepth, curangle, curazimuth)
        obdeviationsurvey.eastWest = east + premodel.eastWest
        vert = calculate_Vert(prevdepth, prevangle, prevazimuth,curdepth, curangle, curazimuth)
        obdeviationsurvey.tvd = vert + premodel.tvd
        obdeviationsurvey.dogLeg = calculate_Dogleg(prevangle, prevazimuth, curangle, curazimuth)
        netdrift = calculate_Net_Drift(prevdepth, prevangle, curdepth, curangle)
        obdeviationsurvey.netDrift = netdrift + premodel.netDrift
        vertsection = calculate_Vertical_Section(netdrift,  prevazimuth, curazimuth)
        obdeviationsurvey.verticalSection = vertsection + premodel.verticalSection
        netdir = calculate_Net_Direction(prevdepth, curdepth, curangle, curazimuth)  
        obdeviationsurvey.netDirection = netdir + premodel.netDirection 
        form = OBDeviationSurveyDataForm(request.POST or None, instance=obdeviationsurvey) 
        if form.is_valid():
            form.save()
            return redirect ('obdeviationsurveydata:list_obdeviationsurvey')
    return render (request, 'obdeviationsurveydata/obdeviationsurvey_form.html', {'form': form})

def update_obdeviationsurvey(request, id):
    selctedoilproducer = SelectedObserver.objects.all().first()
    obdeviationsurvey= OBDeviationsurveydata.objects.get(id=id)
    form = OBDeviationSurveyDataForm(request.POST or None, instance=obdeviationsurvey) 
    obdeviationsurveys = OBDeviationsurveydata.objects.filter(wellid =selctedoilproducer.wellid)
    sortedmodels = obdeviationsurveys.order_by('measuredDepth') 
    previousmodel =sortedmodels.last()
    if request.method == "POST":       
        curdepth = float(request.POST["measuredDepth"])
        curangle = float(request.POST["angle"])
        curazimuth = float(request.POST["azimuth"])   
        if float(curdepth) > previousmodel.measuredDepth:
           premodel = previousmodel
        else:
            for data in obdeviationsurveys:  
                if float(curdepth) > data.measuredDepth :
                    premodel = data
                    break     
        prevdepth = premodel.measuredDepth  
        prevangle = premodel.angle  
        prevazimuth = premodel.azimuth            
        north =calculate_North(prevdepth, prevangle, prevazimuth,curdepth, curangle, curazimuth)
        obdeviationsurvey.northSouth = north + premodel.northSouth
        east = calculate_East(prevdepth, prevangle, prevazimuth,curdepth, curangle, curazimuth)
        obdeviationsurvey.eastWest = east + premodel.eastWest
        vert = calculate_Vert(prevdepth, prevangle, prevazimuth,curdepth, curangle, curazimuth)
        obdeviationsurvey.tvd = vert + premodel.tvd
        obdeviationsurvey.dogLeg = calculate_Dogleg(prevangle, prevazimuth, curangle, curazimuth)
        netdrift = calculate_Net_Drift(prevdepth, prevangle, curdepth, curangle)
        obdeviationsurvey.netDrift = netdrift + premodel.netDrift
        vertsection = calculate_Vertical_Section(netdrift,  prevazimuth, curazimuth)
        obdeviationsurvey.verticalSection = vertsection + premodel.verticalSection
        netdir = calculate_Net_Direction(prevdepth, curdepth, curangle, curazimuth)  
        obdeviationsurvey.netDirection = netdir + premodel.netDirection 
        form = OBDeviationSurveyDataForm(request.POST or None, instance=obdeviationsurvey) 
        if form.is_valid():
            form.save()  
        return redirect ('obdeviationsurveydata:list_obdeviationsurvey')
    return render (request, 'obdeviationsurveydata/obdeviationsurvey_form.html', {'form': form, 'obdeviationsurvey':obdeviationsurvey})

def delete_obdeviationsurvey(request, id):
   obdeviationsurvey = OBDeviationsurveydata.objects.get(id=id)
   
   if request.method == 'POST' :
       obdeviationsurvey.delete()
       return redirect ('obdeviationsurveydata:list_obdeviationsurvey')
   return render (request, 'obdeviationsurveydata/obdeviationsurvey_confirm_delete.html', {'obdeviationsurvey':obdeviationsurvey})

def Import_Deviation_SurveyData(request):     
    if request.method == 'POST' and request.FILES['myfile']:        
        selectedwell = SelectedObserver.objects.first()   
        id = selectedwell.wellid
        devdata = OBDeviationsurveydata.objects.filter(wellid = id)
        devdata.delete()
        myfile = request.FILES['myfile']       
        fs = FileSystemStorage()
        filename = fs.save('deviation_data/'+myfile.name, myfile)
        uploaded_file_url = fs.url(filename)   
        d = os.getcwd()  
        filepath = d+'\media\\'+ filename      
        empexceldata = pd.read_excel(filepath)       
        dbframe = empexceldata
        prevdepth=0
        prevangle=0
        prevazimuth=0
        north=0
        east=0
        vert=0
        dogleg=0
        vertsection=0
        netdrift =0
        netdir =0
        for dbframe in dbframe.itertuples():
            if dbframe.measureddepth ==0:
                obj = OBDeviationsurveydata.objects.create(fgId =selectedwell.fgid, wellid= id, measuredDepth=dbframe.measureddepth,angle=dbframe.angle, azimuth=dbframe.azimuth,
                                                         tvd =0, northSouth=0, eastWest=0, netDrift=0, netDirection=0, verticalSection=0, dogLeg=0)           
                obj.save()
            else:
                curdepth = round(dbframe.measureddepth,2)
                curangle = round(dbframe.angle,2)
                curazimuth = round(dbframe.azimuth,2)
                if curangle==0 | curazimuth == 0:
                    obj = OBDeviationsurveydata.objects.create(fgId =selectedwell.fgid, wellid= id, measuredDepth=curdepth,angle=curangle, azimuth=curazimuth,
                                                         tvd =curdepth, northSouth=0, eastWest=0, netDrift=0, netDirection=0, verticalSection=0, dogLeg=0)           
                    obj.save()  
                else:
                    north += calculate_North(prevdepth, prevangle, prevazimuth,curdepth, curangle, curazimuth)
                    east += calculate_East(prevdepth, prevangle, prevazimuth,curdepth, curangle, curazimuth)
                    vert += calculate_Vert(prevdepth, prevangle, prevazimuth,curdepth, curangle, curazimuth)
                    dogleg = calculate_Dogleg(prevangle, prevazimuth, curangle, curazimuth)
                    netdrift += calculate_Net_Drift(prevdepth, prevangle, curdepth, curangle)
                    vertsection += calculate_Vertical_Section(netdrift,  prevazimuth, curazimuth)
                    netdir += calculate_Net_Direction(prevdepth, curdepth, curangle, curazimuth)  
                    obj = OBDeviationsurveydata.objects.create(fgId =selectedwell.fgid, wellid= id, measuredDepth=curdepth,angle=curangle, azimuth=curazimuth,
                                                             tvd =round(vert,2), northSouth=round(north,2), eastWest=round(east,2), netDrift=round(netdrift,2), netDirection=round(netdir,2), verticalSection=round(vertsection,2), dogLeg=round(dogleg,2))           
                    obj.save()  
                prevdepth=curdepth
                prevangle=curangle
                prevazimuth=curazimuth

        return render(request, 'obdeviationsurveydata/Import_excel.html', {'uploaded_file_url': uploaded_file_url, 'devdata':devdata }) 
    
    return render(request, 'obdeviationsurveydata/Import_excel.html',{})


def calculate_North(previous_depth, previous_angle, previous_azimuth,current_depth, current_angle, current_azimuth):
    depth_diff = current_depth-previous_depth
    ang = math.cos(previous_angle*math.pi/180)- math.cos(current_angle*math.pi/180)
    azi = math.sin(current_azimuth*math.pi/180)-math.sin(previous_azimuth*math.pi/180)    
    north_dir = depth_diff*ang*azi*(180/math.pi)**2 /((current_angle-previous_angle) * (current_azimuth-previous_azimuth))  
    return round(north_dir,2)

def calculate_East(previous_depth, previous_angle, previous_azimuth,current_depth, current_angle, current_azimuth):
    depth_diff = current_depth-previous_depth
    ang = math.cos(previous_angle*math.pi/180)- math.cos(current_angle*math.pi/180)
    azi = math.cos(previous_azimuth*math.pi/180)-math.cos(current_azimuth*math.pi/180)    
    est_dir = depth_diff*ang*azi*(180/math.pi)**2 /((current_angle-previous_angle) * (current_azimuth-previous_azimuth))  
    return round(est_dir,2)

def calculate_Vert(previous_depth, previous_angle, previous_azimuth,current_depth, current_angle, current_azimuth):
    depth_diff = current_depth-previous_depth
    ang = math.sin(current_angle*math.pi/180)- math.sin(previous_angle*math.pi/180)   
    ver_dir = depth_diff*ang*(180/math.pi)/(current_angle-previous_angle) 
    return round(ver_dir,2)

def calculate_Dogleg( previous_angle, previous_azimuth, current_angle, current_azimuth):   
    cosbeta = math.cos(previous_angle* math.pi/180-current_angle*math.pi/180)- math.sin(previous_angle*math.pi/180) *  math.sin(current_angle*math.pi/180) * (1- math.cos((current_azimuth-previous_azimuth)* math.pi/180))
    dogleg =  (math.acos((cosbeta))) * (180 / (math.pi)) ## in degree 
    return round(dogleg,2)

def calculate_Net_Drift(previous_depth, previous_angle, current_depth, current_angle):
    depth_diff = current_depth-previous_depth
    term4 = math.sin((current_angle + previous_angle) * math.pi/180/2)
    net_drift = depth_diff * term4    
    return round(net_drift,2)

def calculate_Vertical_Section(netdrift,  previous_azimuth, current_azimuth):
    verticalSection = netdrift * (math.cos((previous_azimuth + current_azimuth) * math.pi/180 / 2))     
    return round(verticalSection,2)

def calculate_Net_Direction(previous_depth, current_depth, current_angle, current_azimuth):    
    netDirection = (((current_depth - previous_depth)) * (math.sin((current_angle) * math.pi/180)) + ((math.sin((current_azimuth) * math.pi/180)))) 
    return round(netDirection,2)
