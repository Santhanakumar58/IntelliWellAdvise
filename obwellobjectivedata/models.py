from django.db import models
from obwellobjectives.models import OBWellobjective

# Create your models here.
class OBWellobjectivedata(models.Model):  
    obwellobjective = models.ForeignKey(OBWellobjective, on_delete=models.CASCADE)
    obwellid = models.PositiveIntegerField() 
    date = models.DateField()  
    perf_Depth = models.FloatField(null=True, blank=True)
    res_pressure = models.FloatField(null=True, blank=True)
    well_Types = (
        ("Oilproducer", "Oilproducer"),
        ("Gasproducer", "Gasproducer"),
        ("Waterinjector", "Waterinjector"),
        ("Gasinjector", "Gasinjector"),
        ("Observer", "Observer")
    ) 
    well_type=models.CharField(max_length = 20,choices = well_Types,default = '1')
    
