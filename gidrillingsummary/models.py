from django.db import models


class GIDrillingSummary(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField() 
    gistart_Date = models.DateField() 
    giend_Date = models.DateField()
    giliquid_Rate = models.FloatField()   
    giwater_Cut = models.FloatField()   
    gigas_Rate = models.FloatField()   
    gioil_Rate = models.FloatField()     
    gigas_Oil_Ratio = models.FloatField()   
    gidrilling_Summary = models.TextField(max_length=2000) 
    
   
