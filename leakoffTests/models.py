from django.db import models
from casings.models import CasingSizeModel


class LeakoffTest(models.Model):
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    casingModelid = models.PositiveBigIntegerField()
    casingSize=models.ForeignKey(CasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    analyst=models.CharField(max_length=30)
    recorded_Date = models.DateField()
    mudWeight = models.FloatField()
    openholeLength = models.FloatField()

