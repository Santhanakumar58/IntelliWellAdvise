from django.db import models
from blackoilpvt.models import BlackoilPVT
from perforations.models import PerforationModel
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity, get_Rs
from opinflow.utility import draw_CompositePR_PI, draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins
from opinflow.models import ProductivityIndexModel, DarcyModel, WigginsModel, VogelModel, StandingsModel, MultirateModel
import math
from selectedOilProducer.models import SelectedOilProducer
from .utils import calculate_esp_parameters, find_power_when_tdh_is_given
import pandas as pd
from wellcompletion.models import Wellcompletion
import psapy.BeggsandBrill as BB
import psapy.Hagendornandbrown as HB
import psapy.FluidProps, psapy.GasProp
from deviationsurveydata.models import Deviationsurveydata
 


# Create your models here.
class ESPDesignModel(models.Model):    
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()     
    design_Date = models.DateField()  
    design_Liquid = models.FloatField() 
    water_Cut = models.FloatField() 
    water_Salinity= models.FloatField()
    th_Pres = models.FloatField() 
    th_Temp = models.FloatField() 
    curr_Res_Pres = models.FloatField()
    min_Pwf =models.FloatField()
    gas_Oil_Ratio = models.FloatField()  
    water_spgr= models.FloatField(default=1.0) 
    gas_Separator =models.BooleanField(default=True)
    gas_Separator_Efficiency =models.FloatField(default=100)
    pump_depth =models.FloatField(default=1000)
    pvt_Well= models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def total_mass_flowrate(self):
        selectedwell = SelectedOilProducer.objects.first()  
        design_Liquid= self.design_Liquid
        oil = self.design_Liquid*(1-self.water_Cut/100) 
        water = self.design_Liquid*(self.water_Cut/100)  
        gas = oil* self.gas_Oil_Ratio
        pvt = BlackoilPVT.objects.filter(wellName =self.pvt_Well).last()         
        oil_grav = pvt.oilAPIgravity
        solutiongas = pvt.solutionGOR
        gas_grav = pvt.gasGravity    
        oil_spgr = 141.5/(oil_grav+ 131.5) 
        total_mass_flowrate = (((oil*oil_spgr)+(water*self.water_spgr))*5.6146*62.4) +(self.gas_Oil_Ratio*oil*gas_grav *0.0752)        
        return round(total_mass_flowrate)

    @property
    def composite_spgr(self):        
        composite_spgr = self.total_mass_flowrate/(self.design_Liquid*5.6146*62.4)
        return round(composite_spgr,3)

    @property
    def mid_perf_depth(self):
        selectedwell = SelectedOilProducer.objects.first()  
        perfortaions = PerforationModel.objects.filter(wellid=selectedwell.wellid).all().order_by('-perf_Top') 
        perforation = perfortaions.first()
        mid_perf_depth = (perforation.perf_Top + perforation.perf_Bottom)/2
        print(mid_perf_depth)
        return mid_perf_depth

    @property
    def tbg_id(self):
        selectedwell = SelectedOilProducer.objects.first()  
        completions = Wellcompletion.objects.filter(wellid=selectedwell.wellid).all().order_by('equip_Md') 
        tubings=[]       
        for completion in completions:
            if completion.equipment =="Tubing":
                tubingid = completion.equip_Id
                tubings.append(tubingid)
        print(tubings)
        return tubings[0]

    @property
    def tbg_length(self):
        selectedwell = SelectedOilProducer.objects.first()  
        completions = Wellcompletion.objects.filter(wellid=selectedwell.wellid).all().order_by('equip_Md')        
        mds =[]
        for completion in completions:            
            if completion.equipment =="Tubing_end":
                tbg_length = completion.equip_Md
        print(tbg_length)
        return tbg_length 

    @property
    def pip(self): 
        selectedwell = SelectedOilProducer.objects.first()  
        df = pd.DataFrame()  
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
        df['x2']= xc
        df['y2']= y    
    
        x1=[]
        y1=[]
        pwf_inflow=0
        for index, row in df.iterrows(): 
            if self.design_Liquid > row['x2'] :      
               x1 = [self.design_Liquid,self.design_Liquid,0 ]
               y1 = [0,row['y2'],row['y2'] ] 
               pwf_inflow=row['y2']     
               break
        #chart = get_ipr_plot(df, espdata, x1, y1)
        pip = pwf_inflow
         
        return round(pip)

    @property
    def friction_head(self):
        C=120       
        friction_per1000ft = 15.11*math.pow((self.design_Liquid/C),1.852)/math.pow(self.tbg_id, 4.8655)
        friction_head =friction_per1000ft * self.tbg_length/1000        
        return round(friction_head)

    @property
    def thp_head(self):
        thp_head = self.th_Pres/(0.433*self.composite_spgr)        
        return round(thp_head)

    @property
    def vertical_lift_head(self):
        C=120
        pip_depth = self.pip/(0.433*self.composite_spgr) 
        HL = self.pump_depth - pip_depth 
        friction_per1000ft = 15.11*math.pow((self.design_Liquid/C),1.852)/math.pow(self.tbg_id, 4.8655)
        friction_head =friction_per1000ft * self.tbg_length/1000        
        return round(friction_head)


    @property
    def tdh(self):
        tdh = self.vertical_lift_head+self.thp_head+self.friction_head        
        return tdh

    @property
    def required_seal_hp(self):        
        tdh = [268.323,	749.179,	1143.574,	1816.555,	2910.817,	4201.146,	5474.552,	6748.153,	8021.429,	9294.945,	10518.288,	11741.849,	13015.192,	14288.838,	15325.292]
        hp =[ 2.38,	2.539,	2.65,	2.803,	2.902,	3.006,	3.118,	3.214,	3.337,	3.44,	3.557,	3.657,	3.774,	3.867,	3.938]
        required_seal_hp = find_power_when_tdh_is_given (tdh, hp, self.tdh)   
        print(required_seal_hp)   
        return required_seal_hp
 
    @property
    def discharge_pres(self): 
        selectedwell = SelectedOilProducer.objects.first()  
        deviations = Deviationsurveydata.objects.filter(wellid=selectedwell.wellid).all().order_by('measuredDepth')   
        design_Liquid= self.design_Liquid
        oil = self.design_Liquid*(1-self.water_Cut/100) 
        water = self.design_Liquid*(self.water_Cut/100)  
        gas = oil* self.gas_Oil_Ratio
        gor = self.gas_Oil_Ratio
        wc=self.water_Cut/100
        pvt = BlackoilPVT.objects.filter(wellName =self.pvt_Well).last()
        temp_grad = (pvt.reservoirTemperature-self.th_Temp)/self.mid_perf_depth
        avg_temp = (pvt.reservoirTemperature-self.th_Temp)/2
        source = dict(p=self.th_Pres, q=int(oil), temp=self.th_Temp, wtr_rate = water)
        pipe = dict(length=self.tbg_length, angle=90, diam=self.tbg_id)
        fluid = dict(api=pvt.oilAPIgravity, wc=wc, gor=gor, gas_spgr=pvt.gasGravity, wtr_spgr=self.water_spgr)         
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
                grad, hold = BB.Pgrad(p_current, t_current, source['q'], source['wtr_rate'], fluid['gor'],fluid['gas_spgr'],fluid['api'],fluid['wtr_spgr'], pipe['diam'],angle_current)
                p_current= source['p']+ (grad*length)
                pressures.append(p_current)
                holdups.append(hold*100)
                #Hagedorn and Brown
                grad1, hold1 = HB.Pgrad(p_current1, t_current, source['q'], source['wtr_rate'], fluid['gor'],
                                       fluid['gas_spgr'], fluid['api'],fluid['wtr_spgr'], pipe['diam'], angle_current)
                p_current1= source['p']+ (grad1*length)
                pressures1.append(p_current1)
                holdups1.append(hold1*100)
                print(p_current)
                for deviation in deviations:
                    if deviation.measuredDepth >= length:
                        angle_current = deviation.angle                       
                        break
                t_current = source['temp']+ (temp_grad*length)                
    
        pwf_inflow =round((self.pip -50)/100)*100
        pwfdiff = pressures1[-1] - self.pip
        pwfdiff =round((pwfdiff +50)/100)*100
        discharge_pres = round((p_current+50)/100)*100
        print(discharge_pres)
        return discharge_pres

    Pumps=(
        ('400-D800N-60Hz-250-1150bpd', '400-D800N-60Hz-250-1150bpd'),
        ('400-D1100-60Hz-400-1650bpd-154Hp', '400-D1100-60Hz-400-1650bpd-154Hp'),
        ('400-D1050-60Hz-300-1650bpd-154Hp', '400-D1050-60Hz-300-1650bpd-154Hp'),
        ('400-D1750-60Hz-300-1650bpd-154Hp', '400-D1750-60Hz-1200-2050bpd-125Hp'),

    )
    pump = models.CharField(max_length=100, choices = Pumps,default = '400-D1050-60Hz-300-1650bpd-154Hp')

    @property
    def no_of_stages(self):
        if self.pump =='400-D800N-60Hz-250-1150bpd':           
            behead_per_stage =34.69           
            no_of_stages = self.tdh/behead_per_stage          
        elif self.pump =='400-D1100-60Hz-400-1650bpd-154Hp':
            behead_per_stage =34.69
            no_of_stages = self.tdh/behead_per_stage              
        elif self.pump =='400-D1050-60Hz-300-1650bpd-154Hp':
            behead_per_stage =34.69
            no_of_stages = self.tdh/behead_per_stage           
        elif self.pump =='400-D1750-60Hz-300-1650bpd-154Hp':
            behead_per_stage =34.69
            no_of_stages = self.tdh/behead_per_stage                
        else:            
            no_of_stages=0   
        return round(no_of_stages +0.5)

    @property
    def required_Power(self):
        if self.pump =='400-D800N-60Hz-250-1150bpd':           
            bepower_per_stage =0.33          
            required_Power = bepower_per_stage * self.no_of_stages *self.composite_spgr            
        elif self.pump =='400-D1100-60Hz-400-1650bpd-154Hp':
            bepower_per_stage =0.33          
            required_Power = bepower_per_stage * self.no_of_stages *self.composite_spgr  
        elif self.pump =='400-D1050-60Hz-300-1650bpd-154Hp':
            bepower_per_stage =0.33          
            required_Power = bepower_per_stage * self.no_of_stages *self.composite_spgr            
        elif self.pump =='400-D1750-60Hz-300-1650bpd-154Hp':
            bepower_per_stage =0.33          
            required_Power = bepower_per_stage * self.no_of_stages *self.composite_spgr           
        else:            
            required_Power=0   
        return  round(required_Power+0.5) 
    
    @property
    def total_power_required(self) :
        return (self.required_Power +self.required_seal_hp)
    @property
    def best_efficiency(self):
        if self.pump =='400-D800N-60Hz-250-1150bpd':           
            best_efficiency =61.06 
        elif self.pump =='400-D1100-60Hz-400-1650bpd-154Hp':
             best_efficiency =61.06       
        elif self.pump =='400-D1050-60Hz-300-1650bpd-154Hp':
             best_efficiency =61.06         
        elif self.pump =='400-D1750-60Hz-300-1650bpd-154Hp':
            best_efficiency =61.06  
        else:            
            best_efficiency=0   
        return best_efficiency

    Motors=(
        ('375-50Hz-06.25hp-345v-13.5A',  '375-50Hz-06.25hp-345v-13.5A'),
        ('375-50Hz-08.8hp-333v-20.0A',   '375-50Hz-08.8hp-333v-20.0A'),
        ('375-50Hz-08.8hp-575v-12.0A',   '375-50Hz-08.8hp-575v-12.0A'),
        ('375-50Hz-12.5hp-275v-34.0A',   '375-50Hz-12.5hp-275v-34.0A'),
        ('375-50Hz-12.5hp-346v-27.0A',   '375-50Hz-12.5hp-346v-27.0A'),
        ('375-50Hz-16.3hp-346v-35.0A',   '375-50Hz-16.3hp-346v-35.0A'),
        ('375-50Hz-16.3hp-541v-22.5A',   '375-50Hz-16.3hp-541v-22.5A'),
        ('375-50Hz-18.8hp-367v-38.5A',   '375-50Hz-18.8hp-367v-38.5A'),
        ('375-50Hz-18.8hp-625v-22.5A',   '375-50Hz-18.8hp-625v-22.5A'),
        ('375-50Hz-21.8hp-541v-29.5A',   '375-50Hz-21.8hp-541v-29.5A'),
        ('375-50Hz-21.8hp-650v-24.5A',   '375-50Hz-21.8hp-650v-24.5A'),
        ('456-50Hz-08.5hp-367v-15.0A',   '456-50Hz-08.5hp-367v-15.0A'),
        ('456-50Hz-12.5hp-367v-23.0A',   '456-50Hz-12.5hp-367v-23.0A'),
        ('456-50Hz-12.5hp-625v-14.0A',   '456-50Hz-12.5hp-625v-14.0A'),
        ('456-50Hz-16.5hp-383v-28.0A',   '456-50Hz-16.5hp-383v-28.0A'),
        ('456-50Hz-16.5hp-633v-17.0A',   '456-50Hz-16.5hp-633v-17.0A'),
        ('456-50Hz-21.0hp-350v-38.0A',   '456-50Hz-21.0hp-350v-38.0A'),
        ('456-50Hz-21.0hp-483v-22.0A',   '456-50Hz-21.0hp-483v-22.0A'),
        ('456-50Hz-25.0hp-367v-43.0A',   '456-50Hz-25.0hp-367v-43.0A'),
        ('456-50Hz-25.0hp-637v-25.0A',   '456-50Hz-25.0hp-637v-25.0A'),
        ('456-50Hz-29.5hp-333v-55.0A',   '456-50Hz-29.5hp-333v-55.0A'),
        ('456-50Hz-29.5hp-575v-32.0A',   '456-50Hz-29.5hp-575v-32.0A'),
        ('456-50Hz-29.5hp-666v-27.5A',   '456-50Hz-29.5hp-666v-27.5A'),
        ('456-50Hz-33.5hp-375v-57.0A',   '456-50Hz-33.5hp-375v-57.0A'),
        ('456-50Hz-33.5hp-562v-38.0A',   '456-50Hz-33.5hp-562v-38.0A'),
        ('456-50Hz-33.5hp-658v-32.5A',   '456-50Hz-33.5hp-658v-32.5A'),
        ('456-50Hz-33.5hp-750v-28.5A',   '456-50Hz-33.5hp-750v-28.5A'),
        ('456-50Hz-41.5hp-583v-45.5A',   '456-50Hz-41.5hp-583v-45.5A'),
        ('456-50Hz-41.5hp-700v-38.0A',   '456-50Hz-41.5hp-700v-38.0A'),
        ('456-50Hz-41.5hp-816v-32.5A',   '456-50Hz-41.5hp-816v-32.5A'),
        ('456-50Hz-50.0hp-558v-57.0A',   '456-50Hz-50.0hp-558v-57.0A'),
        ('456-50Hz-50.0hp-646v-50.0A',   '456-50Hz-50.0hp-646v-50.0A'),
        ('456-50Hz-50.0hp-700v-45.0A',   '456-50Hz-50.0hp-700v-45.0A'),
        ('456-50Hz-50.0hp-833v-38.0A',   '456-50Hz-50.0hp-833v-38.0A'),
        ('456-50Hz-58.5hp-654v-57.0A',   '456-50Hz-58.5hp-654v-57.0A'),
        ('456-50Hz-58.5hp-816v-45.0A',   '456-50Hz-58.5hp-816v-45.0A'),
        ('456-50Hz-58.5hp-975v-38.0A',   '456-50Hz-58.5hp-975v-38.0A'),
        ('456-50Hz-66.5hp-750v-57.0A',   '456-50Hz-66.5hp-750v-57.0A'),
        ('456-50Hz-66.5hp-933v-45.0A',   '456-50Hz-66.5hp-933v-45.0A'),
        ('456-50Hz-66.5hp-1125v-38.0A',  '456-50Hz-66.5hp-1125v-38.0A'),        
        ('456-50Hz-75.0hp-833v-57.0A',  '456-50Hz-75.0hp-833v-57.0A'),
        ('456-50Hz-75.0hp-1050v-45.0A', '456-50Hz-75.0hp-1050v-45.0A'),
        ('456-50Hz-75.0hp-1250v-38.0A', '456-50Hz-75.0hp-1250v-38.0A'),
        ('456-50Hz-75.0hp-1666v-29.0A', '456-50Hz-75.0hp-1666v-29.0A'),
        ('456-50Hz-83.5hp-808v-66.0A',  '456-50Hz-83.5hp-808v-66.0A'),
        ('456-50Hz-83.5hp-933v-57.0A',  '456-50Hz-83.5hp-933v-57.0Aட'),
        ('456-50Hz-83.5hp-1166v-45.0A', '456-50Hz-83.5hp-1166v-45.0A'),
        ('456-50Hz-83.5hp-2874v-29.0A', '456-50Hz-83.5hp-2874v-29.0A'),
        ('456-50Hz-91.5hp-900v-65.0A',  '456-50Hz-91.5hp-900v-65.0A'),
        ('456-50Hz-91.5hp-1033v-57.0A', '456-50Hz-91.5hp-1033v-57.0A'),
        ('456-50Hz-100.0hp-833v-77.0A', '456-50Hz-100.0hp-833v-77.0A'),
        ('456-50Hz-100.0hp-975v-66.0A', '456-50Hz-100.0hp-975v-66.0A'),
        ('456-50Hz-100.0hp-1125v-57.0A', '456-50Hz-100.0hp-1125v-57.0A'),
        ('456-50Hz-100.0hp-1916v-34.0A', '456-50Hz-100.0hp-1916v-34.0A'),
        ('540-50Hz-16.5hp-371v-29.0A',   '540-50Hz-16.5hp-371v-29.0A'),
        ('540-50Hz-16.5hp-635v-17.0A',   '540-50Hz-16.5hp-635v-17.0A'),
        ('540-50Hz-25.0hp-371v-44.0A',   '540-50Hz-25.0hp-371v-44.0A'),
        ('540-50Hz-25.0hp-600v-27.5A',   '540-50Hz-25.0hp-600v-27.5A'),
        ('540-50Hz-33.5hp-371v-59.0A',   '540-50Hz-33.5hp-371v-59.0A'),
        ('540-50Hz-33.5hp-558v-39.0A',   '540-50Hz-33.5hp-558v-39.0A'),
        ('540-50Hz-33.5hp-616v-36.0A',   '540-50Hz-33.5hp-616v-36.0A'),
        ('540-50Hz-33.5hp-741v-30.0A',   '540-50Hz-33.5hp-741v-30.0A'),
        ('540-50Hz-41.5hp-358v-75.0A',   '540-50Hz-41.5hp-358v-75.0A'),
        ('540-50Hz-41.5hp-616v-44.0A',   '540-50Hz-41.5hp-616v-44.0A'),
        ('540-50Hz-41.5hp-766v-33.0A',   '540-50Hz-41.5hp-766v-33.0A'),
        ('540-50Hz-50.0hp-371v-87.0A',   '540-50Hz-50.0hp-371v-87.0A'),
        ('540-50Hz-50.0hp-554v-58.0A',   '540-50Hz-50.0hp-554v-58.0A'),
        ('540-50Hz-50.0hp-629v-52.0A',   '540-50Hz-50.0hp-629v-52.0A'),
        ('540-50Hz-50.0hp-741v-44.0A',   '540-50Hz-50.0hp-741v-44.0A'),
        ('540-50Hz-50.0hp-825v-39.0A',   '540-50Hz-50.0hp-825v-39.0A'),
        ('540-50Hz-58.5hp-646v-58.0A',   '540-50Hz-58.5hp-646v-58.0A'),
        ('540-50Hz-58.5hp-733v-51.0A',   '540-50Hz-58.5hp-733v-51.0A'),
        ('540-50Hz-58.5hp-862v-44.0A',   '540-50Hz-58.5hp-862v-44.0A'),  
        ('540-50Hz-66.5hp-571v-76.0A',   '540-50Hz-66.5hp-571v-76.0A'),
        ('540-50Hz-66.5hp-641v-68.0A',   '540-50Hz-66.5hp-641v-68.0A'),      
        ('540-50Hz-66.5hp-741v-58.0A',   '540-50Hz-66.5hp-741v-58.0A'),
        ('540-50Hz-66.5hp-987v-44.0A',   '540-50Hz-66.5hp-987v-44.0A'),         
        ('540-50Hz-83.5hp-616v-85.0A',   '540-50Hz-83.5hp-616v-85.0A'),
        ('540-50Hz-83.5hp-712v-74.0A',   '540-50Hz-83.5hp-712v-74.0A'),      
        ('540-50Hz-83.5hp-800v-66.0A',   '540-50Hz-83.5hp-800v-66.0A'),
        ('540-50Hz-83.5hp-916v-58.0A',   '540-50Hz-83.5hp-916v-58.0A'),
        ('540-50Hz-83.5hp-1833v-29.0A',  '540-50Hz-83.5hp-1833v-29.0A'),
        ('540-50Hz-100.0hp-641v-98.0A',   '540-50Hz-100.0hp-641v-98.0A'),      
        ('540-50Hz-100.0hp-741v-85.0A',   '540-50Hz-100.0hp-741v-85.0A'),
        ('540-50Hz-100.0hp-1108v-57.0A',  '540-50Hz-100.0hp-1108v-57.0A'),
        ('540-50Hz-100.0hp-1833v-32.0A',  '540-50Hz-100.0hp-1833v-32.0A'),
        ('540-50Hz-108.0hp-696v-98.0A',   '540-50Hz-108.0hp-696v-98.0A'),      
        ('540-50Hz-108.0hp-804v-84.0A',   '540-50Hz-108.0hp-804v-84.0A'),
        ('540-50Hz-125.0hp-804v-97.0A',   '540-50Hz-125.0hp-804v-97.0A'),      
        ('540-50Hz-125.0hp-960v-75.0A',   '540-50Hz-125.0hp-960v-75.0A'),
        ('540-50Hz-125.0hp-1791v-43.0A',  '540-50Hz-125.0hp-1791v-43.0A'),
        ('540-50Hz-133.0hp-845v-99.0A',   '540-50Hz-133.0hp-845v-99.0A'),      
        ('540-50Hz-133.0hp-1858v-45.0A',  '540-50Hz-133.0hp-1858v-45.0A'),   
        ('540-50Hz-150.0hp-833v-113.0A',  '540-50Hz-150.0hp-833v-113.0A'),   
        ('540-50Hz-150.0hp-1666v-57.0A',   '540-50Hz-150.0hp-1666v-57.0A'),   
        ('540-50Hz-167.0hp-966-105.0A',    '540-50Hz-167.0hp-966-105.0A'),      
        ('540-50Hz-167.0hp-1833v-53.0A',   '540-50Hz-167.0hp-1833v-53.0A'),   
        ('540-50Hz-187.0hp-1000v-120.0A',  '540-50Hz-187.0hp-1000v-120.0A'), 
        ('540-50Hz-187.0hp-1916v-62.5A',   '540-50Hz-187.0hp-1916v-62.5A'), 
        ('738-50Hz-167.0hp-1916v-53.0A',   '738-50Hz-167.0hp-1916v-53.0A'),   
        ('738-50Hz-183.0hp-1916v-97.0A',   '738-50Hz-183.0hp-1916v-97.0A'),      
        ('738-50Hz-183.0hp-1125v-57.0A',   '738-50Hz-183.0hp-1125v-57.0A'),   
        ('738-50Hz-200.0hp-1916v-64.0A',   '738-50Hz-200.0hp-1916v-64.0A'),      
        ('738-50Hz-216.0hp-1916v-70.0A',   '738-50Hz-216.0hp-1916v-70.0A'), 
        ('375-60Hz-07.5hp-415v-13.5A',   '375-60Hz-07.5hp-415v-13.5A'),
        ('375-60Hz-10.5hp-400v-20.0A',   '375-60Hz-10.5hp-400v-20.0A'),
        ('375-60Hz-10.5hp-690v-12.0A',   '375-60Hz-10.5hp-690v-12.0A'),
        ('375-60Hz-15.0hp-330v-34.0A',   '375-60Hz-15.0hp-330v-34.0A'),
        ('375-60Hz-15.0hp-415v-27.0A',   '375-60Hz-15.0hp-415v-27.0A'),
        ('375-60Hz-19.5hp-415v-35.0A',   '375-60Hz-19.5hp-415v-35.0A'),
        ('375-60Hz-19.5hp-650v-22.5A',   '375-60Hz-19.5hp-650v-22.5A'),
        ('375-60Hz-22.5hp-440v-38.5A',   '375-60Hz-22.5hp-440v-38.5A'),
        ('375-60Hz-22.5hp-750v-22.5A',   '375-60Hz-22.5hp-750v-22.5A'),
        ('375-60Hz-25.5hp-650v-29.5A',   '375-60Hz-25.5hp-650v-29.5A'),
        ('375-60Hz-25.5hp-780v-24.5A',   '375-60Hz-25.5hp-780v-24.5A'),
        ('456-60Hz-10.0hp-440v-15.0A',   '456-60Hz-10.0hp-440v-15.0A'),
        ('456-60Hz-15.0hp-400v-23.0A',   '456-60Hz-15.0hp-400v-23.0A'),
        ('456-60Hz-15.0hp-750v-14.0A',   '456-60Hz-15.0hp-750v-14.0A'),
        ('456-60Hz-20.0hp-460v-28.0A',   '456-60Hz-20.0hp-460v-28.0A'),
        ('456-60Hz-20.0hp-760v-17.0A',   '456-60Hz-20.0hp-760v-17.0A'),
        ('456-60Hz-25.0hp-420v-38.0A',   '456-60Hz-25.0hp-420v-38.0A'),
        ('456-60Hz-25.0hp-700v-22.0A',   '456-60Hz-25.0hp-700v-22.0A'),
        ('456-60Hz-30.0hp-440v-43.0A',   '456-60Hz-30.0hp-440v-43.0A'),
        ('456-60Hz-30.0hp-765v-25.0A',   '456-60Hz-30.0hp-765v-25.0A'),
        ('456-60Hz-35.0hp-400v-55.0A',   '456-60Hz-35.0hp-400v-55.0A'),
        ('456-60Hz-35.0hp-690v-32.0A',   '456-60Hz-35.0hp-690v-32.0A'),
        ('456-60Hz-35.0hp-800v-27.5A',   '456-60Hz-35.0hp-800v-27.5A'),
        ('456-60Hz-40.0hp-450v-57.0A',   '456-60Hz-40.0hp-450v-57.0A'),
        ('456-60Hz-40.0hp-675v-38.0A',   '456-60Hz-40.0hp-675v-38.0A'),
        ('456-60Hz-40.0hp-790v-32.5A',   '456-60Hz-40.0hp-790v-32.5A'),
        ('456-60Hz-40.0hp-900v-28.5A',   '456-60Hz-40.0hp-900v-26.5A'),
        ('456-60Hz-50.0hp-700v-45.5A',   '456-60Hz-50.0hp-700v-45.5A'),
        ('456-60Hz-50.0hp-840v-38.0A',   '456-60Hz-50.0hp-840v-38.0A'),
        ('456-60Hz-50.0hp-980v-32.5A',   '456-60Hz-50.0hp-980v-32.5A'),
        ('456-60Hz-60.0hp-670v-57.0A',   '456-60Hz-60.0hp-670v-57.0A'),
        ('456-60Hz-60.0hp-775v-50.0A',   '456-60Hz-60.0hp-775v-50.0A'),
        ('456-60Hz-60.0hp-840v-45.0A',   '456-60Hz-60.0hp-840v-45.0A'),
        ('456-60Hz-60.0hp-1000v-38.0A',  '456-60Hz-60.0hp-1000v-38.0A'),
        ('456-60Hz-70.0hp-785v-57.0A',   '456-60Hz-70.0hp-785v-57.0A'),
        ('456-60Hz-70.0hp-980v-45.0A',   '456-60Hz-70.0hp-980v-45.0A'),
        ('456-60Hz-70.0hp-1170v-38.0A',  '456-60Hz-70.0hp-1170v-38.0A'),
        ('456-60Hz-80.0hp-900v-57.0A',   '456-60Hz-80.0hp-900v-57.0A'),
        ('456-60Hz-80.0hp-1120v-45.0A',  '456-60Hz-80.0hp-1120v-45.0A'),
        ('456-60Hz-80.0hp-1350v-38.0A',  '456-60Hz-80.0hp-1350v-38.0A'),
        ('456-60Hz-90.0hp-1000v-57.0A',  '456-60Hz-90.0hp-1000v-57.0A'),
        ('456-60Hz-90.0hp-1260v-45.0A',  '456-60Hz-90.0hp-1260v-45.0A'),
        ('456-60Hz-90.0hp-1500v-38.0A',  '456-60Hz-90.0hp-1500v-38.0A'),
        ('456-60Hz-90.0hp-2000v-29.0A',  '456-60Hz-90.0hp-2000v-29.0A'),
        ('456-60Hz-100.0hp-970v-66.0A',  '456-60Hz-100.0hp-970v-66.0A'),
        ('456-60Hz-100.0hp-1120v-57.0A', '456-60Hz-100.0hp-1120v-57.0A'),
        ('456-60Hz-100.0hp-1400v-45.0A', '456-60Hz-100.0hp-1400v-45.0A'),
        ('456-60Hz-100.0hp-2250v-29.0A', '456-60Hz-100.0hp-2250v-29.0A'),
        ('456-60Hz-110.0hp-1080v-65.0A', '456-60Hz-110.0hp-1080v-65.0A'),
        ('456-60Hz-110.0hp-1240v-57.0A', '456-60Hz-110.0hp-1240v-57.0A'),
        ('456-60Hz-120.0hp-1000v-77.0A', '456-60Hz-120.0hp-1000v-77.0A'),
        ('456-60Hz-120.0hp-1170v-66.0A', '456-60Hz-120.0hp-1170v-66.0A'),
        ('456-60Hz-120.0hp-1350v-57.0A', '456-60Hz-120.0hp-1350v-57.0A'),
        ('456-60Hz-120.0hp-2300v-34.0A', '456-60Hz-120.0hp-2300v-34.0A'),
        ('540-60Hz-20.0hp-445v-29.0A',   '540-60Hz-20.0hp-445v-29.0A'),
        ('540-60Hz-20.0hp-762v-17.0A',   '540-60Hz-30.0hp-762v-17.0A'),
        ('540-60Hz-30.0hp-445v-44.0A',   '540-60Hz-30.0hp-445v-44.0A'),
        ('540-60Hz-30.0hp-720v-27.5A',   '540-60Hz-30.0hp-720v-27.5A'),
        ('540-60Hz-40.0hp-445v-59.0A',   '540-60Hz-40.0hp-445v-59.0A'),
        ('540-60Hz-40.0hp-670v-39.0A',   '540-60Hz-40.0hp-670v-39.0A'),
        ('540-60Hz-40.0hp-740v-36.0A',   '540-60Hz-40.0hp-740v-36.0A'),
        ('540-60Hz-40.0hp-890v-30.0A',   '540-60Hz-40.0hp-890v-30.0A'),
        ('540-60Hz-50.0hp-430v-75.0A',   '540-60Hz-50.0hp-430v-75.0A'),
        ('540-60Hz-50.0hp-740v-44.0A',   '540-60Hz-50.0hp-740v-44.0A'),
        ('540-60Hz-50.0hp-920v-33.0A',   '540-60Hz-50.0hp-920v-33.0A'),
        ('540-60Hz-60.0hp-445v-87.0A',   '540-60Hz-60.0hp-445v-87.0A'),
        ('540-60Hz-60.0hp-665v-58.0A',   '540-60Hz-60.0hp-665v-58.0A'),
        ('540-60Hz-60.0hp-755v-52.0A',   '540-60Hz-60.0hp-755v-52.0A'),
        ('540-60Hz-60.0hp-890v-44.0A',   '540-60Hz-60.0hp-890v-44.0A'),
        ('540-60Hz-60.0hp-990v-39.0A',   '540-60Hz-50.0hp-740v-44.0A'),
        ('540-60Hz-70.0hp-755v-58.0A',   '540-60Hz-70.0hp-755v-58.0A'),
        ('540-60Hz-70.0hp-880v-51.0A',   '540-60Hz-70.0hp-880v-51.0A'),
        ('540-60Hz-70.0hp-1035-44.0A',   '540-60Hz-70.0hp-1035-44.0A'),  
        ('540-60Hz-80.0hp-685v-76.0A',   '540-60Hz-80.0hp-685v-76.0A'),
        ('540-60Hz-80.0hp-770v-68.0A',   '540-60Hz-80.0hp-770v-68.0A'),      
        ('540-60Hz-80.0hp-890v-58.0A',   '540-60Hz-80.0hp-890v-58.0A'),
        ('540-60Hz-80.0hp-1185v-44.0A',  '540-60Hz-80.0hp-1185v-44.0A'),         
        ('540-60Hz-100.0hp-740v-85.0A',   '540-60Hz-100.0hp-740v-85.0A'),
        ('540-60Hz-100.0hp-855v-74.0A',   '540-60Hz-100.0hp-855v-74.0A'),      
        ('540-60Hz-100.0hp-960v-66.0A',   '540-60Hz-100.0hp-960v-66.0A'),
        ('540-60Hz-100.0hp-1100v-58.0A',  '540-60Hz-100.0hp-1100v-58.0A'),
        ('540-60Hz-100.0hp-2200v-29.0A',  '540-60Hz-100.0hp-2200v-29.0A'),
        ('540-60Hz-120.0hp-770v-98.0A',   '540-60Hz-120.0hp-770v-98.0A'),      
        ('540-60Hz-120.0hp-890v-85.0A',   '540-60Hz-120.0hp-890v-85.0A'),
        ('540-60Hz-120.0hp-1330v-57.0A',  '540-60Hz-120.0hp-1330v-57.0A'),
        ('540-60Hz-120.0hp-2200v-32.0A',  '540-60Hz-120.0hp-2200v-32.0A'),
        ('540-60Hz-130.0hp-835v-98.0A',   '540-60Hz-130.0hp-835v-98.0A'),      
        ('540-60Hz-130.0hp-965v-84.0A',   '540-60Hz-130.0hp-965v-84.0A'),
        ('540-60Hz-150.0hp-965v-97.0A',   '540-60Hz-150.0hp-965v-97.0A'),      
        ('540-60Hz-150.0hp-1150v-75.0A',  '540-60Hz-150.0hp-1150v-75.0A'),
        ('540-60Hz-150.0hp-2150v-43.0A',  '540-60Hz-150.0hp-2150v-43.0A'),
        ('540-60Hz-160.0hp-1015v-99.0A',   '540-60Hz-160.0hp-1015v-99.0A'),      
        ('540-60Hz-160.0hp-2230v-45.0A',   '540-60Hz-160.0hp-2230v-45.0A'),   
        ('540-60Hz-180.0hp-1000v-113.0A',  '540-60Hz-180.0hp-1000v-113.0A'),      
        ('540-60Hz-180.0hp-2000v-57.0A',   '540-60Hz-180.0hp-2000v-57.0A'),   
        ('540-60Hz-200.0hp-1160v-105.0A',  '540-60Hz-200.0hp-1160v-105.0A'),      
        ('540-60Hz-200.0hp-2200v-53.0A',   '540-60Hz-200.0hp-2200v-53.0A'),   
        ('540-60Hz-225.0hp-1200v-120.0A',  '540-60Hz-225.0hp-1200v-120.0A'),      
        ('540-60Hz-225.0hp-2300v-62.5A',   '540-60Hz-225.0hp-2300v-62.5A'), 
        ('738-60Hz-200.0hp-2300v-53.0A',   '738-60Hz-200.0hp-2300v-53.0A'),   
        ('738-60Hz-220.0hp-1350v-97.0A',   '738-60Hz-220.0hp-1350v-97.0A'),      
        ('738-60Hz-220.0hp-2300v-57.0A',   '738-60Hz-220.0hp-2300v-57.0A'),   
        ('738-60Hz-240.0hp-2300v-64.0A',   '738-60Hz-240.0hp-2300v-64.0A'),      
        ('738-60Hz-260.0hp-2300v-70.0A',   '738-60Hz-260.0hp-2300v-70.0A'),  


    )
    motor = models.CharField(max_length=100, choices = Motors,default = '375-50Hz-06.25hp-345v-13.5A')
    
   