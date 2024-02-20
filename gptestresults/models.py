from django.db import models

class GPTestResultModel(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpformation = models.CharField(max_length=100)    
    gptop_MD = models.FloatField()   
    gpbottom_MD = models.FloatField()   
    gptest_Duration = models.FloatField()  
    gpchoke_Size = models.CharField(max_length=100)   
    gpthp = models.FloatField() 
    gpbhp = models.FloatField() 
    gpliquid_Rate =models.FloatField()
    gpoil_Rate =models.FloatField()
    gpgas_Rate =models.FloatField()
    gpwater_Cut =models.FloatField()
    gpremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.gpwellid


