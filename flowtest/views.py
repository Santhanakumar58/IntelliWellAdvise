from django.shortcuts import render, redirect
from .models import FlowTestModel
from .forms import FlowTestForm
from selectedOilProducer.models import SelectedOilProducer
from selectedfgi.models import Selectedfgi
from .utils import *
import pandas as pd
import numpy as np
import math
import os
from django.core.files.storage import FileSystemStorage
from wellcompletion.models import Wellcompletion
from perforations.models import PerforationModel
from deviationsurveydata.models import Deviationsurveydata
import psapy.BeggsandBrill as BB
import psapy.Hagendornandbrown as HB
from opinflow.models import ProductivityIndexModel, DarcyModel, WigginsModel, VogelModel, StandingsModel, MultirateModel
from opinflow.utility import draw_CompositePR_PI, draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins
 
# Create your views here.
def list_flowtest(request):     
    well = SelectedOilProducer.objects.all().first()   
    flowtests = FlowTestModel.objects.all().filter(wellid=well.wellid).order_by("-test_Date")     
    flowtestdata = FlowTestModel.objects.all().filter(wellid=well.wellid).order_by("test_Date")  
    print(flowtestdata.count())
    if flowtestdata.count() >3:
        x=[x.test_Date for x in flowtestdata]
        y=[y.gas_Rate/1000 for y in flowtestdata]
        z=[z.gor for z in flowtestdata]
        y1=[y1.oil_Rate for y1 in flowtestdata]
        y2=[y2.water_Rate for y2 in flowtestdata]
        y3=[y3.liquid_Rate for y3 in flowtestdata]
        y4=[y4.water_Cut for y4 in flowtestdata]
        chart = get_plot(x,y,z,y1,y2, y3, y4) 
        # Decline Curve for flow test data
        df = pd.DataFrame()
        df["date"] = x
        df['q'] = y1
        df['date'] =  pd.to_datetime(df['date'], format='%Y-%m-%d')    
        t = df['date']
        q = df['q']
        print(t,q)
        qi, di, b, RMSE, graph = arps_fit(t, q, plot=True)
        qi=round(qi,0)
        di=round(di,5)
        b=round(b,5)
        RMSE=round(RMSE,6)
        ci95_qi, ci95_di, ci95_b, graph1 = arps_bootstrap(t, q)
        ci95_qi=np.round(ci95_qi,2)
        ci95_di=np.round(ci95_di,5)
        ci95_b=np.round(ci95_b,5)  
        chart1 = graph   
        chart2=graph1
        print("i am in main")
    else:
        date_data=pd.date_range('1/1/2020', periods = 20, freq ='ME') 
        oil_rate =[]
        gas_rate =[]
        water_rate =[]
        liquid_rate =[]
        gas_oil_ratio =[]
        water_cut=[]  
        liquid=0  
        i=0    
        for i in range(0,20,1):            
            liquid= 1000 * math.exp(-i*0.05)
            liquid_rate.append(liquid)
            wc = i*0.01
            water_cut.append(wc)
            wrate = wc*liquid
            water_rate.append(wrate)
            orate = (liquid-wrate)
            oil_rate.append(orate)
            gas = orate*700
            gas_rate.append(gas)
            gas_oil_ratio.append(700)
            print(i, i*0.05, liquid)
          
        chart = get_plot(date_data,gas_rate,gas_oil_ratio,oil_rate,water_rate, liquid_rate, water_cut) 
        df = pd.DataFrame()
        df["date"] = date_data
        df['q'] = oil_rate        
        df['date'] =  pd.to_datetime(df['date'], format='%Y-%m-%d')    
        t = df['date']
        q = df['q']
        print(q)
        qi, di, b, RMSE, graph = arps_fit(t, q, plot=True)
        qi=round(qi,0)
        di=round(di,5)
        b=round(b,5)
        RMSE=round(RMSE,6)
        ci95_qi, ci95_di, ci95_b, graph1 = arps_bootstrap(t, q, 1)
        ci95_qi=np.round(ci95_qi,2)
        ci95_di=np.round(ci95_di,5)
        ci95_b=np.round(ci95_b,5)  
        chart1 = graph   
        chart2=graph1
    
    return render (request, 'flowtest/flowtest.html', {'flowtests': flowtests, 'chart':chart, 'chart1':chart1, 'chart2':chart2,'qi':qi, 'di':di,'b':b, 'RMSE':RMSE,'ci95_qi':ci95_qi, 'ci95_di':ci95_di,'ci95_b':ci95_b  })

