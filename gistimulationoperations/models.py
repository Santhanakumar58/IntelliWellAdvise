from django.db import models
from gistimulation.models import  GIStimulation

class GIStimulationOperation(models.Model):  
    gistimulation = models.ForeignKey(GIStimulation, on_delete=models.CASCADE )
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


