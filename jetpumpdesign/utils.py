from turtle import color
import matplotlib.pyplot  as plt
import matplotlib  as mpl
import base64
from io import BytesIO
import numpy as np
import math
import datetime
from scipy.optimize import curve_fit
import pandas as pd
from blackoilpvt.models import BlackoilPVT
from selectedOilProducer.models import SelectedOilProducer
from opinflow.utility import draw_CompositePR_PI, draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins
from opinflow.models import ProductivityIndexModel, DarcyModel, WigginsModel, VogelModel, StandingsModel, MultirateModel
import psapy

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_viscosity_plot(api, viscosity, dead_viscosity, viscosity1,dead_viscosity1):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(8,6))    
    plt.subplot(1,1,1)
    plt.subplot(1,1,1)
    plt.plot(api, viscosity, label="live viscosity") 
    plt.plot(api, dead_viscosity, label="dead viscosity")   

    plt.plot(api, viscosity1, label=" Beggs live viscosity") 
    plt.plot(api, dead_viscosity1, label="Beggs dead viscosity")     
    plt.xlabel('API')
    plt.ylabel('Viscosity')
    plt.yscale('log')
    plt.legend(loc="upper right")    
    plt.title("API Vs Viscosity")      
    plt.tight_layout()
    graph = get_graph()
    return graph

    graph = get_graph()
    return graph


def get_ipr_plot(df, jetdata, x1, y1):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(8,6))    
    plt.subplot(1,1,1)
    plt.subplot(1,1,1)
    plt.plot(x1, y1,  label=f'Operating Point {x1[1], y1[1]}', color = "r", linestyle="dotted")
    plt.plot(df["x2"], df['y2'],  label='Inflow', color = "g")    
    plt.xlabel('Liquid Rate BOPD')
    plt.ylabel('Pressure in psi')
    plt.legend(loc="upper right")    
    plt.title("Inflow ")
    plt.ylim(0, max(df['y2'])+250)
    plt.xlim(0, max(df["x2"]) + 250)    
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_pressure_depth_plot(pressures, depths, pressures1, depths1, pressures2, depths2, pressures3, depths3, pressures4, depths4):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(8,6))    
    plt.subplot(1,1,1)
    plt.subplot(1,1,1)
    plt.plot(pressures, depths,color="g", label="Hagedorn")   
    plt.plot(pressures1, depths1,color="b",label="Orkiszewski") 
    plt.plot(pressures2, depths2,color="r", label="Beggs")  
    plt.plot(pressures3, depths3,color="violet", label="Fancher_Brown")
    plt.plot(pressures4, depths4,color="pink", label="Duns_Ros")   
    plt.xlabel('Pressure (psi)')
    plt.ylabel('Depth inft')
    plt.legend(loc="upper right")    
    plt.title("Depth Vs Pressure ")
    plt.ylim(max(depths)+250,0)
    plt.xlim(0,max(pressures4) + 250)    
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_jet_plot(CM,CH,CEff, pump, maxeff, M):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8)) 
    fig, ax1 = plt.subplots()
    fig.subplots_adjust(right=0.7) 
    ax1.set_xlabel('M Ratio (q3/q1)') 
    ax1.set_ylabel('Head (ft)', color = 'blue') 
    ax1.plot(CM, CH, color="black")   
    ax1.tick_params(axis ='y', labelcolor = 'blue')    
    ax1.set_ylim(0,0.8)
    ax1.set_xlim(0,3)
    ax2 = ax1.twinx()   
    ax2.set_ylabel('Efficiency (%)', color = 'green') 
    ax2.plot(CM, CEff, color = 'green')   
    ax2.scatter(M, maxeff, color = 'red', s=15, label="Operating Point")    
    ax2.tick_params(axis ='y', labelcolor = 'green')      
    plt.title(f"Pump Performance Curve for {pump}  Pump")
    ax2.set_ylim(0,40)
    plt.tight_layout()
    plt.legend()
    graph = get_graph()
    return graph

def calculate_jetpump(jetdata):
    # assume M=0.5 = liquid Ratio q3/q1
    M=0.5
    inj_Press=4000
    friction_grad = 7.8
    powerfluid_spgr =0.82
    p2 = 2740
    q3 = jetdata.design_Liquid
    fw =jetdata.water_Cut/100
    pr=jetdata.curr_Res_Pres
    pi = 4    
    pvt = BlackoilPVT.objects.filter(wellName =jetdata.pvt_Well).last()
    oil_spgr = 131.5/(131.5+pvt.oilAPIgravity)
    combinedGLR = M*(jetdata.gas_Oil_Ratio * (1-fw))/(1+M)
    q1 = q3/M
    powerfluid_grad = 0.433*powerfluid_spgr
    p1= jetdata.pump_depth * powerfluid_grad - friction_grad*jetdata.pump_depth/1000 + inj_Press
    q2 = q1+q3
    fw2 = fw*q3/(q1+q3)
    p3 = pr-q3/pi
    H = (p2-p3)/(p1-p2)
    H=round(H,3)
    AM =[0,	0.2,0.4,0.6,0.8,1]
    AH=	[1.045,	0.763,	0.547,	0.359,	0.174,	-0.029]
    aEff=[0,0.153,	0.219,	0.215,	0.139,	-0.29]
    AT=	[0,	0.304,	0.673,	1.167,	2.078]	

    BM=	[0,	0.2,	0.4,	0.6,	0.8,	1.0,	1.2,	1.4	]						
    BH=	[0.789,	0.64,	0.515,	0.403,	0.296,	0.188,	0.075,	-0.052]							
    bEff=[0,	0.128,	0.206,	0.242,	0.236,	0.188,	0.09,	-0.073]	
    BT=	[0,	0.32,	0.686,	1.12,	1.674,	2.514,	4.543]							
															
    CM=	[0,	0.2,	0.4,	0.6,	0.8,	1.0,	1.2,	1.4,	1.6,	1.8	]				
    CH=	[0.596,	0.517,	0.445,	0.378,	0.314,	0.25,	0.186,	0.119,	0.047,	-0.032	]				
    cEff=[0,	0.103,	0.178,	0.227,	0.251,	0.25,	0.223,	0.166,	0.075,	-0.058	]
    CT=	[0,	0.342,	0.721,	1.146,	1.637,	2.236,	3.03,	4.293,	7.552]					
															
    DM=	[0,	0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2	]
    DH= [0.453,	0.41,0.369,	0.33,0.291,	0.252,0.214,0.174,0.133,0.09,0.044,-0.005]
    dEff=[0,0.082,	0.148,	0.198,	0.233,	0.252,	0.256,	0.244,	0.213,	0.162,	0.088,	-0.011]
    DT=	[0,	0.371,	0.77,	1.205,	1.685,	2.229,	2.858,	3.637,	4.67,	6.264,	9.742]	

    EM=	[0,	0.2	,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8]
    EH= [0.348,	0.323,	0.3,	0.276,	0.253,	0.23,	0.206,	0.182,	0.157,	0.132,	0.105,	0.077,	0.048,	0.017,	-0.016]
    eEff=[0,	0.065,	0.12,	0.166,	0.202,	0.23,	0.247,	0.255,	0.252,	0.237,	0.21,	0.17,	0.116,	0.044,	-0.045]     	
    ET=	[0,	0.405,	0.833,	1.29,	1.78,	2.313,	2.903,	3.568,	4.343,	5.271,	6.488,	8.228,	11.214]

    AEff = []
    for eff in aEff :
        AEff.append(eff*100)
    BEff = []
    for eff in bEff :
        BEff.append(eff*100)    
    CEff = []
    for eff in cEff :
        CEff.append(eff*100)
    DEff = []
    for eff in dEff :
        DEff.append(eff*100)
    EEff = []
    for eff in eEff :
        EEff.append(eff*100)

    AM.pop()
    AH.pop()
    AEff.pop()
 
    #chart1 = get_jet_plot(CM,CH,CEff,DM,DH,DEff,EM,EH,EEff)
    am, ae=find_M_when_H_is_given (AH, AM,AEff, H)
    bm, be=find_M_when_H_is_given (BH, BM,BEff, H)
    cm, ce=find_M_when_H_is_given (CH, CM,CEff, H)
    dm, de=find_M_when_H_is_given (DH, DM,DEff, H)
    em, ee=find_M_when_H_is_given (EH, EM,EEff, H)
           
    #print(H, am, bm,cm,dm,em, ae,be,ce,de,ee)
    eff=[ae,be,ce,de,ee]
    maxeff= (max(eff))
    if maxeff == ae:
        M=round(am,5)
        R = 0.410
        pump='A'
        chart1 = get_jet_plot(AM,AH,AEff,pump, maxeff, M)
       
    elif maxeff == be:
        M=round(bm,5)
        R = 0.328
        pump='B'
        chart1 = get_jet_plot(BM,BH,BEff,pump,maxeff, M)        
    elif maxeff == ce:
        M=round(cm,5)
        R = 0.262
        pump='C'
        chart1 = get_jet_plot(CM,CH,CEff,pump,maxeff, M)       
    elif maxeff == de:
        M=round(dm,5)
        R = 0.210
        pump='D'
        chart1 = get_jet_plot(DM,DH,DEff,pump,maxeff, M)       
    elif maxeff == ee:
        M=round(em,5)
        R = 0.168
        pump='E'
        chart1 = get_jet_plot(EM,EH,EEff, pump,maxeff, M)
    
    maxeff = round(maxeff,2)

    
    #M=rounddm
    friction_grad=2.22
    p2=2669
    combinedGLR = M*(jetdata.gas_Oil_Ratio * (1-fw))/(1+M)
    q1 = q3/M
    powerfluid_grad = 0.433*powerfluid_spgr
    p1= jetdata.pump_depth * powerfluid_grad - friction_grad*jetdata.pump_depth/1000 + inj_Press
    q2 = q1+q3
    fw2 = fw*q3/(q1+q3)
    p3 = pr-q3/pi
    H = (p2-p3)/(p1-p2)
    H=round(H,3)  
    p1=round(p1) 
    dm, de=find_M_when_H_is_given (DH, DM,DEff, H)
    q1 =q3/dm
    aj = q1/(1214.5* math.sqrt(p1-p3)/powerfluid_spgr)  
    NozzleArea=[]
    NozzleNo=[]
    NozzleDia=[]
    NozzleArea.append(0)
    NozzleNo.append(0)
    NozzleDia.append(0)
    NozzleArea.append(0.00371)
    NozzleDia.append(round(math.sqrt(0.00371*4/math.pi),5))
    NozzleNo.append(1)  
    NozzleA =0.00371
    for i in range(2,21):
        NozzleNo.append(i)          
        NozzleA=1.25*NozzleA
        NozzleD = math.sqrt(NozzleA*4/math.pi)
        NozzleDia.append(round(NozzleD,5))
        NozzleArea.append(round(NozzleA,5))
    
    for i in range(len(NozzleNo)):
        if  NozzleArea[i] >aj:
            NozzleNumber= NozzleNo[i]
            NozArea = NozzleArea[i]            
            break
    
    q1 = 1214.5*NozzleArea[NozzleNumber+1]*math.sqrt((p1-p3)/powerfluid_spgr)
    horsepower = 1.7*math.pow(10,-5)*q1*inj_Press
    horsepower = round(horsepower)
    q1 = round(q1)
    Kj=0.15
    Ic = 1.35
    mc = ((1-R)/R)*math.sqrt(1+Kj) * math.sqrt(p3/(Ic*(p1-p3)+p3))
    
    
    ThroatArea=[]
    ThroatNo=[]
    ThroatDia=[]
    ThroatArea.append(0)
    ThroatNo.append(0)
    ThroatDia.append(0)
    ThroatArea.append(0.00905)
    ThroatDia.append(round(math.sqrt(0.00905*4/math.pi),5))
    ThroatNo.append(1)  
    ThroatA =0.00905
    for i in range(2,25):
        ThroatNo.append(i)          
        ThroatA=1.25*ThroatA
        ThroatD = math.sqrt(ThroatA*4/math.pi)
        ThroatDia.append(round(ThroatD,5))
        ThroatArea.append(round(ThroatA,5))
   
    pump = str(NozzleNumber) + pump

 
    return chart1, p1,p2, p3,q1, pump, horsepower, maxeff,M

