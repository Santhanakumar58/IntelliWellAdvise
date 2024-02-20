from django.db import models

class GasShowModel(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    formation = models.CharField(max_length=100)    
    top_MD = models.FloatField()   
    bottom_MD = models.FloatField()   
    total_Gas = models.FloatField()    
    methane = models.FloatField()   
    ethane = models.FloatField()  
    propane = models.FloatField()  
    iso_Butane = models.FloatField()  
    neo_Butane = models.FloatField()  
    iso_Pentane = models.FloatField()  
    neo_Pentane = models.FloatField()  
    remarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.wellid
