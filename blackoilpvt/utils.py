from cProfile import label
from decimal import *
import math
from re import T
from tkinter import Label
from turtle import color
from matplotlib import gridspec
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
from .models import BlackoilPVT 
import numpy as np
import seaborn as sns
import plotly.express as px
 


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,y1,y2,y3,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,6))
    plt.title("Solution Gas Oil Ratio")
    plt.scatter(x,y, color='red')
    # plt.scatter(x,z, color='blue') 
    plt.scatter(x,y1, color='green')
    #plt.scatter(x,y2, color='red') 
    #plt.scatter(x,y3, color='orange')    
    plt.xticks(rotation=45)
    plt.xlabel('Oil API Gravity')
    plt.ylabel('Pressure (psi)') 
    plt.legend(['BP Pressure', 'Solution GOR'])
    plt.tight_layout()
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph
    
def get_Multiplot(x,y,y1,y2,y3,z, x1):
    plt.switch_backend('AGG')
    figure, axis = plt.subplots(2, 2)    
    fig = plt.figure()
    fig.set_figheight(8)
    fig.set_figwidth(13)
    fig.suptitle("PVT Plots", color='darkgreen', fontname="cursive", fontweight="bold" , fontsize="xx-large")
    spec = gridspec.GridSpec(ncols=2, nrows=2,
                         width_ratios=[2, 2], wspace=0.5,
                         hspace=0.5, height_ratios=[2, 2])
    ax0 = fig.add_subplot(spec[0])
    ax0.scatter(x, y, color='b', s=15)
    ax0.scatter(x, y1, color='black', s=15)   
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.title(" Oil API Vs Pb and Rs", color='b', fontname="cursive", fontweight="bold")      
    plt.xticks( color='g') 
    plt.yticks( color='g')       
    plt.xlabel('Oil API', color='g',fontweight="bold")       
    plt.ylabel('Pressure (psi)', color='g',fontweight="bold")       
    plt.legend(['BP Pressure', 'Solution GOR'])
    gradient = np.linspace(0, 1, 100).reshape(1, -1)
    plt.imshow(gradient , extent=[0, 60, 0,5000], aspect='auto', cmap='autumn')  
    
    ax1 = fig.add_subplot(spec[1])
    ax1.scatter(x, y2, color='b', s=15)   
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.title("Oil API Vs Bo", color='b', fontname="cursive", fontweight="bold")            
    plt.xticks( color='g') 
    plt.yticks( color='g')     
    plt.xlabel('Oil API', color='g', fontweight="bold")     
    plt.ylabel('Oil Formation Volume Factor', color='g', fontweight="bold")     
    gradient = np.linspace(0, 1, 100).reshape(1, -1)
    plt.imshow(gradient , extent=[0, 60, 0, 2.5], aspect='auto', cmap='autumn')   
    
    
    ax2 = fig.add_subplot(spec[2])
    ax2.scatter(x1, y, color='b', s=15)
    ax2.scatter(x1, y1, color='black', s=15)   
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.title("Gas Gravity Vs Pb and Rs", color='b', fontname="cursive", fontweight="bold")    
    plt.xlabel('Gas Gravity', fontweight="bold")      
    plt.ylabel('Pressure (psi)', fontweight="bold")        
    plt.legend(['BP Pressure', 'Solution GOR'])   
    gradient = np.linspace(0, 1, 100).reshape(1, -1)
    plt.imshow(gradient , extent=[0, 1, 0,5000], aspect='auto', cmap='autumn')  
    
    ax3 = fig.add_subplot(spec[3])
    ax3.scatter(x1, y2, color='b', s=15)  
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.title("Gas Gravity Vs Bo", color='b', fontname="cursive", fontweight="bold")    
    plt.xlabel('Gas Gravity', fontweight="bold")       
    plt.ylabel('Oil Formation Volume Factor', fontweight="bold")     
    gradient = np.linspace(0, 1, 100).reshape(1, -1)
    plt.imshow(gradient , extent=[0, 1, 0, 2.5], aspect='auto', cmap='autumn') 
    
    
    
    
    
    
    # ax2 = fig.add_subplot(spec[2])
    # ax2.scatter(x1, y3, color="b", s=15)   
    # plt.tight_layout()
    # plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    # plt.title("Calculated Solution GOR (Rscalc)", color='b')        
    # plt.xticks( color='b') 
    # plt.yticks( color='b')   
    # plt.xlabel('Oil API', color='b')    
    # plt.ylabel('Solution GOR (scf/bbl)', color='b')
    # gradient = np.linspace(0, 1, 100).reshape(1, -1)
    # plt.imshow(gradient , extent=[0, 60, 0, 5000], aspect='auto', cmap='autumn')    
    #    
    # ax3 = fig.add_subplot(spec[3])
    # ax3.scatter(x, z, color="b", s=15)
    # plt.title("Compressibility", color='b')         
    # plt.xticks( color='b') 
    # plt.yticks( color='b')   
    # plt.xlabel('Oil API', color='b')    
    # plt.ylabel('Compressibility of oil (psi-1)', color='b')   
    # gradient = np.linspace(-10,1,100).reshape(1, -1)
    # plt.imshow(gradient , extent=[0, 60, 0, 0.000010], aspect='auto', cmap='autumn')    
    
      
   
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph
  

