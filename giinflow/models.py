from django.db import models
from sublayers.models import Sublayer
from blackoilpvt.models import BlackoilPVT


class GIProductivityIndexModel(models.Model):
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    analysis_Date = models.DateField()
    productivity_index=models.FloatField()
    reservoir_Pressure=models.FloatField()    
    layer_Name = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True)
    pvt_Well= models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE, null=True, blank=True)
 

class GIVogelModel(models.Model):
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    analysis_Date = models.DateField()
    vogel_Test_Rate=models.FloatField()
    vogel_Test_Pressure=models.FloatField()
    reservoir_Pressure=models.FloatField()    
    layer_Name = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True)
    pvt_Well= models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE, null=True, blank=True)

class GIStandingsModel(models.Model):
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    analysis_Date = models.DateField()
    current_Test_Rate=models.FloatField()
    current_Test_Pressure=models.FloatField()
    current_Reservoir_Pressure=models.FloatField() 
    future_Reservoir_Pressure=models.FloatField()    
    current_Relative_Permeability=models.FloatField() 
    future_Relative_Permeability=models.FloatField()    
    layer_Name = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True)
    pvt_Well= models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE, null=True, blank=True)



class GIWigginsModel(models.Model):
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    analysis_Date = models.DateField()
    wiggins_Test_Rate=models.FloatField()
    wiggins_Test_Pressure=models.FloatField()
    current_Reservoir_Pressure=models.FloatField() 
    future_Reservoir_Pressure=models.FloatField()    
    water_Cut=models.FloatField()   
    layer_Name = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True)
    pvt_Well= models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE, null=True, blank=True)



class GIMultirateModel(models.Model):
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    analysis_Date = models.DateField()
    test_Rate1=models.FloatField()
    test_Pressure1=models.FloatField()
    test_Rate2=models.FloatField()
    test_Pressure2=models.FloatField()
    test_Rate3=models.FloatField()
    test_Pressure3=models.FloatField()
    current_Reservoir_Pressure=models.FloatField()    
    layer_Name = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True)
    pvt_Well= models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE, null=True, blank=True)

class GIDarcyModel(models.Model):
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    analysis_Date = models.DateField()
    layer_Permeability=models.FloatField()
    layer_Thickness=models.FloatField()
    drainage_Radius=models.FloatField()
    wellbore_Radius=models.FloatField()
    layer_Skin=models.FloatField()    
    current_Reservoir_Pressure=models.FloatField()    
    layer_Name = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True)
    pvt_Well = models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE, null=True, blank=True)

