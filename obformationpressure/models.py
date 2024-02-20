from django.db import models

class OBFormatioPressureModel(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField()  
    obstat_Group = models.CharField(max_length=100)     
    obstat_Formation = models.CharField(max_length=100)  
    obstat_Member = models.CharField(max_length=100)    
    obmeasured_Depth = models.FloatField()   
    obpressure = models.FloatField()    
    obporosity = models.FloatField()   
    obpermeability = models.FloatField()  
    obtemperature = models.FloatField()  
    obremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.obwellid


