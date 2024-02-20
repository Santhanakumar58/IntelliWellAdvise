from django.db import models
from wicasings.models import WICasingSizeModel
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/wicementbondlogs/', filename)

class WICementBondLogModel(models.Model):  
    wifgid = models.PositiveIntegerField()   
    wiwellid = models.PositiveIntegerField() 
    wicasingSize=models.ForeignKey(WICasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    wianalyst=models.CharField(max_length=30)
    wirecorded_date = models.DateField()
    wiinterpretation=models.TextField( )
    wicblImage = models.ImageField(upload_to=filepath, null=True, blank=True)
   
