from django.db import models

class WITestResultModel(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField()  
    wiformation = models.CharField(max_length=100)    
    witop_MD = models.FloatField()   
    wibottom_MD = models.FloatField()   
    witest_Duration = models.FloatField()  
    wichoke_Size = models.CharField(max_length=100)   
    withp = models.FloatField() 
    wibhp = models.FloatField() 
    wiliquid_Rate =models.FloatField()
    wioil_Rate =models.FloatField()
    wigas_Rate =models.FloatField()
    wiwater_Cut =models.FloatField()
    wiremarks = models.CharField(max_length=100) 
    
    
     
    def __int__(self):
        return self.wiwellid


