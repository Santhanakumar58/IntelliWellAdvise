from django.db import models

# Create your models here.
class PressuredropCalculationModel(models.Model):  
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    model_Date = models.DateField()  
    source_Pressure = models.FloatField()
    source_Flowrate = models.FloatField()
    source_Temp =models.FloatField()
    pipe_Angle=models.FloatField()
    pipe_Length = models.FloatField()
    pipe_Diam = models.FloatField()
    fluid_API = models.FloatField()
    fluid_WaterCut = models.FloatField()
    fluid_GOR = models.FloatField()
    fluid_gas_spgr = models.FloatField()
 