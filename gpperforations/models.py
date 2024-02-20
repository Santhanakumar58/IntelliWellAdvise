from django.db import models
from IntelligentOilWell.custom_context_processors import selectedwell

class GPPerforationModel(models.Model):   
    gpfgid = models.PositiveIntegerField()
    gpwellid =models.PositiveIntegerField()
    gpperf_Date= models.DateField()
    gpperf_Top = models.FloatField()
    gpperf_Bottom = models.FloatField()
    Conditions=(
        ('Over_Balanced', 'Over_Balanced'),
        ('Under_balanced', 'Under_balanced'), 
    )
    gpperf_Condition= models.CharField(max_length = 50,choices = Conditions,default = 'Over_Balanced')
    Conveyance=(
        ('Through_Casing', 'Through_Casing'),
        ('Through_Tubing', 'Through_Tubing'),
        ('TCP', 'TCP'),
      
    )
    gpconveyance_Method = models.CharField(max_length = 50,choices = Conveyance,default = 'Retrievable_Hallow')
    GunTypes=(
        ('Retrievable_Hallow', 'Retrievable_Hallow'),
        ('Expendable', 'Expendable'),
        ('Semi_Expendable', 'Semi_Expendable')
    )
    gpperf_Gun_Type = models.CharField(max_length = 50,choices = GunTypes,default = 'Retrievable_Hallow')
    GunSizes=(
        ('2_in', '2_in'),
        ('2_3/4_In', '2_3/4_in'),
        ('3_1/8_in', '3_1/8_in'),
        ('3_3/8_in', '3_3/8_in')
    )
    gpperf_Gun_Size = models.CharField(max_length=50, choices= GunSizes, default = '2_in' ) 
    gpperf_Gun_Density = models.CharField(max_length=50) 
    gpperf_Charges = models.CharField(max_length=50) 
    gpremarks = models.CharField(max_length=100)


    def __int__(self):
        return self.gpwellid


   
