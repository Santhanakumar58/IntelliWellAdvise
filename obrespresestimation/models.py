from django.db import models

class OBReservoirPressureEstimationModel(models.Model):  
    obfgid = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField()  
    obanalysis_Date = models.DateField()  
    oblayer_Permeability = models.FloatField()
    oblayer_Thickness = models.FloatField()
    oblayer_Porosity =models.FloatField()
    obtotal_Compressibility=models.FloatField()
    obmu_oil = models.FloatField()
    oboil_FVF = models.FloatField()
    obwellbore_Radius = models.FloatField()
    oboil_Prod_Rate = models.FloatField()
    obini_Res_Pres = models.FloatField()
    obdrainage_Radius = models.FloatField() 
    
    def __date__(self):
        return self.obanalysis_Date  

