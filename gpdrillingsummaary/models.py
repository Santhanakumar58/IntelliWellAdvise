from django.db import models


class GPDrillingSummary(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField() 
    gpstart_Date = models.DateField() 
    gpend_Date = models.DateField()
    gpliquid_Rate = models.FloatField()   
    gpwater_Cut = models.FloatField()   
    gpgas_Rate = models.FloatField()   
    gpoil_Rate = models.FloatField()     
    gpgas_Oil_Ratio = models.FloatField()   
    gpdrilling_Summary = models.TextField(max_length=2000) 
    
   