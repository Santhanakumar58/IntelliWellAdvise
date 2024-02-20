from django.db import models
from girigworkover.models import  GIRigworkover

class GIRigworkoverOperation(models.Model):  
    girigworkover = models.ForeignKey(GIRigworkover, on_delete=models.CASCADE )
    gifgid = models.PositiveIntegerField()   
    giwellid = models.PositiveIntegerField() 
    giunitname = models.CharField(max_length=50)
    giop_Date = models.DateField()
    gitime_from = models.TimeField()
    gitime_to=models.TimeField()
    Opcodes =(
    ('None', 'None'),
    ('Operating', 'Operating'),
    ('Standby', 'Standby'),
    ('Mobilization', 'Mobilization'),
     ('Demobilization', 'Demobilization'),
    ('WaitingonEquipment', 'WaitingonEquipment'),
    ('NonProductive', 'NonProductive')
    )
    giop_code=models.CharField(max_length = 50,choices = Opcodes,default = 'Operating') 
    giop_details=models.CharField(max_length = 150) 

    def __str__(self):       
        return self.giunitname 


