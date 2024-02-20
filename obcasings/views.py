from asyncio.windows_events import NULL
from decimal import Decimal
from django.shortcuts import render, redirect
from .utils import get_plot, get_plot2, get_dummyplot
from selectedGasProducer.models import SelectedGasProducer
from .forms import OBCasingModelForm
from .models import OBCasingModel, OBCasingGradeModel, OBCasingSizeModel, OBCasingWeightModel
from obdeviationsurveydata.models import OBDeviationsurveydata
import pandas as pd


# Create your views here.
def list_obcasings(request):
    selectedwell = SelectedGasProducer.objects.first()  
    wellid1 = selectedwell.wellid
    obcasings = OBCasingModel.objects.filter(obwellid=wellid1).all().order_by('obshoedepth')     
    obcasingdf =pd.DataFrame()
    width=0.0
    widths=[]
    depths=[]
    hangers=[]
    cements=[]
    obcasingdefs=[]
    for obcasing in obcasings:    
        csize = OBCasingSizeModel.objects.get(obcasingSize = obcasing.obcasingSize)  
        if csize.obcasingSize =="20":
            width =20*2
        elif csize.obcasingSize == "18 5/8":
            width =18.625*2
        elif csize.obcasingSize == "16":
            width =16*2
        elif csize.obcasingSize == "13 3/8":
            width =13.375*2
        elif csize.obcasingSize == "11 3/4":
            width =11/75*2
        elif csize.obcasingSize == "10 3/4":
            width =10.75*2
        elif csize.obcasingSize == "9 5/8":
            width =9.625*2
        elif csize.obcasingSize == "8 5/8":
            width =8.625*2
        elif csize.obcasingSize == "7 3/4":
            width =7.75*2
        elif csize.obcasingSize == "7 5/8":
            width =7.5*2
        elif csize.obcasingSize == "7":
            width =7.0*2
        elif obcasing.OBCasing_Size == "6 5/8":
            width =6.625*2
        elif csize.obcasingSize == "5":
            width =5*2
        elif csize.obcasingSize == "4 1/2":
            width =4.5*2
        elif csize.obcasingSize == "4":
            width =4*2
        depth = obcasing.shoedepth
        hanger = obcasing.hangerDepth
        cement = obcasing.cementTop
        widths.append(width)
        depths.append(depth)
        hangers.append(hanger)
        cements.append(cement)
        obcasingdef = str(obcasing.obcasingSize)+ "  ,  " + str(obcasing.obcasingWeight) + " ppf, "
        obcasingdefs.append(obcasingdef)
    deviationdata = OBDeviationsurveydata.objects.filter(obwellid=wellid1).all()
    if deviationdata:
        chart2 = get_plot2(widths, depths, hangers, cements, deviationdata, obcasingdefs)
    else:
        chart2 = get_dummyplot()
   
    #deviationdata = Deviationsurveydata.objects.filter(wellid=wellid1).all()
    #depth=[]
    #cement=[] 
    #i=0
    #x=[] 
    #x1=[]
    #x2=[]
    #x3=[]
    #x4=[]
    #x5=[]
    #x6=[]
    #y=[]
    #y1=[] 
    #y2=[]
    #y3=[]
    #y4=[]
    #y5=[]
    #y6=[]
    #z=[]
    #z1=[]
    #z2=[]
    #z3=[]
    #z4=[]
    #z5=[] 
    #z6=[] 
    #previousx=0.0
    #previousmd =0.0
    #xa=0.0
    #ya=0.0
    #xb=0.0
    #yb=0.0
    #xc=0.0
    #yc=0.0
    #obcasinga=""
    #obcasingb="" 
    #obcasingc = """"""
    #for obcasing in obcasings.all() :        
    #    depth = obcasing.shoedepth
    #    cement = obcasing.cementTop 
    #    hanger = obcasing.hangerDepth       
    #    obcasingsize = obcasing.obcasingSize
    #    obcasingWeight = obcasing.obcasingWeight 
    #    obcasingdef = str(obcasingsize)+ "  ,  " + str(obcasingWeight) + " ppf, "
    #    for deviation in deviationdata.all(): 
    #        if i==0 : 
    #            if  deviation.measuredDepth <= depth: 
    #                x.append(float(deviation.eastWest + 45 ))
    #                z.append(float(deviation.eastWest -45 ))
    #                y.append(float(deviation.measuredDepth))
    #                previousx = float(deviation.eastWest+45)
    #                previousmd = float(deviation.measuredDepth)
    #                ya = float(depth)   
    #                xa = float(deviation.eastWest + 45 )
    #                obcasinga = obcasingdef           
    #            if deviation.measuredDepth >= cement and deviation.measuredDepth <= depth : 
    #                x1.append(float(deviation.eastWest +47))
    #                z1.append(float(deviation.eastWest -47))
    #                y1.append(float(deviation.measuredDepth))
    #            else :
    #                nexty =float(deviation.measuredDepth)
    #                nextx = float(deviation.eastWest + 45 )
    #                xdiff = nextx-previousx
    #                ydiff = nexty-previousmd
    #                ydiff1 = float(depth) -previousmd
    #                xcal = previousx + xdiff*ydiff1/ydiff
    #                x.append(xcal)
    #                y.append(depth)
    #                z.append(xcal-90)
    #                x1.append(xcal+2)
    #                y1.append(depth)
    #                z1.append(xcal-92)
    #                break
    #        elif i==1 :
    #            if  deviation.measuredDepth <= depth: 
    #                if deviation.measuredDepth >=hanger:
    #                    x2.append(float(deviation.eastWest + 30))
    #                    z2.append(float(deviation.eastWest -30))
    #                    y2.append(float(deviation.measuredDepth))
    #                    yb = float(depth)   
    #                    xb = float(deviation.eastWest + 30 )
    #                    obcasingb = obcasingdef
    #            if deviation.measuredDepth <= depth : 
    #                if deviation.measuredDepth >=cement:
    #                    x3.append(float(deviation.eastWest +32))
    #                    z3.append(float(deviation.eastWest -32))
    #                    y3.append(float(deviation.measuredDepth))
    #            else :
    #                nexty =float(deviation.measuredDepth)
    #                nextx = float(deviation.eastWest + 30 )
    #                xdiff = nextx-previousx
    #                ydiff = nexty-previousmd
    #                ydiff1 = float(depth) -previousmd
    #                xcal = previousx + xdiff*ydiff1/ydiff
    #                x2.append(xcal)
    #                y2.append(depth)
    #                z2.append(xcal-60)
    #                x3.append(xcal+2)
    #                y3.append(depth)
    #                z3.append(xcal-62)
    #                break
    #        elif i==2:
    #            if  deviation.measuredDepth <=depth : 
    #                if deviation.measuredDepth >=hanger:
    #                    x4.append(float(deviation.eastWest + 15))
    #                    z4.append(float(deviation.eastWest -15))
    #                    y4.append(float(deviation.measuredDepth))
    #                    yc = float(depth)   
    #                    xc = float(deviation.eastWest + 15 )
    #                    obcasingc = obcasingdef 
    #            if deviation.measuredDepth <= depth :  
    #                if deviation.measuredDepth > cement:                 
    #                    x5.append(float(deviation.eastWest +17))
    #                    z5.append(float(deviation.eastWest -17))
    #                    y5.append(float(deviation.measuredDepth)) 
    #            else :
    #                nexty =float(deviation.measuredDepth)
    #                nextx = float(deviation.eastWest + 15 )
    #                xdiff = nextx-previousx
    #                ydiff = nexty-previousmd
    #                ydiff1 = float(depth) -previousmd
    #                xcal = previousx + xdiff*ydiff1/ydiff
    #                x4.append(xcal)
    #                y4.append(depth)
    #                z4.append(xcal-30)
    #                x5.append(xcal+2)
    #                y5.append(depth)
    #                z5.append(xcal-32)                   
    #                break
