from ast import Global
from asyncio.windows_events import NULL
from cProfile import label
from decimal import Decimal
import math
from statistics import linear_regression
from turtle import color
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
import numpy as np
from blackoilpvt.models import BlackoilPVT
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity
from opinflow.models import DarcyModel, MultirateModel, ProductivityIndexModel, StandingsModel, VogelModel, WigginsModel

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,layer1):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title("Composite IPR")
    if x != NULL:
        plt.plot(x, y, color='green', label= layer1)
    plt.xticks(rotation=45)
    plt.xlabel('Liquid Rate bbls/day')
    plt.ylabel('Pressure (psi)') 
    plt.legend()
    plt.tight_layout()
    plt.xlim(0)
    plt.ylim(0)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def get_plot1(x,y, x1,y1,xc, layer1, layer2):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title("Composite IPR")
    if x != NULL:
        plt.plot(x,y, color='red', label=layer1)
    if x1 != NULL:
        plt.plot(x1,y1, color='orange' , label=layer2)
    if xc != NULL:
        plt.plot(xc,y, color='green', label="Composite") 
    plt.xticks(rotation=45)
    plt.xlabel('Liquid Rate bbls/day')
    plt.ylabel('Pressure (psi)') 
    plt.legend()
    plt.tight_layout()
    plt.xlim(0)
    plt.ylim(0)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def get_plot2(x,y, x1,y1, x2, y2,xc, layer1, layer2, layer3):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title("Composite IPR")
    if x != NULL:
        plt.plot(x,y, color='red', label=layer1)
    if x1 != NULL:
        plt.plot(x1,y1, color='orange', label=layer2)
    if x2 != NULL:
        plt.plot(x2,y2, color='gray', label=layer3)
    if xc != NULL:
        plt.plot(xc,y, color='green', label="Composite")   
    plt.xticks(rotation=45)
    plt.xlabel('Liquid Rate bbls/day')
    plt.ylabel('Pressure (psi)') 
    plt.legend()
    plt.tight_layout()
    plt.xlim(0)
    plt.ylim(0)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def get_plot3(x,y, x1,y1, x2, y2,x3, y3,xc, layer1, layer2, layer3, layer4):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title("Composite IPR")
    ax=plt.axes()
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(2.5)  # change width
        ax.spines[axis].set_color('green')    # change color  
    if x != NULL:
        plt.plot(x,y, color='red', label=layer1)
    if x1 != NULL:
        plt.plot(x1,y1, color='orange', label=layer2)
    if x2 != NULL:
        plt.plot(x2,y2, color='gray', label=layer3)
    if x3 != NULL:
        plt.plot(x3,y3, color='blue', label=layer4)
    if xc !=NULL:
        plt.plot(xc,y, color='green', label='Composite')
    plt.xticks(rotation=45)
    plt.xlabel('Liquid Rate bbls/day')
    plt.ylabel('Pressure (psi)') 
    plt.legend()
    plt.tight_layout()
    plt.xlim(0)
    plt.ylim(0)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def get_plot4(x,y,x1,y1,x2,y2,layer1):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,4))
    plt.title("Current and Future IPRs", color='orangered')
    if x != NULL:
        plt.plot(x, y, color='green', label= layer1)
    if x1 != NULL:
        plt.plot(x1, y1, color='red', label= layer1)
    if x2 != NULL:
        plt.plot(x2, y2, color='blue', label= layer1)
    plt.xticks(rotation=45)
    plt.xlabel('Liquid Rate bbls/day')
    plt.ylabel('Pressure (psi)') 
    plt.legend()
    plt.tight_layout()
    plt.xlim(0)
    plt.ylim(0)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def get_loglogplot(logx,logy):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,3))
    plt.title("Log-Log plot for estimating n")
    if logx != NULL:
        # slope, intercept = np.polyfit(np.log(logx), np.log(logy), 1)
        slope, intercept = linear_regression(np.log(logx), np.log(logy))       
        plt.scatter(logx, logy, color='green')
        slope = 1/slope
        slope = math.trunc(slope *1000000)/1000000
        Global.slope = slope
        # plt.loglog(logx, logy, color='red', label='n =' + str(slope))
        z = np.polyfit(logx, logy, 1)
        p = np.poly1d(z)
        plt.plot(logx, p(logx), color='red', label='n =' + str(slope ))
    plt.xticks(rotation=45)
    plt.xlabel('Liquid Rate bbls/day')    
    plt.ylabel('Pr^2 - Pwf^2') 
    plt.legend()
    plt.tight_layout()   
    # plt.title("y=%.6fx+%.6f"%(z[0],z[1]))
   
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def draw_CompositePR_PI (pimodels = ProductivityIndexModel()):
    x=[] 
    y=[]
    x1=[] 
    y1=[]
    x2=[] 
    y2=[]
    x3=[] 
    y3=[]
    xc=[]  
    pis=[]  
    maxResPres =0.0
    k=len(pimodels)
    pimodels
    for pimodel in pimodels :
        if pimodel.reservoir_Pressure > maxResPres:
            maxResPres = pimodel.reservoir_Pressure  
    j=0
    for pimodel in pimodels:            
        delp = maxResPres/100
        pvt = BlackoilPVT.objects.filter(wellName =pimodel.pvt_Well, subLayer =pimodel.layer_Name).last()
        temperature = pvt.reservoirTemperature
        oilgravity = pvt.oilAPIgravity
        solutiongas = pvt.solutionGOR
        gasgravity = pvt.gasGravity
        oilg = 141.5/(oilgravity+ 131.5) 
        Pb = get_Pb( pvt)
        respres = pimodel.reservoir_Pressure
        Qbp = pimodel.productivity_index * (pimodel.reservoir_Pressure - Pb)
        pis.append(pimodel.productivity_index)
        Qmax = Qbp/(1 - 0.2 * ((Pb) / respres) - 0.8 * math.pow((Pb) / respres, 2))
        for i in range(101):
            pres = i*delp
            rate = (Qmax * (1 - 0.2 * (pres / respres) - 0.8 * math.pow(pres / respres, 2)))           
            if k==0:
                x.append(0)
                y.append(0)
                chart=get_plot(x,y, "No Data")
            elif k ==1:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= pimodel.layer_Name
            elif k==2:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= pimodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres)
                    layer2= pimodel.layer_Name
            elif k==3:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= pimodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= pimodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= pimodel.layer_Name
            elif k==4:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= pimodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= pimodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= pimodel.layer_Name
                elif j==3:
                    x3.append(rate)
                    y3.append(pres)
                    layer4= pimodel.layer_Name
        j=j+1
    if k==0:
        x.append(0)
        y.append(0)       
        chart=get_plot(x,y,"No Data")   
    elif k==1:
        for i in range(101):
            xc.append(x[i])
        chart=get_plot(x,y, layer1)
    elif k==2:
        for i in range(101):
            xc.append(x[i] + x1[i])
        chart=get_plot1(x,y, x1,y1,xc, layer1, layer2)
    elif k==3:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i] )
        chart=get_plot2(x,y, x1,y1,x2,y2,xc, layer1, layer2, layer3)
    elif k==4:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i]+ x3[i] )
        chart=get_plot3(x,y, x1,y1,x2,y2,x3,y3,xc,layer1, layer2, layer3, layer4)
    return chart, xc, y, pis

