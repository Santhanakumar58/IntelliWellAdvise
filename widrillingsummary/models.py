from django.db import models


class WIDrillingSummary(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField() 
    wistart_Date = models.DateField() 
    wiend_Date = models.DateField()
    wiliquid_Rate = models.FloatField()   
    wiwater_Cut = models.FloatField()   
    wigas_Rate = models.FloatField()   
    wioil_Rate = models.FloatField()     
    wigas_Oil_Ratio = models.FloatField()   
    widrilling_Summary = models.TextField(max_length=2000) 
    
   