def create_flowtest(request):
    flowtest = FlowTestModel()
    selectedwell = SelectedOilProducer.objects.first()  
    selectfgi = Selectedfgi.objects.first()    
    flowtest.fgId = selectedwell.fgid
    flowtest.wellid = selectedwell.wellid   
    flowtest.formation = selectfgi.selectedsublayername
    form = FlowTestForm(request.POST or None, instance=flowtest)
    if request.method =="POST":  
        form = FlowTestForm(request.POST, request.FILES, instance=flowtest)  
    if form.is_valid():
        form.save()
        return redirect ('flowtest:list_flowtest')
    return render (request, 'flowtest/flowtest_form.html', {'form': form})

def update_flowtest(request, id):
   flowtest = FlowTestModel.objects.get(id=id)
   form = FlowTestForm(request.POST or None, instance=flowtest)
   if form.is_valid():
       form.save()
       return redirect ('flowtest:list_flowtest')
   return render (request, 'flowtest/flowtest_form.html', {'form': form, 'flowtest':flowtest})

def delete_flowtest(request, id):
   flowtest = FlowTestModel.objects.get(id=id)   
   if request.method == 'POST' :
       flowtest.delete()
       return redirect ('flowtest:list_flowtest')
   return render (request, 'flowtest/flowtest_confirm_delete.html', {'flowtest':flowtest})

def load_from_Excel(request):
    if request.method == 'POST' and request.FILES['myfile']: 
        selectedwell = SelectedOilProducer.objects.first()  
        selectfgi = Selectedfgi.objects.first()   
        id = selectedwell.wellid
        flowtests = FlowTestModel.objects.filter(wellid = id)
        flowtests.delete()
        myfile = request.FILES['myfile']       
        fs = FileSystemStorage()
        filename = fs.save('flowtestdata/'+myfile.name, myfile)
        uploaded_file_url = fs.url(filename)   
        d = os.getcwd()  
        filepath = d+'\media\\'+ filename      
        empexceldata = pd.read_excel(filepath)       
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = FlowTestModel.objects.create(fgId =selectedwell.fgid, wellid= id, test_Date=dbframe.Date, test_Duration=dbframe.Duration, 
            choke_Size =dbframe.Choke, th_Pres = dbframe.THP,th_Temp= dbframe.THT, liquid_Rate=dbframe.Liquid,
            oil_Rate = dbframe.Oil, gas_Rate = dbframe.Gas,fl_Pres = dbframe.FLP,fl_Temp= dbframe.FLT,
            sep_Pres = dbframe.SepPres,sep_Temp= dbframe.SepTemp, remarks=dbframe.Remarks, formation =selectfgi.selectedsublayername )        
            obj.save()
          
        flowtests = FlowTestModel.objects.filter(wellid = id)
        return redirect ('flowtest:list_flowtest' )
    return render (request, 'flowtest/load_from_Excel.html', {})

def production_home(request):
   
   return render (request, 'flowtest/production_home.html', {})

