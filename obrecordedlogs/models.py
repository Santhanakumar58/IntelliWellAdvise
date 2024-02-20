from django.db import models
import os

def filepath(request, obfilename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/wirecordedlogs/', obfilename)

class OBRecordedLogsModel(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField()  
    obsurvey_Date = models.DateField()  
    HoleSizes=(
    ( '26_inch', '26_inch'),
    ( '20_inch', '20_inch'),
    ( '16_inch', '16_inch'),
    ( '12_1/4_inch', '12_1/4_inch'),
    ( '8_1/2_inch', '8_1/2_inch'),
    ( '6_1/8_inch', '6_1/8_inch'),
    ( '4_1/2_inch', '4_1/2_inch'),
    )
    obhole_size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    logtypes = (
        ("LWD", "LWD"),
        ("MWD", "MWD"),
        ("Open_Hole", "Open_Hole"),
        ("Cased_Hole", "Cased_Hole"),
    )
    oblog_Type = models.CharField(max_length=50, choices=logtypes, default='Open_Hole' )  
    obtool_string = models.CharField(max_length=100)
    obfrom_MD = models.FloatField()   
    obto_MD = models.FloatField()   
    observice_Provider = models.CharField(max_length=50, null=True, blank=True) 
    obunit_name = models.CharField(max_length=50, null=True, blank=True)
    obanalyst=models.CharField(max_length=30, null=True, blank=True)     
    obinterpretation=models.TextField()
    oblogImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    obremarks = models.CharField(max_length=100)
    Filetypes = (
        ("LAS", "LAS"),
        ("CSV", "CSV"),
        ("DLIS", "DLIS"),
    )
    obfile_type = models.CharField(max_length=50, choices=Filetypes, default="LAS")
    obfile_Name = models.FileField(null=True, blank=True, upload_to=filepath)
         
    def __int__(self):
        return self.obwellid