def get_plot1(x1,y1,x11,y11):
    plt.switch_backend('AGG')
    plt.figure(figsize=(3,3))
    plt.title("Solution GOR")
    plt.plot(x1,y1, color='blue')   
    plt.scatter(x11,y11, color='red')   
    plt.xticks(rotation=45)
    plt.xlabel('Pressure (psi)', color='b')    
    plt.ylabel('Solution GOR (scf/bbl)', color='b')         
    plt.tight_layout()
    plt.grid(color = 'black', linestyle = '--', linewidth = 0.25)
    graph = get_graph()
    return graph
 
def get_plot2(x2,y2):
    plt.switch_backend('AGG')
    plt.figure(figsize=(3,3))
    plt.title("Oil Formation volume Factor")
    plt.plot(x2,y2, color='blue')
    plt.axis([0,3500, 1,2])
    plt.xticks(rotation=45)
    plt.xlabel('Pressure (psi)')
    plt.ylabel('Oil FVF( bbls/stb)') 
    # plt.legend(['Oil FVF'], loc ="lower right")
    plt.tight_layout()
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def get_plot3(x3,y3):
    plt.switch_backend('AGG')
    plt.figure(figsize=(3,3))
    plt.title("Oil Density")
    plt.plot(x3,y3, color='blue')    
    plt.xticks(rotation=45)
    plt.xlabel('Pressure (psi)')
    plt.ylabel('Oil Density( lb/ft3)')     
    plt.tight_layout()
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def get_plot4(x4,y4):
    plt.switch_backend('AGG')
    plt.figure(figsize=(3,3))
    plt.title("Oil Viscosity")
    plt.plot(x4,y4, color='blue')    
    plt.xticks(rotation=45)
    plt.xlabel('Pressure (psi)')
    plt.ylabel('Oil Viscosity(cP)')     
    plt.tight_layout()
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def get_Pb(pvt=BlackoilPVT()):    
    temperature = pvt.reservoirTemperature
    oilgravity = pvt.oilAPIgravity
    solutiongas = pvt.solutionGOR
    gasgravity = pvt.gasGravity   
    oilg = 141.5/(oilgravity+ 131.5)   
    if pvt.pbCorrelation == "_Standing":
        Pas = (0.00091 * temperature) - (0.0125 * oilgravity)
        Pb = 18.2 * ((((solutiongas / gasgravity) **0.83) * 10** Pas) - 1.4 ) 
    elif pvt.pbCorrelation == "_VasquezBeggs":         
        if oilgravity <=30.0:
            Pavaques =-11.172*oilgravity/(temperature+460)
            Pb =((27.624* solutiongas/gasgravity)*10**((Pavaques)))**0.914328          
        elif oilgravity >30.0:
           Pavaques =-10.393*oilgravity/(temperature+460)
           Pb =((56.18* solutiongas/gasgravity)*10**((Pavaques)))**0.84246           
    elif pvt.pbCorrelation == "_Glaso":
        aglass0 = (solutiongas/gasgravity)**0.816 * temperature**0.172 *oilgravity**-0.989
        logvar = (math.log10(aglass0))
        logPbglasso = 1.7669 + 1.7447* logvar- 0.30218*logvar**2.0  
        Pb=10**logPbglasso         
    elif pvt.pbCorrelation == "_Marhoun":
        Pb = 0.00538088*solutiongas**0.715082* gasgravity**-1.87784 * oilg**3.1437 * (temperature+460)**1.32657             
    elif pvt.pbCorrelation == "_PetroskyFarshad":  
        valx = 0.0007916*oilgravity**1.5410-0.00004561*temperature**1.3911
        Pb = (112.727 * solutiongas**0.577421/(gasgravity**0.8439*10**valx)) - 1391.051
   
    return Pb

