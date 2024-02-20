from django.db import models
from giwellobjectives.models import GIWellobjective

# Create your models here.
class GIWellobjectivedata(models.Model):  
    giwellobjective = models.ForeignKey(GIWellobjective, on_delete=models.CASCADE)
    giwellid = models.PositiveIntegerField() 
    date = models.DateField()  
    gas_inj_rate_mmscfd = models.FloatField(null=True, blank=True)
    gas_inj_pressure = models.FloatField(null=True, blank=True)
    co2_percentage = models.FloatField(null=True, blank=True)
    h2s_percentage = models.FloatField(null=True, blank=True)
