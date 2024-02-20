from django.db import models
from gpcasings.models import GPCasingSizeModel
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/gpcementbondlogs/', filename)

class GPCementBondLogModel(models.Model):  
    gpfgid = models.PositiveIntegerField()   
    gpwellid = models.PositiveIntegerField() 
    gpcasingSize=models.ForeignKey(GPCasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    gpanalyst=models.CharField(max_length=30)
    gprecorded_date = models.DateField()
    gpinterpretation=models.TextField( )
    gpcblImage = models.ImageField(upload_to=filepath, null=True, blank=True)
   
