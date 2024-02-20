from django.db import models
from stimulation.models import  Stimulation

class StimulationOperation(models.Model):  
    stimulation = models.ForeignKey(Stimulation, on_delete=models.CASCADE )
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    unitname = models.CharField(max_length=50)
    op_Date = models.DateField()
    time_from = models.TimeField()
    time_to=models.TimeField()
    Opcodes =(
    ('None', 'None'),
    ('Operating', 'Operating'),
    ('Standby', 'Standby'),
    ('Mobilization', 'Mobilization'),
     ('Demobilization', 'Demobilization'),
    ('WaitingonEquipment', 'WaitingonEquipment'),
    ('NonProductive', 'NonProductive')
    )
    op_code=models.CharField(max_length = 50,choices = Opcodes,default = 'Operating') 
    op_details=models.CharField(max_length = 150) 

    def __str__(self):       
        return self.unitname 
