from django.db import models
from wileakoffTests.models import WILeakoffTest
from wicasings.models import WICasingSizeModel

# Create your models here.

class WILeakoffTestData(models.Model):
    wileakoffTest = models.ForeignKey(WILeakoffTest, on_delete=models.CASCADE)
    wicasingSize = models.ForeignKey(WICasingSizeModel, on_delete=models.CASCADE)
    witime = models.FloatField()
    wivolume = models.FloatField()
    wipressure = models.FloatField()
   
   
