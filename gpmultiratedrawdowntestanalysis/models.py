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
    return os.path.join('uploads/gpdrawdown/multirate', filename)

class GPMultiRateDrawdowntest(models.Model):      
    gpfgid = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpsurvey_Date = models.DateField()  
    gpgauge_Depth = models.FloatField()
    gplayer_Porosity =models.FloatField()
    gplayer_Thickness = models.FloatField()
    gpwellbore_Radius = models.FloatField()
    gptotal_Compressibility=models.FloatField()
    gpinitial_Res_Pres =models.FloatField()
    gpoil_Viscosity = models.FloatField()
    gpoil_FVF =models.FloatField()    
    gpfile_Name = models.FileField(null=True, blank=True, upload_to=filepath)
    gptime1 = models.FloatField(null=True, blank=True)
    gppressure1=models.FloatField(null=True, blank=True)
    gptime2 = models.FloatField(null=True, blank=True)
    gppressure2=models.FloatField(null=True, blank=True)
    gptime3 = models.FloatField(null=True, blank=True)
    gppressure3=models.FloatField(null=True, blank=True)
   
       
    def __int__(self):
        return self.gpfgid   


