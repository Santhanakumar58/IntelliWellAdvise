from django.db import models



class GPDrillingWellData(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField() 
    gpsurvey_Date = models.DateField() 
    gprkb_to_WH = models.FloatField()   
    gprkb_to_GL = models.FloatField()   
    gpgl_to_MSL = models.FloatField()   
    gprkb_to_MSL = models.FloatField()     
    gpwh_to_MSL = models.FloatField()   
    gplattitude = models.CharField(max_length=20) 
    gplongitude = models.CharField(max_length=20)     
    gptotal_Measured_Depth = models.FloatField()   
    gptotal_True_Vertical_Depth = models.FloatField()     
    gpafe_No=models.CharField(max_length=40)    
   