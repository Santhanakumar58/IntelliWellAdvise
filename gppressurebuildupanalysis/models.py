from django.db import models
from blackoilpvt.models import BlackoilPVT
import datetime
import os


def filepath(request, filename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/gpbuildupData/', filename)


class GPPressureBuildupModel(models.Model):  
    gpfgid = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpsurvey_Date = models.DateField()  
    gpgauge_Depth = models.FloatField()
    gplayer_Thickness = models.FloatField()
    gplayer_Porosity =models.FloatField()
    gptotal_Compressibility=models.FloatField()
    gpmu_oil = models.FloatField()
    gpoil_FVF = models.FloatField()
    gpwellbore_Radius = models.FloatField()
    gpoil_Prod_Rate = models.FloatField()
    gpwater_Cut = models.FloatField()
    gpt_since_shutin = models.FloatField()
    gppvt_Well = models.ForeignKey(BlackoilPVT, on_delete=models.CASCADE)
    Builduptests=(
        ('Constant_Rate', 'Constant_Rate'),
        ('Constant_Pressure', 'Constant_Pressure'),
        ('Multi_Rate', 'Multi_Rate')
    )   
    gptest_Type = models.CharField(max_length=50, choices=Builduptests, default='Constant_Rate', null=True, blank=True)
    gpguess_Value=models.PositiveBigIntegerField(default=10)
    gpdataFile = models.FileField(upload_to=filepath, null=True, blank=True)
    
       
    def __date__(self):
        return self.gpsurvey_Date  

class GPPressureBuildupDataUploadModel(models.Model):    
    gpsurvey_Date = models.DateField()  
    gptime = models.TimeField()
    gpelapsedtime = models.FloatField()
    gpgauge_pressure = models.FloatField()

    def __date__(self):
        return self.gpsurvey_Date 

