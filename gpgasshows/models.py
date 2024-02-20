from django.db import models

class GPGasShowModel(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpformation = models.CharField(max_length=100)    
    gptop_MD = models.FloatField()   
    gpbottom_MD = models.FloatField()   
    gptotal_Gas = models.FloatField()    
    gpmethane = models.FloatField()   
    gpethane = models.FloatField()  
    gppropane = models.FloatField()  
    gpiso_Butane = models.FloatField()  
    gpneo_Butane = models.FloatField()  
    gpiso_Pentane = models.FloatField()  
    gpneo_Pentane = models.FloatField()  
    gpremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.gpwellid

