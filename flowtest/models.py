from django.db import models

# Create your models here.
class FlowTestModel(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    formation = models.CharField(max_length=100) 
    test_Date = models.DateField()  
    test_Duration = models.FloatField()  
    choke_Size = models.CharField(max_length=100)   
    th_Pres = models.FloatField() 
    th_Temp = models.FloatField() 
    liquid_Rate =models.FloatField()
    oil_Rate =models.FloatField()
    gas_Rate =models.FloatField()   
    fl_Pres =models.FloatField()
    fl_Temp =models.FloatField()
    sep_Pres =models.FloatField()
    sep_Temp =models.FloatField()
    remarks = models.CharField(max_length=100) 

    @property
    def water_Rate(self):        
        return round( (self.liquid_Rate -self.oil_Rate),2)
    
    @property
    def water_Cut(self):        
        return round( (self.water_Rate /self.liquid_Rate * 100),2)

    @property
    def gor(self):        
        return round(self.gas_Rate / self.oil_Rate,2)
     


    def __int__(self):
        return self.wellid

