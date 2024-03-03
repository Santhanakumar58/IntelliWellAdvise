from cmath import log10
from ctypes.wintypes import PBOOL
from decimal import Decimal
from distutils.log import Log
import math
from os import truncate
from pickletools import decimalnl_short
from secrets import choice
from stringprep import c22_specials
from tempfile import tempdir
from unicodedata import decimal
from xml.etree.ElementPath import prepare_self
from django.shortcuts import render
from django.shortcuts import render, redirect
from numpy import double, float_
from .models import BlackoilPVT
from .forms import BlackoilPVTForm
from blackoilpvt.utils import get_Bo, get_Density, get_Pb, get_Rs, get_Viscosity, get_plot, get_plot1, get_plot2, get_plot3, get_plot4 , get_Multiplot
from IntelligentOilWell.custom_context_processors import selectedfgi
from selectedfgi.models import Selectedfgi
import numpy as np
from sublayers.models import Sublayer

def list_blackoilpvt(request): 
    y=[]
    y1=[]
    y2=[]  
    y3=[]     
    z=[]
    x=[]  
    x1=[]   
    selectedfgi=Selectedfgi.objects.first()
    blackoilpvts = BlackoilPVT.objects.filter(fgId = selectedfgi.fgid)    
    for pvt in blackoilpvts:          
      pressure = pvt.reservoirPressure
      temperature = pvt.reservoirTemperature
      oilgravity = pvt.oilAPIgravity
      gasgravity = pvt.gasGravity  
      solutiongas = pvt.solutionGOR 
      oilg = 141.5/(oilgravity+ 131.5)   
      if pvt.pbCorrelation == "_Standing":
         Pas = (0.00091 * temperature) - (0.0125* oilgravity)
         Pb = 18.2 * ((((solutiongas / gasgravity) **0.83) * 10** Pas) -1.4 ) 
         intx = 0.0125  * oilgravity - ( 0.00091  * temperature)
         Rs = gasgravity * ((Pb /18.2 + 1.4) * 10** intx)** 1.2048
         term1 = solutiongas *(gasgravity/oilg)**0.5
         term2 =(1.25* temperature)
         Bo =0.9759 + 0.000120*( term1 + term2)**1.2
         standing_Bo = standing_bo(pressure, temperature, Rs, oilgravity)

         Boabterm1 =4.1646*10**-7*solutiongas**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729      
         Boabterm2= math.log(pressure/Pb)
         BoabovePb = Bo * math.exp(-Boabterm1*Boabterm2) 
         oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bo)        
         if Pb < pressure:
            oildensityabovebp =oildensityatbp
         else :
            oildensityabovebp = (oildensityatbp)*(math.exp(Boabterm1*(pressure**0.4094-(Pb)**0.4094)))
         if Pb > pressure:
               pressure=Pb 
         co = 1.705*10**-8 *solutiongas**0.69357* gasgravity**0.1885 * oilgravity**0.3272*temperature**0.6729 * pressure**-0.5906                
      elif pvt.pbCorrelation == "_VasquezBeggs":         
         if oilgravity <=30.0:
            Pavaques =-11.172*oilgravity/(temperature+460)
            Pb =(27.624* solutiongas/gasgravity)*10**((Pavaques))**0.914328
            var1 = math.exp(25.7240*oilgravity/temperature)
            Rs= 0.0362*gasgravity*(Pb**1.097)*(math.exp(25.7240*oilgravity/(temperature+460)))
            Bo = 1.0 + (0.0004677*solutiongas) + ((temperature-60.0)(oilgravity/gasgravity))*(1.751*10**-5 + (1.811*10**-8*solutiongas))
            Boabterm1 = (-1433+ (5*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))  
            BoabovePb = (Bo) * math.exp(-(Boabterm1 * (pressure**0.4094 - Pb**0.4094)))
            oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bo)
            valueA = 10**-5 * (-1433+ ((5.0)*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))
            if Pb < pressure:
               oildensityabovebp =oildensityatbp
            else :
               oildensityabovebp =oildensityatbp*math.exp(valueA*(math.log(pressure/Pb)))
               # VasquezBeggs Oil compressibility
            if Pb > pressure:
               pressure =Pb
            co = (-1433+ ((5.0)*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))/ pressure
            co= co/100000                    
         elif oilgravity >30.0:
            Pavaques =-(10.393)*oilgravity/(temperature+460)
            Pb =((56.18* solutiongas/gasgravity)*10**((Pavaques)))**0.84246
            var1 = 23.931*(oilgravity/(temperature+460))
            Rs= 0.0178*gasgravity*Pb**1.1870 * (math.exp(var1))                      
            Bo = 1.0 + (0.0004670*solutiongas) + (temperature-60.0)*(oilgravity/gasgravity)*(1.1*10**-5 + (1.337*10**-9*solutiongas))
            Boabterm1 = (-1433+ (5*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))  
            BoabovePb = (Bo) * (math.exp(-(Boabterm1 * (pressure**0.4094 - (Pb)**0.4094))))
            oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bo)
            valueA = 10**-5 * (-1433+ (5.0*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))
            if Pb < pressure:
               oildensityabovebp =oildensityatbp
            else :
               oildensityabovebp = (oildensityatbp)* (math.exp(valueA*(math.log(pressure/Pb))))
               # VasquezBeggs Oil compressibility
            if Pb >pressure:
               pressure =Pb
            # VasquezBeggs Oil compressibility
            co = (-1433+ ((5.0)*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))/ pressure
            co= co/100000  
      elif pvt.pbCorrelation == "_Glaso":
         aglass0 = (solutiongas/gasgravity)**Decimal('0.816') * temperature**Decimal('0.172') *oilgravity**Decimal('-0.989')
         logvar =(math.log10(aglass0))
         logPbglasso =('1.7669') +1.7447* logvar-0.30218*logvar**2.0
         Pb=10**logPbglasso
         var2 =14.1811-(3.3093*(math.log10(Pb)))
         var3 = math.sqrt(var2)
         intx =2.8869 -(var3)
         Rs = gasgravity * ((oilgravity**0.989 / temperature*0.172 ) * 10 ** intx)** 1.22255
         Bob = (solutiongas*(gasgravity/oilg)**0.526) +0.968*temperature
         logBob = math.log10(Bob)         
         A = -6.58511 + (2.91329*logBob) -(0.27683*(logBob)**2.0)
         Bo = 1.0 + 10**A 
         Boabterm1 = 4.1646*10**-7*solutiongas**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729   
         Boabterm2= (math.log(pressure/Pb))
         BoabovePb =(Bo) * (math.exp(-Boabterm1*Boabterm2))          
         oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bo)
         valueA = 10**-5 * (-1433+ ((5.0)*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))
         if Pb < pressure:
            oildensityabovebp =oildensityatbp
         else :
            denterm1 = (math.exp(valueA*(math.log(pressure/(Pb)))))
            oildensityabovebp = (oildensityatbp)* denterm1
        
         if Pb > pressure:
            pressure =Pb
             # McCain Oil compressibility
         valA = -7.573-(1.45*(math.log(pressure)))-(0.383*(math.log(Pb)))+(1.402*(math.log(temperature+460)))+(0.256* (math.log(oilgravity)))+ (0.449*(math.log(solutiongas)))
         co = math.exp(valA)
      elif pvt.pbCorrelation == "_Marhoun":
         Pb = 0.00538088*solutiongas**0.715082* gasgravity**-1.87784 * oilg**3.1437 * (temperature+460)**1.32657
         a1 = 185.843208*(math.pow(gasgravity,1.877840))
         b1=(oilg** -3.1437)
         c1 = ((temperature+ 460.0)**-1.32657)
         Rs = math.pow((a1*b1*c1 * Pb),1.39844)
         F = solutiongas**0.742390 * gasgravity** 0.323294 * oilg**-1.202040
         t = temperature+460
         Bo = 0.497069+ 0.000862963*t +0.00182594*F + 0.00000318099*F**2
         Boabterm1 =4.1646*10**-7*solutiongas**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729
 
         Boabterm2= (math.log(pressure/Pb))
         BoabovePb = (Bo) * (math.exp(-Boabterm1*Boabterm2)) 
         
         oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bo)
         valueA = 10**-5 * (-1433+ (5.0*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))
         if Pb < pressure:
            oildensityabovebp =oildensityatbp
         else :
            oildensityabovebp = (oildensityatbp)* (math.exp(valueA*(math.log(pressure/Pb)))) 
         if Pb >pressure:
               pressure =Pb
             # McCain Oil compressibility
         valA = -7.573-(1.45*(math.log(pressure)))-(0.383*(math.log(Pb)))+(1.402*(math.log(temperature+460)))+(0.256* (math.log(oilgravity)))+ (0.449*(math.log(solutiongas)))
         co = math.exp((valA))
      elif pvt.pbCorrelation == "_PetroskyFarshad":
         valx = 0.0007916*oilgravity**1.5410-0.00004561*temperature**1.3911
         Pb = (112.727 * solutiongas**0.577421/(gasgravity**0.8439*10**valx)) - 1391.051   
         val1 = Pb /(112.727) + 12.340
         val2 = gasgravity**0.8439 
         Rs = ((val1)*(val2)*(10**(valx)))**1.73184
         term1 = solutiongas**0.3738* (gasgravity**0.2914/oilg**0.6265)
         term2 =temperature**0.5371         
         Bo = 1.0113 + 0.000072046*(term1 +  0.24626*term2)**3.0936
         Boabterm1 = 4.1646*10**-7*solutiongas**(0.69357 * gasgravity)**0.1885 *oilgravity**0.3272* temperature **0.6729
    
         Boabterm2= (math.log(pressure/Pb))
         BoabovePb = (Bo) * (math.exp(-Boabterm1*Boabterm2)) 
         oildensityatbp = (62.4*oilg + 0.0136 * solutiongas* gasgravity)/(Bo)        
         if Pb < pressure:
            oildensityabovebp =oildensityatbp
         else :
            oildensityabovebp = (oildensityatbp)* (math.exp(Boabterm1*(pressure**0.4094-(Pb)**0.4094)))
         if Pb > pressure:
               pressure=Pb 
         co = 1.705*10**-8 *solutiongas**0.69357* gasgravity**0.1885 * oilgravity**0.3272*temperature**0.6729 * pressure**-0.5906         
      elif pvt.pbCorrelation == "":
         # Material Balance Equation only foe BO
         oilg = 141.5/(oilgravity+ 131.5)  
         Bo = (62.4 * oilg + 0.0136*solutiongas * gasgravity)/(62.4 * oilg)
      if pvt.viscosityCorrelation=="_Beal":
         vterm = 0.43+(8.33/oilgravity)
         visA1 = 10**(vterm)             
         viscositydead = (0.32 + (1.8*10**7/oilgravity**4.53))*(360/(temperature+200))**(visA1)
         vala = 10.715*(solutiongas+100.0)**-0.515
         valb = 5.44*(solutiongas+150.0)**-0.338  
         viscositydynamicPb = (vala) * viscositydead**(valb)
         if pressure>Pb:
            valuea = -3.9*10**-5.0*pressure -5.0
            valuem = 2.6*pressure**1.187*10**(valuea)            
            viscositydynamic =viscositydynamicPb*(pressure/(Pb))**(valuem)
      elif pvt.viscosityCorrelation=="_BeggsRobinson":       
         valz= 3.0324  - (0.02023 * oilgravity)
         valy = 10**(valz) 
         valx = (valy) * temperature**-1.163       
         viscositydead= (10**(valx))-1.0
         vala = 10.715*(solutiongas+100.0)**-0.515
         valb = 5.44*(solutiongas+150.0)**-0.338  
         viscositydynamicPb = (vala) * viscositydead**(valb) 
         if pressure>Pb:
            valuea = -3.9*10**-5.0*pressure -5.0
            valuem = 2.6*pressure**1.187*10**(valuea)            
            viscositydynamic =(viscositydynamicPb)*(pressure/(Pb))**(valuem)   
      elif pvt.viscosityCorrelation=="_Glaso":
         visA = (10.313* (math.log10(temperature)))- 36.447         
         viscositydead= 3.141*(10**10)*temperature**-3.444*((math.log10(oilgravity))**(visA))
         vala = 10.715*(Rs+100.0)**-0.515
         valb = 5.44*(Rs+150.0)**-0.338  
         viscositydynamicPb = (vala) * viscositydead**(valb)  
         if pressure>Pb:
            valuea = -3.9*10**-5.0*pressure -5.0
            valuem = 2.6*pressure**1.187*10**valuea           
            viscositydynamic =viscositydynamicPb*(pressure/Pb)**(valuem)   
      Rs= math.trunc(Rs * 1000)/1000
      Pb= math.trunc(Pb * 1000)/1000
      Bo= math.trunc(Bo * 1000)/1000
      BoabovePb= math.trunc(BoabovePb * 1000)/1000
      oildensityatbp= math.trunc(oildensityatbp * 1000)/1000
      oildensityabovebp= math.trunc(oildensityabovebp * 1000)/1000
      co= math.trunc(co * 100000000)/100000000
      viscositydead= math.trunc(viscositydead * 1000)/1000
      viscositydynamicPb= math.trunc(viscositydynamicPb * 1000)/1000
      viscositydynamic= math.trunc(viscositydynamic * 1000)/1000
      
      x.append(pvt.oilAPIgravity)
      x1.append(gasgravity)          
      y.append(Pb) 
      y1.append(Rs)
      y2.append(Bo) 
      y3.append(solutiongas)       
      z.append(co)        
      
      # VasquezBeggs Oil compressibility <Pb
      co1 = (-1433+ (5*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))/(10**5 * pressure)              
      # VasquezBeggs Oil compressibility>Pb
      valA = -7.573-(1.45*math.log(pressure))-(0.383*(math.log(Pb)))+(1.402*(math.log(temperature+460)))+(0.256* (math.log(oilgravity)))+ (0.449*(math.log(solutiongas)))
      co1 = math.exp(valA)      
       # Petrosky Oil compressibility
      co1 = 1.705*10**-7 *solutiongas**0.69357* gasgravity**0.1885 * oilgravity**0.3272*temperature**0.6729 * pressure**-0.5906
       # VasquezBeggs Oil compressibility
      co = (-1433+ ((5.0)*solutiongas) +(17.2 * temperature)-(1180 * gasgravity)+(12.61 * oilgravity))/ pressure
      co= math.trunc(co * 10000000)/1000000     
      # Petrosky Oil compressibility
      # VasquezBeggs Oil compressibility
      valA = -7.573-(1.45*(math.log(pressure)))-(0.383*(math.log(Pb)))+(1.402*(math.log(temperature+460)))+(0.256* (math.log(oilgravity)))+ (0.449*(math.log(solutiongas)))
      co = math.exp(valA)
    chart = get_Multiplot(x,y,y1,y2,y3,z,x1) 
    context = {'blackoilpvts':blackoilpvts, 'chart':chart }
    return render (request, 'blackoilpvt/blackoilPVT.html', context)

