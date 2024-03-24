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
    return os.path.join('uploads/opdrawdown/multirate', filename)

class MultiRateDrawdowntest(models.Model):      
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    survey_Date = models.DateField()  
    gauge_Depth_ft = models.FloatField()
    layer_Porosity_fraction =models.FloatField()
    layer_Thickness_ft = models.FloatField()
    wellbore_Radius_ft = models.FloatField()
    total_Compressibility=models.FloatField()
    initial_Res_Pres_psi =models.FloatField()
    oil_Viscosity_cP = models.FloatField()
    oil_FVF_Bo =models.FloatField()    
    file_Name_csv = models.FileField(null=True, blank=True, upload_to=filepath)
    time1 = models.FloatField(null=True, blank=True)
    rate1=models.FloatField(null=True, blank=True)
    time2 = models.FloatField(null=True, blank=True)
    rate2=models.FloatField(null=True, blank=True)
    time3 = models.FloatField(null=True, blank=True)
    rate3=models.FloatField(null=True, blank=True)
   
       
    def __int__(self):
        return self.fgid   

