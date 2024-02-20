from django.db import models
from blackoilpvt.models import BlackoilPVT
from selectedGasProducer.models import SelectedGasProducer
from selectedfgi.models import Selectedfgi
import datetime
import os
from IntelligentOilWell.custom_context_processors import PVTwells


def filepath(request, filename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/gpdrawdown/', filename)

class GPDrawdowntest(models.Model):      
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
    gppvt_Well = models.CharField(max_length=50, blank=True, null=True)
    gpfile_Name = models.FileField(null=True, blank=True, upload_to=filepath)
    Drawdowntests=(
        ('Constant_Rate', 'Constant_Rate'),
        ('Constant_Pressure', 'Constant_Pressure'),
        ('Multi_Rate', 'Multi_Rate')
    )   
    gptest_Type = models.CharField(max_length=50, choices=Drawdowntests, default='Constant_Rate', null=True, blank=True)
    gpliquid_Rate = models.FloatField()
    gpguess_Value=models.PositiveBigIntegerField(default=10)
    gpfbhp = models.FloatField(default =1000, null=True, blank=True)
       
    def __int__(self):
        return self.gpfgid   


