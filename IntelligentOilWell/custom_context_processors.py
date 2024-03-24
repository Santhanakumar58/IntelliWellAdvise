from django.shortcuts import render
from selectedOilProducer.models import SelectedOilProducer
from selectedGasProducer.models import SelectedGasProducer
from selectedWaterInjector.models import SelectedWaterInjector
from selectedGasInjector.models import SelectedGasInjector
from selectedObserver.models import SelectedObserver
from selectedfgi.models import Selectedfgi
from blackoilpvt.models import BlackoilPVT
from math import sqrt, pi, log, sin, cos, radians, log10, e, exp
from PIL import Image
import matplotlib.image as img
import math


def selectedfgi(request):   
    return {'selectedfgi': Selectedfgi.objects.first() }


def selectedwell(request): 
    selectedwell = SelectedOilProducer.objects.all().first()      
    return  {'selectedwell': selectedwell}

def selectedgpwell(request): 
    selectedgpwell = SelectedGasProducer.objects.all().first()      
    return  {'selectedgpwell': selectedgpwell}

def selectedwiwell(request): 
    selectedwiwell = SelectedWaterInjector.objects.all().first()      
    return  {'selectedwiwell': selectedwiwell}

def selectedgiwell(request): 
    selectedgiwell = SelectedGasInjector.objects.all().first()      
    return  {'selectedgiwell': selectedgiwell}

def selectedobwell(request): 
    selectedobwell = SelectedObserver.objects.all().first()      
    return  {'selectedobwell': selectedobwell}

def  PVTwells(request):     
    fgi =Selectedfgi.objects.first()   
    pvt_wells = BlackoilPVT.objects.filter(fgid = fgi.fgid).all()  
    return  {'pvt_wells': pvt_wells}

def tvdCalculation(deviation_datas, md):   
    depth, depth1=0.0, 0.0
    tvd, tvd1=0.0, 0.0
    angle, angle1=0.0, 0.0
    computedtvd, computedangle =0.0, 0.0
    for data in deviation_datas:
        if data.measuredDepth > md:
            depth1 = data.measuredDepth
            angle1 = data.angle
            tvd1 = data.tvd          
            computedtvd = tvd + ((tvd1 - tvd) * (md - depth) / (depth1 - depth))
            computedangle = angle + ((angle1 - angle) * (md - depth) / (depth1 - depth))                                     
            break
        else:
            depth = data.measuredDepth
            angle = data.angle
            tvd = data.tvd           
    return computedtvd, computedangle

def eastCalculation(deviation_datas, md):   
    depth, depth1=0.0, 0.0
    east=0.0
    computedeast=0 
    for data in deviation_datas:
        if data.measuredDepth > md:
            depth1 = data.measuredDepth
            east1 = data.eastWest                   
            computedeast = east + ((east1 - east) * (md - depth) / (depth1 - depth))                                               
            break
        else:
            depth = data.measuredDepth
            east = data.eastWest                  
    return computedeast



def Hagedorn_brown_holdup(p, vsl, vsg, rho_l, mu_l, d, sigma):
    Nvl = round(1.938 * vsl * (rho_l / sigma)**0.25, 3)
    Nvg = round(1.938 * vsg * (rho_l / sigma)**0.25, 3)
    Nd = round(120.872 * (d / 12.0) * (rho_l / sigma)**0.5, 3)
    Nl = round(0.15726 * mu_l * (1.0 / (rho_l * sigma**3))**0.25, 3)

    # Process to calculate the Liquid Holdup
    # fig1= figures('img1.png digital form ')
    NL = [0.00105072,0.000979899,0.001225064,0.001428337,0.001665339,0.001941666,0.002263844,0.00263948,0.003077445	,0.003588081,0.004183446,0.004877599,
          0.005686931,0.006630555,0.007730754,0.009013506,0.010509104,0.012252864,0.014285964,0.016656412	,0.019420186,0.022642549, 0.026399593, 0.030780039, 
          0.035887325, 0.041842056, 0.048784846	, 0.056879643, 0.066317598	, 0.077321579	, 0.090151434, 0.105110127, 0.122550895	, 0.142885583, 0.166594376,
          0.194237134, 0.226466614, 0.264043883, 0.307856293, 0.358938432, 0.418496554, 0.487937066, 0.56889974	,0.663296431, 0.773356224, 0.901678076,0.987298681]	
    
    CNL = [0.001971929, 0.001843194, 0.001967137, 0.00197073, 0.001977935, 0.001997277, 0.002015582 , 0.002041491, 0.002076556, 0.002108372, 0.002139374,
           0.002184076, 0.002233784, 0.002281846, 0.002322451, 0.002373864, 0.002421992, 0.002460597, 0.002515068, 0.002570745, 0.002648513, 0.002748622,
           0.002887426, 0.003040628, 0.003266876, 0.003563736, 0.00386635, 0.004284912, 0.004702797, 0.005189768, 0.005664806, 0.006160802, 0.00669208,
           0.007163834, 0.007710938, 0.008314983, 0.008868718, 0.00945933, 0.01007088, 0.010618133, 0.010906128, 0.011073229, 0.011181514, 0.011222393,
           0.011120474, 0.011073229, 0.011110333 ]   
    for i in range (len(NL)):
        if NL[i] > Nl :  
            x2 = NL[i]
            y2 = CNL[i]              
            CNl =(y1 + (Nl- x1) * (y2 - y1) / (x2 - x1))
            break
        else :
            x1 = NL[i]
            y1 = CNL[i]      
    cons1 = (Nvl* p**0.1 * CNl) / (Nvg**0.575 * p**0.1 * Nd)

    # fig2 = figures('img2.png digital form ')
    CONS1 = [1.14E-07,  1.19E-07,	1.65E-07,	2.29E-07,	3.17E-07,	4.40E-07,	6.10E-07,	8.47E-07,	1.15589E-06,	1.62952E-06,	2.26071E-06,
        3.13638E-06,	4.35124E-06,	6.03667E-06,	8.37494E-06,	1.16189E-05,	1.61195E-05,	2.23632E-05,	3.10255E-05,	4.30431E-05,
        5.97156E-05,	8.28461E-05,	0.000114936,	0.00015478,	0.000199336,	0.000249189,	0.000302375,	0.000361494,	0.000445228,
        0.000548357,	0.000665398,	0.00080742,	0.000979755,	0.001243152,	0.001674105,	0.002322561,	0.003222192,	0.004470291,
        0.006201833,	0.008604079,	0.011936823,	0.016560486,	0.02269194, 0.031874378,	0.044220744,	0.061349407,	0.086174836,
        0.1017536 ]
            
    HLPSI = [ 0.018543563,	0.044182177,	0.027764082,	0.027764082,	0.031868606,	0.033920868,	0.036346268,	0.038025391,	0.035552153,
           0.046980716,	0.053137501,	0.05836144,	0.067689903,	0.08093632,	0.097914122,	0.119183017,	0.145489282,0.174594086,	0.202766043,
           0.23112457,	0.260042804,	0.291946147,	0.331685398,	0.374596327,	0.417437292,	0.460791323,	0.50388882,	0.548354493,
           0.598805929,	0.651993714,	0.700612773,	0.747765931,	0.791205473,	0.836583261,	0.878146745,0.913221765,	0.946057954,
           0.96714028,	0.978147866,	0.983931513,	0.989901729,	0.992327129,	0.997457784,	0.99475253,	0.995312237,	0.996431653,
           0.997329517,	0.998483915]
    for i in range(len(CONS1)):
        if CONS1[i] >cons1 :  
            x2 = CONS1[i]
            y2 = HLPSI[i]              
            Hl_psi =(y1 + (cons1- x1) * (y2 - y1) / (x2 - x1))
            break
        else :
            x1 = CONS1[i]
            y1 = HLPSI[i]          
    cons2 = (Nvg* Nl**0.380) / Nd**2.14        
    # fig3 = figures('img3.png digital form ')
    CONS2 =[ 0.000531304,	0.002826884,	0.005072553,	0.007318222,	0.009564163,	0.011814714,	0.014075303,	0.016333102,	0.018590689,
        0.020852369,	0.023121692,	0.024979059,	0.026122444,	0.027269904,	0.028520376,	0.02956195,	0.031220073,	0.033385892,
        0.035448824,	0.037409137,	0.039472023,	0.041732066,	0.04398565,	0.04623987,	0.048493636,	0.050747765,	0.053000348,	0.055253386,
        0.057505696,	0.059790712,	0.061424551,	0.063445109,	0.065697965,	0.067950457,	0.070202676,	0.072450255,	0.07469738,	0.076944504,
        0.079276158,	0.081437479,	0.083684148,	0.085931636,	0.088178124,	0.090424793,	0.092670644,	0.094916313,	0.097161981,	0.099101422 ]

    PSI2=[ 0.000445568,	0.99829522,	0.99829522,	0.99829522,	0.998816516,	1.00814193,	1.036639469,	1.0598082,	1.082571479,	1.113154204,	1.158333229,
      1.196536811,	1.235789193,	1.282823785,	1.331646921,	1.371404463,	1.418981452,	1.46143236,	1.502336754,	1.542200487,	1.583016068,
      1.610471014,	1.625588611,	1.641922566,	1.657387694,	1.673547884,	1.686754061,	1.700829065,	1.713513945,	1.723679226,1.741120936,
      1.749830931,	1.763558404,	1.776590815,	1.78910193,	1.792751005,	1.795531253,	1.7983115,	1.800072324,	1.801439279,	1.803350699,
      1.806826009,	1.808389898,	1.810301319,	1.81064885,	1.81064885,	1.81064885,	1.81064885 ]

    for i in range(len(CONS2)):
        if  CONS2[i]> cons2:  
            x2 = CONS2[i] 
            y2 = PSI2[i]              
            psi = (y1 + (cons2- x1) * (y2 - y1) / (x2 - x1))
            break
        else :
            x1 = CONS2[i]
            y1 = PSI2[i]

    if psi<1:
        psi=1.0
    Hl = psi * Hl_psi

    return Hl

