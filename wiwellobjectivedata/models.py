from django.db import models
from wiwellobjectives.models import WIWellobjective

# Create your models here.
class WIWellobjectivedata(models.Model):  
    wiwellobjective = models.ForeignKey(WIWellobjective, on_delete=models.CASCADE)
    wiwellid = models.PositiveIntegerField() 
    date = models.DateField()  
    wat_inj_rate = models.FloatField(null=True, blank=True)
    wat_inj_pressure = models.FloatField(null=True, blank=True)
    tds_ppm = models.FloatField(null=True, blank=True)
    pH = models.FloatField(null=True, blank=True)
    wat_sources = (
        ("Treated_Produced_Water", "Treated_Produced_Water"),
        ("Treated_Sea_Water", "Treated_Sea_Water"),
        ("Treated_River_Water", "Treated_River_Water"),
        ("Treated_Ground_Water", "Treated_Ground_Water")
    ) 
    wat_source=models.CharField(max_length = 50,choices = wat_sources,default = '1')
    
