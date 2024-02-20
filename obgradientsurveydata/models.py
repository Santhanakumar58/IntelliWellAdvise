from django.db import models
from obgradientsurveys.models import OBGradientSurvey

# Create your models here.
class OBGradientSurveyData(models.Model):  
    obgradientsurvey = models.ForeignKey(OBGradientSurvey, on_delete=models.CASCADE )
    obwellid = models.PositiveIntegerField()    
    obgauge_Depth = models.FloatField()
    obgauge_Pressure = models.FloatField()
    obgauge_Temperature = models.FloatField()
   
       
    def __int__(self):
        return self.obgradientsurceyid    
 

