from django.db import models

class WIFormatioPressureModel(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField()  
    wistat_Group = models.CharField(max_length=100)     
    wistat_Formation = models.CharField(max_length=100)  
    wistat_Member = models.CharField(max_length=100)    
    wimeasured_Depth = models.FloatField()   
    wipressure = models.FloatField()    
    wiporosity = models.FloatField()   
    wipermeability = models.FloatField()  
    witemperature = models.FloatField()  
    wiremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.wiwellid



