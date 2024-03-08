from django.db import models

class BridgePlug(models.Model):    
    wellid =models.PositiveBigIntegerField()
    fgid = models.PositiveBigIntegerField()
    plug_Date= models.DateField()
    Plug_Types = (
        ("Bridge_Plug", "Bridge_Plug"),
        ("Cement_Retainer", "Cement_Retainer"),
        )
    plug_type = models.CharField(max_length = 20,choices = Plug_Types,default = '1', blank=True, null=True)
    plug_Depth = models.FloatField()
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
    casing_Size= models.CharField(max_length = 20,choices = Casing_Size,default = '1', blank=True, null=True)
    plug_OD = models.FloatField()
    setting_range_ppf = models.CharField(max_length=25, blank=True, null=True)
    Setting_Mechanisms = (
        ("Mechanical", "Mechanical"),
        ("Wireline", "Wireline"),
        )
    setting_mechanism = models.CharField(max_length = 20,choices = Setting_Mechanisms,default = '1', blank=True, null=True)
    plug_Make = models.CharField(max_length=50, blank=True, null=True)   
    plug_Model =  models.CharField(max_length=50, blank=True, null=True)    
    Pressure_rating =   models.FloatField()  
    Temperature_rating =   models.FloatField()  
    plug_setting_Problems = models.TextField(max_length=2500, blank=True, null=True)
