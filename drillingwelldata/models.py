from django.db import models



class DrillingWellData(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField() 
    survey_Date = models.DateField() 
    rkb_to_WH = models.FloatField()   
    rkb_to_GL = models.FloatField()   
    gl_to_MSL = models.FloatField()   
    rkb_to_MSL = models.FloatField()     
    wh_to_MSL = models.FloatField()   
    lattitude = models.CharField(max_length=20) 
    longitude = models.CharField(max_length=20)     
    total_Measured_Depth = models.FloatField()   
    total_True_Vertical_Depth = models.FloatField()     
    afe_No=models.CharField(max_length=40)    
   