def find_M_when_H_is_given (AH, AM,AEff, H):
    i=0
    prevh=0
    prevm=0
    preveff =0
    for h in AH:       
        if h <=  H:
            calcM = AM[i] -((AM[i]-prevm) * (H-h))/(prevh-h)  
            calcEff = AEff[i] -((AEff[i]-preveff) * (H-h))/(prevh-h)           
            break
        else:
            prevh=h 
            prevm=AM[i]
            preveff=AEff[i]           
            i=i+1            
    return calcM, calcEff

def calculate_inflow(jetdata):
    selectedwell = SelectedOilProducer.objects.first()   
    inflowdf = pd.DataFrame()  
    if selectedwell.inflow =='PI':        
        pimodels = ProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        chart,xc,y, pis = draw_CompositePR_PI(pimodels) 
    elif selectedwell.inflow =='Vogel':
        vogelmodels = VogelModel.objects.filter(wellid=selectedwell.wellid).all()        
        chart,xc,y= draw_compositeIPR_Vogel(vogelmodels)  
    elif selectedwell.inflow =='Standing':
        standingmodels = StandingsModel.objects.filter(wellid=selectedwell.wellid).all()        
        chart,xc,y = draw_compositeIPR_Standing(standingmodels) 
    elif selectedwell.inflow =='Wiggins':
        wigginmodels = WigginsModel.objects.filter(wellid=selectedwell.wellid).all()        
        chart,xc,y = draw_compositeIPR_Wiggins(wigginmodels) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodels = MultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        chart,xc,y =draw_CompositeIPR_Multirate(multiratemodels)  
    elif selectedwell.inflow =='Darcy':        
        darcymodels = DarcyModel.objects.filter(wellid=selectedwell.wellid).all()  
        chart,xc,y = draw_CompositeIPR_Darcy(darcymodels) 
    inflowdf['x2']= xc
    inflowdf['y2']= y
    x1=[]
    y1=[]
    pwf_inflow=0
    for index, row in inflowdf.iterrows(): 
        if jetdata.design_Liquid > row['x2'] :      
           x1 = [jetdata.design_Liquid,jetdata.design_Liquid,0 ]
           y1 = [0,row['y2'],row['y2'] ] 
           pwf_inflow=row['y2']     
           break
    #chart = get_ipr_plot(inflowdf, espdata, x1, y1)
    pip = pwf_inflow
    return inflowdf, x1, y1, pip

def calculate_Rs_Standing( temperature_in_R,pressure_psi, oil_API_gravity, gas_sp_gravity):   
    intx = 0.0125  * oil_API_gravity - ( 0.00091  * temperature_in_R)
    Rs = gas_sp_gravity * ((pressure_psi /18.2 + 1.4) * 10** intx)** 1.2048
    return Rs

def calculate_Bo_Standing( temperature_in_R,pressure_psi, oil_API_gravity, gas_sp_gravity, spgr_oil):   
    intx = 0.0125  * oil_API_gravity - ( 0.00091  * temperature_in_R)
    Rs = gas_sp_gravity * ((pressure_psi /18.2 + 1.4) * 10** intx)** 1.2048
    bo = 0.9759+0.00012*math.pow(Rs*math.pow(gas_sp_gravity/spgr_oil,0.5) + 1.25 *(temperature_in_R-460),1.2)
    return bo

def calculate_Pb_Standing( temperature_in_R,solutiongas, oil_API_gravity, gas_sp_gravity):
    Pas = (0.00091 * temperature_in_R) - (0.0125* oil_API_gravity)
    Pb = 18.2 * ((((solutiongas / gas_sp_gravity) **0.83) * 10** Pas) -1.4 ) 
    return Pb

def calculate_z_Hall_Yarborough (avg_pres, avg_temp, spgr_gas):
    ppr = 168 +(325*spgr_gas) - (12.5 * math.pow(spgr_gas,2)) # pseudo-redused Pressure
    tpc= 677+(15*spgr_gas) - (37.5 * math.pow(spgr_gas,2)) # pseudo-redused temperature
    t = tpc/avg_temp 
    y= 0.0125*ppr*t*math.exp(-1.2*math.pow((1-t),2))
    x1=-0.06125*ppr*t*math.exp(-1.2*math.pow((1-t),2))
    x2 = (14.76*t) - (9.76*math.pow(t,2)) + (4.58*math.pow(t,3))
    x3 = (90.7*t) - (242.2*math.pow(t,2)) + (442.4*math.pow(t,3))
    x4 = 2.18+2.82*t
    for i in range (100):
        fy = x1+((math.pow(y,2))+(math.pow(y,3))+(math.pow(y,4)))/math.pow((1-y),3) - (x2*math.pow(y,2)) + x3*(math.pow(y,x4))
        fy_der = (1+4*y+4*math.pow(y,2) - 4* math.pow(y,3)+math.pow(y,4))/(math.pow(1-y,4)) - (2*x2*y) +(x3*x4*math.pow(y,x4-1))
        y1 = y - fy/fy_der 
        if y-y1==0.0000000000001:
            z= 0.06125*ppr*t*math.exp(-1.2*math.pow((1-t),2))
            break
        else:
            y=y1
            z=1

    return z

def calculate_oil_viscosity_Beal(oil_API, avg_temp, rs):
    CorA = math.pow(10, (0.43 + (8.33 / oil_API))) 
    dead_viscosity = (0.32 + (1.8 * math.pow(10, 7)) / math.pow(oil_API, 4.53)) * math.pow((360 / (avg_temp+460-260)), CorA) 
    A= 10.715 *math.pow((rs +100), -0.515)
    B= 5.44 *math.pow((rs +150), -0.338)
    live_oil_viscosity = A*math.pow(dead_viscosity, B)  
    return live_oil_viscosity,dead_viscosity

def calculate_oil_viscosity_Beggs(oil_API, avg_temp, rs):
    z= 3.0324-0.02023 * oil_API
    y= math.pow(10,z)
    x= y*math.pow(avg_temp, -1.163)
    dead_viscosity = math.pow(10,x) -1.00
    A= 10.715 *math.pow((rs +100), -0.515)
    B= 5.44 *math.pow((rs +150), -0.338)
    live_oil_viscosity = A*math.pow(dead_viscosity, B)  
    return live_oil_viscosity,dead_viscosity

def calculate_water_viscosity(avg_p, avg_temp, wat_salility):
    a= (4.518*math.pow(10,-2))+(9.313*math.pow(10,-7)*wat_salility) - (3.93*math.pow(10,-12)*math.pow(wat_salility,2))
    b=70.634 + (9.576*math.pow(10,-10)*math.pow(wat_salility,2))
    ded_vis = a +b/(avg_temp-460)
    water_viscosity = ded_vis *(1+(3.5*math.pow(10,-2) * math.pow(avg_p,2) * (avg_temp -500)))
    return ded_vis

def calculate_z(spgr_Gas, th_Pres, th_Temp):
    TPC = (169.2 - (349 * spgr_Gas) - 74 * math.pow(spgr_Gas, 2))+460 
    PPC = 756.8 - (131.1 * spgr_Gas) - 3.6 * math.pow(spgr_Gas, 2) 
    PPR = th_Pres / PPC 
    TPR = (th_Temp + 460) / TPC 
    A1 = 0.3265 
    A2 = -1.07 
    A3 = -0.5339 
    A4 = 0.01569 
    A5 = -0.05165 
    A6= 0.5475 
    A7 = -0.7361 
    A8 = 0.1844 
    A9= 0.1056 
    A10 = 0.6134 
    A11 = 0.7210 
    Z1=1
    for i in range(100):
        RhoR = 0.27 * PPR / (Z1 * TPR);
        C1TPR = A1 + (A2 / TPR) + (A3 / math.pow(TPR, 3)) + (A4 / math.pow(TPR, 4)) + (A5 / math.pow(TPR, 5));
        C2TPR =A6+(A7/TPR )+(A8/math.pow (TPR,2 ));
        C3TPR = A9 * ((A7 / TPR) + (A8 / math.pow(TPR, 2)));
        C4TPR = A10 *(1+(A11*math .pow (RhoR ,2)))*(math .pow (RhoR,2 )/(math .pow (TPR,3 )))*math.exp (-A11*(math .pow (RhoR,2 )) );
        FY = Z1 - (1 + (C1TPR  * RhoR ) + (C2TPR * math.pow(RhoR, 2)) - (C3TPR * math.pow(RhoR, 5)) + C4TPR );
        DerFY = 1 + (C1TPR  * (RhoR / Z1)) + (2 * C2TPR  * (math.pow(RhoR, 2) / Z1)) - (5 * (C3TPR * (math.pow(RhoR, 5)) / Z1)) + (2 * (A10  * math.pow(RhoR, 2) * (1 + A11* math.pow(RhoR, 2) - math.pow(A11 * math.pow(RhoR, 2), 2)) * math.exp(-A11 * math.pow(RhoR, 2))) / (math.pow(TPR, 3) * Z1));
        Z = Z1 - (FY / DerFY)
        if abs(Z1-Z) <=0.0000000001:
            z= Z 
        else:
            Z1=Z 
    return z

