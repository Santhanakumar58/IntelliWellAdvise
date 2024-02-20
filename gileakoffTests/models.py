from django.db import models
from gicasings.models import GICasingSizeModel


class GILeakoffTest(models.Model):
    gifgid = models.PositiveIntegerField()   
    giwellid = models.PositiveIntegerField() 
    gicasingSize=models.ForeignKey(GICasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    gianalyst=models.CharField(max_length=30)
    girecorded_Date = models.DateField()
    gimudWeight = models.FloatField()
    giopenholeLength = models.FloatField()