def get_Rs(pvt=BlackoilPVT() ):    
    temperature = pvt.reservoirTemperature
    oilgravity = pvt.oilAPIgravity
    solutiongas = pvt.solutionGOR
    gasgravity = pvt.gasGravity
    pressure =(pvt.reservoirPressure )   
    oilg = 141.5/(oilgravity+131.5) 
    Pb=get_Pb(pvt)
    if pressure <Pb :
        if pvt.pbCorrelation == "_Standing":
            intx = (0.0125 * oilgravity) - (0.00091 * temperature)
            Rs = gasgravity * ((pressure / 18.2 +1.4) * 10** intx)**1.2048 
        elif pvt.pbCorrelation == "_VasquezBeggs": 
            if oilgravity<30 :
                var1 = math.exp(25.7240*oilgravity/temperature)
                Rs= 0.0362*(gasgravity)*(pressure**1.097)*(math.exp(25.7240*oilgravity/(temperature+460)))       
            else : 
                var1 = 23.931*oilgravity/(temperature+460)            
                Rs= 0.0178*gasgravity*pressure**1.1870 * math.exp(var1)          
        elif pvt.pbCorrelation == "_Glaso":            
            var2 =14.1811-(3.3093*(math.log10(pressure)))
            var3 = math.sqrt(var2)
            intx = 2.8869 - var3
            Rs = gasgravity * ((oilgravity**0.989 / temperature**0.172 ) * 10 ** intx)** 1.22255        
        elif pvt.pbCorrelation == "_Marhoun":
            a1 = 185.843208*(math.pow(gasgravity,1.877840))
            b1=(oilg** -3.1437)
            c1 = ((temperature+ 460.0)**-1.32657)           
            Rs = math.pow((a1*b1*c1 * pressure),1.39844)
        elif pvt.pbCorrelation == "_PetroskyFarshad":
            valx = 0.0007916*oilgravity**1.5410-0.00004561*temperature**1.3911
            val1 = pressure /(112.727) + 12.340
            val2 = gasgravity**0.8439 
            Rs = ((val1)*(val2)*(10**(valx)))**1.73184
    else :
        Rs = solutiongas  
    return Rs

