from django.db import models

class GPReservoirPressureEstimationModel(models.Model):  
    gpfgid = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpanalysis_Date = models.DateField()  
    gplayer_Permeability = models.FloatField()
    gplayer_Thickness = models.FloatField()
    gplayer_Porosity =models.FloatField()
    gptotal_Compressibility=models.FloatField()
    gpmu_oil = models.FloatField()
    gpoil_FVF = models.FloatField()
    gpwellbore_Radius = models.FloatField()
    gpoil_Prod_Rate = models.FloatField()
    gpini_Res_Pres = models.FloatField()
    gpdrainage_Radius = models.FloatField() 
    
    def __date__(self):
        return self.gpanalysis_Date  
