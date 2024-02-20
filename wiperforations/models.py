from django.db import models
from IntelligentOilWell.custom_context_processors import selectedwiwell

class WIPerforationModel(models.Model):   
    wifgid = models.PositiveIntegerField()
    wiwellid =models.PositiveIntegerField()
    wiperf_Date= models.DateField()
    wiperf_Top = models.FloatField()
    wiperf_Bottom = models.FloatField()
    Conditions=(
        ('Over_Balanced', 'Over_Balanced'),
        ('Under_balanced', 'Under_balanced'), 
    )
    wiperf_Condition= models.CharField(max_length = 50,choices = Conditions,default = 'Over_Balanced')
    Conveyance=(
        ('Through_Casing', 'Through_Casing'),
        ('Through_Tubing', 'Through_Tubing'),
        ('TCP', 'TCP'),
      
    )
    wiconveyance_Method = models.CharField(max_length = 50,choices = Conveyance,default = 'Retrievable_Hallow')
    GunTypes=(
        ('Retrievable_Hallow', 'Retrievable_Hallow'),
        ('Expendable', 'Expendable'),
        ('Semi_Expendable', 'Semi_Expendable')
    )
    wiperf_Gun_Type = models.CharField(max_length = 50,choices = GunTypes,default = 'Retrievable_Hallow')
    GunSizes=(
        ('2_in', '2_in'),
        ('2_3/4_In', '2_3/4_in'),
        ('3_1/8_in', '3_1/8_in'),
        ('3_3/8_in', '3_3/8_in')
    )
    wiperf_Gun_Size = models.CharField(max_length=50, choices= GunSizes, default = '2_in' ) 
    wiperf_Gun_Density = models.CharField(max_length=50) 
    wiperf_Charges = models.CharField(max_length=50) 
    wiremarks = models.CharField(max_length=100)


    def __int__(self):
        return self.wiwellid


   

