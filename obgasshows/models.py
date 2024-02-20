from django.db import models

class OBGasShowModel(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField()  
    obformation = models.CharField(max_length=100)    
    obtop_MD = models.FloatField()   
    obbottom_MD = models.FloatField()   
    obtotal_Gas = models.FloatField()    
    obmethane = models.FloatField()   
    obethane = models.FloatField()  
    obpropane = models.FloatField()  
    obiso_Butane = models.FloatField()  
    obneo_Butane = models.FloatField()  
    obiso_Pentane = models.FloatField()  
    obneo_Pentane = models.FloatField()  
    obremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.obwellid


