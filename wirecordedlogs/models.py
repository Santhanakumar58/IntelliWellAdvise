from django.db import models
import os

def filepath(request, wifilename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/wirecordedlogs/', wifilename)

class WIRecordedLogsModel(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField()  
    wisurvey_Date = models.DateField()  
    HoleSizes=(
    ( '26_inch', '26_inch'),
    ( '20_inch', '20_inch'),
    ( '16_inch', '16_inch'),
    ( '12_1/4_inch', '12_1/4_inch'),
    ( '8_1/2_inch', '8_1/2_inch'),
    ( '6_1/8_inch', '6_1/8_inch'),
    ( '4_1/2_inch', '4_1/2_inch'),
    )
    wihole_size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    logtypes = (
        ("LWD", "LWD"),
        ("MWD", "MWD"),
        ("Open_Hole", "Open_Hole"),
        ("Cased_Hole", "Cased_Hole"),
    )
    wilog_Type = models.CharField(max_length=50, choices=logtypes, default='Open_Hole' )  
    witool_string = models.CharField(max_length=100)
    wifrom_MD = models.FloatField()   
    wito_MD = models.FloatField()   
    wiservice_Provider = models.CharField(max_length=50, null=True, blank=True) 
    wiunit_name = models.CharField(max_length=50, null=True, blank=True)
    wianalyst=models.CharField(max_length=30, null=True, blank=True)     
    wiinterpretation=models.TextField()
    wilogImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    wiremarks = models.CharField(max_length=100)
    Filetypes = (
        ("LAS", "LAS"),
        ("CSV", "CSV"),
        ("DLIS", "DLIS"),
    )
    wifile_type = models.CharField(max_length=50, choices=Filetypes, default="LAS")
    wifile_Name = models.FileField(null=True, blank=True, upload_to=filepath)
         
    def __int__(self):
        return self.wiwellid