def create_blackoilpvt(request): 
   model = BlackoilPVT()
   selectedfgi=Selectedfgi.objects.first()
   model.fgId = selectedfgi.fgid
   sublayer = Sublayer.objects.get(sublayername=selectedfgi.selectedsublayername)
   model.subLayer = sublayer
   form = BlackoilPVTForm(request.POST or None, instance = model)
   if form.is_valid():        
       form.save()
       if request=='POST':
         pressure = request.POST['reservoirPressure']
         temperature = request.POST['reservoirTemperature']
         oilgravity = request.POST['oilAPIgravity']
         gasgravity = request.POST['gasGravity'] 
         solutiongas =request.POST['solutionGOR'] 
         oilg = 141.5/(oilgravity+ 131.5) 
       return redirect ('blackoilpvt:list_blackoilpvt')
   return render (request, 'blackoilpvt/blackoilPVT_form.html', {'form': form})

def update_blackoilpvt(request, id):
   blackoilpvt = BlackoilPVT.objects.get(id=id)
   form = BlackoilPVTForm(request.POST or None, instance=blackoilpvt)
   if form.is_valid():        
        blackoilpvt.save()  
        x1=[]
        y1=[]
        x11=[] 
        y11=[]
        x1=[]
        y1=[]
        x2=[]
        y2=[] 
        x3=[] 
        y3=[]  
        x4=[]  
        y4=[]
        pressure = blackoilpvt.reservoirPressure
        temperature = blackoilpvt.reservoirTemperature
        oilgravity = blackoilpvt.oilAPIgravity
        gasgravity = blackoilpvt.gasGravity  
        solutiongas = blackoilpvt.solutionGOR 
        oilg = 141.5/(oilgravity+ 131.5) 
        delp = pressure/100 
        Pb = get_Pb(blackoilpvt) 
        x11.append(Pb)
        y11.append(blackoilpvt.solutionGOR)
        for i in range(101):
           pres = i*delp + 14.7           
           blackoilpvt.reservoirPressure = pres           
           Rs = get_Rs(blackoilpvt) 
           x1.append(pres)
           y1.append(Rs)
           Bo = get_Bo(blackoilpvt)
           x2.append(pres)
           y2.append(Bo)
           oildensity = get_Density(blackoilpvt)
           x3.append(pres)
           y3.append(oildensity)
           viscosity = get_Viscosity(blackoilpvt)
           x4.append(pres)
           y4.append(viscosity)
        chart1 = get_plot1(x1,y1,x11,y11) 
        chart2 = get_plot2(x2,y2) 
        chart3 = get_plot3(x3,y3)        
        chart4 = get_plot4(x4,y4) 
        
        
        return render (request, 'blackoilpvt/blackoilPVT_form.html', {'form': form, 'blackoilpvt':blackoilpvt, 'chart1':chart1, 'chart2':chart2, 'chart3':chart3, 'chart4':chart4})
   return render (request, 'blackoilpvt/blackoilPVT_form.html', {'form': form, 'blackoilpvt': blackoilpvt})

