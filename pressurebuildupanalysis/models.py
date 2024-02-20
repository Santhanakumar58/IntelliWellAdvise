from django.db import models
from blackoilpvt.models import BlackoilPVT
import datetime
import os


def filepath(request, filename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/buildupData/', filename)


class PressureBuildupModel(models.Model):  
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    survey_Date = models.DateField()  
    gauge_Depth = models.FloatField()
    layer_Thickness = models.FloatField()
    layer_Porosity =models.FloatField()
    total_Compressibility=models.FloatField()
    mu_oil = models.FloatField()
    oil_FVF = models.FloatField()
    wellbore_Radius = models.FloatField()
    oil_Prod_Rate = models.FloatField()
    water_Cut = models.FloatField()
    t_since_shutin = models.FloatField()
    pvt_Well = models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE)
    Builduptests=(
        ('Constant_Rate', 'Constant_Rate'),
        ('Constant_Pressure', 'Constant_Pressure'),
        ('Multi_Rate', 'Multi_Rate')
    )   
    test_Type = models.CharField(max_length=50, choices=Builduptests, default='Constant_Rate', null=True, blank=True)
    guess_Value=models.PositiveBigIntegerField(default=10)
    dataFile = models.FileField(upload_to=filepath, null=True, blank=True)
    
       
    def __date__(self):
        return self.survey_Date  

class PressureBuildupDataUploadModel(models.Model):    
    survey_Date = models.DateField()  
    time = models.TimeField()
    elapsedtime = models.FloatField()
    gauge_pressure = models.FloatField()

    def __date__(self):
        return self.survey_Date 