def griffith_holdup(vsl, vsg):
    vm = vsl+vsg
    factvmbyvs = vm/0.8
    EL = 1-(0.5 * ( 1 + factvmbyvs - sqrt((1+factvmbyvs)**2 - 4*(vsg/0.8))))
    return EL

def fanning_friction_factor_chen (nre, epsi,D):
    flam = 16/nre
    factor1 = -4.0 * log10(0.2698 * (epsi/(D/12))-(5.0452/nre)*log10(0.3539*(epsi/(D/12)**1.1098)+ 5.8506/(nre**0.8981)))
    sqrtf = 1/factor1
    fturb = sqrtf**2
    if nre <=2100:
        f = flam
    elif nre >=4000:
        f= fturb            
    else:
        f = (flam(4000-nre) + fturb*(nre-2000))/2000

    return f

def single_phase_liquid_grad(ql, liquid_density, liquid_vis, A, epsi, D, theta):
    v = ql*5.6145833/(A* 86400)
    nre = 1488 *liquid_density*v*(D/12)/liquid_vis
    flam = 16/nre
    factor1 = -4.0 * log10(0.2698 * (epsi/(D/12))-(5.0452/nre)*log10(0.3539*(epsi/(D/12)**1.1098)+ 5.8506/(nre**0.8981)))
    sqrtf = 1/factor1
    fturb = sqrtf**2
    if nre <=2100:
        f = flam
    elif nre >=4000:
        f= fturb            
    else:
        f = (flam(4000-nre) + fturb*(nre-2000))/2000        
    grad_pe = ((32.17 / 32.17) * (liquid_density *  (cos(radians(theta))))) / 144.0
    grad_f = ((2.0 * f * liquid_density * v**2) / (32.17 * (D / 12.0))) / 144.0
    total_grad = (grad_pe + grad_f)

    return total_grad

def hagedorn_and_brown(ql, qg, p, vsl, vsg, uo, ug, pho_o, pho_g,d, sigma, epsi, l, theta) -> float:
    # Mix velocity
    vm = vsl + vsg
    # Cross sectional area
    A = ((pi / 4) * d**2) / 144.0
    # Fluids flow rates
    ql = vsl * A
    qg = vsg * A
    # print (f"ql = {ql}, qg = {qg}")
    # Determine flow regime
    Lb = 1.071 - 0.2218 * (vm**2 / (6.0/12.0))
    liq = vsl*A
    gas = vsg*A
    holdup_gas = gas/(gas+liq)
    holdup_liq = 1 - holdup_gas
    pho_n = pho_o * holdup_liq + pho_g * (1 - holdup_liq)
    if Lb < 0.13:
        Lb = 0.13
    if holdup_gas <Lb:
        vm = vsl+vsg
        factvmbyvs = vm/0.8
        EL = 1-(0.5 * ( 1 + factvmbyvs - sqrt((1+factvmbyvs)**2 - 4*(vsg/0.8))))
        print('The Griffith is used')      
        print(f"Holdup = {EL}") 
        vl = vsl/EL
        nre = 1488 * pho_o * vl*(d/12)/uo
        # nre = 1488 *liquid_density*v*(D/12)/liquid_vis
        pho_m = pho_o * EL + pho_g * (1 - EL)
         # Friction factor
        flam = 16/nre
        factor1 = -4.0 * log10(0.2698 * (epsi/(d/12))-(5.0452/nre)*log10(0.3539*(epsi/(d/12)**1.1098)+ 5.8506/(nre**0.8981)))
        sqrtf = 1/factor1
        fturb = sqrtf**2
        if nre <=2100:
            f = flam
        elif nre >=4000:
            f= fturb            
        else:
            f = (flam(4000-nre) + fturb*(nre-2000))/2000 
        #f = (1.0 / (1.14 - 2.0 * log10((epsi / (d / 12.0)) + (21.25 / nre**0.9))))**2
        pho_f = pho_n**2 / pho_m
        # Pressure gradient due to potential energy
        grad_pe = ((32.17 / 32.17) * (pho_m * cos(radians(theta))))/ 144.0
        # Pressure gradiente due to friction
        grad_f = ((2.0 * f * pho_f * vm**2) / (32.17 * (d / 12.0))) / 144.0
        print(grad_f, grad_pe)
        dp_total = round((grad_pe + grad_f) * l, 2)
    else :
        print('The Hagedorn & Brown correlation is used')  
        # Calculate the 4 four dimensionless numbers
        Nvl = round(1.938 * vsl * (pho_o / sigma)**0.25, 3)
        Nvg = round(1.938 * vsg * (pho_o / sigma)**0.25, 3)
        Nd = round(120.872 * (d / 12.0) * (pho_o / sigma)**0.5, 3)
        Nl = round(0.15726 * uo * (1.0 / (pho_o * sigma**3))**0.25, 3)

        # Process to calculate the Liquid Holdup
        # fig1= figures('img1.png digital form ')
        NL = [0.00105072,0.000979899,0.001225064,0.001428337,0.001665339,0.001941666,0.002263844,0.00263948,0.003077445	,0.003588081,0.004183446,0.004877599,
              0.005686931,0.006630555,0.007730754,0.009013506,0.010509104,0.012252864,0.014285964,0.016656412	,0.019420186,0.022642549, 0.026399593, 0.030780039, 
              0.035887325, 0.041842056, 0.048784846	, 0.056879643, 0.066317598	, 0.077321579	, 0.090151434, 0.105110127, 0.122550895	, 0.142885583, 0.166594376,
              0.194237134, 0.226466614, 0.264043883, 0.307856293, 0.358938432, 0.418496554, 0.487937066, 0.56889974	,0.663296431, 0.773356224, 0.901678076,0.987298681]	
        
        CNL = [0.001971929, 0.001843194, 0.001967137, 0.00197073, 0.001977935, 0.001997277, 0.002015582 , 0.002041491, 0.002076556, 0.002108372, 0.002139374,
               0.002184076, 0.002233784, 0.002281846, 0.002322451, 0.002373864, 0.002421992, 0.002460597, 0.002515068, 0.002570745, 0.002648513, 0.002748622,
               0.002887426, 0.003040628, 0.003266876, 0.003563736, 0.00386635, 0.004284912, 0.004702797, 0.005189768, 0.005664806, 0.006160802, 0.00669208,
               0.007163834, 0.007710938, 0.008314983, 0.008868718, 0.00945933, 0.01007088, 0.010618133, 0.010906128, 0.011073229, 0.011181514, 0.011222393,
               0.011120474, 0.011073229, 0.011110333 ]   
        for i in range (len(NL)):
            if NL[i] > Nl :  
                x2 = NL[i]
                y2 = CNL[i]              
                CNl =(y1 + (Nl- x1) * (y2 - y1) / (x2 - x1))
                break
            else :
                x1 = NL[i]
                y1 = CNL[i]      

        cons1 = (Nvl* p**0.1 * CNl) / (Nvg**0.575 * p**0.1 * Nd)

        # fig2 = figures('img2.png digital form ')
        CONS1 = [1.14E-07,  1.19E-07,	1.65E-07,	2.29E-07,	3.17E-07,	4.40E-07,	6.10E-07,	8.47E-07,	1.15589E-06,	1.62952E-06,	2.26071E-06,
            3.13638E-06,	4.35124E-06,	6.03667E-06,	8.37494E-06,	1.16189E-05,	1.61195E-05,	2.23632E-05,	3.10255E-05,	4.30431E-05,
            5.97156E-05,	8.28461E-05,	0.000114936,	0.00015478,	0.000199336,	0.000249189,	0.000302375,	0.000361494,	0.000445228,
            0.000548357,	0.000665398,	0.00080742,	0.000979755,	0.001243152,	0.001674105,	0.002322561,	0.003222192,	0.004470291,
            0.006201833,	0.008604079,	0.011936823,	0.016560486,	0.02269194, 0.031874378,	0.044220744,	0.061349407,	0.086174836,
            0.1017536 ]
                
        HLPSI = [ 0.018543563,	0.044182177,	0.027764082,	0.027764082,	0.031868606,	0.033920868,	0.036346268,	0.038025391,	0.035552153,
               0.046980716,	0.053137501,	0.05836144,	0.067689903,	0.08093632,	0.097914122,	0.119183017,	0.145489282,0.174594086,	0.202766043,
               0.23112457,	0.260042804,	0.291946147,	0.331685398,	0.374596327,	0.417437292,	0.460791323,	0.50388882,	0.548354493,
               0.598805929,	0.651993714,	0.700612773,	0.747765931,	0.791205473,	0.836583261,	0.878146745,0.913221765,	0.946057954,
               0.96714028,	0.978147866,	0.983931513,	0.989901729,	0.992327129,	0.997457784,	0.99475253,	0.995312237,	0.996431653,
               0.997329517,	0.998483915]

        for i in range(len(CONS1)):
            if CONS1[i] >cons1 :  
                x2 = CONS1[i]
                y2 = HLPSI[i]              
                Hl_psi =(y1 + (cons1- x1) * (y2 - y1) / (x2 - x1))
                break
            else :
                x1 = CONS1[i]
                y1 = HLPSI[i]          
        cons2 = (Nvg* Nl**0.380) / Nd**2.14        
        # fig3 = figures('img3.png digital form ')
        CONS2 =[ 0.000531304,	0.002826884,	0.005072553,	0.007318222,	0.009564163,	0.011814714,	0.014075303,	0.016333102,	0.018590689,
            0.020852369,	0.023121692,	0.024979059,	0.026122444,	0.027269904,	0.028520376,	0.02956195,	0.031220073,	0.033385892,
            0.035448824,	0.037409137,	0.039472023,	0.041732066,	0.04398565,	0.04623987,	0.048493636,	0.050747765,	0.053000348,	0.055253386,
            0.057505696,	0.059790712,	0.061424551,	0.063445109,	0.065697965,	0.067950457,	0.070202676,	0.072450255,	0.07469738,	0.076944504,
            0.079276158,	0.081437479,	0.083684148,	0.085931636,	0.088178124,	0.090424793,	0.092670644,	0.094916313,	0.097161981,	0.099101422 ]
    
        PSI2=[ 0.000445568,	0.99829522,	0.99829522,	0.99829522,	0.998816516,	1.00814193,	1.036639469,	1.0598082,	1.082571479,	1.113154204,	1.158333229,
          1.196536811,	1.235789193,	1.282823785,	1.331646921,	1.371404463,	1.418981452,	1.46143236,	1.502336754,	1.542200487,	1.583016068,
          1.610471014,	1.625588611,	1.641922566,	1.657387694,	1.673547884,	1.686754061,	1.700829065,	1.713513945,	1.723679226,1.741120936,
          1.749830931,	1.763558404,	1.776590815,	1.78910193,	1.792751005,	1.795531253,	1.7983115,	1.800072324,	1.801439279,	1.803350699,
          1.806826009,	1.808389898,	1.810301319,	1.81064885,	1.81064885,	1.81064885,	1.81064885 ]
   
        for i in range(len(CONS2)):
            if  CONS2[i]> cons2:  
                x2 = CONS2[i] 
                y2 = PSI2[i]              
                psi = (y1 + (cons2- x1) * (y2 - y1) / (x2 - x1))
                break
            else :
                x1 = CONS2[i]
                y1 = PSI2[i]
    
        if psi<1:
            psi=1.0
        Hl = psi * Hl_psi
        # Mix density
        #print(f"hl = {Hl}")
        pho_m = pho_o * Hl + pho_g * (1 - Hl)
        #print(f"miser density {pho_m}, oil density = {pho_o} gas density = {pho_g}")
        # Mix viscosity
        um = uo**Hl * ug**(1 - Hl)
        vl = vsl/Hl
        # Reynolds Number
        nre = (1488 * pho_n* vl * (d/12)) / um
        # Friction factor
        f = (1.0 / (1.14 - 2.0 * log10((epsi / (d / 12.0)) + (21.25 / nre**0.9))))**2
        pho_f = pho_n**2 / pho_m
        # Pressure gradient due to potential energy
        grad_pe = ((32.17 / 32.17) * (pho_m * cos(radians(theta))))/ 144.0
        # Pressure gradiente due to friction
        grad_f = ((2.0 * f * pho_f * vm**2) / (32.17 * (d / 12.0))) / 144.0
        print(grad_f, grad_pe)
        dp_total = round((grad_pe + grad_f) * l, 2)
    return dp_total