def Hagedorn_Brown(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2 ):
    TbgRoughness =0.00015
    oil_Rate = liquid_Rate *(1-water_Cut/100)
    water_Rate =liquid_Rate *water_Cut/100
    gas_Rate = oil_Rate * gas_Oil_Ratio
    tpc = 168 + (325 * spgr_Gas - 12.5 * math.pow(spgr_Gas, 2))
    ppc = 677 + (15 * spgr_Gas - 37.5 * math.pow(spgr_Gas, 2))
    A = (moleH2S + moleCO2)
    spgr_Oil = 141.5/(131.5+oil_API)
    epsilon = 120 * (math.pow(A, 0.9) - math.pow(A, 1.6)) + 15 * (math.pow(moleH2S, 0.5) - math.pow(moleH2S, 4))
    area_tubing= math.pi * (math.pow((tbg_Dia / 12), 2)) / 4
    temp_Gradient = (res_Temp - th_Temp) / well_Depth
    average_Temp= (res_Temp + th_Temp)/2
    presssure=[] 
    depth=[]
    AssumeDepth=well_Depth/100
    cumMD = AssumeDepth
    for i in range(100):
        if th_Pres <3977:
            confact =1 - 0.024 * math.pow(th_Pres, 0.45)
        else:
            confact =1.0
        if th_Temp <= 68:
            sigma_Oil = 39 - (0.257 * oil_API * confact) 
        elif th_Temp > 100:
            sigma_Oil =37.5 - 0.257 * oil_API * confact
        else:            
            sigma_Oil = confact * (((39 - 0.257 * oil_API)) + (((37.5 - 0.257 * oil_API)) - ((39 - 0.257 * oil_API))) * (th_Temp - 68) / 32) 

        sigma_Water = (-9 * math.pow(10, -5) * th_Temp + 0.0815) * 1000
        sigma_Liquid = (sigma_Oil * (1-water_Cut/100)) + (sigma_Water * water_Cut/100) 
        deviation_Angle =90
        Xva = 0.0125 * oil_API - 0.00091 * average_Temp
        RsCalc = spgr_Gas * math.pow((((th_Pres / 18.2) + 1.4) * math.pow(10, Xva)), 1.2048)    
        Bo = 0.9759 + 0.00012 * math.pow((RsCalc * math.pow((spgr_Gas / spgr_Oil), 0.5) + 1.25 * average_Temp), 1.2)
        Aval = (0.00091 * average_Temp) - (0.0125 * oil_API) 
        PB = 18.2 * (math.pow((RsCalc / spgr_Gas), 0.83) * math.pow(10, Aval) - 1.4)
        Z=calculate_z(spgr_Gas, th_Pres, th_Temp)
        Bg = 0.02829 * Z * th_Temp / th_Pres
        spgr_Water = 1 + wat_Salility / 1000000
        Bw = 1 + (1.21 * math.pow(10, -4) * (th_Temp - 60)) + (math.pow(10, -6) * math.pow((th_Temp - 60), 2)) - (3.33 * math.pow(10, -6) * th_Pres)
        saturated_oil_viscosity, dead_viscosity = calculate_oil_viscosity_Beggs(oil_API, th_Temp, RsCalc)
        if th_Pres > PB :
            oil_Viscosity = saturated_oil_viscosity             
        else:           
            afactor=3.9*math.pow(10,-5)*math.pow(th_Pres,-5)
            mfactor = 2.6*math.pow(th_Pres, 1.187)* math.pow(10,afactor)
            oil_Viscosity= saturated_oil_viscosity * math.pow(th_Pres/PB, mfactor) 
        water_Viscosity = math.exp(1.003 - (1.479 * math.pow(10, -2) * average_Temp) + (1.982 * math.pow(10, -5) * math.pow(average_Temp, 2))) 
        molecular_Weight = 29 * spgr_Gas 
        GasVisK = (9.379 + 0.01607 * (molecular_Weight)) * math.pow((average_Temp + 460), 1.5) / (209.2 + (19.26 * molecular_Weight) + (average_Temp + 460)) 
        GasVisX = 3.448 + (986.4 / (average_Temp + 460)) + (0.01009 * molecular_Weight) 
        GasVisY = 2.447 - 0.2224 * GasVisX 
        gas_FVF = 0.0283 * Z * (average_Temp + 460) / th_Pres 
        oil_Density = (350 * spgr_Oil + (0.0764 * RsCalc * spgr_Gas)) / (5.615 * Bo) 
        gas_Density = 0.0433 * spgr_Gas * th_Pres / (Z * (average_Temp + 460)) 
        water_Density = 350.4 * spgr_Water / (5.615 * Bw) 
        FactYY = math.pow(gas_Density, GasVisY) 
        gas_Viscosity = 0.0001 * GasVisK * math.exp(GasVisX * FactYY) 
        liquid_Density = (oil_Density * (1 - water_Cut/100) ) + (water_Density * water_Cut/100) 
        liquid_Viscosity = oil_Viscosity * (1 - water_Cut/100)  + water_Viscosity * water_Cut/100 
        Superficial_GasVelocity = 1.16 * math.pow(10, -5) * oil_Rate * (gas_Oil_Ratio - RsCalc) * gas_FVF / area_tubing 
        Superficial_LiquidVelocity = 6.5 * math.pow(10, -5) * (oil_Rate * Bo + water_Rate * Bw) / area_tubing  
        Mixer_Velocity = Superficial_GasVelocity + Superficial_LiquidVelocity 
        NLV = 1.938 * Superficial_LiquidVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        NFR = 0.373 * math.pow(Mixer_Velocity, 2) / tbg_Dia
        NGV = 1.938 * Superficial_GasVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        NRE = 124 * liquid_Density * Superficial_LiquidVelocity * tbg_Dia / liquid_Viscosity
        ND = 10.1 * tbg_Dia * math.pow((liquid_Density / sigma_Liquid), 0.5)
        NL = 0.157 * liquid_Viscosity * math.pow((1 / (liquid_Density * math.pow(sigma_Liquid, 3))), 0.25)
        MoodyFrictionFactor = 64 / NRE
        GasliquidratioCorrectionfactor = (MoodyFrictionFactor * Superficial_GasVelocity * math.pow(ND, (2 / 3))) / Superficial_LiquidVelocity
        NLV = 1.938 * Superficial_LiquidVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        NFR = 0.373 * math.pow(Mixer_Velocity, 2) / tbg_Dia
        NGV = 1.938 * Superficial_GasVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        NoSlip_LiquidHoldup = Superficial_LiquidVelocity / Mixer_Velocity
        if NoSlip_LiquidHoldup>1:
            NoSlip_LiquidHoldup=1
        NoSlip_GasHoldup= 1-NoSlip_LiquidHoldup
        ND = 10.1 * tbg_Dia * math.pow((liquid_Density / sigma_Liquid), 0.5) 
        NL = 1.57 * liquid_Viscosity * math.pow((1 / (liquid_Density * math.pow(sigma_Liquid, 3))), 0.25) 
        CN1 = -0.618 * math.pow(NL, 4) + 0.6389 * math.pow(NL, 3) - 0.2516 * math.pow(NL, 2) + 0.0659 * NL + 0.0018 
        if (CN1 < 0.002):
            CN1 = 0.002 
        HageDornFactor = (NLV / math.pow(NGV, 0.575)) * math.pow((th_Pres / 14.7), 0.1) * (CN1 / ND)
        HoldupbySigh = 10.78 * math.pow(HageDornFactor, 0.3845)
        HageDornFactor1 = NGV * math.pow(NL, 0.38) / math.pow(ND, 2.14)
        if HageDornFactor1<0.01:
            Sigh1 =1
        else:
            Sigh1 = 0.4352 * math.log10(HageDornFactor1) + 2.9399 
        if Sigh1<0:
            Sigh1 =1
        Holdup = HoldupbySigh * Sigh1
        if Holdup>1: 
            Holdup =1
        MixerViscosity = math.pow(liquid_Viscosity, Holdup) * math.pow(gas_Viscosity, (1 - Holdup)) 
        MixerDensity = liquid_Density * Holdup + gas_Density * (1 - Holdup) 
        Noslipmixerdensity = liquid_Density * NoSlip_LiquidHoldup + gas_Density * (1 - NoSlip_LiquidHoldup) 
        NRE1 = 124 * Noslipmixerdensity * Mixer_Velocity * tbg_Dia / MixerViscosity 
        if NRE1 < 2300:            
            MoodyFrictionFactor = 64 / NRE1            
        else:
            FactorK = TbgRoughness / tbg_Dia 
            FrictionFactorA = (math.pow(FactorK, 1.1098) / 2.857) + math.pow((7.149 / NRE), 0.8981) 
            MoodyFrictionFactor = math.sqrt(1 / (-2 * math.log((FactorK / 3.7065) - ((5.0452 / NRE) * math.log(FrictionFactorA))))) 
        if gas_Oil_Ratio <= RsCalc:
            LiqDensity = (oil_Density * (1-water_Cut/100)) + (water_Density * water_Cut/100) 
            LiquidVelocity = 0.0119 * ((oil_Rate / Bo) + (water_Rate / Bw)) / (math.pow(tbg_Dia, 2)) 
            DPDLEL = (LiqDensity * math.sin(deviation_Angle * math.pi / 180)) / 144 
            DPDLFriction = (1.294 * math.pow(10, -3) * MoodyFrictionFactor * LiqDensity * math.pow(LiquidVelocity, 2)) / tbg_Dia 
            DPDL = DPDLEL + DPDLFriction 
            FlowRegime = "Single_Phase" 
        else:
            DPDLFriction = 1.294 * math.pow(10, -2) * MoodyFrictionFactor * math.pow(Noslipmixerdensity, 2) * math.pow((Mixer_Velocity), 2) / math.pow((tbg_Dia * MixerDensity), 2) 
            DPDLEL = MixerDensity * math.sin(deviation_Angle * math.pi / 180) / 144 
            DPDL = (DPDLEL + DPDLFriction)

        average_Temp = average_Temp + (AssumeDepth * math.sin((90 - deviation_Angle) * math.pi / 180) * temp_Gradient) 
                
        presssure.append(th_Pres)
        depth.append(cumMD)
        th_Pres  = th_Pres+ DPDL* AssumeDepth
        cumMD = cumMD + AssumeDepth
        if cumMD > well_Depth:
            AssumeDepth = well_Depth-cumMD
        if cumMD > well_Depth:
            break

    return presssure, depth

