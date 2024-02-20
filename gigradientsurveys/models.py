from django.db import models

# Create your models here.

class GIGradientSurvey(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField()
    gisurvey_Date = models.DateField() 
    SurveyTypes =(
        ('Floging', 'Floging'),
        ('Static', 'Static')
    )
    gisurvey_Type=models.CharField(max_length = 50,choices = SurveyTypes,default = 'Static') 
    gishutin_Period = models.FloatField()
    gitubinghead_Pressure = models.FloatField()
    gitubinghead_Temperature = models.FloatField()
    giliquid_Rate = models.FloatField()
    giwater_Cut = models.FloatField()
    gigas_Oil_Ratio = models.FloatField()

    def __int__(self):
       return self.gifgId 