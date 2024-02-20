from django.db import models
from gpgradientsurveys.models import GPGradientSurvey

# Create your models here.
class GPGradientSurveyData(models.Model):  
    gpgradientsurvey = models.ForeignKey(GPGradientSurvey, on_delete=models.CASCADE )
    gpwellid = models.PositiveIntegerField()    
    gpgauge_Depth = models.FloatField()
    gpgauge_Pressure = models.FloatField()
    gpgauge_Temperature = models.FloatField()
   
       
    def __int__(self):
        return self.gpgradientsurceyid    
 


