from django.db import models
from differentialliberation.models import DifferentialLiberationModel

# Create your models here.
class DifferentialLiberationdata(models.Model):    
    differentialliberation = models.ForeignKey(DifferentialLiberationModel, on_delete=models.CASCADE, null=True, blank=True )   
    pressure = models.FloatField()    
    solution_gor = models.FloatField() 
    relative_oil_volume = models.FloatField()
    relative_total_volume = models.FloatField()       
    oil_density = models.FloatField(blank=True, null=True)   
    deviation_factor = models.FloatField(blank=True, null=True)
    gas_fvf = models.FloatField()
    incremental_gas_gravity = models.FloatField()


    def __int__(self):       
        return self.differentialliberation 
