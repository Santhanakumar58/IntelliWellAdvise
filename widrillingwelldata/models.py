from django.db import models

class WIDrillingWellData(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField() 
    wisurvey_Date = models.DateField() 
    wirkb_to_WH = models.FloatField()   
    wirkb_to_GL = models.FloatField()   
    wigl_to_MSL = models.FloatField()   
    wirkb_to_MSL = models.FloatField()     
    wiwh_to_MSL = models.FloatField()   
    wilattitude = models.CharField(max_length=20) 
    wilongitude = models.CharField(max_length=20)     
    witotal_Measured_Depth = models.FloatField()   
    witotal_True_Vertical_Depth = models.FloatField()     
    wiafe_No=models.CharField(max_length=40)    
   
