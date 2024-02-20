from django.db import models

# Create your models here.

class PressureBuildupTestDesignModel(models.Model):  
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    design_Date = models.DateField()  
    design_Rate = models.FloatField()
    layer_Thickness = models.FloatField()
    layer_Permeability =models.FloatField()   
    mu_oil = models.FloatField()
    total_Compressibility=models.FloatField()
    

