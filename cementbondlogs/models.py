from django.db import models
from casings.models import CasingSizeModel
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/cementbondlogs/', filename)

class CementBondLogModel(models.Model):  
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    casingSize=models.ForeignKey(CasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    analyst=models.CharField(max_length=30)
    recorded_date = models.DateField()
    interpretation=models.TextField( )
    cblImage = models.ImageField(upload_to=filepath, null=True, blank=True)
   
