from django.db import models
from obcasings.models import OBCasingSizeModel
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/obcementbondlogs/', filename)

class OBCementBondLogModel(models.Model):  
    obfgid = models.PositiveIntegerField()   
    obwellid = models.PositiveIntegerField() 
    obcasingSize=models.ForeignKey(OBCasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True)
    obanalyst=models.CharField(max_length=30)
    obrecorded_date = models.DateField()
    obinterpretation=models.TextField( )
    obcblImage = models.ImageField(upload_to=filepath, null=True, blank=True)
   

