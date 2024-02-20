from django.db import models
from gpwireline.models import  GPWireline

class GPWirelineOperation(models.Model):  
    gpwireline = models.ForeignKey(GPWireline, on_delete=models.CASCADE )
    gpfgid = models.PositiveIntegerField()   
    gpwellid = models.PositiveIntegerField() 
    gpunitname = models.CharField(max_length=50)
    gpop_Date = models.DateField()
    gptime_from = models.TimeField()
    gptime_to=models.TimeField()
    Opcodes =(
    ('None', 'None'),
    ('Operating', 'Operating'),
    ('Standby', 'Standby'),
    ('Mobilization', 'Mobilization'),
     ('Demobilization', 'Demobilization'),
    ('WaitingonEquipment', 'WaitingonEquipment'),
    ('NonProductive', 'NonProductive')
    )
    gpop_code=models.CharField(max_length = 50,choices = Opcodes,default = 'Operating') 
    gpop_details=models.CharField(max_length = 150) 

    def __str__(self):       
        return self.gpunitname 

