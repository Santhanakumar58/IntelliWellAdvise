from turtle import color
import matplotlib.pyplot  as plt
import matplotlib  as mpl
import base64
from io import BytesIO
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from matplotlib.ticker import NullFormatter
from matplotlib.dates import MonthLocator, DateFormatter
import numpy as np
import math
import datetime
from scipy.optimize import curve_fit
import pandas as pd
from shapely.geometry import linestring
from blackoilpvt.models import BlackoilPVT
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity, get_Rs
from perforations.models import PerforationModel
from selectedOilProducer.models import SelectedOilProducer
from opinflow.models import ProductivityIndexModel, DarcyModel, WigginsModel, VogelModel, StandingsModel, MultirateModel
from opinflow.utility import draw_CompositePR_PI, draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,z, y1,y2,y3, y4):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,6))    
    figure, axis = plt.subplots(2, 2)
    figure.set_size_inches(12, 8)
    axis[0,1].plot(x, y, color='red', label = 'Gas Rate')    
    axis[0,1].set_title("Gas Rate")
    axis[0,1].set_xlabel('Date')
    axis[0,1].set_ylabel('Gas Rate scf/day')     
    axis[0,1].xaxis.set_major_locator(MonthLocator(interval=1))
    axis[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%b%y'))
    for label in axis[0,1].get_xticklabels():
        label.set_rotation(45) 

    axis[0,0].plot(x, y1, color='green', label = 'oil')
    axis[0,0].plot(x, y2, color='cyan', label = 'water')
    axis[0,0].plot(x, y3, color='red', label = 'liquid')
    axis[0,0].set_title("Liquid Rates") 
    axis[0,0].set_xlabel('Date')
    axis[0,0].set_ylabel('Liquid Rate Bbls/day')    
    axis[0,0].legend()  
    axis[0,0].xaxis.set_major_locator(MonthLocator(interval=1))
    axis[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%b%y'))
    for label in axis[0,0].get_xticklabels():
        label.set_rotation(45) 

    axis[1,1].plot(x, z, color='red', label = 'GOR')   
    axis[1,1].set_title("Gas Oil Ratio") 
    axis[1,1].set_xlabel('Date')
    axis[1,1].set_ylabel('GOR scf/bbl')   
    axis[1,1].xaxis.set_major_locator(MonthLocator(interval=1))
    axis[1,1].xaxis.set_major_formatter(mdates.DateFormatter('%b%y'))
    for label in axis[1,1].get_xticklabels():
        label.set_rotation(45) 
    
    axis[1,0].plot(x, y4, color='green', label = 'Water Cut %')   
    axis[1,0].set_title("Water Cut") 
    axis[1,0].set_xlabel('Date')
    axis[1,0].set_ylabel('Water Cut %')     
    axis[1,0].xaxis.set_major_locator(MonthLocator(interval=1))
    axis[1,0].xaxis.set_major_formatter(mdates.DateFormatter('%b%y'))
    for label in axis[1,0].get_xticklabels():
        label.set_rotation(45) 


    figure.tight_layout()
    axis[0,0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[0,1].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[1,0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[1,1].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph


def get_ipr_plot(df, espdata, x1, y1):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(8,6))    
    plt.subplot(1,1,1)
    plt.subplot(1,1,1)
   
    #plt.plot(df["x1"], df['y1'],  label='Outflow', color = "r")
    plt.plot(x1, y1,  label='Outflow', color = "r", linestyle="dotted")
    plt.plot(df["x2"], df['y2'],  label='Inflow', color = "g")

    #x2,y2=intersection(df["x1"], df['y1'], df["x2"], df['y2'] )
    

    #plt.scatter(pdrop.liquid_Rate, pdrop.th_Pres)
    #plt.scatter(x2[-1],y2[-1], s=30, color="blue")
    #xx=[x2[-1],x2[-1],0]
    #yy=[0,y2[-1],y2[-1]]
    #plt.plot(xx,yy, color="black" ,linestyle="dotted")
    #xxx2 = round(x2[-1])
    #yyy2 = round(y2[-1])
    #plt.text(x2[-1],y2[-1], f"Intersection Point {xxx2} , {yyy2}")
    
    plt.xlabel('Liquid Rate BOPD')
    plt.ylabel('Pressure in psi')
    plt.legend(loc="upper right")    
    plt.title("Inflow-outflow Plot")
    plt.ylim(0, max(df['y2'])+250)
    plt.xlim(0, max(df["x2"]) + 250)
    
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_esp_plot( q,q1,q2, h,eff, power):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,6))      
    plt.plot(q, h, color='b', label = 'Head')  
    plt.plot(q1, eff, color='g', label = 'Efficiency')  
    plt.plot(q2, power, color='red', label = 'Power')    
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_esp_plot1( q,q1,q2, h,eff, power, rangex, rangey, pump_name):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8)) 
    
    fig, ax1 = plt.subplots()
    fig.subplots_adjust(right=0.7) 
    ax1.set_xlabel('Flow Rate Bbls/day') 
    ax1.set_ylabel('Head (ft)', color = 'blue') 
    ax1.plot(q, h, color = 'blue')    
    ax1.plot(rangex, rangey, color="black")
    ax1.tick_params(axis ='y', labelcolor = 'blue')
    plt.ylim(0,50)
    plt.fill_between(rangex,rangey, alpha=0.3)
    ax2 = ax1.twinx()   
    ax2.set_ylabel('Efficiency (%)', color = 'green') 
    ax2.plot(q1, eff, color = 'green') 
    ax2.tick_params(axis ='y', labelcolor = 'green') 
    plt.ylim(0,70)

    
    ax3 = ax1.twinx()   
    ax3.set_ylabel('Power (Hp)', color = 'red') 
    ax3.plot(q2, power, color = 'red') 
    ax3.tick_params(axis ='y', labelcolor = 'red') 
    plt.ylim(0,0.7)
    rspine = ax3.spines['right']
    rspine.set_position(('axes', 1.15))
    plt.title(f"Pump Performance Curve for {pump_name} ")
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_esp_plot2( q, h, pump_name,  h11, h12, q11, q12, hz, bestEffrate,bestEffhead, berate, behead,minimumrate, minimumhead, maximumrate, maximumhead):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,6))     
    fig, ax1 = plt.subplots()
    fig.subplots_adjust(right=0.7) 
    ax1.set_xlabel('Flow Rate Bbls/day') 
    ax1.set_ylabel('Head (ft)', color = 'blue')      
    ax1.plot(q11, h11, color = 'green', label="50 Hz")  
    ax1.plot(q, h, color = 'blue', label= "60 Hz")   
    ax1.plot(q12, h12, color = 'red', label= "70 Hz")   
    ax1.plot(bestEffrate, bestEffhead, color = 'green', label="Best Efficiency")   
    ax1.plot(maximumrate, maximumhead, color = 'blue') 
    ax1.plot(minimumrate, minimumhead, color = 'blue') 
    plt.ylim(0,70)
    plt.xlim(0,1400)
    plt.grid(linestyle='-')
    plt.legend()     
    plt.title(f"Head curve for different frequencies for {pump_name} ")
    plt.tight_layout()
    graph = get_graph()
    return graph
   
