from django.db import models

class TestResultModel(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    formation = models.CharField(max_length=100)    
    top_MD = models.FloatField()   
    bottom_MD = models.FloatField()   
    test_Duration = models.FloatField()  
    choke_Size = models.CharField(max_length=100)   
    thp = models.FloatField() 
    bhp = models.FloatField() 
    liquid_Rate =models.FloatField()
    oil_Rate =models.FloatField()
    gas_Rate =models.FloatField()
    water_Cut =models.FloatField()
    remarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.wellid

