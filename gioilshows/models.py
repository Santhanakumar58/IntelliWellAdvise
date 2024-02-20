from django.db import models

class GIOilShowModel(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField()  
    giformation = models.CharField(max_length=100)    
    gitop_MD = models.FloatField()   
    gibottom_MD = models.FloatField()   
    gisample_Type = models.CharField(max_length=100)    
    gisample_Description = models.CharField(max_length=500) 
    giremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.giwellid