def Orkiszewski(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2 ):
    TbgRoughness =0.00015
    oil_Rate = liquid_Rate *(1-water_Cut/100)
    water_Rate =liquid_Rate *water_Cut/100
    gas_Rate = oil_Rate * gas_Oil_Ratio
    tpc = 168 + (325 * spgr_Gas - 12.5 * math.pow(spgr_Gas, 2))
    ppc = 677 + (15 * spgr_Gas - 37.5 * math.pow(spgr_Gas, 2))
    A = (moleH2S + moleCO2)
    spgr_Oil = 141.5/(131.5+oil_API)
    epsilon = 120 * (math.pow(A, 0.9) - math.pow(A, 1.6)) + 15 * (math.pow(moleH2S, 0.5) - math.pow(moleH2S, 4))
    area_tubing= math.pi * (math.pow((tbg_Dia / 12), 2)) / 4
    temp_Gradient = (res_Temp - th_Temp) / well_Depth
    average_Temp= (res_Temp + th_Temp)/2
    presssure=[] 
    depth=[]
    AssumeDepth=well_Depth/100
    cumMD = AssumeDepth
    for i in range(100):
        if th_Pres <3977:
            confact =1 - 0.024 * math.pow(th_Pres, 0.45)
        else:
            confact =1.0
        if th_Temp <= 68:
            sigma_Oil = 39 - (0.257 * oil_API * confact) 
        elif th_Temp > 100:
            sigma_Oil =37.5 - 0.257 * oil_API * confact
        else:            
            sigma_Oil = confact * (((39 - 0.257 * oil_API)) + (((37.5 - 0.257 * oil_API)) - ((39 - 0.257 * oil_API))) * (th_Temp - 68) / 32) 

        sigma_Water = (-9 * math.pow(10, -5) * th_Temp + 0.0815) * 1000
        sigma_Liquid = (sigma_Oil * (1-water_Cut/100)) + (sigma_Water * water_Cut/100) 
        deviation_Angle =90
        Xva = 0.0125 * oil_API - 0.00091 * average_Temp
        RsCalc = spgr_Gas * math.pow((((th_Pres / 18.2) + 1.4) * math.pow(10, Xva)), 1.2048)    
        Bo = 0.9759 + 0.00012 * math.pow((RsCalc * math.pow((spgr_Gas / spgr_Oil), 0.5) + 1.25 * average_Temp), 1.2)
        Aval = (0.00091 * average_Temp) - (0.0125 * oil_API) 
        PB = 18.2 * (math.pow((RsCalc / spgr_Gas), 0.83) * math.pow(10, Aval) - 1.4)
        Z=calculate_z(spgr_Gas, th_Pres, th_Temp)
        Bg = 0.02829 * Z * th_Temp / th_Pres
        spgr_Water = 1 + wat_Salility / 1000000
        Bw = 1 + (1.21 * math.pow(10, -4) * (th_Temp - 60)) + (math.pow(10, -6) * math.pow((th_Temp - 60), 2)) - (3.33 * math.pow(10, -6) * th_Pres)
        saturated_oil_viscosity, dead_viscosity = calculate_oil_viscosity_Beggs(oil_API, th_Temp, RsCalc)
        if th_Pres > PB :
            oil_Viscosity = saturated_oil_viscosity             
        else:           
            afactor=3.9*math.pow(10,-5)*math.pow(th_Pres,-5)
            mfactor = 2.6*math.pow(th_Pres, 1.187)* math.pow(10,afactor)
            oil_Viscosity= saturated_oil_viscosity * math.pow(th_Pres/PB, mfactor) 
        water_Viscosity = math.exp(1.003 - (1.479 * math.pow(10, -2) * average_Temp) + (1.982 * math.pow(10, -5) * math.pow(average_Temp, 2))) 
        molecular_Weight = 29 * spgr_Gas 
        GasVisK = (9.379 + 0.01607 * (molecular_Weight)) * math.pow((average_Temp + 460), 1.5) / (209.2 + (19.26 * molecular_Weight) + (average_Temp + 460)) 
        GasVisX = 3.448 + (986.4 / (average_Temp + 460)) + (0.01009 * molecular_Weight) 
        GasVisY = 2.447 - 0.2224 * GasVisX 
        gas_FVF = 0.0283 * Z * (average_Temp + 460) / th_Pres 
        oil_Density = (350 * spgr_Oil + (0.0764 * RsCalc * spgr_Gas)) / (5.615 * Bo) 
        gas_Density = 0.0433 * spgr_Gas * th_Pres / (Z * (average_Temp + 460)) 
        water_Density = 350.4 * spgr_Water / (5.615 * Bw) 
        FactYY = math.pow(gas_Density, GasVisY) 
        gas_Viscosity = 0.0001 * GasVisK * math.exp(GasVisX * FactYY) 
        liquid_Density = (oil_Density * (1 - water_Cut/100) ) + (water_Density * water_Cut/100) 
        liquid_Viscosity = oil_Viscosity * (1 - water_Cut/100)  + water_Viscosity * water_Cut/100 
        Superficial_GasVelocity = 1.16 * math.pow(10, -5) * oil_Rate * (gas_Oil_Ratio - RsCalc) * gas_FVF / area_tubing 
        Superficial_LiquidVelocity = 6.5 * math.pow(10, -5) * (oil_Rate * Bo + water_Rate * Bw) / area_tubing  
        Mixer_Velocity = Superficial_GasVelocity + Superficial_LiquidVelocity 
        NLV = 1.938 * Superficial_LiquidVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        NFR = 0.373 * math.pow(Mixer_Velocity, 2) / tbg_Dia
        NGV = 1.938 * Superficial_GasVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        Slip_Velocity = Superficial_GasVelocity - Superficial_LiquidVelocity 
        LiquidHoldup = (Slip_Velocity - Mixer_Velocity + math.pow((math.pow((Mixer_Velocity - Slip_Velocity), 2) + 4 * Slip_Velocity * Superficial_LiquidVelocity), 0.5)) / (2 * Slip_Velocity)
        
        NRE = 124 * liquid_Density * Superficial_LiquidVelocity * tbg_Dia / (liquid_Viscosity*LiquidHoldup)
        ND = 10.1 * tbg_Dia * math.pow((liquid_Density / sigma_Liquid), 0.5)
        NL = 0.157 * liquid_Viscosity * math.pow((1 / (liquid_Density * math.pow(sigma_Liquid, 3))), 0.25)
        MoodyFrictionFactor = 64 / NRE
        GasliquidratioCorrectionfactor = (MoodyFrictionFactor * Superficial_GasVelocity * math.pow(ND, (2 / 3))) / Superficial_LiquidVelocity
        MixerDensity = liquid_Density * LiquidHoldup + gas_Density * (1 - LiquidHoldup) 
        if ND>=70:
            L2=1
        elif ND<=30:
            L2=2
        else:
            L2 = 33.354 * math.pow(ND, -0.835)
        if ND>=70:
            L1=1.1       
        else:
            L1 = 0.0949 * math.pow(ND, 0.5987)

        NGVBS = L1 + L2 * NLV
        NGVST = 50 + 36 * NLV
        NGVTM = 75 + 84 * math.pow(NLV, 0.75)
        if Superficial_GasVelocity <=0.13:
            NoSlipGasVoidFaction = 1.071 - 0.2662 * (2 * Mixer_Velocity / tbg_Dia)
        else:
            NoSlipGasVoidFaction = Superficial_GasVelocity / Mixer_Velocity

        if gas_Oil_Ratio <= RsCalc:           
            LiquidVelocity = 0.0119 * ((oil_Rate / Bo) + (water_Rate / Bw)) / (math.pow(tbg_Dia, 2)) 
            DPDLEL = (liquid_Density * math.sin(deviation_Angle * math.pi / 180)) / 144 
            DPDLFriction = (1.294 * math.pow(10, -3) * MoodyFrictionFactor * liquid_Density * math.pow(LiquidVelocity, 2)) / tbg_Dia 
            DPDL = DPDLEL + DPDLFriction 
            FlowRegime = "Single_Phase" 
        elif NGV >=0.0 and NGV <= NGVBS:
            SlipVelocity = 0.8 
            LiquidHoldup = ((Slip_Velocity - Mixer_Velocity) + math.pow((math.pow((Mixer_Velocity - Slip_Velocity), 2) + 4 * Slip_Velocity * Superficial_LiquidVelocity), 0.5)) / (2 * Slip_Velocity) 
            DPDLEL = (liquid_Density * LiquidHoldup + gas_Density * (1 - LiquidHoldup)) / 144 
            DPDLFriction = (1.294 * math.pow(10, -3)) * (MoodyFrictionFactor * liquid_Density / tbg_Dia) * math.pow((Superficial_LiquidVelocity / LiquidHoldup), 2) 
            DPDL = DPDLEL + DPDLFriction             
            FlowRegime = "Bubble Flow" 
        elif NGV > NGVBS and NGV < NGVST:
            Vb = 1
            g = 32.17
            NREB = 124 * liquid_Density * Vb * tbg_Dia / liquid_Viscosity 
            NREL = 124 * liquid_Density * Mixer_Velocity * tbg_Dia / liquid_Viscosity
            if NREB <=3000:
                Vb = (0.546 + 8.74 * math.pow(10, -6) * NREL) * math.pow((g * tbg_Dia), 0.5)
            elif NREB >=8000:
                Vb = (0.35 + 8.74 * math.pow(10, 6) * NREL) * math.pow((g * tbg_Dia), 0.5)
            else:
                VBS = (0.251 + 8.74 * math.pow(10, -6) * NREL) * math.pow((g * tbg_Dia), 0.5);
                Vb = 0.5 * (VBS + math.pow((math.pow(VBS, 2) + (13.59 * liquid_Viscosity / (liquid_Density * math.pow(tbg_Dia, 0.5)))), 0.5))
            if Mixer_Velocity <=10:
                Liqdistributionfact = 0.065 * Mixer_Velocity
            else:
                Liqdistributionfact = (Vb / (Mixer_Velocity + Vb)) * (1 - MixerDensity / liquid_Density)

            FlowRegime = "Slug Flow"
            DPDLFriction = 1.294 * math.pow(10, -3) * (MoodyFrictionFactor * liquid_Density * math.pow(Mixer_Velocity, 2) / (tbg_Dia)) * (((Superficial_LiquidVelocity + Vb) / (Mixer_Velocity + Vb)) + Liqdistributionfact)
            DPDLEL = (((liquid_Density * (Superficial_LiquidVelocity + Vb) + gas_Density * Superficial_GasVelocity) / (Mixer_Velocity * Vb)) + Liqdistributionfact * liquid_Density) / 144 
            DPDL = DPDLEL + DPDLFriction
        elif NGVTM < NGV:
            FlowRegime = "Mist" 
            NoSlipLiquidHoldup = Superficial_LiquidVelocity / Mixer_Velocity 
            MixerDensity = liquid_Density * NoSlipLiquidHoldup + gas_Density * (1 - NoSlipLiquidHoldup) 
            NREG = 124 * gas_Density * Superficial_GasVelocity * tbg_Dia / gas_Viscosity 
            NWe = gas_Density * math.pow(Superficial_GasVelocity, 2) * TbgRoughness / sigma_Liquid 
            NMu = math.pow(liquid_Viscosity, 2) / liquid_Density * sigma_Liquid * TbgRoughness 
            if NWe * NMu <= 0.005:            
                K = 0.07498 * sigma_Liquid / (gas_Density * math.pow(Superficial_GasVelocity, 2) * tbg_Dia) 
            elif NWe * NMu > 0.005:
                K = (0.3731 * sigma_Liquid * math.pow((NWe * NMu), 0.302)) / (gas_Density * math.pow(Superficial_GasVelocity, 2) * tbg_Dia) 
            
            FrictionFactor = 4 * (1 / math.pow((4 * math.log10(0.27 * K)), 2) + 0.067 * math.pow(K, 1.73)) 
            DPDLFriction = 1.294 * math.pow(10, -3) * FrictionFactor * liquid_Density * math.pow(Superficial_LiquidVelocity, 2) / tbg_Dia * (1 + Superficial_GasVelocity / Superficial_LiquidVelocity) 
            EK = (liquid_Density * Superficial_LiquidVelocity + gas_Density * Superficial_GasVelocity) * Superficial_GasVelocity / (144 * th_Pres * 32.17) 
            DPDLEL = MixerDensity / 144 
            DPDL = (DPDLEL + DPDLFriction) 
        else:
            FlowRegime = "Transition"
            if GasliquidratioCorrectionfactor<=0.1:
                F5 = -1.3316 * GasliquidratioCorrectionfactor + 1.89
            else:
                F5 = 0.0301 * math.log(GasliquidratioCorrectionfactor) + 0.0941
            if GasliquidratioCorrectionfactor<=0.02:
                F6 = 4410.4 * math.pow(GasliquidratioCorrectionfactor, 2) - 132.28 * GasliquidratioCorrectionfactor + 0.7376
            elif GasliquidratioCorrectionfactor > 0.02 & GasliquidratioCorrectionfactor <= 0.2:
                 F6 = 44.594 * math.pow(GasliquidratioCorrectionfactor, 1.3244)
            else:
                 F6 = 1.5662 * math.pow(GasliquidratioCorrectionfactor, -0.175)
            F7 = 0.0209 * math.pow(GasliquidratioCorrectionfactor, -0.306) 
            DerF6 = 0.029 * ND + F6 
            Sslug = (1 + F5) * (math.pow(NGV, 0.982) + DerF6) / math.pow((1 + F7 * NLV), 2) 
            SlipVelocity = 0.52 * Sslug * math.pow((sigma_Liquid / liquid_Density), 0.25) 
            LiquidHoldup = (SlipVelocity - Mixer_Velocity + math.pow((math.pow((Mixer_Velocity - SlipVelocity), 2) + 4 * SlipVelocity * Superficial_LiquidVelocity), 0.5)) / (2 * SlipVelocity) 
            DPDLEL = MixerDensity * math.sin(deviation_Angle * math.pi / 180) / 144 
            MoodyFrictionFactor = 64 / NRE 
            GasliquidratioCorrectionfactor = (MoodyFrictionFactor * Superficial_GasVelocity *math.pow(ND, (2 / 3))) / Superficial_LiquidVelocity
            if GasliquidratioCorrectionfactor >= 70:
                FrictionFactorF2 = 0.21 
            elif GasliquidratioCorrectionfactor < 70 & GasliquidratioCorrectionfactor >= 0.2:
                FrictionFactorF2 = 0.748 * math.pow(GasliquidratioCorrectionfactor, -0.31)
            else: 
                FrictionFactorF2 = 1.0021 * math.exp(GasliquidratioCorrectionfactor * 0.4358)
            FrictionFactorF3 = 1 + (MoodyFrictionFactor / 4) * math.pow((Superficial_GasVelocity / (50 * Superficial_LiquidVelocity)), 0.5) 
            FrictionFactor = MoodyFrictionFactor * (FrictionFactorF2 / FrictionFactorF3) 
            ReynoldsNo = 124 * (liquid_Density * tbg_Dia * Superficial_LiquidVelocity) / liquid_Viscosity 
            DPDLFriction = 1.294 * math.pow(10, -3) * (FrictionFactor * MixerDensity * math.pow(Superficial_LiquidVelocity, 2) / tbg_Dia) * (1 + Superficial_GasVelocity / Superficial_LiquidVelocity)
            DPDLslug = (DPDLEL + DPDLFriction) 
            NoSlipLiquidHoldup = Superficial_LiquidVelocity / Mixer_Velocity 
            MixerDensity = liquid_Density * NoSlipLiquidHoldup + gas_Density * (1 - NoSlipLiquidHoldup) 
            NREG = 124 * gas_Density * Superficial_GasVelocity * tbg_Dia / gas_Viscosity 
            NWe = gas_Density * math.pow(Superficial_GasVelocity, 2) * TbgRoughness / sigma_Liquid 
            NMu = math.pow(liquid_Viscosity, 2) / liquid_Density * sigma_Liquid * TbgRoughness 
            if (NWe * NMu <= 0.005):
                K = 0.07498 * sigma_Liquid / gas_Density * Superficial_GasVelocity * tbg_Dia 
            else:
                K = (0.3731 * sigma_Liquid * math.pow((NWe * NMu), 0.302)) / gas_Density * math.pow(Superficial_GasVelocity, 2) * tbg_Dia 
            
            FrictionFactor = 4 * (1 / math.pow((4 * math.log(0.27 * K)), 2) + 0.067 * math.pow(K, 1.73)) 
            DPDLFriction = 1.294 * math.pow(10, -3) * FrictionFactor * liquid_Density * math.pow(Superficial_LiquidVelocity, 2) / tbg_Dia * (1 + Superficial_GasVelocity / Superficial_LiquidVelocity) 
            EK = (liquid_Density * Superficial_LiquidVelocity + gas_Density * Superficial_GasVelocity) * Superficial_GasVelocity / (144 * th_Pres * 32.17) 
            DPDLmist = (DPDLEL + DPDLFriction) / (1 - EK) 
            B = ((75 + 84 * math.pow(NLV, 0.75)) - NGV) / ((75 + 84 * math.pow(NLV, 0.75)) - (50 + 36 * NLV)) 
            DPDL = B * DPDLslug + (1 - B) * DPDLmist 


        average_Temp = average_Temp + (AssumeDepth * math.sin((90 - deviation_Angle) * math.pi / 180) * temp_Gradient)                 
        presssure.append(th_Pres)
        depth.append(cumMD)
        th_Pres  = th_Pres+ DPDL* AssumeDepth
        cumMD = cumMD + AssumeDepth
        if cumMD > well_Depth:
            AssumeDepth = well_Depth-cumMD
        if cumMD > well_Depth:
            break

    return presssure, depth

