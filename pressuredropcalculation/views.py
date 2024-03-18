from django.shortcuts import render, redirect
from .models import PressuredropCalculationModel
from .forms import PressureDropCalcForm
from selectedOilProducer.models import SelectedOilProducer
from .utils import get_plot, get_fanning
import psapy.BeggsandBrill as BB
import psapy.Hagendornandbrown as HB
import psapy.FluidProps as FluidProps
from IntelligentOilWell.custom_context_processors import hagedorn_and_brown, beggs_and_brills, oil_sigma, Hagedorn_brown_holdup, griffith_holdup, hagedorn_and_brown1
from IntelligentOilWell.custom_context_processors import sg_avg, gradient_avg, svsl, svsg, Pbub, sol_gor, oil_fvf, oil_visc, oil_dens, oil_sigma, single_phase_liquid_grad
from IntelligentOilWell.custom_context_processors import Tc, Pc, zfact, gvisc, gas_fvf, gas_dens, wtr_sigma, wtr_dens, wtr_fvf, wtr_visc, fanning_friction_factor_chen
from IntelligentOilWell.custom_context_processors import gray_oil
from  math import pi, log10, log, cos, sin, radians
import pandas as pd


def list_pressure_drop(request):     
    well = SelectedOilProducer.objects.all().first()   
    pdrops= PressuredropCalculationModel.objects.filter(wellid=well.wellid).all()  
    pdrop = pdrops.last()
    # Data
    qo = 1000 #bpd
    p = 1700 #psi
    vsl = 3.97 #ft/s
    vsg = 3.86 #ft/s
    uo = 0.97 #cp
    ug = 0.016 #cp
    pho_o = 47.61 #lb/ft3
    pho_g = 5.88 #lb/ft3
    sigma = 8.41 #dynes/cm
    d = 6 #inch
    epsi = 0.0006 #ft
    l = 10000 #ft
    theta = 0

    dp = hagedorn_and_brown1(qo, p, vsl, vsg, uo, ug, pho_o, pho_g, d, sigma, epsi, l, theta)
    print(f' the total pressure drop is: {dp} psia')







    # Data
    T = pdrop.source_Temp # deg F
    Tsep = 100 # deg F
    Psep=150 # psi
    TDS = 0.005 #wt%
    epsi = 0.0006 #ft
    theta=(90-90) # deviation angle
    gas_grav = pdrop.fluid_gas_spgr # Gas Specific Gravity
    oil_grav = pdrop.fluid_API # API gravity
    Gor = pdrop.fluid_GOR # scf/bbl
    p = pdrop.source_Pressure #psi
    wc = pdrop.fluid_WaterCut/100 # fraction
    pb = Pbub(T, Tsep, Psep, gas_grav, oil_grav, Gor)
    rs = sol_gor(T, p, Tsep, Psep, pb, gas_grav, oil_grav)
    ql = pdrop.source_Flowrate #bpd
    qo = ql* (1.0-pdrop.fluid_WaterCut/100) # bopd
    qw = ql* (pdrop.fluid_WaterCut/100) # bwpd
    qg = qo* (pdrop.fluid_GOR-rs) # gas rate scf/d
    D= pdrop.pipe_Diam # Inch
    A = ((pi / 4) * D**2) / 144.0
    # properties      
    bo = oil_fvf(T, p, Tsep, Psep, pb, rs, gas_grav, oil_grav)
    oil_vis = oil_visc(T, p, Tsep, Psep, pb, rs, gas_grav, oil_grav)
    oil_density = oil_dens(T, p, Tsep, Psep, pb,bo, rs, gas_grav, oil_grav)
    bw = wtr_fvf(p, T, TDS)
    water_vis = wtr_visc(p, T, TDS)
    water_density = wtr_dens(p, T, bw, TDS)
    liquid_density = oil_density*(1-wc) + water_density*wc
    liquid_vis = oil_vis*(1-wc) + water_vis*wc
    # print (f"liquid Density = {liquid_density}, liquid Vis = {liquid_vis}")
    if rs >= Gor:
        flow_regime = "Single Phase"
        tot_grad = single_phase_liquid_grad(ql, liquid_density, liquid_vis, A, epsi, D, theta)       
        #print(f"Liquid Density = {liquid_density}, Oil = {oil_density}, water = {water_density}")
        # print (f"Friction gradient= {f} elevation gradient = {grad_pe}" )
    else :
        critical_temp = Tc(gas_grav)
        critical_pres = Pc(gas_grav)
        Tr = (T+459.67)/critical_temp
        Pr = p/critical_pres
        zfactor = zfact(Tr, Pr)
        gas_vis = gvisc(p, (T+460), zfactor, gas_grav)
        gas_density = gas_dens(p, T, zfactor, gas_grav)
        bg = gas_fvf(p, T, gas_grav)
        sigma_oil = oil_sigma(p, T, oil_grav)
        sigma_water = wtr_sigma(p, T)
        sigma = sigma_water*wc + sigma_oil*(1-wc)
        vsl = svsl(ql,D)
        vsg = svsg(qg,1.0, D)       
       #vsl = 3.97 #ft/s
       #vsg = 3.86 #ft/s
       #muo = 0.97 #cp
       #mug = 0.016 #cp
       #rho_o = 47.61 #lb/ft3
       #rho_g = 5.88 #lb/ft3
        # sigma = 8.41 #dynes/cm
        # d = 6 #inch
        epsi = 0.0006 #ft
        l = pdrop.pipe_Length #ft   
        angle=90    
        hl = Hagedorn_brown_holdup(p, vsl, vsg, liquid_density, liquid_vis, D, sigma)
        print(f"hagedorn Hold-up = {hl}")
        hl1 = griffith_holdup(vsl, vsg)
        print(f"Griffith Hold-up = {hl1}")
        dp = hagedorn_and_brown(ql,qg, p, vsl, vsg, oil_vis, gas_vis, oil_density, gas_density, D, sigma, epsi, l, theta)
        print(f' the total pressure drop is: {dp} psia')

        dp_total = beggs_and_brills(ql,liquid_vis, gas_vis, liquid_density, gas_density, d, sigma, epsi, l,angle, qg, Gor)
        (f'Pressure drop is -> {dp_total} psia')

        delphh, delpf, totaldelp = gray_oil(qo, qw, vsl, vsg, liquid_density, gas_density, liquid_vis, gas_vis, sigma_oil, sigma_water,D, theta, epsi)

        print(f" grv_grad = {delphh}, friction ={delpf}, total = {totaldelp}, pdrop = {totaldelp*l} " )
        



    # Data
    qo = 2000 #bpd
    gor = 1.5434 #ft3/ft3
    uo = 16 #cp
    ug = 0.02 #cp
    pho_o = 49.9 #lb/ft3
    pho_g = 2.84 #lb/ft3
    sigma = 30 #dynes/cm
    d = 3 #inch
    epsi = 0.0006 #ft
    l = 10000 #ft
    angle = 90
    #flow_regime = beggs_and_brills(qo, uo, ug, pho_o, pho_g, d, sigma, epsi, l, angle, gor=gor)[0]
    #print(f'The flow regime is -> {flow_regime}')
    #HL = beggs_and_brills(qo, uo, ug, pho_o, pho_g, d, sigma, epsi, l,angle, gor=gor)[1]
    #print(f'The Oil Holdup is -> {HL:.3}')
    #Grad_total = beggs_and_brills(qo, uo, ug, pho_o, pho_g, d, sigma, epsi, l,angle, gor=gor)[2]
    #print(f'The total pressure gradient is -> {Grad_total} psi/ft')    
    #DP = beggs_and_brills(qo, uo, ug, pho_o, pho_g, d, sigma, epsi, l,angle, gor=gor)[3]
    #(f'The total pressure drop is -> {DP} psia')

    
    # Datos
    THP = 250 #psia
    wc = 0.75
    sg_h2o = 1.04
    API = 30
    Q = 2500 #bpd
    ID = 2.875 #in
    tvd = 6000 #ft
    md = 6600 #ft
    C = 120

    SG_Avg = sg_avg(API, wc, sg_h2o)
    print(f'SGavg -> {SG_Avg}')

    Gavg = gradient_avg(API, wc, sg_h2o)
    print(f'Gavg -> {Gavg} psi/ft')

   #pdrop = pdrops.last()   
   #pressures = []
   #holdups = []
   #wtr_spgr =1.001   
   #if pdrop :
   #    source = dict(p=pdrop.source_Pressure, q=int(pdrop.source_Flowrate), temp=pdrop.source_Temp, wtr_rate = pdrop.source_Flowrate*pdrop.fluid_WaterCut/100.0)
   #    pipe = dict(length=pdrop.pipe_Length, angle=pdrop.pipe_Angle, diam=pdrop.pipe_Diam)
   #    fluid = dict(api=pdrop.fluid_API, wc=pdrop.fluid_WaterCut, gor=pdrop.fluid_GOR, gas_spgr=pdrop.fluid_gas_spgr, wtr_spgr=wtr_spgr)     
   #else :
   #    source = dict(p=1000, q=int(1000), temp=175.0, wtr_rate = 1000.0*5.0/100.0)
   #    pipe = dict(length=10000, angle=90.0, diam=2.5)
   #    fluid = dict(api=35.0, wc=5.0, gor=700.0, gas_spgr=0.72, wtr_spgr=1.001)  
   #      
   #pressures=[]
   #holdups=[]
   #pressures1=[]
   #holdups1=[]
   #pipeline_range= list(range(0,int(pipe['length']),100))    
   #p_current = source['p']
   #p_current1 = source['p']    
   #
   #for length in pipeline_range:
   #    if length==0:
   #        pressures.append(source['p'])
   #        holdups.append(50)
   #        pressures1.append(source['p'])
   #        holdups1.append(50)
   #    else:
   #        grad, hold = BB.Pgrad(p_current, source['temp'], source['q'], source['wtr_rate'], fluid['gor'],fluid['gas_spgr'],fluid['api'],fluid['wtr_spgr'], pipe['diam'], pipe['angle'])
   #        p_current= source['p']- (grad*length)
   #        pressures.append(p_current)
   #        holdups.append(hold*100)
   #        #Hagedorn and Brown
   #        grad1, hold1 = HB.Pgrad(p_current1, source['temp'], source['q'], source['wtr_rate'], fluid['gor'],
   #                               fluid['gas_spgr'], fluid['api'],wtr_spgr, pipe['diam'], pipe['angle'])
   #        p_current1= source['p']- (grad1*length)
   #        pressures1.append(p_current1)
   #        holdups1.append(hold1*100)
   #print(pressures1, holdups1 )
   ##holdups[0]=holdups[1]
   ##holdups1[0]=holdups1[1]
   #r1 =  list(range(1,100,10))
   #print(r1)
   #print(len(pipeline_range), len(pressures), len(pressures1), len(holdups), len(holdups1))
   #chart = get_plot(pipeline_range, pressures, pressures1, holdups, holdups1)
    return render (request, 'pressuredropcalculation/pressuredropcalculation.html', {'pdrops': pdrops, })

