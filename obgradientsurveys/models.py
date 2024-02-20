from django.db import models

# Create your models here.

class OBGradientSurvey(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField()
    obsurvey_Date = models.DateField() 
    SurveyTypes =(
        ('Floobng', 'Floobng'),
        ('Static', 'Static')
    )
    obsurvey_Type=models.CharField(max_length = 50,choices = SurveyTypes,default = 'Static') 
    obshutin_Period = models.FloatField()
    obtubinghead_Pressure = models.FloatField()
    obtubinghead_Temperature = models.FloatField()
    obliquid_Rate = models.FloatField()
    obwater_Cut = models.FloatField()
    obgas_Oil_Ratio = models.FloatField()

    def __int__(self):
       return self.obfgId 