def Beggs_Brill(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2 ):
    TbgRoughness =0.00015
    oil_Rate = liquid_Rate *(1-water_Cut/100)
    water_Rate =liquid_Rate *water_Cut/100
    gas_Rate = oil_Rate * gas_Oil_Ratio
    tpc = 168 + (325 * spgr_Gas - 12.5 * math.pow(spgr_Gas, 2))
    ppc = 677 + (15 * spgr_Gas - 37.5 * math.pow(spgr_Gas, 2))
    A = (moleH2S + moleCO2)
    spgr_Oil = 141.5/(131.5+oil_API)
    epsilon = 120 * (math.pow(A, 0.9) - math.pow(A, 1.6)) + 15 * (math.pow(moleH2S, 0.5) - math.pow(moleH2S, 4))
    area_tubing= math.pi * (math.pow((tbg_Dia / 12), 2)) / 4
    temp_Gradient = (res_Temp - th_Temp) / well_Depth
    average_Temp= (res_Temp + th_Temp)/2
    presssure=[] 
    depth=[]
    AssumeDepth=well_Depth/100
    cumMD = AssumeDepth
    for i in range(100):
        if th_Pres <3977:
            confact =1 - 0.024 * math.pow(th_Pres, 0.45)
        else:
            confact =1.0
        if th_Temp <= 68:
            sigma_Oil = 39 - (0.257 * oil_API * confact) 
        elif th_Temp > 100:
            sigma_Oil =37.5 - 0.257 * oil_API * confact
        else:            
            sigma_Oil = confact * (((39 - 0.257 * oil_API)) + (((37.5 - 0.257 * oil_API)) - ((39 - 0.257 * oil_API))) * (th_Temp - 68) / 32) 

        sigma_Water = (-9 * math.pow(10, -5) * th_Temp + 0.0815) * 1000
        sigma_Liquid = (sigma_Oil * (1-water_Cut/100)) + (sigma_Water * water_Cut/100) 
        deviation_Angle =90
        Xva = 0.0125 * oil_API - 0.00091 * average_Temp
        RsCalc = spgr_Gas * math.pow((((th_Pres / 18.2) + 1.4) * math.pow(10, Xva)), 1.2048)    
        Bo = 0.9759 + 0.00012 * math.pow((RsCalc * math.pow((spgr_Gas / spgr_Oil), 0.5) + 1.25 * average_Temp), 1.2)
        Aval = (0.00091 * average_Temp) - (0.0125 * oil_API) 
        PB = 18.2 * (math.pow((RsCalc / spgr_Gas), 0.83) * math.pow(10, Aval) - 1.4)
        Z=calculate_z(spgr_Gas, th_Pres, th_Temp)
        Bg = 0.02829 * Z * th_Temp / th_Pres
        spgr_Water = 1 + wat_Salility / 1000000
        Bw = 1 + (1.21 * math.pow(10, -4) * (th_Temp - 60)) + (math.pow(10, -6) * math.pow((th_Temp - 60), 2)) - (3.33 * math.pow(10, -6) * th_Pres)        
        saturated_oil_viscosity, dead_viscosity = calculate_oil_viscosity_Beggs(oil_API, th_Temp, RsCalc)
        if th_Pres > PB :
            oil_Viscosity = saturated_oil_viscosity          
        else:           
            afactor=3.9*math.pow(10,-5)*math.pow(th_Pres,-5)
            mfactor = 2.6*math.pow(th_Pres, 1.187)* math.pow(10,afactor)
            oil_Viscosity= saturated_oil_viscosity * math.pow(th_Pres/PB, mfactor)      
        water_Viscosity = math.exp(1.003 - (1.479 * math.pow(10, -2) * average_Temp) + (1.982 * math.pow(10, -5) * math.pow(average_Temp, 2)))         
        molecular_Weight = 29 * spgr_Gas 
        GasVisK = (9.379 + 0.01607 * (molecular_Weight)) * math.pow((average_Temp + 460), 1.5) / (209.2 + (19.26 * molecular_Weight) + (average_Temp + 460)) 
        GasVisX = 3.448 + (986.4 / (average_Temp + 460)) + (0.01009 * molecular_Weight) 
        GasVisY = 2.447 - 0.2224 * GasVisX 
        gas_FVF = 0.0283 * Z * (average_Temp + 460) / th_Pres 
        oil_Density = (350 * spgr_Oil + (0.0764 * RsCalc * spgr_Gas)) / (5.615 * Bo) 
        gas_Density = 0.0433 * spgr_Gas * th_Pres / (Z * (average_Temp + 460)) 
        water_Density = 350.4 * spgr_Water / (5.615 * Bw) 
        FactYY = math.pow(gas_Density, GasVisY) 
        gas_Viscosity = 0.0001 * GasVisK * math.exp(GasVisX * FactYY) 
        liquid_Density = (oil_Density * (1 - water_Cut/100) ) + (water_Density * water_Cut/100) 
        liquid_Viscosity = oil_Viscosity * (1 - water_Cut/100)  + water_Viscosity * water_Cut/100 
        Superficial_GasVelocity = 1.16 * math.pow(10, -5) * oil_Rate * (gas_Oil_Ratio - RsCalc) * gas_FVF / area_tubing 
        Superficial_LiquidVelocity = 6.5 * math.pow(10, -5) * (oil_Rate * Bo + water_Rate * Bw) / area_tubing  
        Mixer_Velocity = Superficial_GasVelocity + Superficial_LiquidVelocity 
        VB = 0.79 * math.pow(((sigma_Liquid * (liquid_Density - gas_Density)) / math.pow(liquid_Density, 2)), 0.25)
        GasHoldup = Superficial_GasVelocity / (Mixer_Velocity + VB)
        LiquidHoldup = 1 - GasHoldup
        MixerDensity = liquid_Density * LiquidHoldup + gas_Density * (1 - LiquidHoldup)
        NLV = 1.938 * Superficial_LiquidVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        NFR = 0.373 * math.pow(Mixer_Velocity, 2) / tbg_Dia
        NoSlipLiquidHoldup = Superficial_LiquidVelocity / Mixer_Velocity
        NoSlipGasHoldup = (1 - NoSlipLiquidHoldup)
        ActualLiquidVelocity = Superficial_LiquidVelocity / NoSlipLiquidHoldup
        ActualGasVelocity = Superficial_GasVelocity / NoSlipGasHoldup
        SlipVelocity = ActualGasVelocity - ActualLiquidVelocity
        NoslipmixerDensity = liquid_Density * NoSlipLiquidHoldup + gas_Density * NoSlipGasHoldup      
        NGV = 1.938 * Superficial_GasVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        L1 = 316 * math.pow(NoSlipLiquidHoldup, 0.302)
        L2 = 0.0009252 * math.pow(NoSlipLiquidHoldup, -2.4684)
        L3 = 0.1 * math.pow(NoSlipLiquidHoldup, -1.4516)
        L4 = 0.5 * math.pow(NoSlipLiquidHoldup, -6.738)
        FactA = (L3 - NFR) / (L3 - L2)
        if (NoSlipLiquidHoldup <= 0.01 and  NFR < L1) or (NoSlipLiquidHoldup >= 0.01 and NFR < L2):        
            Holdup = 0.98 * math.pow(NoSlipLiquidHoldup, 0.4846) / math.pow(NFR, 0.0868) 
            ConsC = (1 - NoSlipLiquidHoldup) * math.log(0.011 * math.pow(NoSlipLiquidHoldup, -3.768) * math.pow(NLV, 3.539) * math.pow(NFR, -1.614)) 
            Sigh = 1 + ConsC * (math.sin(1.8 * deviation_Angle * 22 / 7 / 180) - 0.333 * (math.pow((math.sin(1.8 * deviation_Angle * 22 / 7 / 180)), 3))) 
            FlowRegime = "Segregated"  
        elif (NoSlipLiquidHoldup > 0.01 and NoSlipLiquidHoldup <= 0.4 and L3 < NFR and NFR <= L1) or (NoSlipLiquidHoldup >= 0.4 and L3 < NFR and NFR <= L4):         
            Holdup = 0.845 * math.pow(NoSlipLiquidHoldup, 0.5351) / math.pow(NFR, 0.0173)  
            ConsC = (1 - NoSlipLiquidHoldup) * math.log(2.96 * math.pow(NoSlipLiquidHoldup, 0.305) * math.pow(NLV, -0.4473) * math.pow(NFR, 0.0978)) 
            Sigh = 1 + ConsC * (math.sin(1.8 * deviation_Angle * 22 / 7 / 180) - 0.333 * (math.pow((math.sin(1.8 * deviation_Angle * 22 / 7 / 180)), 3)))
            FlowRegime = "Intermittent"           
        elif (NoSlipLiquidHoldup < 0.4 and NFR > L1) or (NoSlipLiquidHoldup >= 0.4 and NFR > L4):         
            Holdup = 1.065 * math.pow(NoSlipLiquidHoldup, 0.5824) / math.pow(NFR, 0.0609)
            ConsC = 0
            Sigh = 1 + ConsC * (math.sin(1.8 * deviation_Angle * 22 / 7 / 180) - 0.333 * (math.pow((math.sin(1.8 * deviation_Angle * 22 / 7 / 180)), 3)))
            FlowRegime = "Distributed"
        elif (NoSlipLiquidHoldup >= 0.01 and L2 < NFR and NFR < L3): 
            BVal = (0.01 * math.pow(NoSlipLiquidHoldup, -1.452) - NFR) / ((0.1 * math.pow(NoSlipLiquidHoldup, -1.452)) - (9.25 * math.pow(10, -4) * math.pow(NoSlipLiquidHoldup, -2.468))) 
            ConsC = 0
            Sigh = 1 + ConsC * (math.sin(1.8 * deviation_Angle) - 0.333 * (math.pow((math.sin(1.8 * deviation_Angle)), 3))) 
            Holdup = BVal * Sigh * (0.98 * math.pow(NoSlipLiquidHoldup, 0.4846) / math.pow(NFR, 0.0868)) + (1 - BVal) * Sigh * (0.845 * math.pow(NoSlipLiquidHoldup, 0.5351) / math.pow(NFR, 0.0173)) 
            FlowRegime = "Transition"
        
        HoldupCorrected = Holdup * Sigh
        MixerDensity = liquid_Density * HoldupCorrected + gas_Density * (1 - HoldupCorrected)
        CorrectedMixerDensity = (liquid_Density * HoldupCorrected) + (1 - HoldupCorrected) * gas_Density 
        NoSlipViscosity = (liquid_Viscosity * NoSlipLiquidHoldup) + (gas_Viscosity * (1 - NoSlipLiquidHoldup)) 
        ReynoldsNo = 124 * (NoslipmixerDensity * tbg_Dia * Mixer_Velocity) / NoSlipViscosity 
        FactY = NoSlipLiquidHoldup / math.pow(Holdup, 2) 
        if FactY >1.0 and FactY<1.2:
            FactS = math.log(FactY) / (-0.0523 + 3.182 * (math.log(FactY)) - 0.8752 * (math.pow(math.log(FactY), 2)) + 0.01853 * math.pow((math.log(FactY)), 4))
        else:
            FactS = math.log(FactY) / (-0.0523 + 3.18 *math.log(FactY) - 0.872 * math.pow((math.log(FactY)), 2) + 0.01853 * math.pow((math.log(FactY)), 4))
        FNS = 0.0056 + 0.5 / (math.pow(ReynoldsNo, 0.32)) 
        FTP = math.exp(FactS) 
        FrictionFactor = FTP * FNS 
        EK = 2.16 * math.pow(10, -4) * Mixer_Velocity * Superficial_GasVelocity * NoslipmixerDensity / th_Pres 
        if gas_Oil_Ratio <= RsCalc:  
            LiquidVelocity = 0.0119 * ((oil_Rate / Bo) + (water_Rate / Bw)) / math.pow(tbg_Dia, 2) 
            DPDLEL = (CorrectedMixerDensity * math.sin(deviation_Angle * math.pi / 180)) / 144 
            DPDLFriction = (1.294 * math.pow(10, -3) * FrictionFactor * liquid_Density * math.pow(LiquidVelocity, 2)) / (tbg_Dia) 
            DPDL = DPDLEL + DPDLFriction 
            FlowRegime = "Single_Phase"
        else:
            DPDLEL = CorrectedMixerDensity * math.sin(deviation_Angle *math.pi / 180) / 144 
            DPDLFriction = (1.294 * math.pow(10, -3) * FrictionFactor * NoslipmixerDensity * math.pow(Mixer_Velocity, 2)) / (tbg_Dia) 
            DPDL = (DPDLEL + DPDLFriction) / (1 - EK) 

        average_Temp = average_Temp + (AssumeDepth * math.sin((90 - deviation_Angle) * math.pi / 180) * temp_Gradient)                 
        presssure.append(th_Pres)
        depth.append(cumMD)
        th_Pres  = th_Pres+ DPDL* AssumeDepth
        cumMD = cumMD + AssumeDepth
        if cumMD > well_Depth:
            AssumeDepth = well_Depth-cumMD
        if cumMD > well_Depth:
            break

    return presssure, depth

