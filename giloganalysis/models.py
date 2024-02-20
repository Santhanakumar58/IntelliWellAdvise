from django.db import models
from gicasings.models import GICasingSizeModel
import datetime
import os

def filepath(request, gifilename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/giloganalysis/', gifilename)

class GILogAnalysisModel(models.Model):  
    gifgid = models.PositiveIntegerField()   
    giwellid = models.PositiveIntegerField() 
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
    gicasingSize=models.CharField(max_length=50, choices=CasingSizes, default="7")
    gianalyst=models.CharField(max_length=30)
    girecorded_date = models.DateField()
    giinterpretation=models.TextField( )
    gilogImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    giremarks = models.CharField(max_length=100)
    Filetypes = (
        ("LAS", "LAS"),
        ("CSV", "CSV"),
        ("DLIS", "DLIS"),
    )
    gifile_type = models.CharField(max_length=50, choices=Filetypes, default="LAS")
    gifile_Name = models.FileField(null=True, blank=True, upload_to=filepath)



