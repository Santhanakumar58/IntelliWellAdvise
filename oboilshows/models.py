from django.db import models

class OBOilShowModel(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField()  
    obformation = models.CharField(max_length=100)    
    obtop_MD = models.FloatField()   
    obbottom_MD = models.FloatField()   
    obsample_Type = models.CharField(max_length=100)    
    obsample_Description = models.CharField(max_length=500) 
    obremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.obwellid

