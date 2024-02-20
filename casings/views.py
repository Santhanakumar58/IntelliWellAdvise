from asyncio.windows_events import NULL
from decimal import Decimal
from django.shortcuts import render, redirect
from .utils import get_plot, get_plot2, get_dummyplot
from selectedOilProducer.models import SelectedOilProducer
from .forms import CasingModelForm
from .models import CasingModel, CasingGradeModel, CasingSizeModel, CasingWeightModel
from deviationsurveydata.models import Deviationsurveydata
import pandas as pd


# Create your views here.
def list_casings(request):
    selectedoilproducer = SelectedOilProducer.objects.first()  
    wellid1 = selectedoilproducer.wellid
    casings = CasingModel.objects.filter(wellid=wellid1).filter(wellid=wellid1).all().order_by('shoedepth')     
    casingdf =pd.DataFrame()
    width=0.0
    widths=[]
    depths=[]
    hangers=[]
    cements=[]
    casingdefs=[]
    for casing in casings:    
        csize = CasingSizeModel.objects.get(casingSize = casing.casingSize)  
        if csize.casingSize =="20":
            width =20*2
        elif csize.casingSize == "18 5/8":
            width =18.625*2
        elif csize.casingSize == "16":
            width =16*2
        elif csize.casingSize == "13 3/8":
            width =13.375*2
        elif csize.casingSize == "11 3/4":
            width =11/75*2
        elif csize.casingSize == "10 3/4":
            width =10.75*2
        elif csize.casingSize == "9 5/8":
            width =9.625*2
        elif csize.casingSize == "8 5/8":
            width =8.625*2
        elif csize.casingSize == "7 3/4":
            width =7.75*2
        elif csize.casingSize == "7 5/8":
            width =7.5*2
        elif csize.casingSize == "7":
            width =7.0*2
        elif casing.Casing_Size == "6 5/8":
            width =6.625*2
        elif csize.casingSize == "5":
            width =5*2
        elif csize.casingSize == "4 1/2":
            width =4.5*2
        elif csize.casingSize == "4":
            width =4*2
        depth = casing.shoedepth
        hanger = casing.hangerDepth
        cement = casing.cementTop
        widths.append(width)
        depths.append(depth)
        hangers.append(hanger)
        cements.append(cement)
        casingdef = str(casing.casingSize)+ "  ,  " + str(casing.casingWeight) + " ppf, "
        casingdefs.append(casingdef)
    deviationdata = Deviationsurveydata.objects.filter(wellid=wellid1).all()
    if deviationdata:
        chart2 = get_plot2(widths, depths, hangers, cements, deviationdata, casingdefs)
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
    #casinga=""
    #casingb="" 
    #casingc = """"""
    #for casing in casings.all() :        
    #    depth = casing.shoedepth
    #    cement = casing.cementTop 
    #    hanger = casing.hangerDepth       
    #    casingsize = casing.casingSize
    #    casingWeight = casing.casingWeight 
    #    casingdef = str(casingsize)+ "  ,  " + str(casingWeight) + " ppf, "
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
    #                casinga = casingdef           
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
    #                    casingb = casingdef
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
    #                    casingc = casingdef 
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
        

    #chart = get_plot(x,y,z,xa,ya, x1,y1,z1, x2,y2,z2,xb,yb, x3,y3,z3, x4,y4,z4,xc,yc, x5,y5,z5, casinga, casingb, casingc)   
      
        
    
    return render (request, 'casings/casing.html', {'casings': casings, 'chart2':chart2})

def create_casing(request):
   selectedwell = SelectedOilProducer.objects.first()
   casing = CasingModel()
   casing.fgid = selectedwell.fgid
   casing.wellid = selectedwell.wellid
   form = CasingModelForm(request.POST or None, instance=casing)
   if request.method == "POST":                  
        casing.casingType =  request.POST.get("casingType")  
        casingSize =  request.POST.get("casingSize") 
        weightid = request.POST.get("casingWeight")  
        print(weightid)     
        casingweight = CasingWeightModel.objects.filter(id=weightid).first()  
        casing.casingID = casingweight.casingID       
        gradeid = request.POST.get("casingGrade")       
        casinggrade = CasingGradeModel.objects.filter(id=gradeid).first()   
        casing.collapsePressure =casinggrade.collapsePressure  
        casing.burstPressure =casinggrade.burstPressure 
   form = CasingModelForm(request.POST, instance=casing)            
   if form.is_valid():
        form.save() 
        return redirect ('casings:list_casings')    
   return render (request, 'casings/casing_form.html', {'form': form})

def update_casing(request, id):
    casing = CasingModel.objects.get(id=id)   
    form = CasingModelForm(request.POST or None , instance=casing)   
    if request.method == "POST":        
        casingweightid = request.POST.get('casingWeight')
        casingweight = CasingWeightModel.objects.filter(id=casingweightid).first()
        casing.casingID =casingweight.casingID             
        gradeid = request.POST.get("casingGrade")         
        casinggrade = CasingGradeModel.objects.filter(id=gradeid).first() 
        casing.collapsePressure =casinggrade.collapsePressure  
        casing.burstPressure =casinggrade.burstPressure 
    form = CasingModelForm(request.POST or None , instance=casing)   
    if form.is_valid():
        form.save()
        return redirect ('casings:list_casings')
    return render (request, 'casings/casing_form.html', {'form': form, 'casing':casing})

def delete_casing(request, id):
   casing = CasingModel.objects.get(id=id)
   
   if request.method == 'POST' :
       casing.delete()
       return redirect ('casings:list_casings')
   return render (request, 'casings/casing_confirm_delete.html', {'casing':casing})

def ajax_load_casingWeight(request):
    casingSize_id = request.GET.get('casingSize_id')   
    casingWeightmodels= CasingWeightModel.objects.filter(casingSize_id = casingSize_id).all()
    print(casingWeightmodels)
    return render (request, 'casings/casingWeight_Dropdown_list_options.html', {'casingWeightmodels':casingWeightmodels})

def ajax_load_casingGrade(request): 
    casingWeight_id = request.GET.get('casingWeight_id')
    casingGrademodels= CasingGradeModel.objects.filter(casingWeight_id=casingWeight_id).all()
    print(casingGrademodels)
    return render (request, 'casings/casing_grade_Dropdown_list_options.html', {'casingGrademodels':casingGrademodels})