from django.db import models

class GIFormatioPressureModel(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField()  
    gistat_Group = models.CharField(max_length=100)     
    gistat_Formation = models.CharField(max_length=100)  
    gistat_Member = models.CharField(max_length=100)    
    gimeasured_Depth = models.FloatField()   
    gipressure = models.FloatField()    
    giporosity = models.FloatField()   
    gipermeability = models.FloatField()  
    gitemperature = models.FloatField()  
    giremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.giwellid