def delete_blackoilpvt(request, id):
    blackoilPVT = BlackoilPVT.objects.get(id=id)
    if request.method == 'POST' :
       blackoilPVT.delete()       
       return redirect ('blackoilpvt:list_blackoilpvt')
    return render (request, 'blackoilpvt/blackoilPVT_confirm_delete.html', {'blackoilPVT':blackoilPVT })

def gas_compressibility_factor(T, P, Pc, Tc, w):
    # Constants
    R = 8.314  # Gas constant
    k = 0.37464 + 1.54226*w - 0.26992*w**2  # Binary interaction parameter
    Tr = T/Tc  # Reduced temperature
    Pr = P/Pc  # Reduced pressure

    # Calculate a, b, and alpha
    a = 0.45724*R**2*Tc**2/Pc
    b = 0.07780*R*Tc/Pc
    alpha = (1 + k*(1 - np.sqrt(Tr)))**2

    # Calculate A, B, and Z
    A = alpha*a*P/(R**2*T**2)
    B = b*P/(R*T)
    Z = np.roots([1, -1, A - B - B**2, -A*B])[np.argmax(np.real(np.roots([1, -1, A - B - B**2, -A*B])))]

    return Z 
 
 
def calculate_Tc_Pc(Tc0, Pc0, w):
    # Constants
    
    R = 8.314  # Gas constant    
    # w accentric factor
    # Tc0: initial guess for critical temperature in Kelvin
    # Pc0: initial guess for critical pressure in Pa

    # Calculate acentric factor parameters
   
    m = 0.480 + 1.574*w - 0.176*w**2
    Tr = Tc0/Pc0

    # Calculate reduced temperature and pressure
    Tr = Tc0/Tc0
    Pr = Pc0/Pc0

    # Calculate parameters
    A = 0.42748*(R**2*Tc0**2.5)/Pc0
    B = 0.08664*R*Tc0/Pc0
    C = 0.187*R**2*Tc0**3/Pc0

    # Calculate constants
    alpha = (1 + m*(1 - np.sqrt(Tr)))**2
    a = (A*alpha)/(R**2*Tc0**2.5)
    b = (B*m)/(R*Tc0)
    c = C/(R**2*Tc0**3)

    # Calculate Zc
    Zc = np.roots([1, -1, (a - b - b**2 - c), (a*b - b**2 - b*c)])[-1]

    # Calculate Pc and Tc
    Pc = Zc*R*Tc0/b
    Tc = (a/(b*R))*(1 + c/a)**(1/3)*(Pc/R)**(2/3)

    return Tc, Pc
 
 