def Fancher_Brown(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2 ):
    TbgRoughness =0.00015
    oil_Rate = liquid_Rate *(1-water_Cut/100)
    water_Rate =liquid_Rate *water_Cut/100
    gas_Rate = oil_Rate * gas_Oil_Ratio
    tpc = 168 + (325 * spgr_Gas - 12.5 * math.pow(spgr_Gas, 2))
    ppc = 677 + (15 * spgr_Gas - 37.5 * math.pow(spgr_Gas, 2))
    A = (moleH2S + moleCO2)
    spgr_Oil = 141.5/(131.5+oil_API)
    epsilon = 120 * (math.pow(A, 0.9) - math.pow(A, 1.6)) + 15 * (math.pow(moleH2S, 0.5) - math.pow(moleH2S, 4))
    area_tubing= math.pi * (math.pow((tbg_Dia / 12), 2)) / 4
    temp_Gradient = (res_Temp - th_Temp) / well_Depth
    average_Temp= (res_Temp + th_Temp)/2
    presssure=[] 
    depth=[]
    AssumeDepth=well_Depth/100
    cumMD = AssumeDepth
    for i in range(100):
        if th_Pres <3977:
            confact =1 - 0.024 * math.pow(th_Pres, 0.45)
        else:
            confact =1.0
        if th_Temp <= 68:
            sigma_Oil = 39 - (0.257 * oil_API * confact) 
        elif th_Temp > 100:
            sigma_Oil =37.5 - 0.257 * oil_API * confact
        else:            
            sigma_Oil = confact * (((39 - 0.257 * oil_API)) + (((37.5 - 0.257 * oil_API)) - ((39 - 0.257 * oil_API))) * (th_Temp - 68) / 32) 

        sigma_Water = (-9 * math.pow(10, -5) * th_Temp + 0.0815) * 1000
        sigma_Liquid = (sigma_Oil * (1-water_Cut/100)) + (sigma_Water * water_Cut/100) 
        deviation_Angle =90
        Xva = 0.0125 * oil_API - 0.00091 * average_Temp
        RsCalc = spgr_Gas * math.pow((((th_Pres / 18.2) + 1.4) * math.pow(10, Xva)), 1.2048)    
        Bo = 0.9759 + 0.00012 * math.pow((RsCalc * math.pow((spgr_Gas / spgr_Oil), 0.5) + 1.25 * average_Temp), 1.2)
        Aval = (0.00091 * average_Temp) - (0.0125 * oil_API) 
        PB = 18.2 * (math.pow((RsCalc / spgr_Gas), 0.83) * math.pow(10, Aval) - 1.4)
        Z=calculate_z(spgr_Gas, th_Pres, th_Temp)
        Bg = 0.02829 * Z * th_Temp / th_Pres
        spgr_Water = 1 + wat_Salility / 1000000
        Bw = 1 + (1.21 * math.pow(10, -4) * (th_Temp - 60)) + (math.pow(10, -6) * math.pow((th_Temp - 60), 2)) - (3.33 * math.pow(10, -6) * th_Pres)
        saturated_oil_viscosity, dead_viscosity = calculate_oil_viscosity_Beggs(oil_API, th_Temp, RsCalc)
        if th_Pres > PB :
            oil_Viscosity = saturated_oil_viscosity             
        else:           
            afactor=3.9*math.pow(10,-5)*math.pow(th_Pres,-5)
            mfactor = 2.6*math.pow(th_Pres, 1.187)* math.pow(10,afactor)
            oil_Viscosity= saturated_oil_viscosity * math.pow(th_Pres/PB, mfactor)  
        water_Viscosity = math.exp(1.003 - (1.479 * math.pow(10, -2) * average_Temp) + (1.982 * math.pow(10, -5) * math.pow(average_Temp, 2))) 
        molecular_Weight = 29 * spgr_Gas 
        GasVisK = (9.379 + 0.01607 * (molecular_Weight)) * math.pow((average_Temp + 460), 1.5) / (209.2 + (19.26 * molecular_Weight) + (average_Temp + 460)) 
        GasVisX = 3.448 + (986.4 / (average_Temp + 460)) + (0.01009 * molecular_Weight) 
        GasVisY = 2.447 - 0.2224 * GasVisX 
        gas_FVF = 0.0283 * Z * (average_Temp + 460) / th_Pres 
        oil_Density = (350 * spgr_Oil + (0.0764 * RsCalc * spgr_Gas)) / (5.615 * Bo) 
        gas_Density = 0.0433 * spgr_Gas * th_Pres / (Z * (average_Temp + 460)) 
        water_Density = 350.4 * spgr_Water / (5.615 * Bw) 
        FactYY = math.pow(gas_Density, GasVisY) 
        gas_Viscosity = 0.0001 * GasVisK * math.exp(GasVisX * FactYY) 
        liquid_Density = (oil_Density * (1 - water_Cut/100) ) + (water_Density * water_Cut/100) 
        liquid_Viscosity = oil_Viscosity * (1 - water_Cut/100)  + water_Viscosity * water_Cut/100 
        Superficial_GasVelocity = 1.16 * math.pow(10, -5) * oil_Rate * (gas_Oil_Ratio - RsCalc) * gas_FVF / area_tubing 
        Superficial_LiquidVelocity = 6.5 * math.pow(10, -5) * (oil_Rate * Bo + water_Rate * Bw) / area_tubing  
        Mixer_Velocity = Superficial_GasVelocity + Superficial_LiquidVelocity 
        VB = 0.79 * math.pow(((sigma_Liquid * (liquid_Density - gas_Density)) / math.pow(liquid_Density, 2)), 0.25)
        GasHoldup = Superficial_GasVelocity / (Mixer_Velocity + VB)
        LiquidHoldup = 1 - GasHoldup
        MixerDensity = liquid_Density * LiquidHoldup + gas_Density * (1 - LiquidHoldup)
        NLV = 1.938 * Superficial_LiquidVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        NFR = 0.373 * math.pow(Mixer_Velocity, 2) / tbg_Dia
        NoSlipLiquidHoldup = Superficial_LiquidVelocity / Mixer_Velocity
        NoSlipGasHoldup = (1 - NoSlipLiquidHoldup)
        ActualLiquidVelocity = Superficial_LiquidVelocity / NoSlipLiquidHoldup
        ActualGasVelocity = Superficial_GasVelocity / NoSlipGasHoldup
        SlipVelocity = ActualGasVelocity - ActualLiquidVelocity
        NoslipmixerDensity = liquid_Density * NoSlipLiquidHoldup + gas_Density * NoSlipGasHoldup      
        NGV = 1.938 * Superficial_GasVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        RHONSVMD = NoslipmixerDensity * Mixer_Velocity * tbg_Dia
        if liquid_Rate<3000:
            if gas_Oil_Ratio <= 1500:
                EnergyFactor = 3.8458 * math.pow(RHONSVMD, -1.314)
            elif gas_Oil_Ratio <= 3000:
                EnergyFactor = 1.4023 * math.pow(RHONSVMD, -1.190)
            else:
                EnergyFactor = 0.6748 * math.pow(RHONSVMD, -1.259)
        else:  
            if gas_Oil_Ratio <= 1500:
                EnergyFactor = 3.8458 * math.pow(RHONSVMD, -1.314)
            elif gas_Oil_Ratio <= 3000:
                EnergyFactor = 1.4023 * math.pow(RHONSVMD, -1.190)*10
            else:
                EnergyFactor = 0.6748 * math.pow(RHONSVMD, -1.259)*100
        NoSlipViscosity = (liquid_Viscosity * NoSlipLiquidHoldup) + (gas_Viscosity * (1 - NoSlipLiquidHoldup)) 
        ReynoldsNo = 124 * (NoslipmixerDensity * tbg_Dia * Mixer_Velocity) / NoSlipViscosity  
        FactY = NoSlipLiquidHoldup / math.pow(LiquidHoldup, 2) 
        if FactY >1.0 and FactY <=1.2:
            FactS =  math.log(2.2 * FactY - 1.2)            
        elif FactY >1.0: 
            FactS = math.log(FactY) / (-0.0523 + 3.182 * (math.log(FactY)) - 0.8752 * math.pow(math.log(FactY), 2) + 0.01853 * math.pow((math.log(FactY)), 4))
        else :
            FactS =math.log(FactY) / (-0.0523 + 3.18 *math.log(FactY) - 0.872 * math.pow((math.log(FactY)), 2) + 0.01853 * math.pow((math.log(FactY)), 4))  
        FNS = 0.0056 + 0.5 / math.pow(ReynoldsNo, 0.32) 
        FTP = math.exp(FactS) 
        FrictionFactor = FTP * FNS         
        if gas_Oil_Ratio <= RsCalc:  
            FrictionFactor = 64 / ReynoldsNo 
            LiqDensity = (oil_Density * (1-water_Cut/100)) + (water_Density * water_Cut/100) 
            LiquidVelocity = 0.0119 * ((oil_Rate / Bo) + (water_Rate / Bw)) / math.pow(tbg_Dia, 2) 
            DPDLEL = (LiqDensity * math.sin(deviation_Angle * math.pi / 180)) / 144 
            DPDLFriction = (1.294 * math.pow(10, -3) * FrictionFactor * LiqDensity * math.pow(LiquidVelocity, 2)) / tbg_Dia 
            DPDL = DPDLEL + DPDLFriction
            FlowRegime = "Single_Phase"                   
        else:            
            DPDLEL = NoslipmixerDensity * math.sin((90 - deviation_Angle) * math.pi / 180) / 144 
            DPDLFriction = 1.294 * math.pow(10, -3) * EnergyFactor * NoslipmixerDensity * math.pow(Mixer_Velocity, 2)*144  / tbg_Dia 
            DPDL = (DPDLEL + DPDLFriction) 
            FlowRegime = "Multi_Phase"

        average_Temp = average_Temp + (AssumeDepth * math.sin((90 - deviation_Angle) * math.pi / 180) * temp_Gradient)                 
        presssure.append(th_Pres)
        depth.append(cumMD)
        th_Pres  = th_Pres+ DPDL* AssumeDepth
        cumMD = cumMD + AssumeDepth
       # print(FlowRegime, th_Pres, DPDL, deviation_Angle)
        if cumMD > well_Depth:
            AssumeDepth = well_Depth-cumMD
        if cumMD > well_Depth:
            break

    return presssure, depth

