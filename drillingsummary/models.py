from django.db import models


class DrillingSummary(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField() 
    start_Date = models.DateField() 
    end_Date = models.DateField()
    liquid_Rate = models.FloatField()   
    water_Cut = models.FloatField()   
    gas_Rate = models.FloatField()   
    oil_Rate = models.FloatField()     
    gas_Oil_Ratio = models.FloatField()   
    drilling_Summary = models.TextField(max_length=2000) 
    
   