def draw_compositeIPR_Vogel(vogelmodels = VogelModel()):
    x=[] 
    y=[]
    x1=[] 
    y1=[]
    x2=[] 
    y2=[]
    x3=[] 
    y3=[]
    xc=[]
    maxResPres =0.0
    k=len(vogelmodels)    
    for vogelmodel in vogelmodels :
        if vogelmodel.reservoir_Pressure > maxResPres:
            maxResPres = vogelmodel.reservoir_Pressure          
    j=0
    for vogelmodel in vogelmodels:            
        delp = maxResPres/100
        pvt = BlackoilPVT.objects.filter(wellName =vogelmodel.pvt_Well, subLayer =vogelmodel.layer_Name).last()
        temperature = pvt.reservoirTemperature
        oilgravity = pvt.oilAPIgravity
        solutiongas = pvt.solutionGOR
        gasgravity = pvt.gasGravity
        oilg = Decimal('141.5')/(oilgravity+ Decimal('131.5')) 
        Pb = get_Pb( pvt)
        respres = vogelmodel.reservoir_Pressure
        Qbp = vogelmodel.vogel_Test_Rate
        pwf =vogelmodel.vogel_Test_Pressure
        Qmax = Qbp/(1 - 0.2 * (float(pwf) / respres) - 0.8 * math.pow(float(pwf) / respres, 2));
        for i in range(101):
            pres = i*delp
            rate = Decimal(Qmax * (1 - 0.2 * (pres / respres) - 0.8 * math.pow(pres / respres, 2)))           
            if k==0:
                x.append(0)
                y.append(0)
                chart=get_plot(x,y, "No Data")                
            elif k ==1:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= 'Composite IPR - ' + str(vogelmodel.layer_Name)                      
            elif k==2:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= vogelmodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres)
                    layer2= vogelmodel.layer_Name
            elif k==3:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= vogelmodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= vogelmodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= vogelmodel.layer_Name
                    
            elif k==4:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= vogelmodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= vogelmodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= vogelmodel.layer_Name
                elif j==3:
                    x3.append(rate)
                    y3.append(pres)
                    layer4= vogelmodel.layer_Name
        j=j+1
    if k==0:
        x.append(0)
        y.append(0)
        chart=get_plot(x,y,"No Data")  
    elif k==1:
        chart=get_plot(x,y,layer1)
    elif k==2:
        for i in range(101):
            xc.append(x[i] + x1[i])
            print(x[i], x1[1], xc)
        chart=get_plot1(x,y, x1,y1,xc, layer1, layer2)
    elif k==3:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i] )
        chart=get_plot2(x,y, x1,y1,x2,y2,xc, layer1, layer2, layer3)
    elif k==4:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i]+x3[i] )
        chart=get_plot3(x,y, x1,y1,x2,y2,x3,y3,xc,layer1, layer2, layer3, layer4)
    return chart,xc, y

