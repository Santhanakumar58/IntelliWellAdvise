from django.db import models
from gigradientsurveys.models import GIGradientSurvey

# Create your models here.
class GIGradientSurveyData(models.Model):  
    gigradientsurvey = models.ForeignKey(GIGradientSurvey, on_delete=models.CASCADE )
    giwellid = models.PositiveIntegerField()    
    gigauge_Depth = models.FloatField()
    gigauge_Pressure = models.FloatField()
    gigauge_Temperature = models.FloatField()
   
       
    def __int__(self):
        return self.gigradientsurceyid    
 


