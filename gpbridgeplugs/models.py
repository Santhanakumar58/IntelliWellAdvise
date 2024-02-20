from django.db import models

class GPBridgePlug(models.Model):    
    gpwellid =models.PositiveBigIntegerField()
    gpfgid = models.PositiveBigIntegerField()
    gpplug_Date= models.DateField()
    Plug_Types = (
        ("Bridge_Plug", "Bridge_Plug"),
        ("Cement_Retainer", "Cement_Retainer"),
        )
    gpplug_type = models.CharField(max_length = 20,choices = Plug_Types,default = '1', blank=True, null=True)
    gpplug_Depth = models.FloatField()
    Casing_Size = (
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
    gpcasing_Size= models.CharField(max_length = 20,choices = Casing_Size,default = '1', blank=True, null=True)
    gpplug_OD = models.FloatField()
    gpsetting_range_ppf = models.TextField(max_length=25, blank=True, null=True)
    Setting_Mechanisms = (
        ("Mechanical", "Mechanical"),
        ("Wireline", "Wireline"),
        )
    gpsetting_mechanism = models.CharField(max_length = 20,choices = Setting_Mechanisms,default = '1', blank=True, null=True)
    gpplug_Make = models.TextField(max_length=50, blank=True, null=True)   
    gpplug_Model =  models.TextField(max_length=50, blank=True, null=True)    
    gpPressure_rating =   models.FloatField()  
    gpTemperature_rating =   models.FloatField()  
    gpplug_setting_Problems = models.TextField(max_length=2500, blank=True, null=True)
