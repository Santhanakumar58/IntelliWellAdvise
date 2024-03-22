from asyncio.windows_events import NULL
from decimal import Decimal
from django.shortcuts import render, redirect
from .utils import get_plot, get_plot2, get_dummyplot
from casings.models import CasingModel, CasingSizeModel
from selectedOilProducer.models import SelectedOilProducer
from .forms import TubingModelForm
from .models import TubingModel, TubingGradeModel, TubingSizeModel, TubingWeightModel
from deviationsurveydata.models import Deviationsurveydata
from IntelligentOilWell.custom_context_processors import linear_interpolation, tvdCalculation, eastCalculation
import pandas as pd


# Create your views here.
def list_tubings(request):
    selectedoilproducer = SelectedOilProducer.objects.first()  
    wellid1 = selectedoilproducer.wellid
    tubings = TubingModel.objects.filter(wellid=wellid1).filter(wellid=wellid1).all().order_by('depth_To')     
    casings = CasingModel.objects.filter(wellid=wellid1).all().order_by('shoedepth') 
    tubingdf =pd.DataFrame()
  
    width=0.0
    widths=[]
    depths=[]
    hangers=[]
    cements=[]
    casingdefs=[]
    #print(len(tubings))
    if casings :
        for casing in casings:
            #print(tubing.tubingSize)
            csize = CasingSizeModel.objects.get(casingSize = casing.casingSize)  
            if csize.casingSize =="20":
                width =20
            elif csize.casingSize == "18 5/8":
                width =18.625
            elif csize.casingSize == "16":
                width =16
            elif csize.casingSize == "13 3/8":
                width =13.375
            elif csize.casingSize == "11 3/4":
                width =11/75
            elif csize.casingSize == "10 3/4":
                width =10.75
            elif csize.casingSize == "9 5/8":
                width =9.625
            elif csize.casingSize == "8 5/8":
                width =8.625
            elif csize.casingSize == "7 3/4":
                width =7.75
            elif csize.casingSize == "7 5/8":
                width =7.5
            elif csize.casingSize == "7":
                width =7.0
            elif csize.casingSize == "6 5/8":
                width =6.625
            elif csize.casingSize == "5":
                width =5
            elif csize.casingSize == "4 1/2":
                width =4.5
            elif csize.casingSize == "4":
                width =4            
            depth = casing.shoedepth
            hanger = casing.hangerDepth
            cement = casing.cementTop
            widths.append(width)
            depths.append(depth)
            hangers.append(hanger)
            cements.append(cement)
            casingdef= str(casing.casingSize)+ "  ,  " + str(casing.casingWeight) + " ppf, "
            casingdefs.append(casingdef)
    deviationdata = Deviationsurveydata.objects.filter(wellid=wellid1).all()   
    equipmentDepth=[]
    equipmentName=[]
    equipmentx =[]
    east=0
    for equip in tubings:
        east = eastCalculation(deviationdata, equip.depth_To)
        east1 = eastCalculation(deviationdata, equip.depth_To)
        equipmentx.append(east)
        equipmentDepth.append(equip.depth_To)
        equipmentN= str(equip.tubingSize) + " inch  " + equip.tubingType + " at " +str(equip.depth_To) + " ft"
        equipmentName.append(equipmentN)    
    if deviationdata:
         chart2= get_plot2(widths, depths, hangers, cements, deviationdata, casingdefs, tubings, equipmentx,equipmentDepth,equipmentName ) 
    else:
        chart2 = get_dummyplot()
    #chart2 = get_plot2(widths, depths, hangers, cements, deviationdata, casingdefs, completion_datas, equipmentx,equipmentDepth,equipmentName )    
    return render (request, 'tubings/tubing.html', {'tubings': tubings, 'chart2':chart2})