def beggs_and_brills(qo,uo, ug, pho_0, pho_g, d, sigma, epsi, l, theta, qg, gor):
    A = (pi * (d / 2.0)**2) / 144.0
    Vsl = (qo * 5.615) / (A * 86400)
    Vsg = qg /(A*86400)   
    Vm = Vsl + Vsg
    holdup_l = Vsl / Vm
    Nfr = Vm**2 / (32.2 * (d/12.0))
    L1 = 316.0 * holdup_l**0.302
    L2 = 0.0009252 * holdup_l**-2.4684
    L3 = 0.10 * holdup_l**(-1.4516)
    L4 = 0.51 * holdup_l**-6.738
    if ((0.001 <= holdup_l < 0.4) and (L3 < Nfr < L1)) or (holdup_l >= 0.001 and Nfr <= L2):
        fr = 'The flow regime is intermitent'
        Hlo = (0.845 * holdup_l**0.5351) / Nfr**0.0173
        Nvl = 1.938 * Vsl * (pho_0 / sigma)**0.25
        C = (1 - holdup_l) * \
        log(2.96 * holdup_l**0.305 * Nvl**-0.4473 * Nfr**0.0978)
        cons = 1 + C * (sin(radians(1.8*theta)) - 0.333 * sin(radians(1.8*theta))**3)
        Hl = cons * Hlo
    elif (holdup_l < 0.01 and Nfr < L1) or (holdup_l >= 0.01 and Nfr <= L2):
        fr = 'The flow regime is segregated'
        Hlo = (0.98 * holdup_l**0.4846) / Nfr**0.0868
        Nvl = 1.938 * Vsl * (pho_0 / sigma)**0.25
        C = (1 - holdup_l) * \
        log(0.011 * holdup_l**-3.5868 * Nvl**3.519 * Nfr**-1.614)
        cons = 1 + C * (sin(radians(1.8*theta)) - 0.333 * sin(radians(1.8*theta))**3)
        Hl = cons * Hlo
    elif (holdup_l < 0.04 and Nfr >= L1) or (holdup_l >= 0.4 and Nfr > L4):
        fr = 'The flow regime is Distributed'
        Hlo = (1.065 * holdup_l**0.5824) / Nfr**0.0609
        C = 0
        cons = 1
        Hl = cons * Hlo
    elif (holdup_l >= 0.01) and (L2 < Nfr <= L3):
        fr = 'The flow regime is Transition'
        A = (L3 - Nfr) / (L3 - L2)
        B = 1 - A
        Hlo_seg = (0.98 * holdup_l ** 0.4846) / Nfr ** 0.0868
        Hlo_inter = (0.845 * holdup_l ** 0.5351) / Nfr ** 0.0173
        Nvl = 1.938 * Vsl * (pho_0 / sigma) ** 0.25
        C_seg = (1 - holdup_l) * \
            log(0.011 * holdup_l ** -3.5868 * Nvl ** 3.519 * Nfr ** -1.614)
        C_inter = (1 - holdup_l) * \
            log(2.96 * holdup_l ** 0.305 * Nvl ** -0.4473 * Nfr ** 0.0978)
        cons_seg = 1 + C_seg * (sin(radians(1.8 * theta)) - 0.333 * sin(radians(1.8 * theta)) ** 3)
        cons_inter = 1 + C_inter * (sin(radians(1.8 * theta)) - 0.333 * sin(radians(1.8 * theta)) ** 3)
        Hl_seg = cons_seg * Hlo_seg
        Hl_inter = cons_inter * Hlo_inter
        Hl = A * Hl_seg + B * Hl_inter
    pho_m = pho_0 * Hl + pho_g * (1 - Hl)
    grad_pe = ((32.2 / 32.2) * pho_m * (sin(radians(theta)))) / 144
    pho_n = pho_0 * holdup_l + pho_g * (1 - holdup_l)
    u_n = uo * holdup_l + ug * (1 - holdup_l)
    Nre_m = (1488 * pho_n * Vm * (d / 12)) / u_n
    f = (1 / (1.14 - 2 * log10((epsi / (d / 12)) + (21.25 / Nre_m**0.9))))**2
    x = holdup_l / (Hl**2)
    s = log(x) / (-0.0523 + 3.182 * log(x) - 0.08725 * \
                      (log(x))**2 + 0.01853 * (log(x))**4)
    ftp = f * e**s
    grad_f = (2.0 * ftp * pho_n * Vm**2) / (32.2 * (d / 12) * 144)
    print(grad_f)
    grad_total = round(grad_pe + grad_f, 4)
    dp_total = round(grad_total * l, 3)
    print(f' the total gradient is: {dp_total} psia')
    return  dp_total