def tubing_performance(request):     
    well = SelectedOilProducer.objects.all().first()   
    flowtest= FlowTestModel.objects.filter(wellid=well.wellid).all().order_by("-test_Date")  
    pdrop = flowtest.first()   
    perfortaions = PerforationModel.objects.filter(wellid=well.wellid).all().order_by('-perf_Top') 
    perforation = perfortaions.first()
    midperf = (perforation.perf_Top + perforation.perf_Bottom)/2
    completions = Wellcompletion.objects.filter(wellid=well.wellid).all() 
    tubings=[]
    mds =[]
    for completion in completions:
        if completion.equipment =="Tubing":
            tubingid = completion.equip_Id
            tubings.append(tubingid)
            md=completion.equip_Md
            mds.append(md)
        if completion.equipment =="Tubing_end":
            pipe_length = completion.equip_Md
    wtr_Rate = pdrop.liquid_Rate - pdrop.oil_Rate
    wtr_Cut = wtr_Rate/pdrop.liquid_Rate
    gor = pdrop.gas_Rate/pdrop.oil_Rate

     # deviation data
    deviations = Deviationsurveydata.objects.filter(wellid=well.wellid).all().order_by('measuredDepth') 
    
    for dev in deviations:
        print(dev.measuredDepth)
   
    pressures = []
    holdups = []
    wtr_spgr =1
    # find source for these parameters
    oil_API =30
    gas_spgr =0.64
    bh_temp = 172
    temp_grad = (bh_temp-pdrop.th_Temp)/pipe_length

    if pdrop :
        source = dict(p=pdrop.th_Pres, q=int(pdrop.oil_Rate), temp=pdrop.th_Temp, wtr_rate = (pdrop.liquid_Rate - pdrop.oil_Rate))
        pipe = dict(length=pipe_length, angle=90, diam=tubings[0])
        fluid = dict(api=oil_API, wc=wtr_Cut, gor=gor, gas_spgr=gas_spgr, wtr_spgr=wtr_spgr)         
        pressures=[]
        holdups=[]
        pressures1=[]
        holdups1=[]
        pipeline_range= list(range(0,int(pipe['length']),100))
        p_current = source['p']
        p_current1 = source['p']     
        angle_current= pipe['angle']  
        t_current = source['temp']  
        for length in pipeline_range:
            if length==0:
                pressures.append(source['p'])
                holdups.append(50)
                pressures1.append(source['p'])
                holdups1.append(50)
            else:
                grad, hold = BB.Pgrad(p_current, t_current, source['q'], source['wtr_rate'], fluid['gor'],fluid['gas_spgr'],fluid['api'],fluid['wtr_spgr'], pipe['diam'], angle_current )
                p_current= source['p']+ (grad*length)
                pressures.append(p_current)
                holdups.append(hold*100)
                #Hagedorn and Brown
                grad1, hold1 = HB.Pgrad(p_current1, t_current, source['q'], source['wtr_rate'], fluid['gor'],
                                       fluid['gas_spgr'], fluid['api'],wtr_spgr, pipe['diam'], angle_current )
                p_current1= source['p']+ (grad1*length)
                pressures1.append(p_current1)
                holdups1.append(hold1*100)
                for deviation in deviations:
                    if deviation.measuredDepth >= length:
                        angle_current = deviation.angle                        
                        break
                t_current = source['temp']+ (temp_grad*length)
    else:
        pipeline_range= range(1,100,10)
        pressures = range(100,1000,10)
        holdups = range(0,10,10)
    
    holdups[0]=holdups[1]
    holdups1[0]=holdups1[1]
    chart = get_Beggs_Hagedorn_plot(pipeline_range, pressures, pressures1, holdups, holdups1)

    # Rate sensitivity 
    oil = round(pdrop.oil_Rate)
    beggs_q_pres=[]
    beggs_q =[]
    beggs_q_liquid =[]
    for q in range( 0, 5* oil, 100):
        oil_Rate =q
        wtr_Rate = oil_Rate/(1-wtr_Cut)        
        source = dict(p=pdrop.th_Pres, q=int(oil_Rate), temp=pdrop.th_Temp, wtr_rate = wtr_Rate)
        pipe = dict(length=pipe_length, angle=90, diam=2)
        fluid = dict(api=oil_API, wc=wtr_Cut, gor=gor, gas_spgr=gas_spgr, wtr_spgr=wtr_spgr)   
        p_current=source['p'] 
        t_current=source['temp']
        angle_current= pipe['angle']  
        for length in pipeline_range:
            if length==0 or q==0:
                pressures.append(source['p'])
                holdups.append(50)               
            else:
                grad, hold = BB.Pgrad(p_current,t_current, oil_Rate, source['wtr_rate'], fluid['gor'],fluid['gas_spgr'],fluid['api'],fluid['wtr_spgr'], pipe['diam'], angle_current)
                #grad, hold = HB.Pgrad(p_current1, t_current, source['q'], source['wtr_rate'], fluid['gor'],
                 #                      fluid['gas_spgr'], fluid['api'],fluid['wtr_spgr'], pipe['diam'], pipe['angle'])

                p_current= source['p']+ (grad*length)
                t_current = source['temp']+ (temp_grad*length)
                for deviation in deviations:
                    if deviation.measuredDepth >= length:
                        angle_current = deviation.angle                        
                        break
                

        beggs_q_pres.append(p_current)
        beggs_q.append(q)
        beggs_q_liquid.append(q + wtr_Rate)
        # get IPR 
        pimodels = ProductivityIndexModel.objects.filter(wellid=well.wellid).all()
        chart2, xc, y = draw_CompositePR_PI(pimodels)
        chart1 = get_Beggs_q_vs_press_plot(beggs_q_liquid, beggs_q_pres, xc,y)

    return render (request, 'flowtest/tubing_performance.html', {'chart':chart, 'chart1':chart1 })

