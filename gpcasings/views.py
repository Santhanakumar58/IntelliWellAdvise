from asyncio.windows_events import NULL
from decimal import Decimal
from django.shortcuts import render, redirect
from .utils import get_plot, get_plot2, get_dummyplot
from selectedGasProducer.models import SelectedGasProducer
from .forms import GPCasingModelForm
from .models import GPCasingModel, GPCasingGradeModel, GPCasingSizeModel, GPCasingWeightModel
from deviationsurveydata.models import Deviationsurveydata
import pandas as pd


# Create your views here.
def list_gpcasings(request):
    selectedwell = SelectedGasProducer.objects.first()  
    wellid1 = selectedwell.wellid
    gpcasings = GPCasingModel.objects.filter(gpwellid=wellid1).all().order_by('gpshoedepth')     
    gpcasingdf =pd.DataFrame()
    width=0.0
    widths=[]
    depths=[]
    hangers=[]
    cements=[]
    gpcasingdefs=[]
    for gpcasing in gpcasings:    
        csize = GPCasingSizeModel.objects.get(gpcasingSize = gpcasing.gpcasingSize)  
        if csize.gpcasingSize =="20":
            width =20*2
        elif csize.gpcasingSize == "18 5/8":
            width =18.625*2
        elif csize.gpcasingSize == "16":
            width =16*2
        elif csize.gpcasingSize == "13 3/8":
            width =13.375*2
        elif csize.gpcasingSize == "11 3/4":
            width =11/75*2
        elif csize.gpcasingSize == "10 3/4":
            width =10.75*2
        elif csize.gpcasingSize == "9 5/8":
            width =9.625*2
        elif csize.gpcasingSize == "8 5/8":
            width =8.625*2
        elif csize.gpcasingSize == "7 3/4":
            width =7.75*2
        elif csize.gpcasingSize == "7 5/8":
            width =7.5*2
        elif csize.gpcasingSize == "7":
            width =7.0*2
        elif gpcasing.GPCasing_Size == "6 5/8":
            width =6.625*2
        elif csize.gpcasingSize == "5":
            width =5*2
        elif csize.gpcasingSize == "4 1/2":
            width =4.5*2
        elif csize.gpcasingSize == "4":
            width =4*2
        depth = gpcasing.shoedepth
        hanger = gpcasing.hangerDepth
        cement = gpcasing.cementTop
        widths.append(width)
        depths.append(depth)
        hangers.append(hanger)
        cements.append(cement)
        gpcasingdef = str(gpcasing.gpcasingSize)+ "  ,  " + str(gpcasing.gpcasingWeight) + " ppf, "
        gpcasingdefs.append(gpcasingdef)
    deviationdata = Deviationsurveydata.objects.filter(wellid=wellid1).all()
    if deviationdata:
        chart2 = get_plot2(widths, depths, hangers, cements, deviationdata, gpcasingdefs)
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
    #gpcasinga=""
    #gpcasingb="" 
    #gpcasingc = """"""
    #for gpcasing in gpcasings.all() :        
    #    depth = gpcasing.shoedepth
    #    cement = gpcasing.cementTop 
    #    hanger = gpcasing.hangerDepth       
    #    gpcasingsize = gpcasing.gpcasingSize
    #    gpcasingWeight = gpcasing.gpcasingWeight 
    #    gpcasingdef = str(gpcasingsize)+ "  ,  " + str(gpcasingWeight) + " ppf, "
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
    #                gpcasinga = gpcasingdef           
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
    #                    gpcasingb = gpcasingdef
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
    #                    gpcasingc = gpcasingdef 
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
        

    #chart = get_plot(x,y,z,xa,ya, x1,y1,z1, x2,y2,z2,xb,yb, x3,y3,z3, x4,y4,z4,xc,yc, x5,y5,z5, gpcasinga, gpcasingb, gpcasingc)   
      
        
    
    return render (request, 'gpcasings/gpcasing.html', {'gpcasings': gpcasings, 'chart2':chart2})

def create_gpcasing(request):
   selectedwell = SelectedGasProducer.objects.first()
   gpcasing = GPCasingModel()
   gpcasing.fgid = selectedwell.fgid
   gpcasing.wellid = selectedwell.wellid
   form = GPCasingModelForm(request.POST or None, instance=gpcasing)
   if request.method == "POST":                  
        gpcasing.gpcasingType =  request.POST.get("gpcasingType")  
        gpcasingSize =  request.POST.get("gpcasingSize") 
        weightid = request.POST.get("gpcasingWeight")  
        print(weightid)     
        gpcasingweight = GPCasingWeightModel.objects.filter(id=weightid).first()  
        gpcasing.gpcasingID = gpcasingweight.gpcasingID       
        gradeid = request.POST.get("gpcasingGrade")       
        gpcasinggrade = GPCasingGradeModel.objects.filter(id=gradeid).first()   
        gpcasing.collapsePressure =gpcasinggrade.collapsePressure  
        gpcasing.burstPressure =gpcasinggrade.burstPressure 
   form = GPCasingModelForm(request.POST, instance=gpcasing)            
   if form.is_valid():
        form.save() 
        return redirect ('gpcasings:list_gpcasings')    
   return render (request, 'gpcasings/gpcasing_form.html', {'form': form})

def update_gpcasing(request, id):
    gpcasing = GPCasingModel.objects.get(id=id)   
    form = GPCasingModelForm(request.POST or None , instance=gpcasing)   
    if request.method == "POST":        
        gpcasingweightid = request.POST.get('gpcasingWeight')
        gpcasingweight = GPCasingWeightModel.objects.filter(id=gpcasingweightid).first()
        gpcasing.gpcasingID =gpcasingweight.gpcasingID             
        gradeid = request.POST.get("gpcasingGrade")         
        gpcasinggrade = GPCasingGradeModel.objects.filter(id=gradeid).first() 
        gpcasing.collapsePressure =gpcasinggrade.collapsePressure  
        gpcasing.burstPressure =gpcasinggrade.burstPressure 
    form = GPCasingModelForm(request.POST or None , instance=gpcasing)   
    if form.is_valid():
        form.save()
        return redirect ('gpcasings:list_gpcasings')
    return render (request, 'gpcasings/gpcasing_form.html', {'form': form, 'gpcasing':gpcasing})

def delete_gpcasing(request, id):
   gpcasing = GPCasingModel.objects.get(id=id)
   
   if request.method == 'POST' :
       gpcasing.delete()
       return redirect ('gpcasings:list_gpcasings')
   return render (request, 'gpcasings/gpcasing_confirm_delete.html', {'gpcasing':gpcasing})

def ajax_load_gpcasingWeight(request):
    gpcasingSize_id = request.GET.get('gpcasingSize_id')   
    gpcasingWeightmodels= GPCasingWeightModel.objects.filter(gpcasingSize_id = gpcasingSize_id).all()
    print(gpcasingWeightmodels)
    return render (request, 'gpcasings/gpcasingWeight_Dropdown_list_options.html', {'gpcasingWeightmodels':gpcasingWeightmodels})

def ajax_load_gpcasingGrade(request): 
    gpcasingWeight_id = request.GET.get('gpcasingWeight_id')
    gpcasingGrademodels= GPCasingGradeModel.objects.filter(gpcasingWeight_id=gpcasingWeight_id).all()
    print(gpcasingGrademodels)
    return render (request, 'gpcasings/gpcasing_grade_Dropdown_list_options.html', {'gpcasingGrademodels':gpcasingGrademodels})