def create_pressure_drop(request):   
    drop = PressuredropCalculationModel()
    selectedwell = SelectedOilProducer.objects.first()  
    drop.fgid = selectedwell.fgid
    drop.wellid = selectedwell.wellid   
    form = PressureDropCalcForm(request.POST or None, instance=drop)
    if request.method =="POST":  
        form = PressureDropCalcForm(request.POST, request.FILES, instance=drop)       
        drop.fgid = selectedwell.fgid
        drop.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('pressuredropcalculation:list_pressure_drop')
    return render (request, 'pressuredropcalculation/pressuredropcalculation_form.html', {'form': form})

def update_pressure_drop(request, id):
    drop = PressuredropCalculationModel.objects.get(id=id)
    form = PressureDropCalcForm(request.POST or None, instance=drop)
    if form.is_valid():
        form.save()
        return redirect ('pressuredropcalculation:list_pressure_drop')
    return render (request, 'pressuredropcalculation/pressuredropcalculation_form.html', {'form': form, 'drop':drop})

def delete_pressure_drop(request, id):
    drop = PressuredropCalculationModel.objects.get(id=id)    
    if request.method == 'POST' :
        drop.delete()
        return redirect ('pressuredropcalculation:list_pbu_test_list_pressure_dropdesign')
    return render (request, 'pressuredropcalculation/pressuredropcalculation_confirm_delete.html', {'drop':drop})

