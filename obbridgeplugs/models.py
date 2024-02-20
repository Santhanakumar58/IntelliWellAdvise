from django.db import models

class OBBridgePlug(models.Model):    
    obwellid =models.PositiveBigIntegerField()
    obfgid = models.PositiveBigIntegerField()
    obplug_Date= models.DateField()
    Plug_Types = (
        ("Bridge_Plug", "Bridge_Plug"),
        ("Cement_Retainer", "Cement_Retainer"),
        )
    obplug_type = models.CharField(max_length = 20,choices = Plug_Types,default = '1', blank=True, null=True)
    obplug_Depth = models.FloatField()
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
    obcasing_Size= models.CharField(max_length = 20,choices = Casing_Size,default = '1', blank=True, null=True)
    obplug_OD = models.FloatField()
    obsetting_range_ppf = models.TextField(max_length=25, blank=True, null=True)
    Setting_Mechanisms = (
        ("Mechanical", "Mechanical"),
        ("Wireline", "Wireline"),
        )
    obsetting_mechanism = models.CharField(max_length = 20,choices = Setting_Mechanisms,default = '1', blank=True, null=True)
    obplug_Make = models.TextField(max_length=50, blank=True, null=True)   
    obplug_Model =  models.TextField(max_length=50, blank=True, null=True)    
    obPressure_rating =   models.FloatField()  
    obTemperature_rating =   models.FloatField()  
    obplug_setting_Problems = models.TextField(max_length=2500, blank=True, null=True)
