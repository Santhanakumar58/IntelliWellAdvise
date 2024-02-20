from django.db import models



class OBDrillingWellData(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField() 
    obsurvey_Date = models.DateField() 
    obrkb_to_WH = models.FloatField()   
    obrkb_to_GL = models.FloatField()   
    obgl_to_MSL = models.FloatField()   
    obrkb_to_MSL = models.FloatField()     
    obwh_to_MSL = models.FloatField()   
    oblattitude = models.CharField(max_length=20) 
    oblongitude = models.CharField(max_length=20)     
    obtotal_Measured_Depth = models.FloatField()   
    obtotal_True_Vertical_Depth = models.FloatField()     
    obafe_No=models.CharField(max_length=40)    
   
