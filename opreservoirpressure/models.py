from django.db import models



class OPReservoirPressure(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()
    survey_Date = models.DateField()
    Pressure_Survey_Types = (
        ("NONE" , "None"),
        ("RFT", "Rft"),
        ("DST" , "Dst"),
        ('PBU', 'Pbu'),
        ('SHUTIN', 'Shutin')
   )
    survey_Type =models.CharField(max_length = 20,choices = Pressure_Survey_Types,default = '1')
    gauge_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    gauge_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    datum_Depth = models.DecimalField(decimal_places=3, max_digits=10)    
    datum_Pressure = models.DecimalField(decimal_places=3, max_digits=10) 
    layer_permeability = models.DecimalField(decimal_places=3, max_digits=10) 
    layer_Thickness = models.DecimalField(decimal_places=3, max_digits=10)    
    layer_Skin = models.DecimalField(decimal_places=3, max_digits=10) 
   