def calculate_esp_parameters(selectedwell,design_Liquid, oil, water,gas,gor, pvt_Well,th_pres, th_temp, respres,min_pwf,water_spgr, pump_depth ):  
    pvt = BlackoilPVT.objects.filter(wellName =pvt_Well).last()
    temperature = pvt.reservoirTemperature
    oil_grav = pvt.oilAPIgravity
    solutiongas = pvt.solutionGOR
    gas_grav = pvt.gasGravity    
    oil_spgr = 141.5/(oil_grav+ 131.5) 
    Pb = get_Pb(pvt)
    rs=get_Rs(pvt)
    vis=get_Viscosity(pvt) 
    perfortaions = PerforationModel.objects.filter(wellid=selectedwell.wellid).all().order_by('-perf_Top') 
    perforation = perfortaions.first()
    midperf = (perforation.perf_Top + perforation.perf_Bottom)/2
    temp_grad = (temperature-th_temp)/midperf
    avg_temp = (temperature-th_temp)/2  
    C=120
    pip=860
    pipe_id= 2.992  
    composite_spgr =0.997    
    totalmass = (((oil*oil_spgr)+(water*water_spgr))*5.6146*62.4) +(gor*oil*gas_grav *0.0752)
    #composite_spgr = totalmass/(self.design_Liquid*5.6146*62.4)
    pip_depth = pip/(0.433*composite_spgr) 
    HL = pump_depth - pip_depth 
    friction_per1000ft = 15.11*math.pow((design_Liquid/C),1.852)/math.pow(pipe_id, 4.8655)
    friction_head =friction_per1000ft * pump_depth/1000
    Hwh = th_pres/(0.433*composite_spgr)
    tdh = HL+friction_head +Hwh  
    print(HL,friction_head ,Hwh , tdh, composite_spgr) 
    return tdh  

def find_power_when_tdh_is_given (tdh, power, given_tdh):
    i=0
    prevpow=0
    prevtdh=0
    for x in tdh:       
        if x >=  given_tdh:
            calcpow = prevpow +((power[i]-prevpow)/(x-given_tdh))             
            break
        else:
            prevpow=power[i]
            prevtdh=x
            i=i+1            
    return round(calcpow+0.5)

