from asyncio.windows_events import NULL
from decimal import Decimal
from django.shortcuts import render, redirect
from .utils import get_plot, get_plot2, get_dummyplot
from selectedWaterInjector.models import SelectedWaterInjector
from .forms import WICasingModelForm
from .models import WICasingModel, WICasingGradeModel, WICasingSizeModel, WICasingWeightModel
from wideviationsurveydata.models import WIDeviationsurveydata
import pandas as pd


# Create your views here.
def list_wicasings(request):
    selectedwell = SelectedWaterInjector.objects.first()  
    wellid1 = selectedwell.wellid
    wicasings = WICasingModel.objects.filter(wiwellid=wellid1).all().order_by('wishoedepth')     
    wicasingdf =pd.DataFrame()
    width=0.0
    widths=[]
    depths=[]
    hangers=[]
    cements=[]
    wicasingdefs=[]
    for wicasing in wicasings:    
        csize = WICasingSizeModel.objects.get(wicasingSize = wicasing.wicasingSize)  
        if csize.wicasingSize =="20":
            width =20*2
        elif csize.wicasingSize == "18 5/8":
            width =18.625*2
        elif csize.wicasingSize == "16":
            width =16*2
        elif csize.wicasingSize == "13 3/8":
            width =13.375*2
        elif csize.wicasingSize == "11 3/4":
            width =11/75*2
        elif csize.wicasingSize == "10 3/4":
            width =10.75*2
        elif csize.wicasingSize == "9 5/8":
            width =9.625*2
        elif csize.wicasingSize == "8 5/8":
            width =8.625*2
        elif csize.wicasingSize == "7 3/4":
            width =7.75*2
        elif csize.wicasingSize == "7 5/8":
            width =7.5*2
        elif csize.wicasingSize == "7":
            width =7.0*2
        elif wicasing.GPCasing_Size == "6 5/8":
            width =6.625*2
        elif csize.wicasingSize == "5":
            width =5*2
        elif csize.wicasingSize == "4 1/2":
            width =4.5*2
        elif csize.wicasingSize == "4":
            width =4*2
        depth = wicasing.shoedepth
        hanger = wicasing.hangerDepth
        cement = wicasing.cementTop
        widths.append(width)
        depths.append(depth)
        hangers.append(hanger)
        cements.append(cement)
        wicasingdef = str(wicasing.wicasingSize)+ "  ,  " + str(wicasing.wicasingWeight) + " ppf, "
        wicasingdefs.append(wicasingdef)
    deviationdata = WIDeviationsurveydata.objects.filter(wiwellid=wellid1).all()
    if deviationdata:
        chart2 = get_plot2(widths, depths, hangers, cements, deviationdata, wicasingdefs)
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
    #wicasinga=""
    #wicasingb="" 
    #wicasingc = """"""
    #for wicasing in wicasings.all() :        
    #    depth = wicasing.shoedepth
    #    cement = wicasing.cementTop 
    #    hanger = wicasing.hangerDepth       
    #    wicasingsize = wicasing.wicasingSize
    #    wicasingWeight = wicasing.wicasingWeight 
    #    wicasingdef = str(wicasingsize)+ "  ,  " + str(wicasingWeight) + " ppf, "
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
    #                wicasinga = wicasingdef           
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
    #                    wicasingb = wicasingdef
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
    #                    wicasingc = wicasingdef 
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
        

    #chart = get_plot(x,y,z,xa,ya, x1,y1,z1, x2,y2,z2,xb,yb, x3,y3,z3, x4,y4,z4,xc,yc, x5,y5,z5, wicasinga, wicasingb, wicasingc)   
      
        
    
    return render (request, 'wicasings/wicasing.html', {'wicasings': wicasings, 'chart2':chart2})

def create_wicasing(request):
   selectedwell = SelectedWaterInjector.objects.first()
   wicasing = WICasingModel()
   wicasing.fgid = selectedwell.fgid
   wicasing.wellid = selectedwell.wellid
   form = WICasingModelForm(request.POST or None, instance=wicasing)
   if request.method == "POST":                  
        wicasing.wicasingType =  request.POST.get("wicasingType")  
        wicasingSize =  request.POST.get("wicasingSize") 
        weightid = request.POST.get("wicasingWeight")  
        print(weightid)     
        wicasingweight = WICasingWeightModel.objects.filter(id=weightid).first()  
        wicasing.wicasingID = wicasingweight.wicasingID       
        gradeid = request.POST.get("wicasingGrade")       
        wicasinggrade = WICasingGradeModel.objects.filter(id=gradeid).first()   
        wicasing.collapsePressure =wicasinggrade.collapsePressure  
        wicasing.burstPressure =wicasinggrade.burstPressure 
   form = WICasingModelForm(request.POST, instance=wicasing)            
   if form.is_valid():
        form.save() 
        return redirect ('wicasings:list_wicasings')    
   return render (request, 'wicasings/wicasing_form.html', {'form': form})

def update_wicasing(request, id):
    wicasing = WICasingModel.objects.get(id=id)   
    form = WICasingModelForm(request.POST or None , instance=wicasing)   
    if request.method == "POST":        
        wicasingweightid = request.POST.get('wicasingWeight')
        wicasingweight = WICasingWeightModel.objects.filter(id=wicasingweightid).first()
        wicasing.wicasingID =wicasingweight.wicasingID             
        gradeid = request.POST.get("wicasingGrade")         
        wicasinggrade = WICasingGradeModel.objects.filter(id=gradeid).first() 
        wicasing.collapsePressure =wicasinggrade.collapsePressure  
        wicasing.burstPressure =wicasinggrade.burstPressure 
    form = WICasingModelForm(request.POST or None , instance=wicasing)   
    if form.is_valid():
        form.save()
        return redirect ('wicasings:list_wicasings')
    return render (request, 'wicasings/wicasing_form.html', {'form': form, 'wicasing':wicasing})

def delete_wicasing(request, id):
   wicasing = WICasingModel.objects.get(id=id)
   
   if request.method == 'POST' :
       wicasing.delete()
       return redirect ('wicasings:list_wicasings')
   return render (request, 'wicasings/wicasing_confirm_delete.html', {'wicasing':wicasing})

def ajax_load_wicasingWeight(request):
    wicasingSize_id = request.GET.get('wicasingSize_id')   
    wicasingWeightmodels= WICasingWeightModel.objects.filter(wicasingSize_id = wicasingSize_id).all()
    print(wicasingWeightmodels)
    return render (request, 'wicasings/wicasingWeight_Dropdown_list_options.html', {'wicasingWeightmodels':wicasingWeightmodels})

def ajax_load_wicasingGrade(request): 
    wicasingWeight_id = request.GET.get('wicasingWeight_id')
    wicasingGrademodels= WICasingGradeModel.objects.filter(wicasingWeight_id=wicasingWeight_id).all()
    print(wicasingGrademodels)
    return render (request, 'wicasings/wicasing_grade_Dropdown_list_options.html', {'wicasingGrademodels':wicasingGrademodels})