def gray_oil (qo, qw, vsl, vsg, rho_liq, rho_gas, vis_liq, vis_gas, sigma_oil, sigma_water,d, theta, epsi):
    k=epsi
    vm = vsg+vsl
    CL = vsl/vm
    CG = vsg/vm
    rho_mixer_noslip = rho_liq * CL + rho_gas * (1-CL)
    vis_mixer_noslip = vis_liq * CL + vis_gas*(1-CL)
    alpha = 0.00220462  # (lbg/s2)/(dynes/cm)
    sigma_liq = alpha *( (qo*sigma_oil) + 0.617 *(qw * sigma_water))/(qo+0.617*qw)
    Rv = vsl/vsg
    N1 = rho_mixer_noslip**2 * vm**4 /(32.2 * sigma_liq *(rho_liq - rho_gas) )
    N2 = 32.2 * d**2 * (rho_liq-rho_gas)/sigma_liq
    N3 = 0.0814 * (1-0.0554* log(1+(730* Rv)/(Rv+1)))
    f1 = -2.314 * (N1 *(1+205/N2))**N3
    EL = 1-(1-CL)*(1-exp(f1))
    rho_mixer = rho_liq * EL + rho_gas * (1-EL)
    vis_mixer = vis_liq * EL + vis_gas *(1-EL)
    k0 = 28.5 * sigma_liq /(rho_mixer_noslip * vm**2)
    if Rv >=0.007 :
        ke = k0
    else:
        ke = k + Rv*((k0-k)/0.007)    
    if ke <= 2.77e-5:
        ke = 2.77e-5
    ftp = 16/107
    delphh = rho_mixer * (32.2/32.2) * cos(radians(theta))/144
    delpf = 2 *ftp * vm**2 * rho_mixer_noslip/(144* 32.2* (d/12))
    totaldelp = delphh+delpf

    return delphh, delpf, totaldelp

def petalas_and_aziz(vsl, vsg):
    vm = vsl+vsg
    bamea = 1 /(1 + (vm/8.66)** 1.39)
    vsgbyvm = vsg/vm

    return 


def ql(qo, Bo, qw, Bw):
    return (qo*Bo)+(qw*Bw)

def qgfree (qg, qo, Rs):
    return qg-(qo*Rs)

def svsl(ql,D):
    return (ql*5.6145833/((pi/4)* D**2))/86400

def svsg(qgfree,Bg, D):
    return (qgfree*Bg/((pi/4)* D**2))/86400

def vm(vsl, vsg):
    return vsl+vsg

def liquidvolumefraction(ql, qg, Bg):
    return ql/(ql+qg*Bg)

def gasvolumefraction(ql, qg, Bg):
    return qg*Bg/(ql+qg*Bg)

def mixerdensity(liquiddensity, gasdensity, holdup):
    return liquiddensity*holdup + gasdensity*(1-holdup)

def Noslipmixerdensity(liquiddensity, gasdensity, liquidvolumefraction):
    return liquiddensity*liquidvolumefraction + gasdensity*(1-liquidvolumefraction)

def mixerviscosity(liquidviscosity, gasviscosity, holdup):
    return liquidviscosity*holdup + gasviscosity*(1-holdup)

def Noslipmixerviscosity(liquidviscosity, gasviscosity, liquidvolumefraction):
    return liquidviscosity*liquidvolumefraction + gasviscosity*(1-liquidvolumefraction)

def Pbub(T, Tsep, Psep, gas_grav, oil_grav, Gor):
    """ CFunction to Calculate Bubble Point Pressure in psia using Standing Correlation"""
    #T          temperature, °F
    #Tsep       separator temperature, °F
    #Psep       separator pressure, psia
    #gas_grav   gas specific gravity
    #oil_grav   API oil gravity
    #Gor        producing gas-oil ratio, scf/stb
    gas_grav_corr = correct(Tsep, Psep, gas_grav, oil_grav)
    if (oil_grav<= 30) :
        C1 = 0.0362
        C2 = 1.0937
        C3 = 25.724
    else:
        C1 = 0.0178
        C2 = 1.187
        C3 = 23.931
    
    Pbubl = (Gor / (C1 * gas_grav_corr * math.exp(C3 * oil_grav / (T + 460)))) **(1 / C2)
    return Pbubl

def correct(Tsep, Psep, gas_grav, oil_grav):
    """Function to Calculate Corrected Gas Gravity"""
    #Tsep       separator temperature, °F
    #Psep       separator pressure, psia
    #gas_grav   gas specific gravity
    #oil_grav   API oil gravity

    return  gas_grav * (1 + 5.912 * 10 ** -5 * oil_grav * Tsep * math.log10(Psep / 114.7) / math.log(10))

def sol_gor(T, P, Tsep, Psep, Pb, gas_grav, oil_grav):
    """Function to Calculate Solution Gas-Oil Ratio in scf/stb"""
    #T          temperature, °F
    #P          pressure, psia
    #Tsep       separator temperature, °F
    #Psep       separator pressure, psia
    #Pb         bubble point pressure, psia
    #gas_grav   gas specific gravity
    #oil_grav   API oil gravity
    gas_grav_corr = correct(Tsep, Psep, gas_grav, oil_grav)
    if (oil_grav <= 30):
        C1 = 0.0362
        C2 = 1.0937
        C3 = 25.724
    else:
        C1 = 0.0178
        C2 = 1.187
        C3 = 23.931
    
    if (P <= Pb):
        Rs = C1 * gas_grav_corr * P** C2 * math.exp(C3 * oil_grav / (T + 460))
    else:
        Rs = C1 * gas_grav_corr * Pb ** C2 * math.exp(C3 * oil_grav / (T + 460))
    
    return Rs

def oil_fvf(T, P, Tsep, Psep, Pb, Rs, gas_grav, oil_grav):
    """Function to Calculate Oil Formation Volume Factor in bbl/stb"""
    #'T          temperature, °F
    #P          pressure, psia
    #Tsep       separator temperature, °F
    #Psep       separator pressure, psia
    #Pb         bubble point pressure, psia
    #Rs         solution gas-oil ratio, scf/stb
    #gas_grav   gas specific gravity
    #oil_grav   API oil gravity
    gas_grav_corr = correct(Tsep, Psep, gas_grav, oil_grav)
    if (oil_grav <= 30) :
        C1 = 0.0004677
        C2 = 1.751E-05
        C3 = -1.811E-08
    else:
        C1 = 0.000467
        C2 = 1.1E-05
        C3 = 1.337E-09
    

    if (P <= Pb):
        Bo = 1 + C1 * Rs + C2 * (T - 60) * (oil_grav / gas_grav_corr) + C3 * Rs * (T - 60) * (oil_grav / gas_grav_corr)
    else:
        Bob = 1 + C1 * Rs + C2 * (T - 60) * (oil_grav / gas_grav_corr)+ C3 * Rs * (T - 60) * (oil_grav / gas_grav_corr)
        co = oil_comp(T, P, Tsep, Psep, Rs, gas_grav, oil_grav)
        Bo = Bob * math.exp(co * (Pb - P))
    
    return  Bo

def oil_comp(T, P, Tsep, Psep, Rs, gas_grav, oil_grav):
    """Function to Calculate Oil Isothermal Compressibility in 1/psi"""
    #'T          temperature, °F
    #'P          pressure, psia
    #'Tsep       separator temperature, °F
    #'Psep       separator pressure, psia
    #'Rs         solution gas-oil ratio, scf/stb
    #'gas_grav   gas specific gravity
    #'oil_grav   API oil gravity
    
    gas_grav_corr = correct(Tsep, Psep, gas_grav, oil_grav)
    oil_compr = (5 * Rs + 17.2 * T - 1180 * gas_grav_corr + 12.61 * oil_grav - 1433) / (P * 10 ** 5)
    return oil_compr

def oil_visc(T, P, Tsep, Psep, Pb, Rs, gas_grav, oil_grav):
    """Function to Calculate Oil Viscosity in cp"""
    #'T          temperature, °F
    #'P          pressure, psia
    #'Tsep       separator temperature, °F
    #'Psep       separator pressure, psia
    #'Pb         bubble point pressure, psia
    #'Rs         solution gas-oil ratio, scf/stb
    #'gas_grav   gas specific gravity
    #'oil_grav   API oil gravity
    
    a = 10.715 * (Rs + 100) ** (-0.515)
    b = 5.44 * (Rs + 150) ** (-0.338)
    Z = 3.0324 - 0.0203 * oil_grav
    Y = 10 **Z
    x = Y * T ** (-1.163)
    visc_oD = 10 ** x - 1
    if (P <= Pb):
        visc_o = a * visc_oD ** b
    else:
        M = 2.6 * P ** 1.187 * math.exp(-11.513 - 8.98E-05 * P)
        visc_ob = a * visc_oD ** b
        visc_o = visc_ob * (P / Pb) ** M

    return visc_o

def oil_dens(T, P, Tsep, Psep, Pb, Bo, Rs, gas_grav, oil_grav):
    """Function to Calculate Oil Density in lb/ft"""
    #'T          temperature, °F
    #'P          pressure, psia
    #'Tsep       separator temperature, °F
    #'Psep       separator pressure, psia
    #'Pb         bubble point pressure, psia
    #'Bo         oil formation volume factor, bbl/stb
    #'Rs         solution gas-oil ratio, scf/stb
    #'gas_grav   gas specific gravity
    #'oil_grav   API oil gravity
    oil_grav_sp = 141.5 / (oil_grav + 131.5)
    if (P <= Pb):
        rho_o = (350 * oil_grav_sp + 0.0764 * gas_grav * Rs) / (5.615 * Bo)
    else:
        co = oil_comp(T, P, Tsep, Psep, Rs, gas_grav, oil_grav)
        Bob = Bo / (math.exp(co * (P - Pb)))
        rho_ob = (350 * oil_grav_sp + 0.0764 * gas_grav * Rs) / (5.615 * Bob)
        rho_o = rho_ob * Bo / Bob
    
    return rho_o

