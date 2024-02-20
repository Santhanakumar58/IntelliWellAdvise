from django.db import models

class OBReservoirPressure(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField()
    obsurvey_Date = models.DateField()
    Pressure_Survey_Types = (
        ("NONE" , "None"),
        ("RFT", "Rft"),
        ("DST" , "Dst"),
        ('PBU', 'Pbu'),
        ('SHUTIN', 'Shutin')
   )
    obsurvey_Type =models.CharField(max_length = 20,choices = Pressure_Survey_Types,default = '1')
    obgauge_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    obgauge_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    obdatum_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    obdatum_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    oblayer_permeability = models.DecimalField(decimal_places=3, max_digits=10) 
    oblayer_Thickness = models.DecimalField(decimal_places=3, max_digits=10)    
    oblayer_Skin = models.DecimalField(decimal_places=3, max_digits=10) 
   
