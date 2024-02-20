from django.db import models

class GPFormatioPressureModel(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpstat_Group = models.CharField(max_length=100)     
    gpstat_Formation = models.CharField(max_length=100)  
    gpstat_Member = models.CharField(max_length=100)    
    gpmeasured_Depth = models.FloatField()   
    gppressure = models.FloatField()    
    gpporosity = models.FloatField()   
    gppermeability = models.FloatField()  
    gptemperature = models.FloatField()  
    gpremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.gpwellid


