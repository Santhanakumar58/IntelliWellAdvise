from django.db import models
from IntelligentOilWell.custom_context_processors import selectedwell

class OBPerforationModel(models.Model):   
    obfgid = models.PositiveIntegerField()
    obwellid =models.PositiveIntegerField()
    obperf_Date= models.DateField()
    obperf_Top = models.FloatField()
    obperf_Bottom = models.FloatField()
    Conditions=(
        ('Over_Balanced', 'Over_Balanced'),
        ('Under_balanced', 'Under_balanced'), 
    )
    obperf_Condition= models.CharField(max_length = 50,choices = Conditions,default = 'Over_Balanced')
    Conveyance=(
        ('Through_Casing', 'Through_Casing'),
        ('Through_Tubing', 'Through_Tubing'),
        ('TCP', 'TCP'),
      
    )
    obconveyance_Method = models.CharField(max_length = 50,choices = Conveyance,default = 'Retrievable_Hallow')
    GunTypes=(
        ('Retrievable_Hallow', 'Retrievable_Hallow'),
        ('Expendable', 'Expendable'),
        ('Semi_Expendable', 'Semi_Expendable')
    )
    obperf_Gun_Type = models.CharField(max_length = 50,choices = GunTypes,default = 'Retrievable_Hallow')
    GunSizes=(
        ('2_in', '2_in'),
        ('2_3/4_In', '2_3/4_in'),
        ('3_1/8_in', '3_1/8_in'),
        ('3_3/8_in', '3_3/8_in')
    )
    obperf_Gun_Size = models.CharField(max_length=50, choices= GunSizes, default = '2_in' ) 
    obperf_Gun_Density = models.CharField(max_length=50) 
    obperf_Charges = models.CharField(max_length=50) 
    obremarks = models.CharField(max_length=100)


    def __int__(self):
        return self.gpwellid


   

