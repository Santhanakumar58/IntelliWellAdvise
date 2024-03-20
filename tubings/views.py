from asyncio.windows_events import NULL
from decimal import Decimal
from django.shortcuts import render, redirect
#from .utils import get_plot, get_plot2, get_dummyplot, get_plot21
from selectedOilProducer.models import SelectedOilProducer
from .forms import TubingModelForm
from .models import TubingModel, TubingGradeModel, TubingSizeModel, TubingWeightModel
from deviationsurveydata.models import Deviationsurveydata
import pandas as pd


# Create your views here.
def list_tubings(request):
    selectedoilproducer = SelectedOilProducer.objects.first()  
    wellid1 = selectedoilproducer.wellid
    tubings = TubingModel.objects.filter(wellid=wellid1).filter(wellid=wellid1).all().order_by('depth_From')  
    
    tubingdf =pd.DataFrame()
    width=0.0
    widths=[]
    depths=[]
    hangers=[]
    cements=[]
    tubingdefs=[]
    #print(len(tubings))
    if tubings :
        for tubing in tubings:
            #print(tubing.tubingSize)
            csize = TubingSizeModel.objects.get(tubingSize = tubing.tubingSize)  
            if csize.tubingSize =="20":
                width =20
            elif csize.tubingSize == "18 5/8":
                width =18.625
            elif csize.tubingSize == "16":
                width =16
            elif csize.tubingSize == "13 3/8":
                width =13.375
            elif csize.tubingSize == "11 3/4":
                width =11/75
            elif csize.tubingSize == "10 3/4":
                width =10.75
            elif csize.tubingSize == "9 5/8":
                width =9.625
            elif csize.tubingSize == "8 5/8":
                width =8.625
            elif csize.tubingSize == "7 3/4":
                width =7.75
            elif csize.tubingSize == "7 5/8":
                width =7.5
            elif csize.tubingSize == "7":
                width =7.0
            elif tubing.Tubing_Size == "6 5/8":
                width =6.625
            elif csize.tubingSize == "5":
                width =5
            elif csize.tubingSize == "4 1/2":
                width =4.5
            elif csize.tubingSize == "4":
                width =4            
            #depth = tubing.shoedepth
            #hanger = tubing.hangerDepth
            #cement = tubing.cementTop
            #widths.append(width)
            #depths.append(depth)
            #hangers.append(hanger)
            #cements.append(cement)
            #tubingdef = str(tubing.tubingSize)+ "  ,  " + str(tubing.tubingWeight) + " ppf, "
            #tubingdefs.append(tubingdef)
    deviationdata = Deviationsurveydata.objects.filter(wellid=wellid1).all()   
    
    return render (request, 'tubings/tubing.html', {'tubings': tubings})

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
        print(weightid)     
        tubingweight = TubingWeightModel.objects.filter(id=weightid).first()  
        tubing.tubingID = tubingweight.tubingID       
        gradeid = request.POST.get("tubingGrade")       
        tubinggrade = TubingGradeModel.objects.filter(id=gradeid).first()   
        tubing.collapsePressure =tubinggrade.collapsePressure  
        tubing.burstPressure =tubinggrade.burstPressure 
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
