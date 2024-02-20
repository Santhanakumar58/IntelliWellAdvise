from django.db import models



class GIReservoirPressure(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField()
    gisurvey_Date = models.DateField()
    Pressure_Survey_Types = (
        ("NONE" , "None"),
        ("RFT", "Rft"),
        ("DST" , "Dst"),
        ('PBU', 'Pbu'),
        ('SHUTIN', 'Shutin')
   )
    gisurvey_Type =models.CharField(max_length = 20,choices = Pressure_Survey_Types,default = '1')
    gigauge_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    gigauge_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    gidatum_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    gidatum_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    gilayer_permeability = models.DecimalField(decimal_places=3, max_digits=10) 
    gilayer_Thickness = models.DecimalField(decimal_places=3, max_digits=10)    
    gilayer_Skin = models.DecimalField(decimal_places=3, max_digits=10) 
   




