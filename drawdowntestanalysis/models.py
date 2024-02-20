from django.db import models
from blackoilpvt.models import BlackoilPVT
from selectedOilProducer.models import SelectedOilProducer
from selectedfgi.models import Selectedfgi
import datetime
import os
from IntelligentOilWell.custom_context_processors import PVTwells


def filepath(request, filename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/opdrawdown/', filename)

class Drawdowntest(models.Model):      
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    survey_Date = models.DateField()  
    gauge_Depth = models.FloatField()
    layer_Porosity =models.FloatField()
    layer_Thickness = models.FloatField()
    wellbore_Radius = models.FloatField()
    total_Compressibility=models.FloatField()
    initial_Res_Pres =models.FloatField()
    oil_Viscosity = models.FloatField()
    oil_FVF =models.FloatField()     
    pvt_Well = models.CharField(max_length=50, blank=True, null=True)
    file_Name = models.FileField(null=True, blank=True, upload_to=filepath)
    Drawdowntests=(
        ('Constant_Rate', 'Constant_Rate'),
        ('Constant_Pressure', 'Constant_Pressure'),
        ('Multi_Rate', 'Multi_Rate')
    )   
    test_Type = models.CharField(max_length=50, choices=Drawdowntests, default='Constant_Rate', null=True, blank=True)
    liquid_Rate = models.FloatField()
    guess_Value=models.PositiveBigIntegerField(default=10)
    fbhp = models.FloatField(default =1000, null=True, blank=True)
       
    def __int__(self):
        return self.fgid   

