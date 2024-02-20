from django.db import models

class GIReservoirPressureEstimationModel(models.Model):  
    gifgid = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField()  
    gianalysis_Date = models.DateField()  
    gilayer_Permeability = models.FloatField()
    gilayer_Thickness = models.FloatField()
    gilayer_Porosity =models.FloatField()
    gitotal_Compressibility=models.FloatField()
    gimu_oil = models.FloatField()
    gioil_FVF = models.FloatField()
    giwellbore_Radius = models.FloatField()
    gioil_Prod_Rate = models.FloatField()
    giini_Res_Pres = models.FloatField()
    gidrainage_Radius = models.FloatField() 
    
    def __date__(self):
        return self.gianalysis_Date  

