from django.db import models
from wicoiltubing.models import  WICoiltubing
class WICoiltubingOperation(models.Model):  
    wicoiltubingid = models.ForeignKey(WICoiltubing, on_delete=models.CASCADE )
    wifgid = models.PositiveIntegerField()   
    wiwellid = models.PositiveIntegerField() 
    wictname = models.CharField(max_length=50)
    wiop_Date = models.DateField()
    witime_from = models.TimeField()
    witime_to=models.TimeField()
    witotalhrs=models.FloatField()
    Opcodes =(
    ('None', 'None'),
    ('Operating', 'Operating'),
    ('Standby', 'Standby'),
    ('Mobilization', 'Mobilization'),
     ('Demobilization', 'Demobilization'),
    ('WaitingonEquipment', 'WaitingonEquipment'),
    ('NonProductive', 'NonProductive')
    )
    wiop_code=models.CharField(max_length = 50,choices = Opcodes,default = 'Operating') 
    wiop_details=models.CharField(max_length = 150) 

    def __str__(self):       
        return self.wictname 