def draw_compositeIPR_Standing(standingmodels = StandingsModel()):
    x=[] 
    y=[]
    x1=[] 
    y1=[]
    x2=[] 
    y2=[]
    x3=[] 
    y3=[]
    xc=[]
    maxResPres =0.0
    k=len(standingmodels)               
    for standingmodel in standingmodels :
        if standingmodel.future_Reservoir_Pressure > maxResPres:
            maxResPres = standingmodel.future_Reservoir_Pressure  
    j=0      
    for standingmodel in standingmodels:            
       # delp = maxResPres/100
        pvt = BlackoilPVT.objects.filter(wellName =standingmodel.pvt_Well, subLayer =standingmodel.layer_Name).last()
        oilgravity = pvt.oilAPIgravity
        Pb = get_Pb( pvt)
        Bo =get_Bo(pvt)
        viscosity = get_Viscosity(pvt)
        respres = standingmodel.current_Reservoir_Pressure
        futurerespres = standingmodel.future_Reservoir_Pressure
        Ql = standingmodel.current_Test_Rate
        pwf =standingmodel.current_Test_Pressure           
        crelperm =standingmodel.current_Relative_Permeability
        frelperm =standingmodel.future_Relative_Permeability
        Qmax = Ql/((1 - (pwf / respres)) * float(1.0+0.8*(pwf / respres)))
        zerodrawdownPI = 1.8 * Qmax /respres
        pressureFunctionCurrent = crelperm/(float(Bo) * float(viscosity))
        pvt.reservoirPressure = float(standingmodel.future_Reservoir_Pressure)
        Bof =get_Bo(pvt)
        viscosityf = get_Viscosity(pvt)
        pressureFunctionFuture = frelperm/float(Bof * viscosityf)            
        futurePI = zerodrawdownPI * pressureFunctionFuture/pressureFunctionCurrent
        delp = maxResPres/100
        for i in range(101):
            pres = i*delp
            rate = (futurePI * futurerespres /1.8) * (1 - 0.2 * (pres / futurerespres) - 0.8 * math.pow(pres / futurerespres, 2))
            
            if k==0:
                x.append(0)
                y.append(0)
                chart=get_plot(x,y, "No Data")                
            elif k ==1:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= 'Composite IPR - ' + str(standingmodel.layer_Name)                                          
            elif k==2:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= standingmodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres)
                    layer2= standingmodel.layer_Name
                    print(pres, rate)
            elif k==3:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= standingmodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= standingmodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= standingmodel.layer_Name
            elif k==4:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= standingmodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= standingmodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= standingmodel.layer_Name
                elif j==3:
                    x3.append(rate)
                    y3.append(pres)
                    layer4= standingmodel.layer_Name
        j=j+1  
    if k==1:
        chart=get_plot(x,y,layer1)
    elif k==2:
        for i in range(101):
            xc.append(x[i] + x1[i])
        chart=get_plot1(x,y, x1,y1,xc, layer1, layer2)
    elif k==3:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i] )
        chart=get_plot2(x,y, x1,y1,x2,y2,xc, layer1, layer2, layer3)
    elif k==4:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i]+x3[i] )
        chart=get_plot3(x,y, x1,y1,x2,y2,x3,y3,xc,layer1, layer2, layer3, layer4) 
    return chart, xc, y

