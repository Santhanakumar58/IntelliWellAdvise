from django.shortcuts import render, redirect
from .models import PressuredropCalculationModel
from .forms import PressureDropCalcForm
from selectedOilProducer.models import SelectedOilProducer
from .utils import get_plot
import psapy.BeggsandBrill as BB
import psapy.Hagendornandbrown as HB
import psapy.FluidProps as FluidProps

def list_pressure_drop(request):     
    well = SelectedOilProducer.objects.all().first()   
    pdrops= PressuredropCalculationModel.objects.filter(wellid=well.wellid).all()
    pdrop = pdrops.last()
   
    pressures = []
    holdups = []
    wtr_spgr =1
    if pdrop :
        source = dict(p=pdrop.source_Pressure, q=int(pdrop.source_Flowrate), temp=pdrop.source_Temp, wtr_rate = pdrop.source_Flowrate*pdrop.fluid_WaterCut/100)
        pipe = dict(length=pdrop.pipe_Length, angle=pdrop.pipe_Angle, diam=pdrop.pipe_Diam)
        fluid = dict(api=pdrop.fluid_API, wc=pdrop.fluid_WaterCut, gor=pdrop.fluid_GOR, gas_spgr=pdrop.fluid_gas_spgr, wtr_spgr=wtr_spgr)
        wtr_spgr =1
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
                p_current= source['p']- (grad*length)
                pressures.append(p_current)
                holdups.append(hold*100)
                #Hagedorn and Brown
                grad1, hold1 = HB.Pgrad(p_current1, source['temp'], source['q'], source['wtr_rate'], fluid['gor'],
                                       fluid['gas_spgr'], fluid['api'],wtr_spgr, pipe['diam'], pipe['angle'])
                p_current1= source['p']- (grad1*length)
                pressures1.append(p_current1)
                holdups1.append(hold1*100)
    else:
        pipeline_range= range(1,100,10)
        pressures = range(100,1000,10)
        holdups = range(0,10,10)
        pressures1 = range(100,1000,10)
        holdups1 = range(0,10,10)

    print(pressures1, holdups1 )
    #holdups[0]=holdups[1]
    #holdups1[0]=holdups1[1]
    chart = get_plot(pipeline_range, pressures, pressures1, holdups, holdups1)
    return render (request, 'pressuredropcalculation/pressuredropcalculation.html', {'pdrops': pdrops,'chart':chart })

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

