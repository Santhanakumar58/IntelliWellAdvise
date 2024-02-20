from django.db import models

class OilShowModel(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    formation = models.CharField(max_length=100)    
    top_MD = models.FloatField()   
    bottom_MD = models.FloatField()   
    sample_Type = models.CharField(max_length=100)    
    sample_Description = models.CharField(max_length=500) 
    remarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.wellid
