from django.db import models

# Create your models here.

class GPGradientSurvey(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()
    gpsurvey_Date = models.DateField() 
    SurveyTypes =(
        ('Flogpng', 'Flogpng'),
        ('Static', 'Static')
    )
    gpsurvey_Type=models.CharField(max_length = 50,choices = SurveyTypes,default = 'Static') 
    gpshutin_Period = models.FloatField()
    gptubinghead_Pressure = models.FloatField()
    gptubinghead_Temperature = models.FloatField()
    gpliquid_Rate = models.FloatField()
    gpwater_Cut = models.FloatField()
    gpgas_Oil_Ratio = models.FloatField()

    def __int__(self):
       return self.gpfgId 
