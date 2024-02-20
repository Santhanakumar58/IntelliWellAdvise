from django.db import models


class OBDrillingSummary(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField() 
    obstart_Date = models.DateField() 
    obend_Date = models.DateField()
    obliquid_Rate = models.FloatField()   
    obwater_Cut = models.FloatField()   
    obgas_Rate = models.FloatField()   
    oboil_Rate = models.FloatField()     
    obgas_Oil_Ratio = models.FloatField()   
    obdrilling_Summary = models.TextField(max_length=2000) 
    
   