def create_tubing(request):
   selectedwell = SelectedOilProducer.objects.first()
   tubing = TubingModel()
   tubing.fgid = selectedwell.fgid
   tubing.wellid = selectedwell.wellid
   form = TubingModelForm(request.POST or None, instance=tubing)
   if request.method == "POST":                  
        tubing.tubingType =  request.POST.get("tubingType")  
        tubingSize =  request.POST.get("tubingSize") 
        weightid = request.POST.get("tubingWeight")            
        tubingweight = TubingWeightModel.objects.filter(id=weightid).first()  
        tubing.tubingID = tubingweight.tubingID       
        gradeid = request.POST.get("tubingGrade")       
        tubinggrade = TubingGradeModel.objects.filter(id=gradeid).first()   
        tubing.collapsePressure =tubinggrade.collapsePressure  
        tubing.burstPressure =tubinggrade.burstPressure 
        tubing.depth_From =   request.POST.get("depth_From")
        tubing.depth_To =   request.POST.get("depth_To")
        deviation = Deviationsurveydata.objects.filter(wellid=selectedwell.wellid).all()  
        for dev in deviation:
            if dev.measuredDepth <= float(tubing.depth_To):
                x1 = dev.measuredDepth
                y1 =dev.tvd
            else :
                x2 = dev.measuredDepth
                y2 =dev.tvd
                angle = dev.angle
                break
        tubing.tvd_To = linear_interpolation(float(tubing.depth_To), float(x1),float(y1), float(x2),float(y2))
        tubing.angle_To = angle       
        form = TubingModelForm(request.POST, instance=tubing)            
        if form.is_valid():
            form.save() 
            return redirect ('tubings:list_tubings')    
   return render (request, 'tubings/tubing_form.html', {'form': form})

def update_tubing(request, id):
    tubing = TubingModel.objects.get(id=id)   
    form = TubingModelForm(request.POST or None , instance=tubing)   
    if request.method == "POST":        
        tubingweightid = request.POST.get('tubingWeight')
        tubingweight = TubingWeightModel.objects.filter(id=tubingweightid).first()
        tubing.tubingID =tubingweight.tubingID             
        gradeid = request.POST.get("tubingGrade")         
        tubinggrade = TubingGradeModel.objects.filter(id=gradeid).first() 
        tubing.collapsePressure =tubinggrade.collapsePressure  
        tubing.burstPressure =tubinggrade.burstPressure 
        tubing.depth_From =   request.POST.get("depth_From")
        tubing.depth_To =   request.POST.get("depth_To")
        deviation = Deviationsurveydata.objects.filter(wellid=tubing.wellid).all()  
        for dev in deviation:
            if dev.measuredDepth <= float(tubing.depth_To):
                x1 = dev.measuredDepth
                y1 =dev.tvd
            else :
                x2 = dev.measuredDepth
                y2 =dev.tvd
                angle = dev.angle
                break        
        tubing.tvd_To = linear_interpolation(float(tubing.depth_To), float(x1),float(y1), float(x2),float(y2))
        tubing.angle_To = angle        
    form = TubingModelForm(request.POST or None , instance=tubing)   
    if form.is_valid():
        form.save()
        return redirect ('tubings:list_tubings')
    return render (request, 'tubings/tubing_form.html', {'form': form, 'tubing':tubing})

def delete_tubing(request, id):
   tubing = TubingModel.objects.get(id=id)
   
   if request.method == 'POST' :
       tubing.delete()
       return redirect ('tubings:list_tubings')
   return render (request, 'tubings/tubing_confirm_delete.html', {'tubing':tubing})

def ajax_load_tubingWeight(request):
    tubingSize_id = request.GET.get('tubingSize_id')   
    tubingWeightmodels= TubingWeightModel.objects.filter(tubingSize_id = tubingSize_id).all()
    print(tubingWeightmodels)
    return render (request, 'tubings/tubingWeight_Dropdown_list_options.html', {'tubingWeightmodels':tubingWeightmodels})

def ajax_load_tubingGrade(request): 
    tubingWeight_id = request.GET.get('tubingWeight_id')
    tubingGrademodels= TubingGradeModel.objects.filter(tubingWeight_id=tubingWeight_id).all()
    print(tubingGrademodels)
    return render (request, 'tubings/tubing_grade_Dropdown_list_options.html', {'tubingGrademodels':tubingGrademodels})