def pressure_vs_depth(request):     
    well = SelectedOilProducer.objects.all().first()   
    flowtest= FlowTestModel.objects.filter(wellid=well.wellid).all().order_by("-test_Date")      
    pdrop = flowtest.first() 
    if not pdrop : 
        pdrop=FlowTestModel()
        pdrop.liquid_Rate=1000.0
        pdrop.oil_Rate = 900.0
        pdrop.gas_Rate = 675000
        pdrop.th_Pres =100
        pdrop.th_Temp =110
        pdrop.choke_Size =10

    print(pdrop.liquid_Rate, pdrop.th_Temp, pdrop.th_Pres)
    perfortaions = PerforationModel.objects.filter(wellid=well.wellid).all().order_by('-perf_Top') 
    perforation = perfortaions.first()
    #midperf = (perforation.perf_Top + perforation.perf_Bottom)/2
    if perforation :
        midperf = (perforation.perf_Top + perforation.perf_Bottom)/2
    else :
        midperf=1000.0
    print(midperf)
    completions = Wellcompletion.objects.filter(wellid=well.wellid).all() 
    tubings=[]
    mds =[]
    if completions:
        for completion in completions:
            if completion.equipment =="Tubing":
                tubingid = completion.equip_Id
                tubings.append(tubingid)
                md=completion.equip_Md
                mds.append(md)
            if completion.equipment =="Tubing_end":
                pipe_length = completion.equip_Md
    else :
        tubings.append(2.441)
        tubings.append(2.121)
        mds.append(1000.0)
        mds.append(800.0)
        pipe_length = midperf
    wtr_Rate = pdrop.liquid_Rate - pdrop.oil_Rate
    wtr_Cut = wtr_Rate/pdrop.liquid_Rate
    gor = pdrop.gas_Rate/pdrop.oil_Rate
    print(wtr_Rate, wtr_Cut,gor)
    pressures = []
    holdups = []
    wtr_spgr =1.01
    # find source for these parameters
    oil_API =30.0
    gas_spgr =0.64
    bh_temp = 172.0
    temp_grad = (bh_temp-pdrop.th_Temp)/pipe_length
    print(pdrop)
    if pdrop :
        source = dict(p=pdrop.th_Pres, q=int(pdrop.oil_Rate), temp=pdrop.th_Temp, wtr_rate = (pdrop.liquid_Rate - pdrop.oil_Rate))
        pipe = dict(length=pipe_length, angle=60.0, diam=tubings[0])
        fluid = dict(api=oil_API, wc=wtr_Cut, gor=gor, gas_spgr=gas_spgr, wtr_spgr=wtr_spgr)         
        pressures=[]
        holdups=[]
        pressures1=[]
        holdups1=[]
        pipeline_range= list(range(0,int(pipe['length']),100))
        p_current = source['p']
        p_current1 = source['p']       
        for length in pipeline_range:
            if length==0:
                pressures.append(source['p'])
                holdups.append(50)
                pressures1.append(source['p'])
                holdups1.append(50)
            else:
                grad, hold = BB.Pgrad(p_current, source['temp'], source['q'], source['wtr_rate'], fluid['gor'],fluid['gas_spgr'],fluid['api'],fluid['wtr_spgr'], pipe['diam'], pipe['angle'])
                p_current= source['p']+ (grad*length)
                pressures.append(p_current)
                holdups.append(hold*100)
                #Hagedorn and Brown
                grad1, hold1 = HB.Pgrad(p_current1, source['temp'], source['q'], source['wtr_rate'], fluid['gor'],
                                       fluid['gas_spgr'], fluid['api'],wtr_spgr, pipe['diam'], pipe['angle'])
                p_current1= source['p']+ (grad1*length)
                pressures1.append(p_current1)
                holdups1.append(hold1*100)
    else:
        pipeline_range= range(1,100,10)
        pressures = range(100,1000,10)
        holdups = range(0,10,10)
    
    holdups[0]=holdups[1]
    holdups1[0]=holdups1[1]
    chart = get_Beggs_Hagedorn_plot(pipeline_range, pressures, pressures1, holdups, holdups1)

    return render (request, 'flowtest/pressure_vs_depth.html', {'chart':chart})
 
