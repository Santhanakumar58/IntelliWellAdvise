from django.db import models

class ReservoirPressureEstimationModel(models.Model):  
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    analysis_Date = models.DateField()  
    layer_Permeability = models.FloatField()
    layer_Thickness = models.FloatField()
    layer_Porosity =models.FloatField()
    total_Compressibility=models.FloatField()
    mu_oil = models.FloatField()
    oil_FVF = models.FloatField()
    wellbore_Radius = models.FloatField()
    oil_Prod_Rate = models.FloatField()
    ini_Res_Pres = models.FloatField()
    drainage_Radius = models.FloatField() 
    
    def __date__(self):
        return self.analysis_Date  
