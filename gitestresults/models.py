from django.db import models

class GITestResultModel(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField()  
    giformation = models.CharField(max_length=100)    
    gitop_MD = models.FloatField()   
    gibottom_MD = models.FloatField()   
    gitest_Duration = models.FloatField()  
    gichoke_Size = models.CharField(max_length=100)   
    githp = models.FloatField() 
    gibhp = models.FloatField() 
    giliquid_Rate =models.FloatField()
    gioil_Rate =models.FloatField()
    gigas_Rate =models.FloatField()
    giwater_Cut =models.FloatField()
    giremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.giwellid



