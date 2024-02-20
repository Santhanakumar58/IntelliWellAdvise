from django.db import models
from gpcasings.models import GPCasingSizeModel


class GPLeakoffTest(models.Model):
    gpfgid = models.PositiveIntegerField()   
    gpwellid = models.PositiveIntegerField() 
    gpcasingSize=models.ForeignKey(GPCasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    gpanalyst=models.CharField(max_length=30)
    gprecorded_Date = models.DateField()
    gpmudWeight = models.FloatField()
    gpopenholeLength = models.FloatField()