def draw_compositeIPR_Wiggins(wigginmodels= WigginsModel()):
    x=[] 
    y=[]
    x1=[] 
    y1=[]
    x2=[] 
    y2=[]
    x3=[] 
    y3=[]
    xc=[]
    maxResPres =0.0
    k=len(wigginmodels)  
               
    for wigginmodel in wigginmodels :
        if wigginmodel.current_Reservoir_Pressure> maxResPres:
            maxResPres = wigginmodel.current_Reservoir_Pressure  
    j=0         
    for wigginmodel in wigginmodels: 
        pvt = BlackoilPVT.objects.filter(wellName =wigginmodel.pvt_Well, subLayer =wigginmodel.layer_Name).last()
        oilgravity = pvt.oilAPIgravity           
        respres = wigginmodel.current_Reservoir_Pressure
        futurerespres = wigginmodel.future_Reservoir_Pressure
        Ql = wigginmodel.wiggins_Test_Rate
        pwf =wigginmodel.wiggins_Test_Pressure           
        wc =wigginmodel.water_Cut  
        OilRate = Ql * (1.0 - wc / 100);
        WaterRate = Ql * (wc / 100);
        QmaxOil = OilRate / (1 - 0.52 * (pwf / respres) - 0.48 * math.pow(pwf / respres, 2))
        QmaxWater = WaterRate / (1 - 0.72 * (pwf / respres) - 0.28 * math.pow(pwf / respres, 2))
        delp = maxResPres/100
        for i in range(101):
            pres = i*delp
            oilRate1 = QmaxOil * (1 - 0.52 * (pres / respres) - 0.48 * math.pow(pres / respres, 2));
            waterRate1 = QmaxWater * (1 - 0.72 * (pres / respres) - 0.28 * math.pow(pres / respres, 2));
            rate = oilRate1 +waterRate1
            if k==0:
                x.append(0)
                y.append(0)
                chart=get_plot(x,y, "No Data")
            elif k ==1:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= 'Composite IPR - ' + str(wigginmodel.layer_Name)                                         
            elif k==2:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= wigginmodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres)
                    layer2= wigginmodel.layer_Name
                   
            elif k==3:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= wigginmodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= wigginmodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= wigginmodel.layer_Name
            elif k==4:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= wigginmodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= wigginmodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= wigginmodel.layer_Name
                elif j==3:
                    x3.append(rate)
                    y3.append(pres)
                    layer4= wigginmodel.layer_Name
        j=j+1
    if k==1:
        chart=get_plot(x,y,layer1)
    elif k==2:
        for i in range(101):
            xc.append(x[i] + x1[i])
        chart=get_plot1(x,y, x1,y1,xc, layer1, layer2)
    elif k==3:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i] )
        chart=get_plot2(x,y, x1,y1,x2,y2,xc, layer1, layer2, layer3)
    elif k==4:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i]+x3[i] )
        chart=get_plot3(x,y, x1,y1,x2,y2,x3,y3,xc,layer1, layer2, layer3, layer4)
    return chart, xc, y