def Duns_Ros(well_Depth,res_Temp, tbg_Dia, liquid_Rate, water_Cut, gas_Oil_Ratio, th_Pres, th_Temp, oil_API, spgr_Water, spgr_Gas,wat_Salility, moleH2S,moleCO2 ):
    TbgRoughness =0.00015
    oil_Rate = liquid_Rate *(1-water_Cut/100)
    water_Rate =liquid_Rate *water_Cut/100
    gas_Rate = oil_Rate * gas_Oil_Ratio
    tpc = 168 + (325 * spgr_Gas - 12.5 * math.pow(spgr_Gas, 2))
    ppc = 677 + (15 * spgr_Gas - 37.5 * math.pow(spgr_Gas, 2))
    A = (moleH2S + moleCO2)
    spgr_Oil = 141.5/(131.5+oil_API)
    epsilon = 120 * (math.pow(A, 0.9) - math.pow(A, 1.6)) + 15 * (math.pow(moleH2S, 0.5) - math.pow(moleH2S, 4))
    area_tubing= math.pi * (math.pow((tbg_Dia / 12), 2)) / 4
    temp_Gradient = (res_Temp - th_Temp) / well_Depth
    average_Temp= (res_Temp + th_Temp)/2
    presssure=[] 
    depth=[]
    AssumeDepth=well_Depth/100
    cumMD = AssumeDepth
    for i in range(100):
        if th_Pres <3977:
            confact =1 - 0.024 * math.pow(th_Pres, 0.45)
        else:
            confact =1.0
        if th_Temp <= 68:
            sigma_Oil = 39 - (0.257 * oil_API * confact) 
        elif th_Temp > 100:
            sigma_Oil =37.5 - 0.257 * oil_API * confact
        else:            
            sigma_Oil = confact * (((39 - 0.257 * oil_API)) + (((37.5 - 0.257 * oil_API)) - ((39 - 0.257 * oil_API))) * (th_Temp - 68) / 32) 
        
        sigma_Water = (-9 * math.pow(10, -5) * th_Temp + 0.0815) * 1000
        sigma_Liquid = (sigma_Oil * (1-water_Cut/100)) + (sigma_Water * water_Cut/100) 
        deviation_Angle =90
        Xva = 0.0125 * oil_API - 0.00091 * average_Temp
        RsCalc = spgr_Gas * math.pow((((th_Pres / 18.2) + 1.4) * math.pow(10, Xva)), 1.2048)    
        Bo = 0.9759 + 0.00012 * math.pow((RsCalc * math.pow((spgr_Gas / spgr_Oil), 0.5) + 1.25 * average_Temp), 1.2)
        Aval = (0.00091 * average_Temp) - (0.0125 * oil_API) 
        PB = 18.2 * (math.pow((RsCalc / spgr_Gas), 0.83) * math.pow(10, Aval) - 1.4)
        Z=calculate_z(spgr_Gas, th_Pres, th_Temp)
        Gasspecificweight = (spgr_Gas * 0.0764 * th_Pres * 520) / (14.7 * (average_Temp + 460) * Z)
        Bg = 0.02829 * Z * th_Temp / th_Pres
        spgr_Water = 1 + wat_Salility / 1000000
        Bw = 1 + (1.21 * math.pow(10, -4) * (th_Temp - 60)) + (math.pow(10, -6) * math.pow((th_Temp - 60), 2)) - (3.33 * math.pow(10, -6) * th_Pres)
        saturated_oil_viscosity, dead_viscosity = calculate_oil_viscosity_Beggs(oil_API, th_Temp, RsCalc)
        if th_Pres > PB :
            oil_Viscosity = saturated_oil_viscosity             
        else:           
            afactor=3.9*math.pow(10,-5)*math.pow(th_Pres,-5)
            mfactor = 2.6*math.pow(th_Pres, 1.187)* math.pow(10,afactor)
            oil_Viscosity= saturated_oil_viscosity * math.pow(th_Pres/PB, mfactor) 
        water_Viscosity = math.exp(1.003 - (1.479 * math.pow(10, -2) * average_Temp) + (1.982 * math.pow(10, -5) * math.pow(average_Temp, 2))) 
        molecular_Weight = 29 * spgr_Gas 
        GasVisK = (9.379 + 0.01607 * (molecular_Weight)) * math.pow((average_Temp + 460), 1.5) / (209.2 + (19.26 * molecular_Weight) + (average_Temp + 460)) 
        GasVisX = 3.448 + (986.4 / (average_Temp + 460)) + (0.01009 * molecular_Weight) 
        GasVisY = 2.447 - 0.2224 * GasVisX 
        gas_FVF = 0.0283 * Z * (average_Temp + 460) / th_Pres 
        oil_Density = (350 * spgr_Oil + (0.0764 * RsCalc * spgr_Gas)) / (5.615 * Bo) 
        gas_Density = 0.0433 * spgr_Gas * th_Pres / (Z * (average_Temp + 460)) 
        water_Density = 350.4 * spgr_Water / (5.615 * Bw) 
        FactYY = math.pow(gas_Density, GasVisY) 
        gas_Viscosity = 0.0001 * GasVisK * math.exp(GasVisX * FactYY) 
        liquid_Density = (oil_Density * (1 - water_Cut/100) ) + (water_Density * water_Cut/100) 
        liquid_Viscosity = oil_Viscosity * (1 - water_Cut/100)  + water_Viscosity * water_Cut/100 
        Superficial_GasVelocity = 1.16 * math.pow(10, -5) * oil_Rate * (gas_Oil_Ratio - RsCalc) * gas_FVF / area_tubing 
        Superficial_LiquidVelocity = 6.5 * math.pow(10, -5) * (oil_Rate * Bo + water_Rate * Bw) / area_tubing  
        Mixer_Velocity = Superficial_GasVelocity + Superficial_LiquidVelocity 
        NRE = 124 * liquid_Density * Superficial_LiquidVelocity * tbg_Dia / liquid_Viscosity
        ReynoldsNo = 124 * (liquid_Density * tbg_Dia * Mixer_Velocity) / liquid_Viscosity
        MoodyFrictionFactor = 64 / ReynoldsNo
        NLV = 1.938 * Superficial_LiquidVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        NFR = 0.373 * math.pow(Mixer_Velocity, 2) / tbg_Dia
        NGV = 1.938 * Superficial_GasVelocity * math.pow((liquid_Density / sigma_Liquid), 0.25)
        VB = 0.79 * math.pow(((sigma_Liquid * (liquid_Density - gas_Density)) / math.pow(liquid_Density, 2)), 0.25)
        VG = Mixer_Velocity + VB
        GasHoldup = Superficial_GasVelocity / (Mixer_Velocity + VB)
        LiquidHoldup = 1 - GasHoldup
        MixerDensity = liquid_Density * LiquidHoldup + gas_Density * (1 - LiquidHoldup)
        liquid_Velocity = 0.0119 * ((oil_Rate / Bo) + (water_Rate / Bw)) / (math.pow(tbg_Dia, 2)) 
        SlipVelocity = VG - liquid_Velocity 
        ND = 10.1 * tbg_Dia * math.pow((liquid_Density / sigma_Liquid), 0.5) 
        NL = 0.1573 * liquid_Viscosity * math.pow((1 / (liquid_Density * math.pow(sigma_Liquid, 3))), 0.25) 
        GasliquidratioCorrectionfactor = (MoodyFrictionFactor * Superficial_GasVelocity * math.pow(ND, (2 / 3))) / Superficial_LiquidVelocity 
        if ND>=70:
            L2=1.0
        elif ND<=30:
            L2 =2 
        else:
            L2= 33.354 * math.pow(ND, -0.835)
    
        if ND>=70:
            L1=1.1        
        else:
            L1 = 0.0949 * math.pow(ND, 0.5987) 
        NGVBS = L1 + L2 * NLV 
        NGVST = 50 + 36 * NLV 
        NGVTM = 75 + 84 * math.pow(NLV, 0.75) 
        if gas_Oil_Ratio <= RsCalc:
            DPDLEL = (liquid_Density * math.sin(deviation_Angle * math.pi / 180)) / 144 
            DPDLFriction = (1.294 * math.pow(10, -3) * MoodyFrictionFactor * liquid_Density * math.pow(liquid_Density, 2)) / tbg_Dia 
            DPDL = DPDLEL + DPDLFriction
            FlowRegime = "Single_Phase"  
        elif NGV >= NGVBS and NGV <= NGVST:
            FlowRegime = "Slug";
            if (NL <= 0.1) :
                F5 = -0.038 * math.log(NL) - 0.0083
            elif (NL >= 0.2):
                F5 = 0.0301 * math.log(NL) + 0.0941
            if (NL <= 0.02):
                F6 = 4410.4 * math.pow(NL, 2) - 132.28 * NL + 0.7376   
            elif (NL >= 0.02 and NL <= 0.2):
                F6 = 44.594 * math.pow(NL, 1.3244)  
            elif (NL >= 0.2):
                F6 = 1.5662 * math.pow(NL, -0.175)
            F7 = 0.0209 * math.pow(NL, -0.306)
            DerF6 = 0.029 * ND + F6 
            Sslug = (1 + F5) * (math.pow(NGV, 0.982) + DerF6) / math.pow((1 + F7 * NLV), 2) 
            SlipVelocity = 0.52 * Sslug * math.pow((sigma_Liquid / liquid_Density), 0.25) 
            LiquidHoldup = (SlipVelocity - Mixer_Velocity + math.pow((math.pow((Mixer_Velocity - SlipVelocity), 2) + 4 * SlipVelocity * Superficial_LiquidVelocity), 0.5)) / (2 * SlipVelocity);
            MixerDensity = liquid_Density * LiquidHoldup + Gasspecificweight * (1 - LiquidHoldup) 
            DPDLEL = liquid_Density * math.sin(deviation_Angle * math.pi / 180) / 144 
            if (GasliquidratioCorrectionfactor > 100):
                FrictionFactorF2 = 0.21 
            elif (GasliquidratioCorrectionfactor < 100 and GasliquidratioCorrectionfactor > 0.2):
                FrictionFactorF2 = 0.748 * math.pow(GasliquidratioCorrectionfactor, -0.31) 
            elif (GasliquidratioCorrectionfactor <= 0.2):
                FrictionFactorF2 = 1.0021 * math.exp(GasliquidratioCorrectionfactor * 0.4358) 
            FrictionFactorF3 = 1 + (MoodyFrictionFactor / 4) * math.pow((Superficial_GasVelocity / (50 * Superficial_LiquidVelocity)), 0.5) 
            FrictionFactor = MoodyFrictionFactor * (FrictionFactorF2 / FrictionFactorF3)            
            DPDLFriction = 1.294 * math.pow(10, -3) * (FrictionFactor * liquid_Density * math.pow(Superficial_LiquidVelocity, 2) / tbg_Dia) * (1 + (Superficial_GasVelocity / Superficial_LiquidVelocity)) 
            DPDL = (DPDLEL + DPDLFriction) 
        elif NGV>NGVTM:
            FlowRegime = "Mist";
            NoSlipLiquidHoldup = Superficial_LiquidVelocity / Mixer_Velocity;
            MixerDensity = liquid_Density * NoSlipLiquidHoldup + gas_Density * (1 - NoSlipLiquidHoldup);
            NREG = 124 * gas_Density * Superficial_GasVelocity * tbg_Dia / gas_Viscosity;
            NWe = gas_Density * math.pow(Superficial_GasVelocity, 2) * TbgRoughness / sigma_Liquid;
            NMu = math.pow(liquid_Viscosity, 2) / liquid_Density * sigma_Liquid * TbgRoughness;
            if (NWe * NMu <= 0.005):
                K = 0.07498 * sigma_Liquid / (gas_Density * math.pow(Superficial_GasVelocity, 2) * tbg_Dia)
            elif (NWe * NMu >= 0.005):
                K = (0.3731 * sigma_Liquid * math.pow((NWe * NMu), 0.302)) / (gas_Density * math.pow(Superficial_GasVelocity, 2) * tbg_Dia)
            
            FrictionFactor = 4 * (1 / math.pow((4 * math.log(0.027 * K)), 2) + 0.067 * math.pow(K, 1.73))         
            DPDLFriction = 1.294 * math.pow(10, -3) * (FrictionFactor * gas_Density * math.pow(Superficial_GasVelocity, 2) / tbg_Dia)
            EK = (liquid_Density * Superficial_LiquidVelocity + gas_Density * Superficial_GasVelocity) * Superficial_GasVelocity / (144 * th_Pres * 32.17) 
            DPDLEL = MixerDensity * math.sin(deviation_Angle * math.pi / 180) / 144 
            DPDL = (DPDLEL + DPDLFriction) / (1 - EK) 
        elif (NGV >= 0 and NGV <= NGVBS):
            FlowRegime = "Bubble"
            if NL <= 0.02:
                F1=1.4
                F2=0.25
            else:
                F1 = 17.027 * math.pow(NL, 6) + 79.673 * math.pow(NL, 5) - 145.08 * math.pow(NL, 4) + 130.49 * math.pow(NL, 3) - 60.17 * math.pow(NL, 2) + 12.108 * NL + 1.2007 
                F2 = 17.887 * math.pow(NL, 6) + 82.136 * math.pow(NL, 5) - 147 * math.pow(NL, 4) + 130.07 * math.pow(NL, 3) - 58.87 * math.pow(NL, 2) + 12.221 * NL + 0.1553 
            F3 = 5.0193 * math.pow(NL, 0.2758)
            if NL>0.8:
                F4=56
            else:
                F4=18.014 * math.log(NL) + 104.97
            DerF3 = F3 - F4 / ND
            MoodyFrictionFactor = 64 / NRE;
            GasliquidratioCorrectionfactor = (MoodyFrictionFactor * Superficial_GasVelocity * math.pow(ND, (2 / 3))) / Superficial_LiquidVelocity 
            if (GasliquidratioCorrectionfactor > 100):
                FrictionFactorF2 = 0.21
            elif (GasliquidratioCorrectionfactor < 100 and GasliquidratioCorrectionfactor > 0.2):
                FrictionFactorF2 = 0.748 * math.pow(GasliquidratioCorrectionfactor, -0.31)
            elif (GasliquidratioCorrectionfactor <= 0.2):
                FrictionFactorF2 = 1.0021 * math.exp(GasliquidratioCorrectionfactor * 0.4358)
            FrictionFactorF3 = 1 + (MoodyFrictionFactor / 4) *math.pow((Superficial_GasVelocity / (50 * Superficial_LiquidVelocity)), 0.5) 
            FrictionFactor = MoodyFrictionFactor * (FrictionFactorF2 / FrictionFactorF3)               
            DPDLFriction = 1.294 * math.pow(10, -3) * (FrictionFactor * liquid_Density * math.pow(Superficial_LiquidVelocity, 2) / tbg_Dia)
            DPDLEL = MixerDensity * math.sin(deviation_Angle * math.pi / 180) / 144 
            DPDL = (DPDLEL + DPDLFriction) 
        else:            
            FlowRegime = "Transition"
            if (NL <= 0.1):            
                F5 = -0.038 * math.log(NL) - 0.0083
            elif (NL >= 0.2):
                F5 = 0.0301 * math.log(NL) + 0.0941 
            if (NL <= 0.02):
                F6 = 4410.4 * math.pow(NL, 2) - 132.28 * NL + 0.7376    
            elif (NL >= 0.02 & NL <= 0.2):
                F6 = 44.594 * math.pow(NL, 1.3244) 
            elif (NL >= 0.2):
                F6 = 1.5662 *math.pow(NL, -0.175)  
            F7 = 0.0209 * math.pow(NL, -0.306) 
            DerF6 = 0.029 * ND + F6 
            Sslug = (1 + F5) * (math.pow(NGV, 0.982) + DerF6) / math.pow((1 + F7 * NLV), 2) 
            SlipVelocity = 0.52 * Sslug * math.pow((sigma_Liquid / liquid_Density), 0.25) 
            LiquidHoldup = (SlipVelocity - Mixer_Velocity + math.pow((math.pow((Mixer_Velocity - SlipVelocity), 2) + 4 * SlipVelocity * Superficial_LiquidVelocity), 0.5)) / (2 * SlipVelocity);
            DPDLEL = MixerDensity * math.sin(deviation_Angle * math.pi / 180) / 144 
            MoodyFrictionFactor = 64 / NRE 
            GasliquidratioCorrectionfactor = (MoodyFrictionFactor * Superficial_GasVelocity * math.pow(ND, (2 / 3))) / Superficial_LiquidVelocity;
            if (GasliquidratioCorrectionfactor > 100):
                FrictionFactorF2 = 0.21 
            elif (GasliquidratioCorrectionfactor < 100 and GasliquidratioCorrectionfactor > 0.2):
                FrictionFactorF2 = 0.748 * math.pow(GasliquidratioCorrectionfactor, -0.31) 
            elif (GasliquidratioCorrectionfactor < 0.2):
                FrictionFactorF2 = 1.0021 * math.exp(GasliquidratioCorrectionfactor * 0.4358) 
            FrictionFactorF3 = 1 + (MoodyFrictionFactor / 4) * math.pow((Superficial_GasVelocity / (50 * Superficial_LiquidVelocity)), 0.5) 
            FrictionFactor = MoodyFrictionFactor * (FrictionFactorF2 / FrictionFactorF3) 
            ReynoldsNo = 124 * (liquid_Density * tbg_Dia * Superficial_LiquidVelocity) / liquid_Viscosity 
            DPDLFriction = 1.294 * math.pow(10, -3) * (FrictionFactor * MixerDensity * math.pow(Superficial_LiquidVelocity, 2) / tbg_Dia) * (1 + Superficial_GasVelocity / Superficial_LiquidVelocity) 
            DPDLslug = (DPDLEL + DPDLFriction) 
            NoSlipLiquidHoldup = Superficial_LiquidVelocity / Mixer_Velocity 
            #MixerDensity = LiqDensity * NoSlipLiquidHoldup + GasDensity * (1 - NoSlipLiquidHoldup) 
            NREG = 124 * gas_Density * Superficial_GasVelocity * tbg_Dia / gas_Viscosity 
            NWe = gas_Density * math.pow(Superficial_GasVelocity, 2) * TbgRoughness / sigma_Liquid 
            NMu = math.pow(liquid_Viscosity, 2) / liquid_Density * sigma_Liquid * TbgRoughness 
            if (NWe * NMu <= 0.005):
                K = 0.07498 * sigma_Liquid / (gas_Density * math.pow(Superficial_GasVelocity, 2) * tbg_Dia) 
            elif (NWe * NMu > 0.005):
                K = (0.3731 * sigma_Liquid * math.pow((NWe * NMu), 0.302)) / (gas_Density * math.pow(Superficial_GasVelocity, 2) * tbg_Dia) 
            FrictionFactor = 4 * (1 / math.pow((4 * math.log(0.27 * K)), 2) + 0.067 * math.pow(K, 1.73));
            DPDLFriction = 1.294 * math.pow(10, -3) * FrictionFactor * liquid_Density * math.pow(Superficial_LiquidVelocity, 2) / tbg_Dia * (1 + Superficial_GasVelocity / Superficial_LiquidVelocity) 
            EK = (liquid_Density * Superficial_LiquidVelocity + gas_Density * Superficial_GasVelocity) * Superficial_GasVelocity / (144 * th_Pres * 32.17) 
            DPDLmist = (DPDLEL + DPDLFriction) / (1 - EK);
            B = ((75 + 84 * math.pow(NLV, 0.75)) - NGV) / ((75 + 84 * math.pow(NLV, 0.75)) - (50 + 36 * NLV)) 
            DPDL = B * DPDLslug + (1 - B) * DPDLmist 

        average_Temp = average_Temp + (AssumeDepth * math.sin((90 - deviation_Angle) * math.pi / 180) * temp_Gradient)                 
        presssure.append(th_Pres)
        depth.append(cumMD)
        th_Pres  = th_Pres+ DPDL* AssumeDepth
        cumMD = cumMD + AssumeDepth       
        if cumMD > well_Depth:
            AssumeDepth = well_Depth-cumMD
        if cumMD > well_Depth:
            break

    return presssure, depth