def oil_sigma(P, T, oil_grav):
    """Function to Calculate Gas-Oil Interfacial Tension in dynes/cm"""
    #P          pressure, psia
    #T          temperature, °F
    #oil_grav   API oil gravity
    s68 = 39 - 0.2571 * oil_grav
    s100 = 37.5 - 0.2571 * oil_grav
    if (T <= 68):
        st = s68
    elif(T >= 100):
        st = s100
    else:
        st = s68 - (T - 68) * (s68 - s100) / 32
    
    c = 1 - 0.024 * P ** 0.45
    so = c * st
    if (so < 1):
        so = 1
    
    return so

def Tc(grav):
    """Function to Calculate Gas Critical Temperature in °R"""
    #grav       gas specific gravity
    return 169.2 + 349.5 * grav - 74 * grav ** 2

def Pc(grav):
    """Function to Calculate Gas Critical Pressure in psia"""
    #grav       gas specific gravity
    return 756.8 - 131 * grav - 3.6 * grav**2

def zfact(Tr, Pr):
    """Function to Calculate Gas Compressibility Factor"""
    #'Tr         reduced temperatue
    #'Pr         reduced pressure
    a = 1.39 * (Tr - 0.92) ** 0.5 - 0.36 * Tr - 0.101
    b = (0.62 - 0.23 * Tr) * Pr + (0.066 / (Tr - 0.86) - 0.037) * Pr ** 2 + 0.32 * Pr ** 6 / (10** (9 * (Tr - 1)))
    c = (0.132 - 0.32 * math.log10(Tr))
    d = 10 ** (0.3106 - 0.49 * Tr + 0.1824 * Tr **2)
    zfact = a + (1 - a) * math.exp(-b) + c * Pr **d
    return zfact

def gvisc(P, T, Z, grav):
    """Function to Calculate Gas Viscosity in cp"""
    #P          pressure, psia
    #T          temperature, °R
    #Z          gas compressibility factor
    #grav       gas specific gravity
    M = 28.964 * grav
    x = 3.448 + 986.4 / T + 0.01009 * M
    Y = 2.447 - 0.2224 * x
    rho = (1.4926 / 1000) * P * M / Z / T
    if Y<0 or rho<0:
       print ('epa')
    K = (9.379 + 0.01607 * M) * T ** 1.5 / (209.2 + 19.26 * M + T)
 
    return K * math.exp(x * rho ** Y) / 10000

def gas_fvf(P, T, grav):
    """Function to Calculate Gas Formation Volume Factor in ft_/scf"""
    #P          pressure, psia
    #T          temperature,°F
    #grav       gas specific gravity
    Tr = (T + 460) / Tc(grav)
    Pr = P / Pc(grav)
    Z = zfact(Tr, Pr)
    return 0.0283 * Z * (T + 460) / P

def gas_dens(P, T, z, grav):
    """Function to Calculate gas density in lbm/cu. ft"""
    #P          pressure, psia
    #T          temperature,°F
    #grav       gas specific gravity
    # z         compressibility factor (zfactor)
    rhog = 28.96*grav*P/(z*10.732 *(T+459.67))
    return rhog

def wtr_fvf(P, T, TDS):
    """Function to Calculate Water Formation Volume Factor in bbl/stb"""
    #P          pressure, psia
    #T          temperature, °F
    #TDS        total dissolved solids, wt%
    Y = 10000 * TDS
    x = 5.1 * 10 ** -8 * P + (T - 60) * (5.47 * 10 ** -6 - 1.95 * 10 ** -10 * P) + (T - 60) ** 2 * (-3.23 * 10 ** -8 + 8.5 * 10 ** -13 * P)
    C1 = 0.9911 + 6.35E-05 * T + 8.5 * 10 ** -7 * T ** 2
    C2 = 1.093 * 10 ** -6 - 3.497 * 10 ** -9 * T + 4.57 * 10 ** -12 * T ** 2
    C3 = -5 * 10 ** -11 + 6.429 * 10 ** -13 * T - 1.43 * 10 ** -15 * T ** 2
    Bwp = C1 + C2 * P + C3 * P ** 2
    Bw = Bwp * (1 + 0.0001 * x * Y)
    return Bw

def  sol_gwr(P, T, TDS):
    """Function to Calculate Solution Gas-Water Ratio in scf/stb"""
    #P          pressure, psia
    #T          temperature, °F
    #TDS        total dissolved solids, wt%
    Y = 10000 * TDS
    x = 3.471 * T ** -0.837
    C1 = 2.12 + 0.00345 * T - 3.59E-05 * T ** 2
    C2 = 0.0107 - 5.26E-05 * T + 1.48 * 10 ** -11 * T ** 2
    C3 = -8.75 * 10 ** -7 + 3.9 * 10 ** -9 * T - 1.02 * 10 ** -11 * T ** 2
    Rswp = C1 + C2 * P + C3 * P ** 2
    Rsw = Rswp * (1 - 0.0001 * x * Y)
    return Rsw

def wtr_dens(P, T, Bw, TDS):
    """Function to Calculate Water Density in lb/ft"""
    #P          pressure, psia
    #T          temperature, °F
    #Bw         water formation volume factor, bbl/stb
    #TDS        total dissolved solids, wt%
    rho = (62.368 + 0.438603 * TDS + 1.60074 * 10 ** -3 * TDS ** 2) / Bw
    return rho

def wtr_visc(P, T, TDS):
    """Function to Calculate Water viscosity in cp"""
    #P          pressure, psia
    #T          temperature, °F
    #TDS        total dissolved solids, wt%
    Y = 10000 * TDS
    a = -0.04518 + 9.313 * 10 ** -7 * Y - 3.93 * 10 ** -12 * Y ** 2
    b = 70.634 + 9.576 * 10 ** -10 * Y ** 2
    muwd = a + b / T
    mu = muwd * (1 + 3.5 * 10 ** -12 * P ** 2 * (T - 40))
    return mu

def salinity(wtr_grav):
    """Function to Calculate Water Salinity at 60°F and 1 atm"""
    #wtr_grav   specific gravity of water
    rho = 62.368 * wtr_grav
    a = 0.00160074
    b = 0.438603
    c = 62.368 - rho
    s = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return s

def wtr_sigma(P, T):
    """Function to Calculate Gas-Water Interfacial Tension in dynes/cm"""
    #P          pressure, psia
    #T          temperature, °F
    s74 = 75 - 1.108 * P ** 0.349
    s280 = 53 - 0.1048 * P ** 0.637
    if (T <= 74):
        sw = s74
    elif(T >= 280):
        sw = s280
    else:
        sw = s74 - (T - 74) * (s74 - s280) / 206
    
    if (sw < 1):
        sw = 1
    
    return sw

def linear_interpolation ( x,x1,y1, x2,y2):
    y = y1+((x-x1)*(y2-y1)/(x2-x1))
    return y



# Productivity Index (darcy law)
def j_darcy(ko, h, bo, uo, re, rw, s, flow_regime = 'seudocontinuo'):
    if flow_regime == 'seudocontinuo':
        J_darcy = ko * h / (141.2 * bo * uo * (log(re / rw) - 0.75 + s))
    elif flow_regime == 'continuo':
        J_darcy = ko * h / (141.2 * bo * uo * (log(re / rw) + s))
    return J_darcy 

# Productivity Index
def j(q_test, pwf_test, pr, pb, ef=1, ef2=None):
    if ef == 1:
        if pwf_test >= pb:
            J = q_test / (pr - pwf_test)
        else:
            J = q_test / ((pr - pb) + (pb / 1.8) * (1 - 0.2 * (pwf_test / pb) - 0.8 * (pwf_test / pb)**2))
    elif ef != 1 and ef2 is None:
        if pwf_test >= pb:
            J = q_test / (pr - pwf_test)
        else:
            J = q_test / ((pr - pb) + (pb / 1.8) * (1.8 * (1 - pwf_test / pb) - 0.8 * ef * (1 - pwf_test / pb)**2))
    elif ef !=1 and ef2 is not None:
        if pwf_test >= pb:
            J = (q_test / (pr - pwf_test) / ef) * ef2
        else:
            J = (q_test / ((pr - pb) + (pb / 1.8) * (1.8 * (1 - pwf_test / pb) - 0.8 * ef * (1 - pwf_test / pb)**2)) / ef) * ef2
    return J

# Q(bpd) @ Pb 
def Qb(q_test, pwf_test, pr, pb, ef=1, ef2=None):
    qb = j(q_test, pwf_test, pr, pb, ef, ef2) * (pr - pb)
    return qb

# Qo (bpd) @ Darcy Conditions
def qo_darcy(q_test, pwf_test, pr, pwf, pb):
    qo = j(q_test, pwf_test, pr, pb) * (pr - pwf)
    return qo