#
    #    i=i+1
        

    #chart = get_plot(x,y,z,xa,ya, x1,y1,z1, x2,y2,z2,xb,yb, x3,y3,z3, x4,y4,z4,xc,yc, x5,y5,z5, obcasinga, obcasingb, obcasingc)   
      
        
    
    return render (request, 'obcasings/obcasing.html', {'obcasings': obcasings, 'chart2':chart2})

def create_obcasing(request):
   selectedwell = SelectedGasProducer.objects.first()
   obcasing = OBCasingModel()
   obcasing.fgid = selectedwell.fgid
   obcasing.wellid = selectedwell.wellid
   form = OBCasingModelForm(request.POST or None, instance=obcasing)
   if request.method == "POST":                  
        obcasing.obcasingType =  request.POST.get("obcasingType")  
        obcasingSize =  request.POST.get("obcasingSize") 
        weightid = request.POST.get("obcasingWeight")  
        print(weightid)     
        obcasingweight = OBCasingWeightModel.objects.filter(id=weightid).first()  
        obcasing.obcasingID = obcasingweight.obcasingID       
        gradeid = request.POST.get("obcasingGrade")       
        obcasinggrade = OBCasingGradeModel.objects.filter(id=gradeid).first()   
        obcasing.collapsePressure =obcasinggrade.collapsePressure  
        obcasing.burstPressure =obcasinggrade.burstPressure 
   form = OBCasingModelForm(request.POST, instance=obcasing)            
   if form.is_valid():
        form.save() 
        return redirect ('obcasings:list_obcasings')    
   return render (request, 'obcasings/obcasing_form.html', {'form': form})