def inflow_outflow(request):     
    well = SelectedOilProducer.objects.all().first()   
    flowtest= FlowTestModel.objects.filter(wellid=well.wellid).all().order_by("-test_Date")  
    pdrop = flowtest.first()   
    perfortaions = PerforationModel.objects.filter(wellid=well.wellid).all().order_by('-perf_Top') 
    perforation = perfortaions.first()
    midperf = (perforation.perf_Top + perforation.perf_Bottom)/2
    completions = Wellcompletion.objects.filter(wellid=well.wellid).all() 
    tubings=[]
    mds =[]
    for completion in completions:
        if completion.equipment =="Tubing":
            tubingid = completion.equip_Id
            tubings.append(tubingid)
            md=completion.equip_Md
            mds.append(md)
        if completion.equipment =="Tubing_end":
            pipe_length = completion.equip_Md
    wtr_Rate = pdrop.liquid_Rate - pdrop.oil_Rate
    wtr_Cut = wtr_Rate/pdrop.liquid_Rate
    gor = pdrop.gas_Rate/pdrop.oil_Rate   
    pressures = []
    holdups = []
    wtr_spgr =1   
    oil_API =30
    gas_spgr =0.64
    bh_temp = 172
    temp_grad = (bh_temp-pdrop.th_Temp)/pipe_length  
    oil = round(pdrop.oil_Rate)
    beggs_q_pres=[]
    beggs_q =[]
    
    beggs_q_liquid =[]    
    for q in range( 0, 5050,50):
        oil_Rate =q
        wtr_Rate = oil_Rate/(1-wtr_Cut)        
        source = dict(p=pdrop.th_Pres, q=int(oil_Rate), temp=pdrop.th_Temp, wtr_rate = wtr_Rate)
        pipe = dict(length=pipe_length, angle=90, diam=tubings[0])
        fluid = dict(api=oil_API, wc=wtr_Cut, gor=gor, gas_spgr=gas_spgr, wtr_spgr=wtr_spgr)   
        p_current=source['p'] 
        t_current=source['temp']
        pipeline_range= list(range(0,int(pipe['length']),100))
        for length in pipeline_range:
            if length==0 or q==0:
                pressures.append(source['p'])
                holdups.append(50)               
            else:
                #grad, hold = BB.Pgrad(p_current,t_current, oil_Rate, source['wtr_rate'], fluid['gor'],fluid['gas_spgr'],fluid['api'],fluid['wtr_spgr'], pipe['diam'], pipe['angle'])
                grad, hold = HB.Pgrad(p_current, t_current, oil_Rate, source['wtr_rate'], fluid['gor'],
                                      fluid['gas_spgr'], fluid['api'],fluid['wtr_spgr'], pipe['diam'], pipe['angle'])

                p_current= source['p']+ (grad*length)
                t_current = source['temp']+ (temp_grad*length)
        beggs_q_pres.append(p_current)
        beggs_q.append(q)
        beggs_q_liquid.append(q + wtr_Rate)
        
    df = pd.DataFrame()  
    df['x1']= beggs_q_liquid
    df['y1']= beggs_q_pres    
    # get IPR 
    if well.inflow =='PI':        
        pimodels = ProductivityIndexModel.objects.filter(wellid=well.wellid).all()
        chart,xc,y,pis = draw_CompositePR_PI(pimodels)       
    elif well.inflow =='Vogel':
        vogelmodels = VogelModel.objects.filter(wellid=well.wellid).all()        
        chart,xc,y= draw_compositeIPR_Vogel(vogelmodels)  
    elif well.inflow =='Standing':
        standingmodels = StandingsModel.objects.filter(wellid=well.wellid).all()        
        chart,xc,y = draw_compositeIPR_Standing(standingmodels) 
    elif well.inflow =='Wiggins':
        wigginmodels = WigginsModel.objects.filter(wellid=well.wellid).all()        
        chart,xc,y = draw_compositeIPR_Wiggins(wigginmodels) 
    elif well.inflow =='MultiRate':
        multiratemodels = MultirateModel.objects.filter(wellid=well.wellid).all()
        chart,xc,y =draw_CompositeIPR_Multirate(multiratemodels)  
    elif well.inflow =='Darcy':        
        darcymodels = DarcyModel.objects.filter(wellid=well.wellid).all()  
        chart,xc,y = draw_CompositeIPR_Darcy(darcymodels) 
    df['x2']= xc
    df['y2']= y    
    chart1 = get_Beggs_q_vs_press_plot(df, pdrop)

    return render (request, 'flowtest/inflow_outflow.html', {'pdrop': pdrop ,'chart1':chart1 })

