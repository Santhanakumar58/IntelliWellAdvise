from django.db import models

# Create your models here.

class GradientSurvey(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()
    survey_Date = models.DateField() 
    SurveyTypes =(
        ('Flowing', 'Flowing'),
        ('Static', 'Static')
    )
    survey_Type=models.CharField(max_length = 50,choices = SurveyTypes,default = 'Static') 
    shutin_Period = models.FloatField()
    tubinghead_Pressure = models.FloatField()
    tubinghead_Temperature = models.FloatField()
    liquid_Rate = models.FloatField()
    water_Cut = models.FloatField()
    gas_Oil_Ratio = models.FloatField()

    def __int__(self):
       return self.fgId 
  