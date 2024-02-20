from django.db import models



class GPReservoirPressure(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()
    gpsurvey_Date = models.DateField()
    Pressure_Survey_Types = (
        ("NONE" , "None"),
        ("RFT", "Rft"),
        ("DST" , "Dst"),
        ('PBU', 'Pbu'),
        ('SHUTIN', 'Shutin')
   )
    gpsurvey_Type =models.CharField(max_length = 20,choices = Pressure_Survey_Types,default = '1')
    gpgauge_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    gpgauge_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    gpdatum_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    gpdatum_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    gplayer_permeability = models.DecimalField(decimal_places=3, max_digits=10) 
    gplayer_Thickness = models.DecimalField(decimal_places=3, max_digits=10)    
    gplayer_Skin = models.DecimalField(decimal_places=3, max_digits=10) 
   