def tubing_Sensitivity(request):     
    well = SelectedOilProducer.objects.all().first()   
    flowtest= FlowTestModel.objects.filter(wellid=well.wellid).all().order_by("-test_Date")  
    pdrop = flowtest.first()   
    perfortaions = PerforationModel.objects.filter(wellid=well.wellid).all().order_by('-perf_Top') 
    perforation = perfortaions.first()
    midperf = (perforation.perf_Top + perforation.perf_Bottom)/2
    completions = Wellcompletion.objects.filter(wellid=well.wellid).all() 
    tubings=[]
    mds =[]
    for completion in completions:
        if completion.equipment =="Tubing":
            tubingid = completion.equip_Id
            tubings.append(tubingid)
            md=completion.equip_Md
            mds.append(md)
        if completion.equipment =="Tubing_end":
            pipe_length = completion.equip_Md
    wtr_Rate = pdrop.liquid_Rate - pdrop.oil_Rate
    wtr_Cut = wtr_Rate/pdrop.liquid_Rate
    gor = pdrop.gas_Rate/pdrop.oil_Rate   
    pressures = []
    holdups = []
    wtr_spgr =1   
    oil_API =30
    gas_spgr =0.64
    bh_temp = 172
    temp_grad = (bh_temp-pdrop.th_Temp)/pipe_length  
    oil = round(pdrop.oil_Rate)
    t1_liquid =[]
    t1_pressure =[]
    t1_oil =[]
    t2_liquid =[]
    t2_pressure =[]
    t2_oil =[]
    t3_liquid =[]
    t3_pressure =[]
    t3_oil =[]
    t4_liquid =[]
    t4_pressure =[]
    t4_oil =[]
    tubingsizes=[2.441, 2.867, 3.883] 
    for tubing in tubingsizes:
        for q in range( 0, 2525,25):
            oil_Rate =q
            wtr_Rate = oil_Rate/(1-wtr_Cut)        
            source = dict(p=pdrop.th_Pres, q=int(oil_Rate), temp=pdrop.th_Temp, wtr_rate = wtr_Rate)
            pipe = dict(length=pipe_length, angle=90, diam=tubing)
            fluid = dict(api=oil_API, wc=wtr_Cut, gor=gor, gas_spgr=gas_spgr, wtr_spgr=wtr_spgr)   
            p_current=source['p'] 
            t_current=source['temp']
            pipeline_range= list(range(0,int(pipe['length']),100))
            for length in pipeline_range:
                if length==0 or q==0:
                    pressures.append(source['p'])
                    holdups.append(50)               
                else:
                    #grad, hold = BB.Pgrad(p_current,t_current, oil_Rate, source['wtr_rate'], fluid['gor'],fluid['gas_spgr'],fluid['api'],fluid['wtr_spgr'], pipe['diam'], pipe['angle'])
                    grad, hold = HB.Pgrad(p_current, t_current, oil_Rate, source['wtr_rate'], fluid['gor'],
                                          fluid['gas_spgr'], fluid['api'],fluid['wtr_spgr'], pipe['diam'], pipe['angle'])
                    p_current= source['p']+ (grad*length)
                    t_current = source['temp']+ (temp_grad*length)
            if tubing==2.441:
                t1_liquid.append(q + wtr_Rate)
                t1_pressure.append(p_current)
                t1_oil.append(q)                
            if tubing==2.867:
                t2_liquid.append(q + wtr_Rate)
                t2_pressure.append(p_current)
                t2_oil.append(q)
            if tubing==3.883:
                t3_liquid.append(q + wtr_Rate)
                t3_pressure.append(p_current)
                t3_oil.append(q)            
        
    df = pd.DataFrame()  
    df['x1']=t1_liquid
    df['y1']= t1_pressure   
    df['y2']= t2_pressure   
    df['y3']= t3_pressure   
   
    # get IPR 
    if well.inflow =='PI':        
        pimodels = ProductivityIndexModel.objects.filter(wellid=well.wellid).all()
        chart,xc,y, pis = draw_CompositePR_PI(pimodels)       
    elif well.inflow =='Vogel':
        vogelmodels = VogelModel.objects.filter(wellid=well.wellid).all()        
        chart,xc,y= draw_compositeIPR_Vogel(vogelmodels)  
    elif well.inflow =='Standing':
        standingmodels = StandingsModel.objects.filter(wellid=well.wellid).all()        
        chart,xc,y = draw_compositeIPR_Standing(standingmodels) 
    elif well.inflow =='Wiggins':
        wigginmodels = WigginsModel.objects.filter(wellid=well.wellid).all()        
        chart,xc,y = draw_compositeIPR_Wiggins(wigginmodels) 
    elif well.inflow =='MultiRate':
        multiratemodels = MultirateModel.objects.filter(wellid=well.wellid).all()
        chart,xc,y =draw_CompositeIPR_Multirate(multiratemodels)  
    elif well.inflow =='Darcy':        
        darcymodels = DarcyModel.objects.filter(wellid=well.wellid).all()  
        chart,xc,y = draw_CompositeIPR_Darcy(darcymodels) 
    df['x5']= xc
    df['y5']= y       
    chart1 = get_tubing_sensitivity_plot(df, pdrop)

    return render (request, 'flowtest/tubing_SENSITIVITY.html', {'pdrop': pdrop ,'chart1':chart1 })

