from django.db import models
from obcasings.models import OBCasingSizeModel


class OBLeakoffTest(models.Model):
    obfgid = models.PositiveIntegerField()   
    obwellid = models.PositiveIntegerField() 
    obcasingSize=models.ForeignKey(OBCasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    obanalyst=models.CharField(max_length=30)
    obrecorded_Date = models.DateField()
    obmudWeight = models.FloatField()
    obopenholeLength = models.FloatField()



