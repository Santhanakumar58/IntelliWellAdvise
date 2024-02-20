from django.db import models

class OBTestResultModel(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField()  
    obformation = models.CharField(max_length=100)    
    obtop_MD = models.FloatField()   
    obbottom_MD = models.FloatField()   
    obtest_Duration = models.FloatField()  
    obchoke_Size = models.CharField(max_length=100)   
    obthp = models.FloatField() 
    obbhp = models.FloatField() 
    obliquid_Rate =models.FloatField()
    oboil_Rate =models.FloatField()
    obgas_Rate =models.FloatField()
    obwater_Cut =models.FloatField()
    obremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.obwellid