def gor_Sensitivity(request):     
    well = SelectedOilProducer.objects.all().first()   
    flowtest= FlowTestModel.objects.filter(wellid=well.wellid).all().order_by("-test_Date")  
    pdrop = flowtest.first()   
    perfortaions = PerforationModel.objects.filter(wellid=well.wellid).all().order_by('-perf_Top') 
    perforation = perfortaions.first()
    midperf = (perforation.perf_Top + perforation.perf_Bottom)/2
    completions = Wellcompletion.objects.filter(wellid=well.wellid).all() 
    tubings=[]
    mds =[]
    for completion in completions:
        if completion.equipment =="Tubing":
            tubingid = completion.equip_Id
            tubings.append(tubingid)
            md=completion.equip_Md
            mds.append(md)
        if completion.equipment =="Tubing_end":
            pipe_length = completion.equip_Md
    wtr_Rate = pdrop.liquid_Rate - pdrop.oil_Rate
    wtr_Cut = wtr_Rate/pdrop.liquid_Rate
    gor = pdrop.gas_Rate/pdrop.oil_Rate   
    pressures = []
    holdups = []
    wtr_spgr =1   
    oil_API =30
    gas_spgr =0.64
    bh_temp = 172
    temp_grad = (bh_temp-pdrop.th_Temp)/pipe_length  
    oil = round(pdrop.oil_Rate)
    gor1_liquid =[]
    gor1_pressure =[]
    gor1_oil =[]
    gor2_liquid =[]
    gor2_pressure =[]
    gor2_oil =[]
    gor3_liquid =[]
    gor3_pressure =[]
    gor3_oil =[]
    gor4_liquid =[]
    gor4_pressure =[]
    gor4_oil =[]
    gor5_liquid =[]
    gor5_pressure =[]
    gor5_oil =[]
    sgors=[gor*0.80, gor*0.90, gor, gor*1.10, gor*1.20] 
    for sgor in sgors:
        for q in range( 0, 5050,50):
            oil_Rate =q
            wtr_Rate = oil_Rate/(1-wtr_Cut)        
            source = dict(p=pdrop.th_Pres, q=int(oil_Rate), temp=pdrop.th_Temp, wtr_rate = wtr_Rate)
            pipe = dict(length=pipe_length, angle=90, diam=tubings[0])
            fluid = dict(api=oil_API, wc=wtr_Cut, gor=sgor, gas_spgr=gas_spgr, wtr_spgr=wtr_spgr)   
            p_current=source['p'] 
            t_current=source['temp']
            pipeline_range= list(range(0,int(pipe['length']),100))
            for length in pipeline_range:
                if length==0 or q==0:
                    pressures.append(source['p'])
                    holdups.append(50)               
                else:
                    #grad, hold = BB.Pgrad(p_current,t_current, oil_Rate, source['wtr_rate'], fluid['gor'],fluid['gas_spgr'],fluid['api'],fluid['wtr_spgr'], pipe['diam'], pipe['angle'])
                    grad, hold = HB.Pgrad(p_current, t_current, oil_Rate, source['wtr_rate'], fluid['gor'],
                                          fluid['gas_spgr'], fluid['api'],fluid['wtr_spgr'], pipe['diam'], pipe['angle'])
                    p_current= source['p']+ (grad*length)
                    t_current = source['temp']+ (temp_grad*length)
            if sgor==gor*0.8:
                gor1_liquid.append(q + wtr_Rate)
                gor1_pressure.append(p_current)
                gor1_oil.append(q)               
            if sgor==gor*0.9:
                gor2_liquid.append(q + wtr_Rate)
                gor2_pressure.append(p_current)
                gor2_oil.append(q)
            if sgor==gor:
                gor3_liquid.append(q + wtr_Rate)
                gor3_pressure.append(p_current)
                gor3_oil.append(q)
            if sgor==gor*1.1:
                gor4_liquid.append(q + wtr_Rate)
                gor4_pressure.append(p_current)
                gor4_oil.append(q)
            if sgor==gor*1.2:
                gor5_liquid.append(q + wtr_Rate)
                gor5_pressure.append(p_current)
                gor5_oil.append(q)
        
    df = pd.DataFrame()  
    df['x1']= gor1_liquid
    df['y1']= gor1_pressure   
    df['y2']= gor2_pressure   
    df['y3']= gor3_pressure   
    df['y4']= gor4_pressure
    df['y5']= gor5_pressure
    # get IPR    
    if well.inflow =='PI':        
        pimodels = ProductivityIndexModel.objects.filter(wellid=well.wellid).all()
        chart,xc,y,pis = draw_CompositePR_PI(pimodels)       
    elif well.inflow =='Vogel':
        vogelmodels = VogelModel.objects.filter(wellid=well.wellid).all()        
        chart,xc,y= draw_compositeIPR_Vogel(vogelmodels)  
    elif well.inflow =='Standing':
        standingmodels = StandingsModel.objects.filter(wellid=well.wellid).all()        
        chart,xc,y = draw_compositeIPR_Standing(standingmodels) 
    elif well.inflow =='Wiggins':
        wigginmodels = WigginsModel.objects.filter(wellid=well.wellid).all()        
        chart,xc,y = draw_compositeIPR_Wiggins(wigginmodels) 
    elif well.inflow =='MultiRate':
        multiratemodels = MultirateModel.objects.filter(wellid=well.wellid).all()
        chart,xc,y =draw_CompositeIPR_Multirate(multiratemodels)  
    elif well.inflow =='Darcy':        
        darcymodels = DarcyModel.objects.filter(wellid=well.wellid).all()  
        chart,xc,y = draw_CompositeIPR_Darcy(darcymodels) 
    df['x6']= xc
    df['y6']= y   
    chart1 = get_gor_sensitivity_plot(df, pdrop)
    return render (request, 'flowtest/gor_sensitivity.html', {'pdrop': pdrop ,'chart1':chart1 })

