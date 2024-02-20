from django.db import models
import os

def filepath(request, gifilename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/wirecordedlogs/', gifilename)

class GIRecordedLogsModel(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField()  
    gisurvey_Date = models.DateField()  
    HoleSizes=(
    ( '26_inch', '26_inch'),
    ( '20_inch', '20_inch'),
    ( '16_inch', '16_inch'),
    ( '12_1/4_inch', '12_1/4_inch'),
    ( '8_1/2_inch', '8_1/2_inch'),
    ( '6_1/8_inch', '6_1/8_inch'),
    ( '4_1/2_inch', '4_1/2_inch'),
    )
    gihole_size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    logtypes = (
        ("LWD", "LWD"),
        ("MWD", "MWD"),
        ("Open_Hole", "Open_Hole"),
        ("Cased_Hole", "Cased_Hole"),
    )
    gilog_Type = models.CharField(max_length=50, choices=logtypes, default='Open_Hole' )  
    gitool_string = models.CharField(max_length=100)
    gifrom_MD = models.FloatField()   
    gito_MD = models.FloatField()   
    giservice_Provider = models.CharField(max_length=50, null=True, blank=True) 
    giunit_name = models.CharField(max_length=50, null=True, blank=True)
    gianalyst=models.CharField(max_length=30, null=True, blank=True)     
    giinterpretation=models.TextField()
    gilogImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    giremarks = models.CharField(max_length=100)
    Filetypes = (
        ("LAS", "LAS"),
        ("CSV", "CSV"),
        ("DLIS", "DLIS"),
    )
    gifile_type = models.CharField(max_length=50, choices=Filetypes, default="LAS")
    gifile_Name = models.FileField(null=True, blank=True, upload_to=filepath)
         
    def __int__(self):
        return self.giwellid





