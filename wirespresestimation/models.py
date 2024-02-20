from django.db import models

class WIReservoirPressureEstimationModel(models.Model):  
    wifgid = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField()  
    wianalysis_Date = models.DateField()  
    wilayer_Permeability = models.FloatField()
    wilayer_Thickness = models.FloatField()
    wilayer_Porosity =models.FloatField()
    witotal_Compressibility=models.FloatField()
    wimu_oil = models.FloatField()
    wioil_FVF = models.FloatField()
    wiwellbore_Radius = models.FloatField()
    wioil_Prod_Rate = models.FloatField()
    wiini_Res_Pres = models.FloatField()
    widrainage_Radius = models.FloatField() 
    
    def __date__(self):
        return self.wianalysis_Date  
