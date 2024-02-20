from django.db import models
from obslickline.models import  OBSlickline

class OBSlicklineOperation(models.Model):  
    obslickline = models.ForeignKey(OBSlickline, on_delete=models.CASCADE )
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


