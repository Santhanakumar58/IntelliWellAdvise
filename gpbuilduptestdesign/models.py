from django.db import models

# Create your models here.

class GPPressureBuildupTestDesignModel(models.Model):  
    gpfgid = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpdesign_Date = models.DateField()  
    gpdesign_Rate = models.FloatField()
    gplayer_Thickness = models.FloatField()
    gplayer_Permeability =models.FloatField()   
    gpmu_oil = models.FloatField()
    gptotal_Compressibility=models.FloatField()
    


