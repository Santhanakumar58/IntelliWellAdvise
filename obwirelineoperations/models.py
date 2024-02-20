from django.db import models
from obwireline.models import  OBWireline

class OBWirelineOperation(models.Model):  
    obwireline = models.ForeignKey(OBWireline, on_delete=models.CASCADE )
    obfgid = models.PositiveIntegerField()   
    obwellid = models.PositiveIntegerField() 
    obunitname = models.CharField(max_length=50)
    obop_Date = models.DateField()
    obtime_from = models.TimeField()
    obtime_to=models.TimeField()
    Opcodes =(
    ('None', 'None'),
    ('Operating', 'Operating'),
    ('Standby', 'Standby'),
    ('Mobilization', 'Mobilization'),
     ('Demobilization', 'Demobilization'),
    ('WaitingonEquipment', 'WaitingonEquipment'),
    ('NonProductive', 'NonProductive')
    )
    obop_code=models.CharField(max_length = 50,choices = Opcodes,default = 'Operating') 
    obop_details=models.CharField(max_length = 150) 

    def __str__(self):       
        return self.obunitname 