def get_Bo( pvt=BlackoilPVT()):    
    temperature = pvt.reservoirTemperature
    oilgravity = pvt.oilAPIgravity
    solutiongas = pvt.solutionGOR
    gasgravity = pvt.gasGravity   
    pressure = pvt.reservoirPressure
    oilg = 141.5/(oilgravity+131.5)  
    Pb = get_Pb(pvt)
    Rs = get_Rs(pvt)
    if pvt.pbCorrelation == "_Standing":
        if pressure <=Pb:
            term1 = Rs *(gasgravity/oilg)**0.5
            term2 =(1.25* temperature)
            Bo = 0.9759 + 0.000120*( term1 + term2)**1.2  
        else :
            term1 = solutiongas *(gasgravity/oilg)**0.5
            term2 =(1.25* temperature)
            Bobp = 0.9759 + 0.000120*( term1 + term2)**1.2 
            Boabterm1 = 4.1646*10**-7*Rs**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729
            Boabterm1= Boabterm1
            Boabterm2= math.log((pressure)/(Pb))
            Bo = (Bobp) * (math.exp(-Boabterm1*Boabterm2)) 
    elif pvt.pbCorrelation == "_VasquezBeggs": 
        Bobp = 1.0 + (0.0004670*solutiongas) + ((temperature-60.0)*(oilgravity/gasgravity))*(1.1*10**-5 + (1.337*10**-9*solutiongas)) 
        if oilgravity<=30:
            if pressure <Pb :
                 Bo = 1.0 + (0.0004677*Rs) + ((temperature-60.0)*(oilgravity/gasgravity))*(1.751*10**-5 + (1.811*10**-8*Rs))
            else :
                Boabterm1 = 4.1646*10**-7*Rs**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729
                Boabterm1= (Boabterm1)
                Boabterm2= (math.log(pressure/Pb))
                Bo = (Bobp) * (math.exp(-Boabterm1*Boabterm2))
                # Boabterm1 = (10**-5)*(Decimal('-1433')+ (5*Rs) +(Decimal('17.2') * temperature)-(Decimal('1180') * gasgravity)+(Decimal('12.61') * oilgravity))  
                # Bo = Decimal(Bobp) * math.exp(-Decimal(Boabterm1 * (pressure**Decimal('0.4094') - (Pb**Decimal('0.4094')))))
        elif oilgravity >30:
            Bobp = 1.0 + (0.0004670*solutiongas) + ((temperature-60.0)*(oilgravity/gasgravity))*(1.1*10**-5 + (1.337*10**-9*solutiongas))
            if pressure <Pb: 
                Bo = 1.0 + (0.0004670*Rs) + ((temperature-60.0)*(oilgravity/gasgravity))*(1.1*10**-5 + (1.337*10**-9*Rs))
            else :
                Boabterm1 = 4.1646*10**-7*Rs**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729
                Boabterm1= (Boabterm1)
                Boabterm2= (math.log(pressure/Pb))
                Bo = (Bobp) * (math.exp(-Boabterm1*Boabterm2))
                # Boabterm1 = Decimal(10**-5)*(Decimal('-1433')+ (Decimal('5')*Rs) +(Decimal('17.2') * temperature)-(Decimal('1180') * gasgravity)+(Decimal('12.61') * oilgravity))  
                # Bo = Decimal(Bobp) * Decimal(math.exp(-Decimal(Boabterm1 * (pressure**Decimal('0.4094') - Decimal(Pb)**Decimal('0.4094')))))
    elif pvt.pbCorrelation == "_Glaso": 
        Bob = (solutiongas*(gasgravity/oilg)**0.526) + 0.968*temperature
        logBob = math.log10((Bob))         
        A = -6.58511 + (2.91329*(logBob)) -(0.27683*(logBob)**2.0)
        Bobp = 1.0 + 10**A         
        if pressure <Pb:
            Bob = (Rs*(gasgravity/oilg)**0.526) + 0.968*temperature
            logBob = math.log10((Bob))         
            A = -6.58511 + (2.91329*logBob) -(0.27683*(logBob)**2.0)
            Bo = 1.0 + 10**A 
        else :
            Boabterm1 = 4.1646*10**-7*solutiongas**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729
            Boabterm1= (Boabterm1)
            Boabterm2= (math.log(pressure/Pb))
            Bo = (Bobp) * (math.exp(-Boabterm1*Boabterm2)) 
    elif pvt.pbCorrelation == "_Marhoun":
        F = solutiongas**0.742390 * gasgravity** 0.323294 * oilg**-1.202040
        t = temperature+460
        Bobp = 0.497069+ 0.000862963*t + 0.00182594*F + 0.00000318099*F**2 
        if pressure <Pb :            
            F = (Rs)**0.742390 * gasgravity** 0.323294 * oilg**-1.202040
            t = temperature+460
            Bo = 0.497069+ 0.000862963*t + 0.00182594*F + 0.00000318099*F**2            
        else:
            Boabterm1 = 4.1646*10**-7*(Rs)**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729
            Boabterm1= (Boabterm1)
            Boabterm2= (math.log((pressure)/(Pb)))
            Bo = (Bobp) * (math.exp(-Boabterm1*Boabterm2))
    elif pvt.pbCorrelation == "_PetroskyFarshad":
        term1 = solutiongas**0.3738* (gasgravity**0.2914/oilg**0.6265)
        term2 =temperature**0.5371         
        Bobp = 1.0113 + 0.000072046*(term1 +  0.24626*term2)**3.0936
        if pressure <Pb :
            term1 = Rs**0.3738* (gasgravity**0.2914/oilg**0.6265)
            term2 =temperature**0.5371         
            Bo = 1.0113 + 0.000072046*(term1 +  0.24626*term2)**3.0936            
        else:
            Boabterm1 = 4.1646*10**-7*(Rs)**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729
            Boabterm1= (Boabterm1)
            Boabterm2= (math.log(pressure/Pb))
            Bo = (Bobp) * (math.exp(-Boabterm1*Boabterm2))
   
    return Bo

