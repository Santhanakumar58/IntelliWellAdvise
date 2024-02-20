from django.db import models

class WIGasShowModel(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField()  
    wiformation = models.CharField(max_length=100)    
    witop_MD = models.FloatField()   
    wibottom_MD = models.FloatField()   
    witotal_Gas = models.FloatField()    
    wimethane = models.FloatField()   
    wiethane = models.FloatField()  
    wipropane = models.FloatField()  
    wiiso_Butane = models.FloatField()  
    wineo_Butane = models.FloatField()  
    wiiso_Pentane = models.FloatField()  
    wineo_Pentane = models.FloatField()  
    wiremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.wiwellid

