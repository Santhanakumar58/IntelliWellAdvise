from django.db import models

from django.db import models

class WIBridgePlug(models.Model):    
    wiwellid =models.PositiveBigIntegerField()
    wifgid = models.PositiveBigIntegerField()
    wiplug_Date= models.DateField()
    Plug_Types = (
        ("Bridge_Plug", "Bridge_Plug"),
        ("Cement_Retainer", "Cement_Retainer"),
        )
    wiplug_type = models.CharField(max_length = 20,choices = Plug_Types,default = '1', blank=True, null=True)
    wiplug_Depth = models.FloatField()
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
    wicasing_Size= models.CharField(max_length = 20,choices = Casing_Size,default = '1', blank=True, null=True)
    wiplug_OD = models.FloatField()
    wisetting_range_ppf = models.TextField(max_length=25, blank=True, null=True)
    Setting_Mechanisms = (
        ("Mechanical", "Mechanical"),
        ("Wireline", "Wireline"),
        )
    wisetting_mechanism = models.CharField(max_length = 20,choices = Setting_Mechanisms,default = '1', blank=True, null=True)
    wiplug_Make = models.TextField(max_length=50, blank=True, null=True)   
    wiplug_Model =  models.TextField(max_length=50, blank=True, null=True)    
    wiPressure_rating =   models.FloatField()  
    wiTemperature_rating =   models.FloatField()  
    wiplug_setting_Problems = models.TextField(max_length=2500, blank=True, null=True)

