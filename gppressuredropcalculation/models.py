from django.db import models

# Create your models here.
class GPPressuredropCalculationModel(models.Model):  
    gpfgid = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpmodel_Date = models.DateField()  
    gpsource_Pressure = models.FloatField()
    gpsource_Flowrate = models.FloatField()
    gpsource_Temp =models.FloatField()
    gppipe_Angle=models.FloatField()
    gppipe_Length = models.FloatField()
    gppipe_Diam = models.FloatField()
    gpfluid_API = models.FloatField()
    gpfluid_WaterCut = models.FloatField()
    gpfluid_GOR = models.FloatField()
    gpfluid_gas_spgr = models.FloatField()
 
