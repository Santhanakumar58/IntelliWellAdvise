from django.db import models

# Create your models here.
class GasLiftModel(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()     
    design_Date = models.DateField()  
    design_Liquid = models.FloatField() 
    water_Cut = models.FloatField() 
    th_Pres = models.FloatField() 
    th_Temp = models.FloatField() 
    gas_Inj_Pres = models.FloatField()
    available_Gas = models.FloatField()
    kick_Off_Pres = models.FloatField()
    kill_Fluid_Grad = models.FloatField()
    port_Size = models.FloatField()
    min_Valve_Sapcing = models.FloatField()



   