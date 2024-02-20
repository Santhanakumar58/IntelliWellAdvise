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
    return os.path.join('uploads/opdrawdown/constantpressure', filename)

class ConstantPressureDrawdowntest(models.Model):      
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
    pwf = models.FloatField()
    file_Name = models.FileField(null=True, blank=True, upload_to=filepath) 
       
    def __int__(self):
        return self.fgid   

