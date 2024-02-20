from django.db import models

class GIGasShowModel(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField()  
    giformation = models.CharField(max_length=100)    
    gitop_MD = models.FloatField()   
    gibottom_MD = models.FloatField()   
    gitotal_Gas = models.FloatField()    
    gimethane = models.FloatField()   
    giethane = models.FloatField()  
    gipropane = models.FloatField()  
    giiso_Butane = models.FloatField()  
    gineo_Butane = models.FloatField()  
    giiso_Pentane = models.FloatField()  
    gineo_Pentane = models.FloatField()  
    giremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.giwellid


