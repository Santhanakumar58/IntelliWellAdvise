from django.db import models

class WIOilShowModel(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField()  
    wiformation = models.CharField(max_length=100)    
    witop_MD = models.FloatField()   
    wibottom_MD = models.FloatField()   
    wisample_Type = models.CharField(max_length=100)    
    wisample_Description = models.CharField(max_length=500) 
    wiremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.wiwellid