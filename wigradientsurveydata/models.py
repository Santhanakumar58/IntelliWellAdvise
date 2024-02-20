from django.db import models
from wigradientsurveys.models import WIGradientSurvey

# Create your models here.
class WIGradientSurveyData(models.Model):  
    wigradientsurvey = models.ForeignKey(WIGradientSurvey, on_delete=models.CASCADE )
    wiwellid = models.PositiveIntegerField()    
    wigauge_Depth = models.FloatField()
    wigauge_Pressure = models.FloatField()
    wigauge_Temperature = models.FloatField()
   
       
    def __int__(self):
        return self.wigradientsurceyid    
 

