from django.db import models

# Create your models here.

class WIGradientSurvey(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField()
    wisurvey_Date = models.DateField() 
    SurveyTypes =(
        ('Flowing', 'Flowing'),
        ('Static', 'Static')
    )
    wisurvey_Type=models.CharField(max_length = 50,choices = SurveyTypes,default = 'Static') 
    wishutin_Period = models.FloatField()
    witubinghead_Pressure = models.FloatField()
    witubinghead_Temperature = models.FloatField()
    wiliquid_Rate = models.FloatField()
    wiwater_Cut = models.FloatField()
    wigas_Oil_Ratio = models.FloatField()

    def __int__(self):
       return self.wifgId 
  