def gaslift_design(request):
    well = SelectedOilProducer.objects.all().first()   
    flowtest= FlowTestModel.objects.filter(wellid=well.wellid).all().order_by("-test_Date")  
    pdrop = flowtest.first()   
    perfortaions = PerforationModel.objects.filter(wellid=well.wellid).all().order_by('-perf_Top') 
    perforation = perfortaions.first()
    midperf = (perforation.perf_Top + perforation.perf_Bottom)/2
    completions = Wellcompletion.objects.filter(wellid=well.wellid).all()      
    wellhead_pressure = 100.0
    total_depth = 7500.0
    Pcs = 870.0
    Pko = 920.0
    Glf=0.5
    Gs =0.5
    Q=600.0
    BHSP = 2000.0
    J=2.55
    Tre =180.0
    Ts = 100.0
    R =0.1534
    print(total_depth)
    df,Pwf,Pwh1,Pwh2,Pcs,Pko,total_depth,reservoir_line = gaslift_design_function(total_depth,wellhead_pressure, Pcs ,Pko,Glf,Gs,Q,BHSP,J,Tre,Ts,R)
    print(df)    
    chart1 = get_gaslift_design_plot(df,Pwf,Pwh1,Pwh2,Pcs,Pko,total_depth,reservoir_line)

    return render (request, 'flowtest/gaslift_design.html', {'pdrop': pdrop ,'chart1':chart1 })




    """
    total_depth : total depth to the pay zone  ( ft )
    wellhead_pressure : tuning pressure at the surface ( psi )
    Pcs : surface casing pressure ( injection pressure) ( psi )
    Pko : kick_off pressure if it exists ( psi )
    Glf : load flowing gradient ( psi/ft )
    Gs : static gradient ( psi/ft )
    Q : oil flow rate ( bbl/day)
    BHSP : bottom_hole static pressure -> reservoir pressure
    J : productivity index 
    Tres : reservoir temperature ( F )
    Ts : surface following temperature ( F )
    R: port size 
    """
    reservoir_line,casing_line = get_equations(Pcs,J,BHSP,Q,Gs,total_depth)
    injection_depth,injection_pressure = find_intersection(reservoir_line,casing_line)
    Gf1,Gf2,Pwh2 = get_GF1_GF2(wellhead_pressure,Pcs,injection_depth,injection_pressure)
    df=get_spacings(wellhead_pressure,Pwh2,Pcs,Pko,Glf,Gf2,injection_depth,injection_pressure) 
    # make the Ct and get Pd and also Pvo
    Ct_data= pd.read_csv("Ct_Data.csv")
    Tg= ((Tre-Ts) / total_depth)
    df["Temp"] = np.round(Ts + Tg * df["Depth"],2)
    df["Pdt"] = np.round((1-R)*df["P1"] + R*df["P2"],2)
    df["Ct"]= df.Temp.apply(lambda T: (Ct_data[(Ct_data["temp"]== round(T))]["Ct"].values)[0] ) 
    df["Pd"]=round(df["Pdt"] * df["Ct"],2)
    df["Pvo"] = round(df["Pd"] / (1-R) ,2)
    
    return df