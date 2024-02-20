from django.db import models
from obcasings.models import OBCasingSizeModel
import datetime
import os

def filepath(request, obfilename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/obloganalysis/', obfilename)

class OBLogAnalysisModel(models.Model):  
    obfgid = models.PositiveIntegerField()   
    obwellid = models.PositiveIntegerField() 
    CasingSizes=(
        ("4", "4"),
        ("4 1/2", "4 1/2"),
        ("5", "5"),
        ("5 1/2", "5 1/2"),
        ("6 5/8", "6 5/8"),
        ("7", "7"),
        ("7 5/8", "7 5/8"),
        ("7 3/4", "7 3/4"),
        ("8 5/8", "8 5/8"),
        ("9 5/8", "9 5/8"),
        ("10 3/4", "10 3/3"),
        ("11 3/4", "11 3/3"),
        ("13 3/8", "13 3/8"),
        ("16", "16"),
        ("18 5/8", "18 5/8"),
        ("20", "20"),
    )
    obcasingSize=models.CharField(max_length=50, choices=CasingSizes, default="7")
    obanalyst=models.CharField(max_length=30)
    obrecorded_date = models.DateField()
    obinterpretation=models.TextField( )
    oblogImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    obremarks = models.CharField(max_length=100)
    Filetypes = (
        ("LAS", "LAS"),
        ("CSV", "CSV"),
        ("DLIS", "DLIS"),
    )
    obfile_type = models.CharField(max_length=50, choices=Filetypes, default="LAS")
    obfile_Name = models.FileField(null=True, blank=True, upload_to=filepath)

