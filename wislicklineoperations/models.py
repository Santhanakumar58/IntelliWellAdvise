from django.db import models
from wislickline.models import  WISlickline

class WISlicklineOperation(models.Model):  
    wislickline = models.ForeignKey(WISlickline, on_delete=models.CASCADE )
    wifgid = models.PositiveIntegerField()   
    wiwellid = models.PositiveIntegerField() 
    wiunitname = models.CharField(max_length=50)
    wiop_Date = models.DateField()
    witime_from = models.TimeField()
    witime_to=models.TimeField()
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
        return self.wiunitname 