def draw_CompositeIPR_Multirate(multiratemodels= MultirateModel()):
    x=[] 
    y=[]
    x1=[] 
    y1=[]
    x2=[] 
    y2=[]
    x3=[] 
    y3=[]
    xc=[]
    logx=[]
    logy=[]
    maxResPres =0.0
    k=len(multiratemodels)               
    for multiratemodel in multiratemodels :
        if multiratemodel.current_Reservoir_Pressure> maxResPres:
            maxResPres = multiratemodel.current_Reservoir_Pressure  
    j=0         
    for multiratemodel in multiratemodels: 
        resPres = multiratemodel.current_Reservoir_Pressure
        pwf1 = (math.pow(resPres, 2) - math.pow(multiratemodel.test_Pressure1, 2))
        pwf2 = (math.pow(resPres, 2) - math.pow(multiratemodel.test_Pressure2, 2))
        pwf3 = (math.pow(resPres, 2) - math.pow(multiratemodel.test_Pressure3, 2))
        logx.append( multiratemodel.test_Rate1)
        logx.append( multiratemodel.test_Rate2)
        logx.append( multiratemodel.test_Rate3)
        logy.append(pwf1)
        logy.append(pwf2)
        logy.append(pwf3)           
        slope = get_MultirateSlope(logx,logy)       
        n = (math.log(multiratemodel.test_Rate3) - math.log(multiratemodel.test_Rate1)) / (math.log(pwf3) - math.log(pwf1));
        c1 = multiratemodel.test_Rate1 / math.pow(pwf1, slope)
        c2 = multiratemodel.test_Rate2 / math.pow(pwf2, slope)
        c3 = multiratemodel.test_Rate3 / math.pow(pwf3, slope)
        averageC = (c1 + c2 + c3 ) / 3
        delp = maxResPres/100
        
        for i in range(101):
            pres = i*delp
            rate = c3 * math.pow((math.pow(resPres, 2) - math.pow(pres, 2)), slope)                
            if k ==1:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= 'Composite IPR - ' + str(multiratemodel.layer_Name)                                       
            elif k==2:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= multiratemodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres)
                    layer2= multiratemodel.layer_Name
                    
            elif k==3:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= multiratemodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= multiratemodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= multiratemodel.layer_Name
            elif k==4:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= multiratemodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= multiratemodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= multiratemodel.layer_Name
                elif j==3:
                    x3.append(rate)
                    y3.append(pres)
                    layer4= multiratemodel.layer_Name
        j=j+1
    if k==0:
        x.append(0)
        y.append(0)
        chart=get_plot(x,y, "No Data")
    if k==1:
        chart=get_plot(x,y,layer1)
    elif k==2:
        for i in range(101):
            xc.append(x[i] + x1[i])
        chart=get_plot1(x,y, x1,y1,xc, layer1, layer2)
    elif k==3:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i] )
        chart=get_plot2(x,y, x1,y1,x2,y2,xc, layer1, layer2, layer3)
    elif k==4:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i]+x3[i] )
        chart=get_plot3(x,y, x1,y1,x2,y2,x3,y3,xc,layer1, layer2, layer3, layer4)    
    return chart, xc, y

def draw_CompositeIPR_Darcy(darcymodels = DarcyModel()):
    x=[] 
    y=[]
    x1=[] 
    y1=[]
    x2=[] 
    y2=[]
    x3=[] 
    y3=[]
    xc=[]
    maxResPres =0.0
    k=len(darcymodels)
    for darcymodel in darcymodels :
        if darcymodel.current_Reservoir_Pressure> maxResPres:
            maxResPres = darcymodel.current_Reservoir_Pressure  
    j=0         
    for darcymodel in darcymodels: 
        pvt = BlackoilPVT.objects.filter(wellName =darcymodel.pvt_Well, subLayer =darcymodel.layer_Name).last()
        oilgravity = pvt.oilAPIgravity  
        pvt.reservoirPressure = darcymodel.current_Reservoir_Pressure
        Pb = get_Pb(pvt)
        Bo = get_Bo(pvt)  
        viscosity = get_Viscosity(pvt)       
        respres = darcymodel.current_Reservoir_Pressure
        perm = darcymodel.layer_Permeability
        thick = darcymodel.layer_Thickness
        drainage = darcymodel.drainage_Radius
        wellbore = darcymodel.wellbore_Radius
        skin = darcymodel.layer_Skin           
        delp = maxResPres/100
        for i in range(101):
            pres = i*delp
            pi = 0.00708 * perm * thick / (float(viscosity * Bo) * (math.log(drainage /wellbore) - 0.75 + skin))
            if respres > Pb and  pres > Pb:                   
                rate = pi*(respres- pres)
            else:
                rate = pi/(2*float(Pb))*(respres**2 - pres**2)
            if k==0:
                x.append(0)
                y.append(0)
                chart=get_plot(x,y, "No Data")
            elif k ==1:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= 'Composite IPR - ' + str(darcymodel.layer_Name) 
                                        
            elif k==2:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= darcymodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres)
                    layer2= darcymodel.layer_Name
            elif k==3:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= darcymodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= darcymodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= darcymodel.layer_Name
            elif k==4:
                if j==0:
                    x.append(rate)
                    y.append(pres)
                    layer1= darcymodel.layer_Name
                elif j==1:
                    x1.append(rate)
                    y1.append(pres) 
                    layer2= darcymodel.layer_Name                    
                elif j==2:
                    x2.append(rate)
                    y2.append(pres)
                    layer3= darcymodel.layer_Name
                elif j==3:
                    x3.append(rate)
                    y3.append(pres)
                    layer4= darcymodel.layer_Name
        j=j+1
    if k==0:
        x.append(0)
        y.append(0)
        chart=get_plot(x,y,"No Data")
    elif k==1:
        chart=get_plot(x,y,layer1)
    elif k==2:
        for i in range(101):
            xc.append(x[i] + x1[i])
        chart=get_plot1(x,y, x1,y1,xc, layer1, layer2)
    elif k==3:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i] )
        chart=get_plot2(x,y, x1,y1,x2,y2,xc, layer1, layer2, layer3)
    elif k==4:
        for i in range(101):
            xc.append(x[i] + x1[i] + x2[i]+x3[i] )
        chart=get_plot3(x,y, x1,y1,x2,y2,x3,y3,xc,layer1, layer2, layer3, layer4)
    return chart, xc, y

