from django.db import models
import os

def filepath(request, filename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/recordedlogs/', filename)

class RecordedLogsModel(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    survey_Date = models.DateField()  
    HoleSizes=(
    ( '26_inch', '26_inch'),
    ( '20_inch', '20_inch'),
    ( '16_inch', '16_inch'),
    ( '12_1/4_inch', '12_1/4_inch'),
    ( '8_1/2_inch', '8_1/2_inch'),
    ( '6_1/8_inch', '6_1/8_inch'),
    ( '4_1/2_inch', '4_1/2_inch'),
    )
    hole_size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    logtypes = (
        ("LWD", "LWD"),
        ("MWD", "MWD"),
        ("Open_Hole", "Open_Hole"),
        ("Cased_Hole", "Cased_Hole"),
    )
    log_Type = models.CharField(max_length=50, choices=logtypes, default='Open_Hole' )  
    tool_string = models.CharField(max_length=100)
    from_MD = models.FloatField()   
    to_MD = models.FloatField()   
    service_Provider = models.CharField(max_length=50, null=True, blank=True) 
    unit_name = models.CharField(max_length=50, null=True, blank=True)
    analyst=models.CharField(max_length=30, null=True, blank=True)     
    interpretation=models.TextField()
    logImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    remarks = models.CharField(max_length=100)
    Filetypes = (
        ("LAS", "LAS"),
        ("CSV", "CSV"),
        ("DLIS", "DLIS"),
    )
    file_type = models.CharField(max_length=50, choices=Filetypes, default="LAS")
    file_Name = models.FileField(null=True, blank=True, upload_to=filepath)
         
    def __int__(self):
        return self.wellid

