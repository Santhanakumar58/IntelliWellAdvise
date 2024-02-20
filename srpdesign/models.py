from django.db import models
from blackoilpvt.models import BlackoilPVT

class SRPDesignModel(models.Model):    
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()     
    design_Date = models.DateField()  
    design_Liquid = models.FloatField(default=100) 
    water_Cut = models.FloatField() 
    gas_Oil_Ratio = models.FloatField()  
    water_spgr= models.FloatField(default=1.0) 
    th_Pres = models.FloatField() 
    th_Temp = models.FloatField() 
    curr_Res_Pres = models.FloatField()
    min_Pwf =models.FloatField()
    pump_Depth =models.FloatField()
    fluid_Level= models.FloatField()
    pumping_Speed = models.PositiveIntegerField()
    surface_Stroke_Length= models.FloatField()
   
    anchored = models.BooleanField(default=True)    
    Rod_Numbers= (
                ('44','44'),
                ('54','54'),
                ('55','55'),
                ('64','64'),
                ('65','65'),
                ('66','66'),
                ('75','75'),
                ('76','76'),
                ('77','77'),
                ('85','85'),
                ('86','86'),
                ('87','87'),                  
                ('88','88'),
                ('96','96'),
                ('97','97'),
                ('98','98'),
                ('99','99'),
                ('107','107'),  
                ('108','108'), 
                ('109','109') 
            )
    rod_No = models.CharField(max_length=100, choices=Rod_Numbers, default="44")
    plunger_Diameters = (
            ('1.06', '1.06'),
            ('1.25', '1.25'),
            ('1.50', '1.50'),
            ('1.75', '1.75'),
            ('2.00', '2.00'),
            ('2.25', '2.25'),
            ('2.50', '2.50'),
            ('2.75', '2.75'),
            ('3.25', '3.25'),
            ('3.75', '3.75'),
            ('4.75', '4.75'),
        )
    plunger_Dia = models.CharField(max_length=10, choices=plunger_Diameters, default ="1.06")    

    @property 
    def rod_Weight(self):
        if self.rod_No=='44' :
            rod_Weight = 0.7260
            print(self.rod_No)
        else:
            rod_Weight =0.67
        return rod_Weight
    pvt_Well= models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE, null=True, blank=True)