#Qo(bpd) @ vogel conditions
def qo_vogel(q_test, pwf_test, pr, pwf, pb):
    if pr > pb: # Yac. subsaturado
        if pwf >= pb:
            qo = qo_darcy(q_test, pwf_test, pr, pwf, pb)
        elif pwf < pb: 
            qo =  Qb(q_test, pwf_test, pr, pb) + ((j(q_test, pwf_test, pr, pb) * pb) / (1.8)) * \
            (1 - 0.2 * (pwf / pb) - 0.8 * ( pwf / pb)**2)
    elif pr <= pb: # Yac. Saturado
        qo = aof(q_test, pwf_test, pr, pb) * (1 - 0.2 * (pwf / pr) - 0.8 * ( pwf / pr)**2)
    return qo


# Qo (bpd) @ Standing conditions
def qo_standing(q_test, pwf_test, pr, pwf, pb, ef, ef2=None):
    if (ef < 1 and ef2 is None):
        if pr > pb:
            if pwf >= pb:
                qo = qo_darcy(q_test, pwf_test, pr, pwf, pb)
            elif pwf < pb:
                qo = Qb(q_test, pwf_test, pr, pb, ef) + ((j(q_test, pwf_test, pr, pb, ef) * pb) / (1.8)) * \
                (1.8 * (1 - pwf / pb) - 0.8 * ef * (1 - pwf / pb)**2)
        elif pr <= pb:
            qo = q_test / (1.8 * ef * (1 - pwf_test/pr) - 0.8 * ef**2 * (1 - pwf_test/pr)**2) * \
            (1.8 * ef * (1 - pwf / pr) - 0.8 * ef**2 * (1 - pwf / pr)**2)
    elif (ef > 1 and ef2 is None):
        if pr > pb:
            if pwf >= pb:
                qo = qo_darcy(q_test, pwf_test, pr, pwf, pb)
            elif pwf < pb:
                qo = Qb(q_test, pwf_test, pr, pb, ef) + ((j(q_test, pwf_test, pr, pb, ef) * pb) / (1.8)) * \
            (1.8 * (1 - pwf / pb) - 0.8 * ef * (1 - pwf / pb)**2)
        elif pr <= pb:
            qo = q_test / (1.8 * ef * (1 - pwf_test/pr) - 0.8 * ef**2 * (1 - pwf_test/pr)**2) * \
            (1.8 * ef * (1 - pwf / pr) - 0.8 * ef**2 * (1 - pwf / pr)**2)
    elif (ef < 1 and ef2 >= 1):
        if pr > pb:
            if pwf >= pb:
                qo = qo_darcy(q_test, pwf_test, pr, pwf, pb)
            elif pwf < pb:
                qo = Qb(q_test, pwf_test, pr, pb, ef, ef2) + ((j(q_test, pwf_test, pr, pb, ef, ef2) * pb) / (1.8)) * \
                (1.8 * (1 - pwf / pb) - 0.8 * ef2 * (1 - pwf / pb)**2)
        elif pr <= pb:
             qo = q_test / (1.8 * ef * (1 - pwf_test/pr) - 0.8 * ef**2 * (1 - pwf_test/pr)**2) * \
                (1.8 * ef2 * (1 - pwf / pr) - 0.8 * ef2**2 * (1 - pwf / pr)**2)
    elif (ef > 1 and ef2 <= 1):
        if pr > pb:
            if pwf >= pb:
                qo = qo_darcy(q_test, pwf_test, pr, pwf, pb)
            elif pwf < pb:
                qo = Qb(q_test, pwf_test, pr, pb, ef, ef2) + ((j(q_test, pwf_test, pr, pb, ef, ef2) * pb) / (1.8)) * \
            (1.8 * (1 - pwf / pb) - 0.8 * ef2 * (1 - pwf / pb)**2)
        elif pr <= pb:
            qo = q_test / (1.8 * ef * (1 - pwf_test/pr) - 0.8 * ef**2 * (1 - pwf_test/pr)**2) * \
            (1.8 * ef2 * (1 - pwf / pr) - 0.8 * ef2**2 * (1 - pwf / pr)**2)
    return qo

# Qo (bpd) @ any condition
def Qo(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None):
    if (ef == 1 and ef2 is None):
        if pr > pb:
            if pwf >= pb:
                qo = qo_darcy(q_test, pwf_test, pr, pwf, pb)
            elif pwf < pb:
                qo = qo_vogel(q_test, pwf_test, pr, pwf, pb)
        elif pr <= pb:
            qo = qo_vogel(q_test, pwf_test, pr, pwf, pb)
    elif ((ef < 1 or ef > 1) and ef2 is None):
        if pr > pb:
            if pwf >= pb:
                qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef)
            elif pwf < pb:
                qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef)
        elif pr <= pb:
            qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef)
    elif (ef < 1 and ef2 >= 1):
        if pr > pb:
            if pwf >= pb:
                qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef, ef2)
            elif pwf < pb:
                qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef, ef2)
        elif pr <= pb:
            qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef, ef2)
    elif (ef > 1 and ef2 <= 1):
        if pr > pb:
            if pwf >= pb:
                qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef, ef2)
            elif pwf < pb:
                qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef, ef2)
        elif pr <= pb:
            qo = qo_standing(q_test, pwf_test, pr, pwf, pb, ef, ef2)
    return qo

# AOF(bpd)
def aof(q_test, pwf_test, pr, pb, ef=1, ef2=None):
    if (ef == 1 and ef2 is None):
        if pr > pb: # Yac. subsaturado
            if pwf_test >= pb:
                AOF = j(q_test, pwf_test, pr, pb) * pr
            elif pwf_test <  pb:
                AOF = Qb(q_test, pwf_test, pr, pb, ef=1) + ((j(q_test, pwf_test, pr, pb) * pb) / (1.8))
        else: # Yac. Saturado
            AOF = q_test / (1 - 0.2 * (pwf_test / pr) - 0.8 * (pwf_test / pr)**2)
    elif (ef < 1 and ef2 is None):
        if pr > pb:
            if pwf_test >= pb:
                AOF = j(q_test, pwf_test, pr, pb, ef) * pr
            elif pwf_test < pb:
                AOF = Qb(q_test, pwf_test, pr, pb, ef) + ((j(q_test, pwf_test, pr, pb, ef) * pb) / (1.8)) * (1.8 - 0.8 * ef)
        else:
            AOF = q_test / (1.8 * ef * (1 - pwf_test/pr) - 0.8 * ef**2 * (1 - pwf_test/pr)**2) * (1.8 * ef - 0.8 * ef**2)
    elif (ef > 1 and ef2 is None):
        if pr > pb:
            if pwf_test >= pb:
                AOF = j(q_test, pwf_test, pr, pb, ef) * pr
            elif pwf_test < pb:
                AOF = Qb(q_test, pwf_test, pr, pb, ef) +  ((j(q_test, pwf_test, pr, pb, ef) * pb) / (1.8)) * (0.624 + 0.376 * ef)
        else:
            AOF = q_test / (1.8 * ef * (1 - pwf_test/pr) - 0.8 * ef**2 * (1 - pwf_test/pr)**2) * (0.624 + 0.376 * ef)
    elif (ef < 1 and ef2 >= 1):
        if pr > pb:
            if pwf_test >= pb:
                AOF =  j(q_test, pwf_test, pr, pb, ef, ef2) * pr
            elif pwf_test < pb:
                AOF = Qb(q_test, pwf_test, pr, pb, ef, ef2) + (j(q_test, pwf_test, pr, pb, ef, ef2) * pb / 1.8) * (0.624 + 0.376 * ef2)
        else:
            AOF = q_test / (1.8 * ef * (1 - pwf_test/pr) - 0.8 * ef**2 * (1 - pwf_test/pr)**2) * (0.624 + 0.376 * ef2)
    elif (ef > 1 and ef2 <= 1):
        if pr > pb:
            if pwf_test >= pb:
                AOF = j(q_test, pwf_test, pr, pb, ef, ef2) * pr
            elif pwf_test < pb:
                AOF = Qb(q_test, pwf_test, pr, pb, ef, ef2) + (j(q_test, pwf_test, pr, pb, ef, ef2) * pb / 1.8) * (1.8 - 0.8 * ef2)
        else:
            AOF = q_test / (1.8 * ef * (1 - pwf_test/pr) - 0.8 * ef**2 * (1 - pwf_test/pr)**2) * (1.8 * ef - 0.8 * ef2**2)
    return AOF



# SGOil using API
def sg_oil(API):
    SG_oil = 141.5 / (131.5 + API)
    return SG_oil

# SG average of fluids
def sg_avg(API, wc, sg_h2o):
    sg_avg = wc * sg_h2o + (1-wc) * sg_oil(API)
    return sg_avg

# Average Gradient using fresh water gradient (0.433 psi/ft)
def gradient_avg(API, wc, sg_h2o):
    g_avg = sg_avg(API, wc, sg_h2o) * 0.433
    return g_avg

# Friction factor (f) from darcy-weisbach equation
def f_darcy(Q, ID, C=120):
    f = (2.083 * (((100 * Q)/(34.3 * C))**1.85 * (1 / ID)**4.8655)) / 1000
    return f

def pwf_darcy(q_test, pwf_test, q, pr, pb):
    pwf = pr - (q / j(q_test, pwf_test, pr, pb))
    return pwf

