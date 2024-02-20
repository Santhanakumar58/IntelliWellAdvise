from django.db import models
from blackoilpvt.models import BlackoilPVT

# Create your models here.
class JetPumpDesignModel(models.Model):    
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()     
    design_Date = models.DateField()  
    design_Liquid = models.FloatField() 
    water_Cut = models.FloatField() 
    water_Spgr= models.FloatField()
    th_Pres = models.FloatField() 
    th_Temp = models.FloatField() 
    curr_Res_Pres = models.FloatField()
    min_Pwf =models.FloatField()
    gas_Oil_Ratio = models.FloatField()   
    pump_depth =models.FloatField()
    pvt_Well= models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE, null=True, blank=True)