def update_obcasing(request, id):
    obcasing = OBCasingModel.objects.get(id=id)   
    form = OBCasingModelForm(request.POST or None , instance=obcasing)   
    if request.method == "POST":        
        obcasingweightid = request.POST.get('obcasingWeight')
        obcasingweight = OBCasingWeightModel.objects.filter(id=obcasingweightid).first()
        obcasing.obcasingID =obcasingweight.obcasingID             
        gradeid = request.POST.get("obcasingGrade")         
        obcasinggrade = OBCasingGradeModel.objects.filter(id=gradeid).first() 
        obcasing.collapsePressure =obcasinggrade.collapsePressure  
        obcasing.burstPressure =obcasinggrade.burstPressure 
    form = OBCasingModelForm(request.POST or None , instance=obcasing)   
    if form.is_valid():
        form.save()
        return redirect ('obcasings:list_obcasings')
    return render (request, 'obcasings/obcasing_form.html', {'form': form, 'obcasing':obcasing})

def delete_obcasing(request, id):
   obcasing = OBCasingModel.objects.get(id=id)
   
   if request.method == 'POST' :
       obcasing.delete()
       return redirect ('obcasings:list_obcasings')
   return render (request, 'obcasings/obcasing_confirm_delete.html', {'obcasing':obcasing})

def ajax_load_obcasingWeight(request):
    obcasingSize_id = request.GET.get('obcasingSize_id')   
    obcasingWeightmodels= OBCasingWeightModel.objects.filter(obcasingSize_id = obcasingSize_id).all()
    print(obcasingWeightmodels)
    return render (request, 'obcasings/obcasingWeight_Dropdown_list_options.html', {'obcasingWeightmodels':obcasingWeightmodels})

def ajax_load_obcasingGrade(request): 
    obcasingWeight_id = request.GET.get('obcasingWeight_id')
    obcasingGrademodels= OBCasingGradeModel.objects.filter(obcasingWeight_id=obcasingWeight_id).all()
    print(obcasingGrademodels)
    return render (request, 'obcasings/obcasing_grade_Dropdown_list_options.html', {'obcasingGrademodels':obcasingGrademodels})