# Pwf @ vogel conditions
def pwf_vogel(q_test, pwf_test, pr, qo, pb):
    if pr > pb:
        if qo <= Qb(q_test, pwf_test, pr, pb):
            pwf = pr - qo / j(q_test, pwf_test, pr, pb)
        elif qo > Qb(q_test, pwf_test, pr, pb):
            Qmax = Qb(q_test, pwf_test, pr, pb) + ((j(q_test, pwf_test, pr, pb) * pb) / (1.8))
            pwf = 0.125*pr*(-1 + sqrt(81 - 80*qo/Qmax))
    elif pr <= pb:
        Qmax = q_test / (1 - 0.2 * (pwf_test / pr) - 0.8 * (pwf_test / pr)**2)
        pwf = 0.125*pr*(-1 + sqrt(81 - 80*qo/Qmax))
    return pwf    


# Function that state the Hagedorn and Brown correlation for multiphase flow
def hagedorn_and_brown1(qo, p, vsl, vsg, uo, ug, pho_o, pho_g,d, sigma, epsi, l, theta) -> float:
    # Mix velocity
    vm = vsl + vsg
    # Cross sectional area
    A = ((pi / 4) * d**2) / 144
    # Fluids flow rates
    ql = vsl * A
    qg = vsg * A
    # Determine flow regime
    Lb = 1.071 - 0.2218 * (vm**2 / (6/12))
    if Lb < 0.13:
        Lb = 0.13
    holdup_g = qg / (ql + qg)
    if holdup_g > Lb:
        print('The Hagedorn & Brown correlation can be used')
        Hl = Hagedorn_brown_holdup(p, vsl, vsg, pho_o, uo, d, sigma)
    else:
        print('The Griffith must be used')
        Hl=griffith_holdup(vsl, vsg)
    holdup_l = 1 - holdup_g
    # Non holdup mix density
    pho_n = pho_o * holdup_l + pho_g * (1 - holdup_g)
    # Calculate the 4 four dimensionless numbers   
    Hl = Hagedorn_brown_holdup(p, vsl, vsg, pho_o, uo, d, sigma)
    # Mix density
    pho_m = pho_o * Hl + pho_g * (1 - Hl)
    # Mix viscosity
    um = uo**Hl * ug**(1 - Hl)
    # Reynolds Number
    Nre_m = (1488 * pho_n* vm * (d/12)) / um
    # Friction factor
    f1 = fanning_friction_factor_chen(Nre_m, epsi, d)
    print(f" fanning f = {f1}")
    f = (1 / (1.14 - 2 * log10((epsi / (d / 12)) + (21.25 / Nre_m**0.9))))**2
    print(f" friction f = {f}")
    pho_f = pho_n**2 / pho_m
    # Pressure gradient due to potential energy
    grad_pe = ((32.17 / 32.17) * (pho_m * cos(theta))) / 144
    # Pressure gradiente due to friction
    grad_f = ((2 * f * pho_f * vm**2) / (32.17 * (d / 12))) / 144
    dp_total = round((grad_pe + grad_f) * l, 2)
    return dp_total


## TRANSIENT WELL TEST

def radius_dimensionless(re, rw):
  """Calculate dimensionless radius (rD)"""
  return re / rw

def time_dimensionless(perm, t, poro, mu, ct, rw):
  """Calculate dimensionless time (tD)"""
  return (.0002637 * perm * t) / (poro * mu * ct * (rw**2))

def pressure_multirate(pD, delta_q, pi, B, mu, perm, h):
  """Calculate Flowing Pressure as Sum of Constant Rates"""
  import numpy as np
  return pi - ((B * mu / (.007082 * perm * h)) * (np.sum(pD * delta_q)))

def rate_multipressure(qD, delta_p, B, mu, perm, h):
  """Calculate Rate as Sum of Constant Flowing Pressures"""
  import numpy as np
  return ((.007082 * perm * h) / (B * mu)) * (np.sum(qD * delta_p))

def time_finite_acting(perm, poro, mu, ct, rw, re):
  """Calculate time at flow starts behaving infinite-acting"""
  r_D = re / rw
  t_Dw = 0.25 * r_D**2
  return (poro * mu * ct * (rw**2) * t_Dw) / (.0002637 * perm)

def pressure_dimensionless(rD, tD):
    """
    Calculate Dimensionless Pressure from Constant Rate Flow
    """
    import numpy as np
    if tD < (0.25 * rD**2):
        # Infinite-acting solution for constant-rate (Towler, Eq. 6.20; from Lee, 1982)
        pD = 0.5 * (np.log(tD) + .80907)
    if tD > (0.25 * rD**2):
        # Finite-acting solution for constant-rate (Towler, Eq. 6.19; from Lee, 1982)
        pD = (2 * tD / rD**2) + np.log(rD) - .75
    return pD

def rate_dimensionless(rD, tD):
    """
    Calculate Dimensionless Rate from Constant Pressure Flow
    """
    import numpy as np
    import pandas as pd
    from scipy.interpolate import griddata
    
    if tD < (0.25 * rD**2):
        # Infinite-acting solution for constant-rate (Towler, Eq. 6.42, 6.43; from Edwardson et al, 1962)
        if tD > 0.01 and tD < 200:
          # Eq. 6.42
          qD = (26.7544 + (45.5537 * np.sqrt(tD)) + (13.3813 * tD) + (0.492949 * tD * np.sqrt(tD))) / ((47.4210 * np.sqrt(tD)) + (35.5372 * tD) + (2.60967 * tD * np.sqrt(tD)))
        if tD >= 200:
          # Eq. 6.43
          qD = ((2.02623 * tD * (np.log(tD) - 1)) + 3.90086) / (tD * ((np.log(tD))**2))

    if tD > (0.25 * rD**2):
        # Finite-acting solution for constant-rate (Towler, Eq. 7.32; from Jacob and Lohman, 1952)
        qD = np.nan
        qD = 2 / (np.log(tD) + .80907)
#         columns = ['rd', 'td', 'qd']
#         veh = pd.read_csv('/content/pyreservoir/welltest/Appendix A-4.csv', names=columns)
#         rd = veh['rd'].values
#         td = veh['td'].values
#         qd = veh['qd'].values

#         ## gridding and interpolation
#         data = np.stack((rd, td), axis=1)
#         qD = griddata(data, qd, [rD, tD], method='linear')

    return qD
  
def check_validity(solver='constant_rate', time='infinite', tmin=0.1, rw=0.5, re=1000, perm=100, poro=0.2, mu=2, ct=3E-6):
  """Check validity of using the Approaches to Flow Solutions"""
  import numpy as np
  if solver == 'constant_rate':
      if time == 'infinite':
          # Infinite-acting solution for constant-rate (Towler, Eq. 6.20; from Lee, 1982)
          rw_lim = np.sqrt((.0002637 * perm * tmin) / (100 * poro * mu * ct))
          if rw < rw_lim:
              print('valid')
          else:
              print('invalid')
      if time == 'finite':
          # Finite-acting solution for constant-rate (Towler, Eq. 6.19; from Lee, 1982)
          rw_lim = np.sqrt((.0002637 * perm * tmin) / (25 * poro * mu * ct))
          rD2 = (re / rw)**2
          if rw < rw_lim and rD2 > 1:
              print('valid')
          else:
              print('invalid')     
  if solver == 'constant_pressure':
      if time == 'infinite':
          # Infinite-acting solution for constant-pressure (Towler, Eq. 6.42, 6.43; from Edwardson et al, 1962)
          rw_lim = np.sqrt((.0002637 * perm * tmin) / (.01 * poro * mu * ct))
          if rw < rw_lim:
              print('valid')
          else:
              print('invalid')
      if time == 'finite':
          # Finite-acting solution for constant-pressure (Towler, Appendix A-4)
          print('valid')      

def simulate_multirate_test(p_initial, t_step, t_change, q_change,
                            re, rw, perm, poro, mu, ct, Bo, h):
  """
  Simulate the Multiple Constant Rate Test Started from 0th Hour 
  Based on Superposition Principle
  """
  import numpy as np
  import matplotlib.pyplot as plt
  import matplotlib.patches as mpl_patches
  
  # calculate finite-acting time
  t_finite_acting = time_finite_acting(perm, poro, mu, ct, rw, re)

  # produce time array
  t_end = t_change[-1]
  time = np.arange(0, t_end+1, t_step)

  # calculate dimensionless radius
  rD = re / rw

  # calculate delta rate (Δq)
  t_change = np.append(0, t_change)
  delta_q = [j-i for i, j in zip(q_change[:-1], q_change[1:])]
  delta_q = np.concatenate((np.array([0, q_change[0]]), delta_q))

  # create rate step profile
  tmax = t_change[-1] + 1
  t = []
  q = []
  pwf = []

  for i in range(len(time)):  
      for j in range(0, len(t_change)-1):
          if time[i] > t_change[j] and time[i] <= t_change[j+1]:
              # produce t and q profile
              t.append(time[i])
              q.append(q_change[j])
              
              # calculate dimensionless time tD (tD1, tD2, ..., tDn) at each time
              tn = time[i] - t_change[:j+1] # is an array   
              tD = time_dimensionless(perm, tn, poro, mu, ct, rw)
              
              # calculate dimensionless pressure pD at each time
              pD = []
              for k in range(len(tD)):
                  _ = pressure_dimensionless(rD, tD[k])
                  # _ = pd(rD, tD[k])
                  pD.append(_)
              
              # calculate final pressure after superposition
              delta_qn = delta_q[1:j+2] # is an array 
              
              pwf_ = pressure_multirate(pD, delta_qn, p_initial, Bo, mu, perm, h)
              pwf.append(pwf_)       

  t, q, pwf = np.append(0, t), np.append(q_change[0], q), np.append(p_initial, pwf)

  # plot well rate and flowing pressure profile
  plt.figure(figsize=(17,5))

  ## output the finite-acting time into the plot
  labels = []
  labels.append("Time @ Finite-acting = {} hours".format(np.round(t_finite_acting, 2)))

  handles = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", 
                                  lw=0, alpha=0)] * 1

  ## plot rate
  plt.subplot(1,2,1)
  plt.step(t, q, color='blue')
  plt.title('Well Rate Profile', size=20, pad=15)
  plt.xlim(0, t_end)
  plt.ylim(ymax=max(q)+200)
  plt.xlabel('Time (hours)'); plt.ylabel('Rate (STB/D)')

  plt.legend(handles, labels, loc='upper right', fontsize=12, 
              fancybox=True, framealpha=0.7, 
              handlelength=0, handletextpad=0) 

  ## plot BHFP
  plt.subplot(1,2,2)
  # t = np.arange(len(pwf))
  plt.plot(t, pwf, color='red')
  plt.title('Well Flowing Pressure Profile', size=20, pad=15)
  plt.xlim(0, t_end)
  plt.xlabel('Time (hours)'); plt.ylabel('BHFP (psia)')

  plt.show()
  