def get_Density(pvt=BlackoilPVT()):    
    temperature = pvt.reservoirTemperature
    oilgravity = pvt.oilAPIgravity
    solutiongas = pvt.solutionGOR
    gasgravity = pvt.gasGravity   
    pressure = pvt.reservoirPressure
    oilg = 141.5/(oilgravity+131.5)  
    Pb = get_Pb(pvt)
    Rs = get_Rs(pvt)
    Bo = get_Bo(pvt)
    if pvt.pbCorrelation == "_Standing":
        term1 = solutiongas *(gasgravity/oilg)**0.5
        term2 =(1.25* temperature)
        Bobp = 0.9759 + 0.000120*( term1 + term2)**1.2 
        oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bobp) 
        if pressure <=Pb:
             oildensity = (62.4*oilg + 0.0136 * Rs* gasgravity)/(Bo) 
        else :
            valueA = 10**-5 * (-1433+ ((5.0)*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))
            oildensity = (oildensityatbp)* (math.exp((valueA)*((math.log(pressure/Pb)))))
            # Boabterm1 = Decimal('4.1646')*10**Decimal('-7')*solutiongas**(Decimal('0.69357') * gasgravity)**Decimal('0.1885') *oilgravity**Decimal('0.3272')* temperature **Decimal('0.6729')
            # Boabterm1= Decimal(Boabterm1)
            # oildensity = Decimal(oildensityatbp)* Decimal(math.exp(Boabterm1*(pressure**Decimal('0.4094')-Decimal(Pb)**Decimal('0.4094'))))
    elif pvt.pbCorrelation == "_VasquezBeggs":  
        oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bo)
        valueA = 10**-5 * (-1433+ (5.0*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))
        if oilgravity<=30:
            if pressure <Pb :
                oildensity = (62.4*oilg + 0.0136 * Rs* gasgravity)/(Bo)   
            else :               
                oildensity = (oildensityatbp)* (math.exp((valueA)*((math.log(pressure/Pb)))))
        elif oilgravity >30:            
            if pressure <Pb: 
                oildensity = (62.4*oilg + 0.0136 * Rs* gasgravity)/(Bo)   
            else :
                oildensity = (oildensityatbp)* (math.exp((valueA)*((math.log(pressure/Pb)))))
    elif pvt.pbCorrelation == "_Glaso": 
        oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bo)  
        valueA = 10**-5 * (-1433+ ((5.0)*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))      
        if pressure <Pb:
             oildensity = (62.4*oilg + 0.0136 * Rs* gasgravity)/(Bo)
        else :
            oildensity = (oildensityatbp)* (math.exp((valueA)*(math.log(pressure/Pb)))) 
    elif pvt.pbCorrelation == "_Marhoun":
        F = solutiongas**0.742390 * gasgravity** 0.323294 * oilg**-1.202040
        t = temperature+460
        Bobp = 0.497069+ 0.000862963*t + 0.00182594*F + 0.00000318099*F**2 
        oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bobp) 
        if pressure <Pb :
            oildensity = (62.4*oilg + 0.0136 * (Rs)* gasgravity)/(Bo)           
        else:
            valueA = 10**-5 * (-1433+ ((5.0)*(Rs)) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))
            oildensity = (oildensityatbp)* (math.exp((valueA)*((math.log(pressure/Pb))))) 
    elif pvt.pbCorrelation == "_PetroskyFarshad":
        term1 = solutiongas**0.3738* (gasgravity**0.2914/oilg**0.6265)
        term2 =temperature**0.5371         
        Bobp = 1.0113 + 0.000072046*(term1 +  0.24626*term2)**3.0936
        oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bobp)
        if pressure <Pb :
             oildensity = (62.4*oilg + 0.0136 * Rs* gasgravity)/(Bo)               
        else:
            valueA = 10**-5 * (-1433+ ((5.0)*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))
            oildensity = (oildensityatbp)* (math.exp(Decimal(valueA)*((math.log(pressure/Pb)))))
            # Boabterm1 = Decimal('4.1646')*10**Decimal('-7')*Rs**(Decimal('0.69357') * gasgravity)**Decimal('0.1885') *oilgravity**Decimal('0.3272')* temperature **Decimal('0.6729')
            # Boabterm1= Decimal(Boabterm1)
            # oildensity = Decimal(oildensityatbp)* Decimal(math.exp(Boabterm1*(pressure**Decimal('0.4094')-Decimal(Pb)**Decimal('0.4094'))))
    return oildensity

