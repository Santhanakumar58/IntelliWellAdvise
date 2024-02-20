from django.db import models
from leakoffTests.models import LeakoffTest
from casings.models import CasingSizeModel

# Create your models here.

class LeakoffTestData(models.Model):
    leakoffTest = models.ForeignKey(LeakoffTest, on_delete=models.CASCADE)
    casingSize = models.ForeignKey(CasingSizeModel, on_delete=models.CASCADE)
    time = models.FloatField()
    volume = models.FloatField()
    pressure = models.FloatField()
   
   