from django.db import models

class FormatioPressureModel(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    stat_Group = models.CharField(max_length=100)     
    stat_Formation = models.CharField(max_length=100)  
    stat_Member = models.CharField(max_length=100)    
    measured_Depth = models.FloatField()   
    pressure = models.FloatField()    
    porosity = models.FloatField()   
    permeability = models.FloatField()  
    temperature = models.FloatField()  
    remarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.wellid