def calculate_inflow(espdata):
    selectedwell = SelectedOilProducer.objects.first()   
    inflowdf = pd.DataFrame()  
    if selectedwell.inflow =='PI':        
        pimodels = ProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        chart,xc,y, pis = draw_CompositePR_PI(pimodels)   
        #print(pis)    
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
        if espdata.design_Liquid > row['x2'] :      
           x1 = [espdata.design_Liquid,espdata.design_Liquid,0 ]
           y1 = [0,row['y2'],row['y2'] ] 
           pwf_inflow=row['y2']     
           break
    #chart = get_ipr_plot(inflowdf, espdata, x1, y1)
    pip = pwf_inflow
    return inflowdf, x1, y1, pip
  
def Generate_pump_curves(espdata):
    selectedwell = SelectedOilProducer.objects.first()  
    berate =0
    behead =0
    bepower =0
    beeff =0
    hz =0
    minrate =0
    maxrate=0
    rangex = []
    rangey =[]
    q=[]
    head=[]
    q1=[]
    eff=[]
    q2=[]
    power=[]
    q11=[]
    q12=[]
    h11=[]
    h12=[]
    pump_name = espdata.pump
    if espdata.pump =='400-D800N-60Hz-250-1150bpd': 
        q=[37.229,57.801,78.369,98.936,119.504,140.068,160.637,181.204,201.766,222.33,242.892,263.455,284.018,304.579,325.139,345.7,366.259,386.816,407.375,427.934,448.488,	469.042,489.596,	511.64,	530.705,	551.257,	571.81,	592.359,	612.909,	633.458,	654.005,	674.551,	695.097,	715.642,	736.183,	756.724,	777.263,	797.788, 818.311,	838.828,	859.343,	879.855,	900.362,	920.867,	941.367,	961.865,	982.359,	1002.852,	1023.335,	1043.822,	1064.301,	1084.779,	1105.255,	1125.726,	1146.195,	1166.66,	1187.121,	1206.652,	1226.18,	1245.706,	1264.296,	1282.886,	1300.543,	1316.34,	1330.257,	1351.148,	1363.722,	1380.444,	1393.484]
        head=[40.121,	40.122,	40.086,	40.037,	40.005,	39.924,	39.902,	39.852,	39.757,	39.68,	39.585,	39.508,	39.413,	39.309,	39.2,	39.092,	38.969,	38.824,	38.702,	38.57,	38.402,	38.23,	38.052,	38.002,	37.712,	37.522,	37.335,	37.113,	36.895,	36.677,	36.436,	36.182,	35.923,	35.664,	35.359,	35.064,	34.736,	34.277,	33.799,	33.258,	32.703,	32.112,	31.475,	30.819,	30.114,	29.391,	28.617,	27.843,	26.97,	26.132,	25.227,	24.298,	23.361,	22.364,	21.353,	20.307,	19.214,	18.169,	17.103,	16.012,	14.906,	13.811,	12.736,	11.75,	10.676,	9.874,	8.727,	7.65,	7.152]

        q1= [27.165,	37.579,	47.042,	56.506,	66.908,	78.245,	89.602,	100.937,	112.264,	124.534,	136.804,	149.069,	162.277,	175.479,	188.674,	201.871,	216.004,	232.017,	248.967,	265.911,	282.853,	299.788,	317.663,	337.409,	358.092,	378.767,	399.437,	420.102,	440.764,	461.417,	482.065,	502.713,	523.351,	543.986,	564.615,	585.242,	605.864,	626.478,	647.091,	667.698,	688.303,	708.901,	729.498,	750.088,	770.676,	791.253,	811.823,	832.384,	852.934,	873.474,	894.005,	914.53,	935.045,	955.553,	976.052,	996.544,	1017.027,	1037.503,	1057.973,	1077.506,	1096.101,	1114.692,	1132.349,	1149.07,	1164.865,	1181.571,	1198.285,	1213.133,	1227.979,	1241.893,	1255.807,	1269.716,	1282.694,	1295.671,	1308.645,	1321.617,	1334.584,	1346.625,	1357.737,	1368.848,	1379.957,	1392.002]
        eff=[7.602,	9.371,	10.926,	12.494,	14.09,	15.7,	17.567,	19.142,	20.612,	22.189,	23.761,	25.259,	26.878,	28.407,	29.846,	31.305,	32.774,	34.383,	36.03,	37.576,	39.115,	40.536,	42.032,	43.542,	45.079,	46.508,	47.873,	49.155,	50.399,	51.528,	52.581,	53.634,	54.552,	55.414,	56.205,	56.971,	57.667,	58.261,	58.822,	59.314,	59.767,	60.132,	60.483,	60.739,	60.963,	61.04,	61.022,	60.863,	60.571,	60.132,	59.578,	58.922,	58.145,	57.266,	56.266,	55.163,	53.947,	52.628,	51.219,	49.792,	48.315,	46.795,	45.289,	43.765,	42.361,	40.64,	39.021,	37.456,	35.866,	34.319,	32.764,	31.146,	29.589,	28.023,	26.396,	24.76,	23.053,	21.457,	19.957,	18.435,	16.901,	15.363]

        q2 =[28.656,	49.268,	69.879,	90.49,	111.102,	131.712,	152.323,	172.935,	193.544,	214.155,	234.764,	255.374,	275.985,	296.593,	317.202,	337.812,	358.42,	379.027,	399.636,	420.244,	440.853,	461.461,	482.067,	502.675,	523.283,	543.89,	564.497,	585.105,	605.71,	626.317,	646.924,	667.529,	688.136,	708.742,	729.348,	749.953,	770.559,	791.163,	811.768,	832.373,	852.977,	873.58,	894.184,	914.786,	935.389,	955.991,	976.594,	997.196,	1017.797,	1038.398,	1058.999,	1079.6,	1100.199,	1120.8,	1141.399,	1162,	1182.596,	1203.194,	1223.79,	1244.388,	1264.984,	1285.58,	1306.175,	1326.769,	1347.363,	1367.956,	1388.548,	1402.587]
        power = [0.153,	0.158,	0.164,	0.169,	0.175,	0.18,	0.186,	0.191,	0.196,	0.202,	0.207,	0.212,	0.217,	0.223,	0.228,	0.233,	0.238,	0.243,	0.248,	0.253,	0.258,	0.263,	0.268,	0.273,	0.278,	0.283,	0.288,	0.293,	0.297,	0.302,	0.307,	0.312,	0.317,	0.321,	0.326,	0.331,	0.335,	0.34,	0.344,	0.349,	0.354,	0.358,	0.362,	0.367,	0.371,	0.375,	0.379,	0.384,	0.388,	0.392,	0.396,	0.4,	0.404,	0.408,	0.411,	0.415,	0.419,	0.422,	0.426,	0.429,	0.433,	0.436,	0.439,	0.442,	0.445,	0.448,	0.451,	0.453]

        berate =790
        behead =34.69
        bepower =0.33
        beeff =61.06
        hz =60
        minrate =250
        maxrate=1150
        rangex = minrate,minrate,maxrate,maxrate
        rangey = 0,50,50,0
        pump_name = espdata.pump
    elif espdata.pump =='400-D1100-60Hz-400-1650bpd-154Hp':
         # to be Updated
        q=[37.229,57.801,78.369,98.936,119.504,140.068,160.637,181.204,201.766,222.33,242.892,263.455,284.018,304.579,325.139,345.7,366.259,386.816,407.375,427.934,448.488,	469.042,489.596,	511.64,	530.705,	551.257,	571.81,	592.359,	612.909,	633.458,	654.005,	674.551,	695.097,	715.642,	736.183,	756.724,	777.263,	797.788, 818.311,	838.828,	859.343,	879.855,	900.362,	920.867,	941.367,	961.865,	982.359,	1002.852,	1023.335,	1043.822,	1064.301,	1084.779,	1105.255,	1125.726,	1146.195,	1166.66,	1187.121,	1206.652,	1226.18,	1245.706,	1264.296,	1282.886,	1300.543,	1316.34,	1330.257,	1351.148,	1363.722,	1380.444,	1393.484]
        head=[40.121,	40.122,	40.086,	40.037,	40.005,	39.924,	39.902,	39.852,	39.757,	39.68,	39.585,	39.508,	39.413,	39.309,	39.2,	39.092,	38.969,	38.824,	38.702,	38.57,	38.402,	38.23,	38.052,	38.002,	37.712,	37.522,	37.335,	37.113,	36.895,	36.677,	36.436,	36.182,	35.923,	35.664,	35.359,	35.064,	34.736,	34.277,	33.799,	33.258,	32.703,	32.112,	31.475,	30.819,	30.114,	29.391,	28.617,	27.843,	26.97,	26.132,	25.227,	24.298,	23.361,	22.364,	21.353,	20.307,	19.214,	18.169,	17.103,	16.012,	14.906,	13.811,	12.736,	11.75,	10.676,	9.874,	8.727,	7.65,	7.152]

        q1= [27.165,	37.579,	47.042,	56.506,	66.908,	78.245,	89.602,	100.937,	112.264,	124.534,	136.804,	149.069,	162.277,	175.479,	188.674,	201.871,	216.004,	232.017,	248.967,	265.911,	282.853,	299.788,	317.663,	337.409,	358.092,	378.767,	399.437,	420.102,	440.764,	461.417,	482.065,	502.713,	523.351,	543.986,	564.615,	585.242,	605.864,	626.478,	647.091,	667.698,	688.303,	708.901,	729.498,	750.088,	770.676,	791.253,	811.823,	832.384,	852.934,	873.474,	894.005,	914.53,	935.045,	955.553,	976.052,	996.544,	1017.027,	1037.503,	1057.973,	1077.506,	1096.101,	1114.692,	1132.349,	1149.07,	1164.865,	1181.571,	1198.285,	1213.133,	1227.979,	1241.893,	1255.807,	1269.716,	1282.694,	1295.671,	1308.645,	1321.617,	1334.584,	1346.625,	1357.737,	1368.848,	1379.957,	1392.002]
        eff=[7.602,	9.371,	10.926,	12.494,	14.09,	15.7,	17.567,	19.142,	20.612,	22.189,	23.761,	25.259,	26.878,	28.407,	29.846,	31.305,	32.774,	34.383,	36.03,	37.576,	39.115,	40.536,	42.032,	43.542,	45.079,	46.508,	47.873,	49.155,	50.399,	51.528,	52.581,	53.634,	54.552,	55.414,	56.205,	56.971,	57.667,	58.261,	58.822,	59.314,	59.767,	60.132,	60.483,	60.739,	60.963,	61.04,	61.022,	60.863,	60.571,	60.132,	59.578,	58.922,	58.145,	57.266,	56.266,	55.163,	53.947,	52.628,	51.219,	49.792,	48.315,	46.795,	45.289,	43.765,	42.361,	40.64,	39.021,	37.456,	35.866,	34.319,	32.764,	31.146,	29.589,	28.023,	26.396,	24.76,	23.053,	21.457,	19.957,	18.435,	16.901,	15.363]

        q2 =[28.656,	49.268,	69.879,	90.49,	111.102,	131.712,	152.323,	172.935,	193.544,	214.155,	234.764,	255.374,	275.985,	296.593,	317.202,	337.812,	358.42,	379.027,	399.636,	420.244,	440.853,	461.461,	482.067,	502.675,	523.283,	543.89,	564.497,	585.105,	605.71,	626.317,	646.924,	667.529,	688.136,	708.742,	729.348,	749.953,	770.559,	791.163,	811.768,	832.373,	852.977,	873.58,	894.184,	914.786,	935.389,	955.991,	976.594,	997.196,	1017.797,	1038.398,	1058.999,	1079.6,	1100.199,	1120.8,	1141.399,	1162,	1182.596,	1203.194,	1223.79,	1244.388,	1264.984,	1285.58,	1306.175,	1326.769,	1347.363,	1367.956,	1388.548,	1402.587]
        power = [0.153,	0.158,	0.164,	0.169,	0.175,	0.18,	0.186,	0.191,	0.196,	0.202,	0.207,	0.212,	0.217,	0.223,	0.228,	0.233,	0.238,	0.243,	0.248,	0.253,	0.258,	0.263,	0.268,	0.273,	0.278,	0.283,	0.288,	0.293,	0.297,	0.302,	0.307,	0.312,	0.317,	0.321,	0.326,	0.331,	0.335,	0.34,	0.344,	0.349,	0.354,	0.358,	0.362,	0.367,	0.371,	0.375,	0.379,	0.384,	0.388,	0.392,	0.396,	0.4,	0.404,	0.408,	0.411,	0.415,	0.419,	0.422,	0.426,	0.429,	0.433,	0.436,	0.439,	0.442,	0.445,	0.448,	0.451,	0.453]

        berate =790
        behead =34.69
        bepower =0.33
        beeff =61.06
        hz =60
        minrate =250
        maxrate=1150
        rangex = minrate,minrate,maxrate,maxrate
        rangey = 0,50,50,0        

    elif espdata.pump =='400-D1050-60Hz-300-1650bpd-154Hp':
        # to be Updated
        q=[37.229,57.801,78.369,98.936,119.504,140.068,160.637,181.204,201.766,222.33,242.892,263.455,284.018,304.579,325.139,345.7,366.259,386.816,407.375,427.934,448.488,	469.042,489.596,	511.64,	530.705,	551.257,	571.81,	592.359,	612.909,	633.458,	654.005,	674.551,	695.097,	715.642,	736.183,	756.724,	777.263,	797.788, 818.311,	838.828,	859.343,	879.855,	900.362,	920.867,	941.367,	961.865,	982.359,	1002.852,	1023.335,	1043.822,	1064.301,	1084.779,	1105.255,	1125.726,	1146.195,	1166.66,	1187.121,	1206.652,	1226.18,	1245.706,	1264.296,	1282.886,	1300.543,	1316.34,	1330.257,	1351.148,	1363.722,	1380.444,	1393.484]
        head=[40.121,	40.122,	40.086,	40.037,	40.005,	39.924,	39.902,	39.852,	39.757,	39.68,	39.585,	39.508,	39.413,	39.309,	39.2,	39.092,	38.969,	38.824,	38.702,	38.57,	38.402,	38.23,	38.052,	38.002,	37.712,	37.522,	37.335,	37.113,	36.895,	36.677,	36.436,	36.182,	35.923,	35.664,	35.359,	35.064,	34.736,	34.277,	33.799,	33.258,	32.703,	32.112,	31.475,	30.819,	30.114,	29.391,	28.617,	27.843,	26.97,	26.132,	25.227,	24.298,	23.361,	22.364,	21.353,	20.307,	19.214,	18.169,	17.103,	16.012,	14.906,	13.811,	12.736,	11.75,	10.676,	9.874,	8.727,	7.65,	7.152]

        q1= [27.165,	37.579,	47.042,	56.506,	66.908,	78.245,	89.602,	100.937,	112.264,	124.534,	136.804,	149.069,	162.277,	175.479,	188.674,	201.871,	216.004,	232.017,	248.967,	265.911,	282.853,	299.788,	317.663,	337.409,	358.092,	378.767,	399.437,	420.102,	440.764,	461.417,	482.065,	502.713,	523.351,	543.986,	564.615,	585.242,	605.864,	626.478,	647.091,	667.698,	688.303,	708.901,	729.498,	750.088,	770.676,	791.253,	811.823,	832.384,	852.934,	873.474,	894.005,	914.53,	935.045,	955.553,	976.052,	996.544,	1017.027,	1037.503,	1057.973,	1077.506,	1096.101,	1114.692,	1132.349,	1149.07,	1164.865,	1181.571,	1198.285,	1213.133,	1227.979,	1241.893,	1255.807,	1269.716,	1282.694,	1295.671,	1308.645,	1321.617,	1334.584,	1346.625,	1357.737,	1368.848,	1379.957,	1392.002]
        eff=[7.602,	9.371,	10.926,	12.494,	14.09,	15.7,	17.567,	19.142,	20.612,	22.189,	23.761,	25.259,	26.878,	28.407,	29.846,	31.305,	32.774,	34.383,	36.03,	37.576,	39.115,	40.536,	42.032,	43.542,	45.079,	46.508,	47.873,	49.155,	50.399,	51.528,	52.581,	53.634,	54.552,	55.414,	56.205,	56.971,	57.667,	58.261,	58.822,	59.314,	59.767,	60.132,	60.483,	60.739,	60.963,	61.04,	61.022,	60.863,	60.571,	60.132,	59.578,	58.922,	58.145,	57.266,	56.266,	55.163,	53.947,	52.628,	51.219,	49.792,	48.315,	46.795,	45.289,	43.765,	42.361,	40.64,	39.021,	37.456,	35.866,	34.319,	32.764,	31.146,	29.589,	28.023,	26.396,	24.76,	23.053,	21.457,	19.957,	18.435,	16.901,	15.363]

        q2 =[28.656,	49.268,	69.879,	90.49,	111.102,	131.712,	152.323,	172.935,	193.544,	214.155,	234.764,	255.374,	275.985,	296.593,	317.202,	337.812,	358.42,	379.027,	399.636,	420.244,	440.853,	461.461,	482.067,	502.675,	523.283,	543.89,	564.497,	585.105,	605.71,	626.317,	646.924,	667.529,	688.136,	708.742,	729.348,	749.953,	770.559,	791.163,	811.768,	832.373,	852.977,	873.58,	894.184,	914.786,	935.389,	955.991,	976.594,	997.196,	1017.797,	1038.398,	1058.999,	1079.6,	1100.199,	1120.8,	1141.399,	1162,	1182.596,	1203.194,	1223.79,	1244.388,	1264.984,	1285.58,	1306.175,	1326.769,	1347.363,	1367.956,	1388.548,	1402.587]
        power = [0.153,	0.158,	0.164,	0.169,	0.175,	0.18,	0.186,	0.191,	0.196,	0.202,	0.207,	0.212,	0.217,	0.223,	0.228,	0.233,	0.238,	0.243,	0.248,	0.253,	0.258,	0.263,	0.268,	0.273,	0.278,	0.283,	0.288,	0.293,	0.297,	0.302,	0.307,	0.312,	0.317,	0.321,	0.326,	0.331,	0.335,	0.34,	0.344,	0.349,	0.354,	0.358,	0.362,	0.367,	0.371,	0.375,	0.379,	0.384,	0.388,	0.392,	0.396,	0.4,	0.404,	0.408,	0.411,	0.415,	0.419,	0.422,	0.426,	0.429,	0.433,	0.436,	0.439,	0.442,	0.445,	0.448,	0.451,	0.453]

        berate =790
        behead =34.69
        bepower =0.33
        beeff =61.06
        hz =60
        minrate =250
        maxrate=1150
        rangex = minrate,minrate,maxrate,maxrate
        rangey = 0,50,50,0
        pump_name = espdata.pump

    elif espdata.pump =='400-D1750-60Hz-300-1650bpd-154Hp':
        # to be Updated
        q=[37.229,57.801,78.369,98.936,119.504,140.068,160.637,181.204,201.766,222.33,242.892,263.455,284.018,304.579,325.139,345.7,366.259,386.816,407.375,427.934,448.488,	469.042,489.596,	511.64,	530.705,	551.257,	571.81,	592.359,	612.909,	633.458,	654.005,	674.551,	695.097,	715.642,	736.183,	756.724,	777.263,	797.788, 818.311,	838.828,	859.343,	879.855,	900.362,	920.867,	941.367,	961.865,	982.359,	1002.852,	1023.335,	1043.822,	1064.301,	1084.779,	1105.255,	1125.726,	1146.195,	1166.66,	1187.121,	1206.652,	1226.18,	1245.706,	1264.296,	1282.886,	1300.543,	1316.34,	1330.257,	1351.148,	1363.722,	1380.444,	1393.484]
        head=[40.121,	40.122,	40.086,	40.037,	40.005,	39.924,	39.902,	39.852,	39.757,	39.68,	39.585,	39.508,	39.413,	39.309,	39.2,	39.092,	38.969,	38.824,	38.702,	38.57,	38.402,	38.23,	38.052,	38.002,	37.712,	37.522,	37.335,	37.113,	36.895,	36.677,	36.436,	36.182,	35.923,	35.664,	35.359,	35.064,	34.736,	34.277,	33.799,	33.258,	32.703,	32.112,	31.475,	30.819,	30.114,	29.391,	28.617,	27.843,	26.97,	26.132,	25.227,	24.298,	23.361,	22.364,	21.353,	20.307,	19.214,	18.169,	17.103,	16.012,	14.906,	13.811,	12.736,	11.75,	10.676,	9.874,	8.727,	7.65,	7.152]

        q1= [27.165,	37.579,	47.042,	56.506,	66.908,	78.245,	89.602,	100.937,	112.264,	124.534,	136.804,	149.069,	162.277,	175.479,	188.674,	201.871,	216.004,	232.017,	248.967,	265.911,	282.853,	299.788,	317.663,	337.409,	358.092,	378.767,	399.437,	420.102,	440.764,	461.417,	482.065,	502.713,	523.351,	543.986,	564.615,	585.242,	605.864,	626.478,	647.091,	667.698,	688.303,	708.901,	729.498,	750.088,	770.676,	791.253,	811.823,	832.384,	852.934,	873.474,	894.005,	914.53,	935.045,	955.553,	976.052,	996.544,	1017.027,	1037.503,	1057.973,	1077.506,	1096.101,	1114.692,	1132.349,	1149.07,	1164.865,	1181.571,	1198.285,	1213.133,	1227.979,	1241.893,	1255.807,	1269.716,	1282.694,	1295.671,	1308.645,	1321.617,	1334.584,	1346.625,	1357.737,	1368.848,	1379.957,	1392.002]
        eff=[7.602,	9.371,	10.926,	12.494,	14.09,	15.7,	17.567,	19.142,	20.612,	22.189,	23.761,	25.259,	26.878,	28.407,	29.846,	31.305,	32.774,	34.383,	36.03,	37.576,	39.115,	40.536,	42.032,	43.542,	45.079,	46.508,	47.873,	49.155,	50.399,	51.528,	52.581,	53.634,	54.552,	55.414,	56.205,	56.971,	57.667,	58.261,	58.822,	59.314,	59.767,	60.132,	60.483,	60.739,	60.963,	61.04,	61.022,	60.863,	60.571,	60.132,	59.578,	58.922,	58.145,	57.266,	56.266,	55.163,	53.947,	52.628,	51.219,	49.792,	48.315,	46.795,	45.289,	43.765,	42.361,	40.64,	39.021,	37.456,	35.866,	34.319,	32.764,	31.146,	29.589,	28.023,	26.396,	24.76,	23.053,	21.457,	19.957,	18.435,	16.901,	15.363]

        q2 =[28.656,	49.268,	69.879,	90.49,	111.102,	131.712,	152.323,	172.935,	193.544,	214.155,	234.764,	255.374,	275.985,	296.593,	317.202,	337.812,	358.42,	379.027,	399.636,	420.244,	440.853,	461.461,	482.067,	502.675,	523.283,	543.89,	564.497,	585.105,	605.71,	626.317,	646.924,	667.529,	688.136,	708.742,	729.348,	749.953,	770.559,	791.163,	811.768,	832.373,	852.977,	873.58,	894.184,	914.786,	935.389,	955.991,	976.594,	997.196,	1017.797,	1038.398,	1058.999,	1079.6,	1100.199,	1120.8,	1141.399,	1162,	1182.596,	1203.194,	1223.79,	1244.388,	1264.984,	1285.58,	1306.175,	1326.769,	1347.363,	1367.956,	1388.548,	1402.587]
        power = [0.153,	0.158,	0.164,	0.169,	0.175,	0.18,	0.186,	0.191,	0.196,	0.202,	0.207,	0.212,	0.217,	0.223,	0.228,	0.233,	0.238,	0.243,	0.248,	0.253,	0.258,	0.263,	0.268,	0.273,	0.278,	0.283,	0.288,	0.293,	0.297,	0.302,	0.307,	0.312,	0.317,	0.321,	0.326,	0.331,	0.335,	0.34,	0.344,	0.349,	0.354,	0.358,	0.362,	0.367,	0.371,	0.375,	0.379,	0.384,	0.388,	0.392,	0.396,	0.4,	0.404,	0.408,	0.411,	0.415,	0.419,	0.422,	0.426,	0.429,	0.433,	0.436,	0.439,	0.442,	0.445,	0.448,	0.451,	0.453]

        berate =790
        behead =34.69
        bepower =0.33
        beeff =61.06
        hz =60
        minrate =250
        maxrate=1150
        rangex = minrate,minrate,maxrate,maxrate
        rangey = 0,50,50,0
        pump_name = espdata.pump
    else :
        print('please select a pump' )
        #common calculations
    q11 = [i * (hz-10)/hz for i in q]  
    q12 = [i * (hz+10)/hz for i in q]  
    h11 = [i * math.pow((hz-10)/hz,2) for i in head]    
    h12 = [i * math.pow((hz+10)/hz,2) for i in head]    
    minimumrate=[minrate *(hz-10)/hz, minrate, minrate*(hz+10)/hz]
    maximumrate=[maxrate *(hz-10)/hz, maxrate, maxrate*(hz+10)/hz]
    bestEffrate=[berate *(hz-10)/hz, berate, berate*(hz+10)/hz]
    minimumhead=[]
    maximumhead=[]
    bestEffhead=[behead * math.pow((hz-10)/hz,2), behead, behead*math.pow((hz+10)/hz,2)]    
    minihead=find_head_when_rate_is_given(q11,h11, minimumrate[0])
    minimumhead.append(minihead)
    minihead1=find_head_when_rate_is_given(q ,head, minimumrate[1])
    minimumhead.append(minihead1)
    minihead2=find_head_when_rate_is_given(q12,h12, minimumrate[2])
    minimumhead.append(minihead2)
    maxhead=find_head_when_rate_is_given(q11,h11, maximumrate[0])
    maximumhead.append(maxhead)
    maxhead=find_head_when_rate_is_given(q ,head, maximumrate[1])
    maximumhead.append(maxhead)
    maxhead=find_head_when_rate_is_given(q12,h12, maximumrate[2])
    maximumhead.append(maxhead) 
        

    return q,q1,q2,head,eff,power, rangex, rangey, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead

def find_head_when_rate_is_given (rates, heads, given_rate):
    i=0
    prevrate=0
    prevhead=0
    for rate in rates:       
        if rate >=  given_rate:
            calchead = prevhead +((heads[i]-prevhead)*(given_rate-prevrate)/(rate-prevrate))             
            break
        else:
            prevrate=rate 
            prevhead=heads[i]
            i=i+1            
    return calchead

def vlp_curve_for_esp(espdata):
    x= [espdata.curr_Res_Pres,espdata.pip, espdata.discharge_pres, espdata.th_Pres]
    y= [espdata.mid_perf_depth,espdata.pump_depth, espdata.pump_depth,0]
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,10))     
    plt.plot(x, y, color='b', label = 'Head') 
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.xlim(0, 5000)
    plt.ylim (10000,0)
    plt.grid(linestyle='-')   
    graph = get_graph()
    return graph