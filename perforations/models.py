from django.db import models
from IntelligentOilWell.custom_context_processors import selectedwell

class PerforationModel(models.Model):   
    fgid = models.PositiveIntegerField()
    wellid =models.PositiveIntegerField()
    perf_Date= models.DateField()
    perf_Top = models.FloatField()
    perf_Bottom = models.FloatField()
    Conditions=(
        ('Over_Balanced', 'Over_Balanced'),
        ('Under_balanced', 'Under_balanced'), 
    )
    perf_Condition= models.CharField(max_length = 50,choices = Conditions,default = 'Over_Balanced')
    Conveyance=(
        ('Through_Casing', 'Through_Casing'),
        ('Through_Tubing', 'Through_Tubing'),
        ('TCP', 'TCP'),
      
    )
    conveyance_Method = models.CharField(max_length = 50,choices = Conveyance,default = 'Retrievable_Hallow')
    GunTypes=(
        ('Retrievable_Hallow', 'Retrievable_Hallow'),
        ('Expendable', 'Expendable'),
        ('Semi_Expendable', 'Semi_Expendable')
    )
    perf_Gun_Type = models.CharField(max_length = 50,choices = GunTypes,default = 'Retrievable_Hallow')
    GunSizes=(
        ('2_in', '2_in'),
        ('2_3/4_In', '2_3/4_in'),
        ('3_1/8_in', '3_1/8_in'),
        ('3_3/8_in', '3_3/8_in')
    )
    perf_Gun_Size = models.CharField(max_length=50, choices= GunSizes, default = '2_in' ) 
    perf_Gun_Density = models.CharField(max_length=50) 
    perf_Charges = models.CharField(max_length=50) 
    remarks = models.CharField(max_length=100)


    def __int__(self):
        return self.wellid


   
