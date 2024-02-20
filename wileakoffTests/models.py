from django.db import models
from wicasings.models import WICasingSizeModel


class WILeakoffTest(models.Model):
    wifgid = models.PositiveIntegerField()   
    wiwellid = models.PositiveIntegerField() 
    wicasingSize=models.ForeignKey(WICasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    wianalyst=models.CharField(max_length=30)
    wirecorded_Date = models.DateField()
    wimudWeight = models.FloatField()
    wiopenholeLength = models.FloatField()