def get_layeripr(x,y,layer1):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4.5,3.5))
    plt.title("Layer IPR")
    if x != NULL:
        plt.plot(x, y, color='green', label= layer1)
    plt.xticks(rotation=45)
    plt.xlabel('Liquid Rate bbls/day')
    plt.ylabel('Pressure (psi)') 
    plt.legend()
    plt.tight_layout()
    plt.xlim(0)
    plt.ylim(0)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def draw_LayerIPR_Darcy(darcymodel = DarcyModel()):
    x=[] 
    y=[]  
    print (darcymodel.pvt_Well)
    pvt = BlackoilPVT.objects.filter(wellName =darcymodel.pvt_Well, subLayer =darcymodel.layer_Name).first()
    oilgravity = pvt.oilAPIgravity  
    pvt.reservoirPressure = darcymodel.current_Reservoir_Pressure
    Pb = get_Pb(pvt)
    Bo = get_Bo(pvt)  
    viscosity = get_Viscosity(pvt)       
    respres = darcymodel.current_Reservoir_Pressure
    perm = darcymodel.layer_Permeability
    thick = darcymodel.layer_Thickness
    drainage = darcymodel.drainage_Radius
    wellbore = darcymodel.wellbore_Radius
    skin = darcymodel.layer_Skin 
    layer =darcymodel.layer_Name          
    delp = respres/100
    for i in range(101):
        pres = i*delp
        pi = 0.00708 * perm * thick / (float(viscosity * Bo) * (math.log(drainage /wellbore) - 0.75 + skin))
        if respres >=Pb and  pres >= Pb:                   
            rate = pi*(respres- pres)
            x.append(rate)
            y.append(pres)
        else:
            rate = pi/(2*float(Pb))*(respres**2 - pres**2)
            x.append(rate)
            y.append(pres)        
    chart=get_layeripr(x,y,layer)
    return chart

def draw_LayerIPR_Multirate(multiratemodel = MultirateModel()):
    x=[] 
    y=[]
    logx=[]
    logy=[]
    resPres = multiratemodel.current_Reservoir_Pressure
    pwf1 = (math.pow(resPres, 2) - math.pow(multiratemodel.test_Pressure1, 2))
    pwf2 = (math.pow(resPres, 2) - math.pow(multiratemodel.test_Pressure2, 2))
    pwf3 = (math.pow(resPres, 2) - math.pow(multiratemodel.test_Pressure3, 2))
    logx.append( multiratemodel.test_Rate1)
    logx.append( multiratemodel.test_Rate2)
    logx.append( multiratemodel.test_Rate3)
    layer = multiratemodel.layer_Name
    logy.append(pwf1)
    logy.append(pwf2)
    logy.append(pwf3)           
    slope = get_MultirateSlope(logx,logy)              
    n = (math.log(multiratemodel.test_Rate3) - math.log(multiratemodel.test_Rate1)) / (math.log(pwf3) - math.log(pwf1));
    c1 = multiratemodel.test_Rate1 / math.pow(pwf1, slope)
    c2 = multiratemodel.test_Rate2 / math.pow(pwf2, slope)
    c3 = multiratemodel.test_Rate3 / math.pow(pwf3, slope)
    averageC = (c1 + c2 + c3 ) / 3
    delp = resPres/100
   
    for i in range(101):
        pres = i*delp
        rate = c1 * math.pow((math.pow(resPres, 2) - math.pow(pres, 2)), slope) 
        x.append(rate)
        y.append(pres)        
    chart=get_layeripr(x,y,layer)    
    return chart