def calculate_Standing_Bo(P, Pb, Rs, T, Bgi):
    Bo = (1 + (0.0004677 * (P - Pb)) - (1.751e-09 * (P - Pb)**2)) * (Rs * (T + 460) / 5.615) / Bgi
    return Bo
def standing_bo(pressure, temperature, rs, oilgravity):
    """
    Standing's correlation for oil formation volume factor (Bo).

    Args:
        pressure (float): pressure in psia
        temperature (float): temperature in °F
        rs (float): solution gas-oil ratio (scf/STB)

    Returns:
        float: oil formation volume factor (Bo) in RB/STB
    """
    pb = 14.7 + 0.036 * pressure
    co = (1.205 * 10**-3) * (rs + 1.25) / (temperature + 460)
    x = 3.14159 * ((0.00000677 * rs * temperature**1.175) / (oilgravity / 141.5))**0.3265
    y = 10**(-x)
    bo = (0.9759 + 1.34 * 10**-4 * (rs * temperature)**1.2) * (1 - co * (pressure - pb)) * y

    return bo
 
def calculate_Vasquez_Beggs_Bo(Rs, T, Pb, Bgi, Gp):
    Bo = (0.001 * (Rs * (T + 460))**1.175) / (Pb**0.515 * (Bgi**1.25 * (1 + 0.001 * (Gp / (Bo * ((T + 460)**1.5)))))**0.5)**1.2
    return Bo
 
