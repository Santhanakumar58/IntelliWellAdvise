from django.db import models
import os

def filepath(request, gpfilename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/wirecordedlogs/', gpfilename)

class GPRecordedLogsModel(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()  
    gpsurvey_Date = models.DateField()  
    HoleSizes=(
    ( '26_inch', '26_inch'),
    ( '20_inch', '20_inch'),
    ( '16_inch', '16_inch'),
    ( '12_1/4_inch', '12_1/4_inch'),
    ( '8_1/2_inch', '8_1/2_inch'),
    ( '6_1/8_inch', '6_1/8_inch'),
    ( '4_1/2_inch', '4_1/2_inch'),
    )
    gphole_size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    logtypes = (
        ("LWD", "LWD"),
        ("MWD", "MWD"),
        ("Open_Hole", "Open_Hole"),
        ("Cased_Hole", "Cased_Hole"),
    )
    gplog_Type = models.CharField(max_length=50, choices=logtypes, default='Open_Hole' )  
    gptool_string = models.CharField(max_length=100)
    gpfrom_MD = models.FloatField()   
    gpto_MD = models.FloatField()   
    gpservice_Provider = models.CharField(max_length=50, null=True, blank=True) 
    gpunit_name = models.CharField(max_length=50, null=True, blank=True)
    gpanalyst=models.CharField(max_length=30, null=True, blank=True)     
    gpinterpretation=models.TextField()
    gplogImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    gpremarks = models.CharField(max_length=100)
    Filetypes = (
        ("LAS", "LAS"),
        ("CSV", "CSV"),
        ("DLIS", "DLIS"),
    )
    gpfile_type = models.CharField(max_length=50, choices=Filetypes, default="LAS")
    gpfile_Name = models.FileField(null=True, blank=True, upload_to=filepath)
         
    def __int__(self):
        return self.gpwellid




