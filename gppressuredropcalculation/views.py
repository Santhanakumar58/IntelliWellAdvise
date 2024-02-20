from django.shortcuts import render, redirect
from .models import GPPressuredropCalculationModel
from .forms import GPPressureDropCalcForm
from selectedGasProducer.models import SelectedGasProducer
from .utils import get_plot, get_dummy_plot
import psapy.BeggsandBrill as BB
import psapy.Hagendornandbrown as HB
import psapy.FluidProps

def list_gppressure_drop(request):     
    well = SelectedGasProducer.objects.all().first()   
    pdrops= GPPressuredropCalculationModel.objects.filter(gpwellid=well.wellid).all()
    pdrop = pdrops.last()   
    pressures = []
    holdups = []
    wtr_spgr =1
    if pdrop :
        source = dict(p=pdrop.source_Pressure, q=int(pdrop.source_Flowrate), temp=pdrop.source_Temp, wtr_rate = pdrop.source_Flowrate*pdrop.fluid_WaterCut/100)
        pipe = dict(length=pdrop.pipe_Length, angle=pdrop.pipe_Angle, diam=pdrop.pipe_Diam)
        fluid = dict(api=pdrop.fluid_API, wc=pdrop.fluid_WaterCut, gor=pdrop.fluid_GOR, gas_spgr=pdrop.fluid_gas_spgr, wtr_spgr=wtr_spgr)
    else:
        source = dict(p=1000, q=int(1000), temp=150, wtr_rate = 250)
        pipe = dict(length=5000, angle=45, diam=2.441)
        fluid = dict(api=35, wc=25, gor=800, gas_spgr=0.72, wtr_spgr=1.01)    
    print(pipe['angle'])     
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
            grad1, hold1 = HB.Pgrad(p_current1, source['temp'], source['q'], source['wtr_rate'], fluid['gor'],fluid['gas_spgr'], fluid['api'],wtr_spgr, pipe['diam'], pipe['angle'])
            p_current1= source['p']- (grad1*length)
            pressures1.append(p_current1)
            holdups1.append(hold1*100)
    chart = get_plot(pipeline_range, pressures, pressures1, holdups, holdups1)
    #else:
    #    DPs = []          ## Start as the empty list
    #    Temps=[]
    #    Press=[]
    #    PressList=[]
    #    DepthList=[]
    #    #list.append('a')   ## Use append() to add elements
    #    #list.append('b')
#
    #    Oil_Rate=682.0
    #    Water_Rate=76.0
    #    GOR=84.0
    #    GasGrav=0.7
    #    WaterGrav=1.05                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    #    ID=2.995
    #    Angle=90
    #    FBHT=180.0
    #    FWHP=200.0
    #    FWHT=80.0
    #    Depth=9700.0
    #    nSteps=20
    #    API=40.0
    #    Tgrad= (FBHT-FWHT)/ Depth
#
    #    i=0
    #    PressList.append(FWHP)
    #    Temps.append(FWHT)
    #    DepthList.append(0)
    #    DPs.append(0)
#
    #    i=1
    #    while (i<= nSteps):   
    #        DeltaD= Depth/nSteps*i
    #        DepthList.append(DeltaD)    
    #        T=Temps[i-1]+Tgrad*DeltaD
    #        Temps.append(T)
    #        p=PressList[i-1]
    #        dp= HB.Pgrad(p,T,Oil_Rate,Water_Rate,GOR,GasGrav,API, WaterGrav, ID, Angle)
    #        DPs.append(dp)
    #        #print dp
    #        p=PressList[i-1]+DPs[i]*(DepthList[i]-DepthList[i-1])  
    #        PressList.append(p)
    #        #print p  ,  DeltaD
    #        i=i+1
    #    chart = get_dummy_plot(PressList, DepthList)
    #    #pipeline_range= range(1,100,10)
    #    #pressures = range(100,1000,10)
    #    #holdups = range(0,10,10)
    ##print(pressures1, holdups1 )
    ##holdups[0]=holdups[1]
    ##holdups1[0]=holdups1[1]
   
    return render (request, 'gppressuredropcalculation/gppressuredropcalculation.html', {'pdrops': pdrops,'chart':chart })

def create_gppressure_drop(request):   
    drop = GPPressuredropCalculationModel()
    selectedwell = SelectedGasProducer.objects.first()  
    drop.fgid = selectedwell.fgid
    drop.wellid = selectedwell.wellid   
    form = GPPressureDropCalcForm(request.POST or None, instance=drop)
    if request.method =="POST":  
        form = GPPressureDropCalcForm(request.POST, request.FILES, instance=drop)       
        drop.fgid = selectedwell.fgid
        drop.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('gppressuredropcalculation:list_gppressure_drop')
    return render (request, 'gppressuredropcalculation/gppressuredropcalculation_form.html', {'form': form})

def update_gppressure_drop(request, id):
    drop = GPPressuredropCalculationModel.objects.get(id=id)
    form = GPPressureDropCalcForm(request.POST or None, instance=drop)
    if form.is_valid():
        form.save()
        return redirect ('gppressuredropcalculation:list_gppressure_drop')
    return render (request, 'gppressuredropcalculation/gppressuredropcalculation_form.html', {'form': form, 'drop':drop})

def delete_gppressure_drop(request, id):
    drop = GPPressuredropCalculationModel.objects.get(id=id)    
    if request.method == 'POST' :
        drop.delete()
        return redirect ('gppressuredropcalculation:list_pbu_test_list_gppressure_dropdesign')
    return render (request, 'gppressuredropcalculation/gppressuredropcalculation_confirm_delete.html', {'drop':drop})


# Create your views here.