def draw_LayerIPR_Wiggin(wigginmodel = WigginsModel()):
    x=[] 
    y=[]
    pvt = BlackoilPVT.objects.filter(wellName =wigginmodel.pvt_Well, subLayer =wigginmodel.layer_Name).last()
    oilgravity = pvt.oilAPIgravity           
    respres = wigginmodel.current_Reservoir_Pressure
    futurerespres = wigginmodel.future_Reservoir_Pressure
    Ql = wigginmodel.wiggins_Test_Rate
    pwf =wigginmodel.wiggins_Test_Pressure           
    wc =wigginmodel.water_Cut  
    OilRate = Ql * (1.0 - wc / 100);
    WaterRate = Ql * (wc / 100);
    QmaxOil = OilRate / (1 - 0.52 * (pwf / respres) - 0.48 * math.pow(pwf / respres, 2))
    QmaxWater = WaterRate / (1 - 0.72 * (pwf / respres) - 0.28 * math.pow(pwf / respres, 2))
    delp = respres/100
    layer = wigginmodel.layer_Name
    for i in range(101):
        pres = i*delp
        oilRate1 = QmaxOil * (1 - 0.52 * (pres / respres) - 0.48 * math.pow(pres / respres, 2));
        waterRate1 = QmaxWater * (1 - 0.72 * (pres / respres) - 0.28 * math.pow(pres / respres, 2));
        rate = oilRate1 +waterRate1
        x.append(rate)
        y.append(pres)        
    chart=get_layeripr(x,y,layer)
    return chart

def draw_LayerIPR_Standing(standingmodel=StandingsModel()):
    x=[] 
    y=[]
    x1=[] 
    y1=[]
    x2=[] 
    y2=[]
    pvt = BlackoilPVT.objects.filter(wellName =standingmodel.pvt_Well, subLayer =standingmodel.layer_Name).last()
    oilgravity = pvt.oilAPIgravity
    Pb = get_Pb( pvt)
    Bo =get_Bo(pvt)
    viscosity = get_Viscosity(pvt)
    respres = standingmodel.current_Reservoir_Pressure
    futurerespres = standingmodel.future_Reservoir_Pressure
    Ql = standingmodel.current_Test_Rate
    pwf =standingmodel.current_Test_Pressure           
    crelperm =standingmodel.current_Relative_Permeability
    frelperm =standingmodel.future_Relative_Permeability
    Qmax = Ql/((1 - (pwf / respres)) * float(1.0+0.8*(pwf / respres)))
    zerodrawdownPI = 1.8 * Qmax /respres
    pressureFunctionCurrent = crelperm/(float(Bo) * float(viscosity))
    pvt.reservoirPressure = float(standingmodel.future_Reservoir_Pressure)
    Bof =get_Bo(pvt)
    viscosityf = get_Viscosity(pvt)
    pressureFunctionFuture = frelperm/float(Bof * viscosityf)            
    futurePI = zerodrawdownPI * pressureFunctionFuture/pressureFunctionCurrent
    futurePI1 = zerodrawdownPI * futurerespres/respres
    delp = respres/100
    for i in range(101):
        pres = i*delp
        rate = (zerodrawdownPI * respres /1.8) * (1 - 0.2 * (pres / respres) - 0.8 * math.pow(pres / respres, 2))
        rate1 =(futurePI * futurerespres /1.8) * (1 - 0.2 * (pres / futurerespres) - 0.8 * math.pow(pres / futurerespres, 2))
        rate2 =(futurePI1 * futurerespres /1.8) * (1 - 0.2 * (pres / futurerespres) - 0.8 * math.pow(pres / futurerespres, 2))
        x.append(rate)
        y.append(pres)
        x1.append(rate1)
        y1.append(pres)
        x2.append(rate2)
        y2.append(pres)
    layer =standingmodel.layer_Name
    chart=get_plot4(x,y,x1,y1,x2,y2,layer)
    return chart

