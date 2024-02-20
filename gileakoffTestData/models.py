from django.db import models
from gileakoffTests.models import GILeakoffTest
from gicasings.models import GICasingSizeModel

# Create your models here.

class GILeakoffTestData(models.Model):
    gileakoffTest = models.ForeignKey(GILeakoffTest, on_delete=models.CASCADE)
    gicasingSize = models.ForeignKey(GICasingSizeModel, on_delete=models.CASCADE)
    gitime = models.FloatField()
    givolume = models.FloatField()
    gipressure = models.FloatField()
   
   