def simulate_multipressure_test(p_initial, t_step, t_change, p_change,
                                re, rw, perm, poro, mu, ct, Bo, h):
  """
  Simulate the Multiple Constant Borehole Flowing Pressure (BHFP) Test 
  Based on Superposition Principle
  """
  import numpy as np
  import matplotlib.pyplot as plt
  import matplotlib.patches as mpl_patches
  
  # calculate finite-acting time
  t_finite_acting = time_finite_acting(perm, poro, mu, ct, rw, re)  

  # produce time array
  t_end = t_change[-1]
  time = np.arange(0, t_end+1, t_step)

  # calculate dimensionless radius
  rD = re / rw

  # calculate delta rate (Δq)
  t_change = np.append(0, t_change)
  pi_min_p0 = p_initial - p_change[0]
  delta_p = [i-j for i, j in zip(p_change[:-1], p_change[1:])]
  delta_p = np.concatenate((np.array([0, pi_min_p0]), delta_p))

  # create rate step profile
  tmax = t_change[-1] + 1
  t = []
  pwf = []
  q = []

  for i in range(len(time)):  
      for j in range(0, len(t_change)-1):
          if time[i] > t_change[j] and time[i] <= t_change[j+1]:
              # produce t and p profile
              t.append(time[i])
              pwf.append(p_change[j])
              
              # calculate dimensionless time tD (tD1, tD2, ..., tDn) at each time
              tn = time[i] - t_change[:j+1] # is an array   
              tD = time_dimensionless(perm, tn, poro, mu, ct, rw)
              
              # calculate dimensionless rate qD at each time
              qD = []
              for k in range(len(tD)):
                  _ = rate_dimensionless(rD, tD[k])
                  # _ = qd(rD, tD[k])
                  qD.append(_)
              
              # calculate final rate after superposition
              delta_pn = delta_p[1:j+2] # is an array 
              
              q_ = rate_multipressure(qD, delta_pn, Bo, mu, perm, h)
              q.append(q_)     

  # plot flowing pressure and well rate profile
  plt.figure(figsize=(17,5))

  ## output the finite-acting time into the plot
  labels = []
  labels.append("Time @ Finite-acting = {} hours".format(np.round(t_finite_acting, 2)))

  handles = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", 
                                  lw=0, alpha=0)] * 1

  ## plot BHFP
  plt.subplot(1,2,1)
  plt.step(t, pwf, color='red')
  plt.title('Well Flowing Pressure Profile', size=20, pad=15)
  plt.xlim(0, t_end)
  plt.ylim(ymax=max(pwf)+200)
  plt.xlabel('Time (hours)'); plt.ylabel('Pressure (psia)')

  plt.legend(handles, labels, loc='upper right', fontsize=12, 
              fancybox=True, framealpha=0.7, 
              handlelength=0, handletextpad=0) 

  ## plot rate
  plt.subplot(1,2,2)
  # t = np.arange(len(pwf))
  plt.plot(t, q, color='blue')
  plt.title('Well Rate Profile', size=20, pad=15)
  plt.xlim(0, t_end)
  plt.xlabel('Time (hours)'); plt.ylabel('Rate (STB/D)')

  plt.show()
  
            
def constant_terminal_rate(time, distance, re, rw, pi, q, poro, ct, k, h, mu_oil, Bo):
  """
  Constant Terminal Rate Solution (Approximation Method)

  INPUT:

  time: Time at which flow is evaluated, hour
  distance: Distance from the wellbore, ft (NOT distance from centre of wellbore)
  re: Reservoir extent, ft
  rw: Wellbore radius, ft
  pi: Initial reservoir pressure, psia
  q: Wellbore flowing rate, STB/D
  poro: Porosity
  ct: Total compressibility, sip
  k: Permeability, md
  h: Reservoir net thickness, ft
  mu_oil: Oil viscosity, cp
  Bo: Oil FVF, RB/STB

  OUTPUT:

  td: Dimensionless time
  pd: Dimensionless pressure
  pwf: Wellbore flowing pressure (psia)
  """
  import numpy as np
  import scipy.special

  # Access to Ei-function table
  Ei_table = Ei_table = np.loadtxt("https://raw.githubusercontent.com/yohanesnuwara/reservoir-engineering/master/Appendix%20A.%20Values%20and%20Tabulations/Table%20A-1-Values%20for%20Exponential%20Integral.txt") 

  r = rw + distance
  t_finite_acting = time_finite_acting(k, poro, mu_oil, ct, rw, re)

  if time > 0 and time < t_finite_acting:
    """Time behaving infinite acting"""
    td = time_dimensionless(time, rw, poro, mu_oil, ct, k)
    if r==rw:
      # Your distance is at the wellbore
      if td > 100:
        # Eq 6.20
        pd = 0.5 * (((np.log(td)) + 0.80907)) 
        pwf = pi - ((pd * q * Bo * mu_oil) / (0.007082 * k * h))
      if td < 100:
        # No solution
        pd = np.nan
        pwf = np.nan

    if r>rw:
      # Your distance is away from the wellbore, in the reservoir
      td = time_dimensionless(time, r, poro, mu_oil, ct, k)
      if td > 12.5:
        # pd can be approximated using Eq 6.28

        pd = 0.5 * (np.log(td) + 0.80907)
        # pd_arr.append(float(pd))
        
        "Calculate pwf after n hours"
        pwf = pi - ((pd * q * Bo * mu_oil) / (0.007082 * k * h))  

      if td < 12.5:
        # pd calculated using Eq 6.26. Find the value of integral exponent function -Ei(-x) using tabulation    

        x = 0.25 * (1 / td)

        if x >= 0 and x <= 0.209:
          x_new = round(x, 3)

          # "Tabulation value finder"
          index = np.where(Ei_table[:,0] == x_new)
          index = np.array((index)[0])
          index = int(index)
          minusEi = Ei_table[index, 1]

        if x > 0.209 and x <= 2.09:
          x_new = round(x, 2) 

          # "Tabulation value finder"
          index = np.where(Ei_table[:,0] == x_new)
          index = np.array((index)[0])
          index = int(index)
          minusEi = Ei_table[index, 1]

        if x > 2.09 and x <= 10.9:
          x_new = round(x, 1) 

          # "Tabulation value finder"
          index = np.where(Ei_table[:,0] == x_new)
          index = np.array((index)[0])
          index = int(index)
          minusEi = Ei_table[index, 1]

        if x > 10.9:
          # if x above 10.9, meaning Table A-1 can't be used because it's limited to only x below 10.9. so use scipy
          x_new = x
          minusEi = -scipy.special.expi(-x) # from scipy.expi
        
        "Calculate pd"
        pd = 0.5 * minusEi

        "Calculate pwf after n hours"
        pwf = pi - ((pd * q * Bo * mu_oil) / (0.007082 * k * h))
      # pd, pwf = np.nan, np.nan

  elif time == 0:
    """Time at start of flow"""
    td = time_dimensionless(time, rw, poro, mu_oil, ct, k)
    pd = np.nan
    pwf = pi
    
  elif time >= t_finite_acting:
    """Time behaving finite acting"""
    td = time_dimensionless(time, rw, poro, mu_oil, ct, k)
    if r==rw:
      # Your distance is at wellbore
      if td > 25:
        # Calculate dimensionless radius at reservoir outer boundary (r=re)
        r_eD = radius_dimensionless(re, rw)
        # Eq 6.19
        pd = (2 * td / (r_eD**2)) + np.log(r_eD) - 0.75 # Eq 6.19
        pwf = pi - ((pd * q * Bo * mu_oil) / (0.007082 * k * h))

      if td < 25:
        # No solution
        pd = np.nan
        pwf = np.nan
    
    if r>rw:
      # Your distance is outside the wellbore, inside the reservoir
      pd, pwf = np.nan, np.nan # No solution

  return td, pd, pwf