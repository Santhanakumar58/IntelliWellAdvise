from asyncio.windows_events import NULL
from decimal import Decimal
from django.shortcuts import render, redirect
from .utils import get_plot, get_plot2, get_dummyplot
from selectedGasInjector.models import SelectedGasInjector
from .forms import GICasingModelForm
from .models import GICasingModel, GICasingGradeModel, GICasingSizeModel, GICasingWeightModel
from gideviationsurveydata.models import GIDeviationsurveydata
import pandas as pd


# Create your views here.
def list_gicasings(request):
    selectedwell = SelectedGasInjector.objects.first()  
    wellid1 = selectedwell.wellid
    gicasings = GICasingModel.objects.filter(giwellid=wellid1).all().order_by('gishoedepth')     
    gicasingdf =pd.DataFrame()
    width=0.0
    widths=[]
    depths=[]
    hangers=[]
    cements=[]
    gicasingdefs=[]
    for gicasing in gicasings:    
        csize = GICasingSizeModel.objects.get(gicasingSize = gicasing.gicasingSize)  
        if csize.gicasingSize =="20":
            width =20*2
        elif csize.gicasingSize == "18 5/8":
            width =18.625*2
        elif csize.gicasingSize == "16":
            width =16*2
        elif csize.gicasingSize == "13 3/8":
            width =13.375*2
        elif csize.gicasingSize == "11 3/4":
            width =11/75*2
        elif csize.gicasingSize == "10 3/4":
            width =10.75*2
        elif csize.gicasingSize == "9 5/8":
            width =9.625*2
        elif csize.gicasingSize == "8 5/8":
            width =8.625*2
        elif csize.gicasingSize == "7 3/4":
            width =7.75*2
        elif csize.gicasingSize == "7 5/8":
            width =7.5*2
        elif csize.gicasingSize == "7":
            width =7.0*2
        elif gicasing.GPCasing_Size == "6 5/8":
            width =6.625*2
        elif csize.gicasingSize == "5":
            width =5*2
        elif csize.gicasingSize == "4 1/2":
            width =4.5*2
        elif csize.gicasingSize == "4":
            width =4*2
        depth = gicasing.shoedepth
        hanger = gicasing.hangerDepth
        cement = gicasing.cementTop
        widths.append(width)
        depths.append(depth)
        hangers.append(hanger)
        cements.append(cement)
        gicasingdef = str(gicasing.gicasingSize)+ "  ,  " + str(gicasing.gicasingWeight) + " ppf, "
        gicasingdefs.append(gicasingdef)
    deviationdata = GIDeviationsurveydata.objects.filter(giwellid=wellid1).all()
    if deviationdata:
        chart2 = get_plot2(widths, depths, hangers, cements, deviationdata, gicasingdefs)
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
    #gicasinga=""
    #gicasingb="" 
    #gicasingc = """"""
    #for gicasing in gicasings.all() :        
    #    depth = gicasing.shoedepth
    #    cement = gicasing.cementTop 
    #    hanger = gicasing.hangerDepth       
    #    gicasingsize = gicasing.gicasingSize
    #    gicasingWeight = gicasing.gicasingWeight 
    #    gicasingdef = str(gicasingsize)+ "  ,  " + str(gicasingWeight) + " ppf, "
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
    #                gicasinga = gicasingdef           
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
    #                    gicasingb = gicasingdef
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
    #                    gicasingc = gicasingdef 
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
        

    #chart = get_plot(x,y,z,xa,ya, x1,y1,z1, x2,y2,z2,xb,yb, x3,y3,z3, x4,y4,z4,xc,yc, x5,y5,z5, gicasinga, gicasingb, gicasingc)   
      
        
    
    return render (request, 'gicasings/gicasing.html', {'gicasings': gicasings, 'chart2':chart2})

def create_gicasing(request):
   selectedwell = SelectedGasInjector.objects.first()
   gicasing = GICasingModel()
   gicasing.fgid = selectedwell.fgid
   gicasing.wellid = selectedwell.wellid
   form = GICasingModelForm(request.POST or None, instance=gicasing)
   if request.method == "POST":                  
        gicasing.gicasingType =  request.POST.get("gicasingType")  
        gicasingSize =  request.POST.get("gicasingSize") 
        weightid = request.POST.get("gicasingWeight")  
        print(weightid)     
        gicasingweight = GICasingWeightModel.objects.filter(id=weightid).first()  
        gicasing.gicasingID = gicasingweight.gicasingID       
        gradeid = request.POST.get("gicasingGrade")       
        gicasinggrade = GICasingGradeModel.objects.filter(id=gradeid).first()   
        gicasing.collapsePressure =gicasinggrade.collapsePressure  
        gicasing.burstPressure =gicasinggrade.burstPressure 
   form = GICasingModelForm(request.POST, instance=gicasing)            
   if form.is_valid():
        form.save() 
        return redirect ('gicasings:list_gicasings')    
   return render (request, 'gicasings/gicasing_form.html', {'form': form})

def update_gicasing(request, id):
    gicasing = GICasingModel.objects.get(id=id)   
    form = GICasingModelForm(request.POST or None , instance=gicasing)   
    if request.method == "POST":        
        gicasingweightid = request.POST.get('gicasingWeight')
        gicasingweight = GICasingWeightModel.objects.filter(id=gicasingweightid).first()
        gicasing.gicasingID =gicasingweight.gicasingID             
        gradeid = request.POST.get("gicasingGrade")         
        gicasinggrade = GICasingGradeModel.objects.filter(id=gradeid).first() 
        gicasing.collapsePressure =gicasinggrade.collapsePressure  
        gicasing.burstPressure =gicasinggrade.burstPressure 
    form = GICasingModelForm(request.POST or None , instance=gicasing)   
    if form.is_valid():
        form.save()
        return redirect ('gicasings:list_gicasings')
    return render (request, 'gicasings/gicasing_form.html', {'form': form, 'gicasing':gicasing})

def delete_gicasing(request, id):
   gicasing = GICasingModel.objects.get(id=id)
   
   if request.method == 'POST' :
       gicasing.delete()
       return redirect ('gicasings:list_gicasings')
   return render (request, 'gicasings/gicasing_confirm_delete.html', {'gicasing':gicasing})

def ajax_load_gicasingWeight(request):
    gicasingSize_id = request.GET.get('gicasingSize_id')   
    gicasingWeightmodels= GICasingWeightModel.objects.filter(gicasingSize_id = gicasingSize_id).all()
    print(gicasingWeightmodels)
    return render (request, 'gicasings/gicasingWeight_Dropdown_list_options.html', {'gicasingWeightmodels':gicasingWeightmodels})

def ajax_load_gicasingGrade(request): 
    gicasingWeight_id = request.GET.get('gicasingWeight_id')
    gicasingGrademodels= GICasingGradeModel.objects.filter(gicasingWeight_id=gicasingWeight_id).all()
    print(gicasingGrademodels)
    return render (request, 'gicasings/gicasing_grade_Dropdown_list_options.html', {'gicasingGrademodels':gicasingGrademodels})