def calculate_Glasso_Bo(Rs, T):
    Bo = 0.9759 + (0.00012 * (Rs * T)) - (1.489e-9 * (Rs * T)**2)
    return Bo
 
def calculate_Marhoun_Bo(Rsb, G, Pb, P, API):
    if API > 45:
        m1, m2, m3 = 0.0008, 23.76, 0.972
    elif API >= 35 and API <= 45:
        m1, m2, m3 = 0.0012, 18.16, 0.987
    elif API < 35:
        m1, m2, m3 = 0.0016, 12.94, 1.015
    Bo = (1 + m1 * Rsb) * (m2 * (G - Rsb) / (Pb - P)) ** m3
    return Bo
 
def calculate_Petrosky_Farshad_Bo(Rsb, G, Pb, P, API, SGg):
    if SGg > 0.7 and API < 35:
        m, n, a = 0.0125, 0.9, 0.85
    elif SGg > 0.7 and API >= 35:
        m, n, a = 0.0175, 0.9, 0.85
    elif SGg <= 0.7 and API < 35:
        m, n, a = 0.0125, 1.1, 0.8
    elif SGg <= 0.7 and API >= 35:
        m, n, a = 0.0175, 1.1, 0.8
    Bo = (1 + m * Rsb) * ((Pb / P) ** n) * ((G - Rsb) / ((API / 141.5) ** 0.326)) ** a
    return Bo
 
def calculate_Mccain_Bo(Rsb, Bg, T, Boi, Tbi):
    if Rsb < 200:
        C1, C2, C3, C4 = 1.0113, -1.093e-3, 2.94e-4, -1.38e-6
    elif Rsb < 800:
        C1, C2, C3, C4 = 1.1215, -1.5e-3, 3.6e-4, -2.6e-6
    elif Rsb < 2000:
        C1, C2, C3, C4 = 1.1484, -1.86e-3, 4.42e-4, -3.59e-6
    else:
        C1, C2, C3, C4 = 1.1888, -2.6e-3, 6.05e-4, -5.45e-6

    return C1 * Boi ** C2 * (Rsb / Bg) ** C3 * (T - Tbi) ** C4
 
def Calculate_Chukwu_Bo(Rsb, Bg, T, Boi, Tbi, a, b, c, d, e):
    return (a * Rsb ** b * Boi ** c * (T - Tbi) ** d) / (Bg ** e)