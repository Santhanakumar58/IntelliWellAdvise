from django.db import models
from gpcasings.models import GPCasingSizeModel
import datetime
import os

def filepath(request, gpfilename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/gploganalysis/', gpfilename)

class GPLogAnalysisModel(models.Model):  
    gpfgid = models.PositiveIntegerField()   
    gpwellid = models.PositiveIntegerField() 
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
    gpcasingSize=models.CharField(max_length=50, choices=CasingSizes, default="7")
    gpanalyst=models.CharField(max_length=30)
    gprecorded_date = models.DateField()
    gpinterpretation=models.TextField( )
    gplogImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    gpremarks = models.CharField(max_length=100)
    Filetypes = (
        ("LAS", "LAS"),
        ("CSV", "CSV"),
        ("DLIS", "DLIS"),
    )
    gpfile_type = models.CharField(max_length=50, choices=Filetypes, default="LAS")
    gpfile_Name = models.FileField(null=True, blank=True, upload_to=filepath)


