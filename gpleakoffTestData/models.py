from django.db import models
from gpleakoffTests.models import GPLeakoffTest
from gpcasings.models import GPCasingSizeModel

# Create your models here.

class GPLeakoffTestData(models.Model):
    gpleakoffTest = models.ForeignKey(GPLeakoffTest, on_delete=models.CASCADE)
    gpcasingSize = models.ForeignKey(GPCasingSizeModel, on_delete=models.CASCADE)
    gptime = models.FloatField()
    gpvolume = models.FloatField()
    gppressure = models.FloatField()
   
   