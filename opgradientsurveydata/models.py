from django.db import models
from opgradientsurveys.models import GradientSurvey

# Create your models here.
class GradientSurveyData(models.Model):  
    gradientsurvey = models.ForeignKey(GradientSurvey, on_delete=models.CASCADE )
    wellid = models.PositiveIntegerField()    
    gauge_Depth = models.FloatField()
    gauge_Pressure = models.FloatField()
    gauge_Temperature = models.FloatField()
   
       
    def __int__(self):
        return self.gradientsurceyid    
 