def draw_LayerIPR_Vogel(vogelmodel=VogelModel()):
    x=[] 
    y=[]
    pvt = BlackoilPVT.objects.filter(wellName =vogelmodel.pvt_Well, subLayer =vogelmodel.layer_Name).last()
    temperature = pvt.reservoirTemperature
    oilgravity = pvt.oilAPIgravity
    solutiongas = pvt.solutionGOR
    gasgravity = pvt.gasGravity
    oilg = Decimal('141.5')/(oilgravity+ Decimal('131.5')) 
    Pb = get_Pb( pvt)   
    respres = vogelmodel.reservoir_Pressure
    Qbp = vogelmodel.vogel_Test_Rate
    pwf =vogelmodel.vogel_Test_Pressure
    Qmax = Qbp/(1 - 0.2 * (float(pwf) / respres) - 0.8 * math.pow(float(pwf) / respres, 2));
    delp = respres/100
    for i in range(101):
        pres = i*delp
        rate = Decimal(Qmax * (1 - 0.2 * (pres / respres) - 0.8 * math.pow(pres / respres, 2)))           
        x.append(rate)
        y.append(pres)
        
    layer =vogelmodel.layer_Name
    chart=get_layeripr(x,y,layer)
    return chart

def draw_LayerIPR_PI(pimodel=ProductivityIndexModel()):
    x=[] 
    y=[] 
     
    pvt = BlackoilPVT.objects.filter(wellName =pimodel.pvt_Well).first()
    Pb = get_Pb( pvt)
    respres = pimodel.reservoir_Pressure
    Qbp = pimodel.productivity_index * (pimodel.reservoir_Pressure - float(Pb))
    Qmax = Qbp/(1 - 0.2 * (float(Pb) / respres) - 0.8 * math.pow(float(Pb) / respres, 2));
    delp = respres/100
    for i in range(101):
        pres = i*delp
        rate = Decimal(Qmax * (1 - 0.2 * (pres / respres) - 0.8 * math.pow(pres / respres, 2)))
        x.append(rate)
        y.append(pres)
       
    layer =pimodel.layer_Name
    chart=get_layeripr(x,y,layer)
    return chart

def get_MultirateSlope(logx,logy):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.suptitle("Composite IPR")
    if logx != NULL:
        # slope, intercept = np.polyfit(np.log(logx), np.log(logy), 1)
        slope, intercept = linear_regression(np.log(logx), np.log(logy))       
        plt.scatter(logx, logy, color='green')
        slope = 1/slope
        slope = math.trunc(slope *1000000)/1000000        
        plt.loglog(logx, logy, color='red', label='slope =' + str(slope))
        z = np.polyfit(logx, logy, 1)
        p = np.poly1d(z)
    plt.xticks(rotation=45)
    plt.xlabel('Liquid Rate bbls/day')    
    plt.ylabel('Pr^2 - Pwf^2') 
    plt.legend()
    plt.tight_layout()   
    # plt.title("y=%.6fx+%.6f"%(z[0],z[1]))
   
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return slope

def draw_Multirateloglogplot(multiratemodel=MultirateModel()):
    logx=[]
    logy=[]
    resPres = multiratemodel.current_Reservoir_Pressure
    pwf1 = (math.pow(resPres, 2) - math.pow(multiratemodel.test_Pressure1, 2))
    pwf2 = (math.pow(resPres, 2) - math.pow(multiratemodel.test_Pressure2, 2))
    pwf3 = (math.pow(resPres, 2) - math.pow(multiratemodel.test_Pressure3, 2))
    logx.append( multiratemodel.test_Rate1)
    logx.append( multiratemodel.test_Rate2)
    logx.append( multiratemodel.test_Rate3)
    layer = multiratemodel.layer_Name
    logy.append(pwf1)
    logy.append(pwf2)
    logy.append(pwf3)           
    loglogchart = get_loglogplot(logx,logy) 
    return loglogchart 