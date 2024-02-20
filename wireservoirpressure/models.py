from django.db import models

class WIReservoirPressure(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField()
    wisurvey_Date = models.DateField()
    Pressure_Survey_Types = (
        ("NONE" , "None"),
        ("RFT", "Rft"),
        ("DST" , "Dst"),
        ('PBU', 'Pbu'),
        ('SHUTIN', 'Shutin')
   )
    wisurvey_Type =models.CharField(max_length = 20,choices = Pressure_Survey_Types,default = '1')
    wigauge_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    wigauge_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    widatum_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    widatum_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    wilayer_permeability = models.DecimalField(decimal_places=3, max_digits=10) 
    wilayer_Thickness = models.DecimalField(decimal_places=3, max_digits=10)    
    wilayer_Skin = models.DecimalField(decimal_places=3, max_digits=10) 
   