def get_Viscosity(pvt=BlackoilPVT()):    
    temperature = pvt.reservoirTemperature
    oilgravity = pvt.oilAPIgravity
    solutiongas = pvt.solutionGOR
    gasgravity = pvt.gasGravity   
    pressure = pvt.reservoirPressure
    oilg = 141.5/(oilgravity+131.5) 
    Pb = get_Pb(pvt)
    Rs = get_Rs(pvt)
    # Bo = get_Bo(pvt)   
    if pvt.viscosityCorrelation=="_Beal":
        vterm = 0.43+(8.33/oilgravity)
        visA1 = 10**(vterm)             
        viscositydead = (0.32 + (1.8*10**7/oilgravity**4.53))*(360/(temperature+200))**(visA1)
        vala = 10.715*(solutiongas+100.0)**-0.515
        valb = 5.44*(solutiongas+150.0)**-0.338  
        viscositydynamicPb = (vala) * viscositydead**(valb)        
        if pressure<Pb:
            vala = 10.715*((Rs)+100.0)**-0.515
            valb = 5.44*((Rs)+150.0)**-0.338  
            viscosity = (vala) * viscositydead**(valb)
        else :
            valuea = -3.9*10**-5.0*(pressure)-5.0
            valuem = 2.6*(pressure)**1.187*10**valuea            
            viscosity =viscositydynamicPb*((pressure)/Pb)**(valuem)
    elif pvt.viscosityCorrelation=="_BeggsRobinson":
            valz= 3.0324  - (0.02023 * oilgravity)
            valy = 10**(valz) 
            valx = (valy) * temperature**-1.163       
            viscositydead= 10**(valx)-1.0
            vala = 10.715*(solutiongas+100.0)**-0.515
            valb = 5.44*(solutiongas+150.0)**-0.338  
            viscositydynamicPb = (vala) * viscositydead**(valb) 
            if pressure < Pb:                 
                vala = 10.715*((Rs)+100.0)**-0.515
                valb = 5.44*((Rs)+150.0)**-0.338  
                viscosity = (vala) * viscositydead**(valb) 
            else:
                valuea = -3.9*10**-5.0*(pressure) -5.0
                valuem = 2.6*(pressure)**1.187*10**(valuea)            
                viscosity =viscositydynamicPb*((pressure)/Pb)**(valuem) 
    elif pvt.viscosityCorrelation=="_Glaso":
        visA = (10.313* (math.log10(temperature)))- 36.447         
        viscositydead= 3.141*(10**10)*temperature**-3.444*((math.log10(oilgravity))**(visA))
        vala = 10.715*(solutiongas+100.0)**-0.515
        valb = 5.44*(solutiongas+150.0)**-0.338  
        viscositydynamicPb = (vala) * viscositydead**(valb)  
        if pressure <Pb : 
            vala = 10.715*((Rs)+100.0)**-0.515
            valb = 5.44*((Rs)+150.0)**-0.338  
            viscosity = (vala) * viscositydead**(valb) 
        else :
            valuea = -3.9*10**-5.0*pressure -5.0
            valuem = 2.6*pressure**1.187*10**(valuea)            
            viscosity =viscositydynamicPb*(pressure/Pb)**(valuem) 
    return viscosity

def get_OilCompressibility(pvt=BlackoilPVT()):    
    temperature = pvt.reservoirTemperature
    oilgravity = pvt.oilAPIgravity
    solutiongas = pvt.solutionGOR
    gasgravity = pvt.gasGravity   
    pressure = pvt.reservoirPressure
    oilg = 141.5/(oilgravity+131.5) 
    Pb = get_Pb(pvt)
    Rs = get_Rs(pvt)
    Bo = get_Bo(pvt)   
    if pvt.pbCorrelation == "_Standing":
        co = 1.705*10**-8 *solutiongas**0.69357* gasgravity**0.1885 * oilgravity**0.3272*temperature**0.6729 * pressure**-0.5906
    elif pvt.pbCorrelation == "_VasquezBeggs":  
        oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bo)
        valueA = 10**-5 * (-1433+ ((5.0)*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))
        if oilgravity<=30:
            co = 10**-5*(-1433+ ((5.0)*Rs) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))/ pressure
        elif oilgravity >30:            
            co = (-1433+ ((5.0)*Rs) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))/ pressure
    elif pvt.pbCorrelation == "_Glaso": 
        valA = -7.573-(1.45*(math.log(pressure)))-(0.383*(math.log(Pb)))+(1.402*(math.log(temperature+460)))+(0.256* (math.log(oilgravity)))+ (0.449*(math.log(solutiongas)))
        co = math.exp((valA))
    elif pvt.pbCorrelation == "_Marhoun":
        valA = -7.573-(1.45*(math.log(pressure)))-(0.383*(math.log(Pb)))+(1.402*(math.log(temperature+460)))+(0.256* (math.log(oilgravity)))+ (0.449*(math.log(Rs)))
        co = math.exp(Decimal(valA))
    elif pvt.pbCorrelation == "_PetroskyFarshad":
        co = 1.705*10**-8 *solutiongas**0.69357* gasgravity**0.1885 * oilgravity**0.3272*temperature**0.6729 * pressure**-0.5906
    return co
  