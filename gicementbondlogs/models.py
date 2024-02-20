from django.db import models
from gicasings.models import GICasingSizeModel
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/gicementbondlogs/', filename)

class GICementBondLogModel(models.Model):  
    gifgid = models.PositiveIntegerField()   
    giwellid = models.PositiveIntegerField() 
    gicasingSize=models.ForeignKey(GICasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    gianalyst=models.CharField(max_length=30)
    girecorded_date = models.DateField()
    giinterpretation=models.TextField( )
    gicblImage = models.ImageField(upload_to=filepath, null=True, blank=True)
   

