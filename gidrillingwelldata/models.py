from django.db import models



class GIDrillingWellData(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField() 
    gisurvey_Date = models.DateField() 
    girkb_to_WH = models.FloatField()   
    girkb_to_GL = models.FloatField()   
    gigl_to_MSL = models.FloatField()   
    girkb_to_MSL = models.FloatField()     
    giwh_to_MSL = models.FloatField()   
    gilattitude = models.CharField(max_length=20) 
    gilongitude = models.CharField(max_length=20)     
    gitotal_Measured_Depth = models.FloatField()   
    gitotal_True_Vertical_Depth = models.FloatField()     
    giafe_No=models.CharField(max_length=40)    
   
