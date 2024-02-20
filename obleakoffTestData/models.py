from django.db import models
from obleakoffTests.models import OBLeakoffTest
from obcasings.models import OBCasingSizeModel

# Create your models here.

class OBLeakoffTestData(models.Model):
    obleakoffTest = models.ForeignKey(OBLeakoffTest, on_delete=models.CASCADE)
    obcasingSize = models.ForeignKey(OBCasingSizeModel, on_delete=models.CASCADE)
    obtime = models.FloatField()
    obvolume = models.FloatField()
    obpressure = models.FloatField()
   
   
