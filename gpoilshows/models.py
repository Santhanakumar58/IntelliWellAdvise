from django.db import models

class GPOilShowModel(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpformation = models.CharField(max_length=100)    
    gptop_MD = models.FloatField()   
    gpbottom_MD = models.FloatField()   
    gpsample_Type = models.CharField(max_length=100)    
    gpsample_Description = models.CharField(max_length=500) 
    gpremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.gpwellid
