from django.db import models
from coiltubing.models import  Coiltubing
class CoiltubingOperation(models.Model):  
    coiltubingid = models.ForeignKey(Coiltubing, on_delete=models.CASCADE )
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    ctname = models.CharField(max_length=50)
    op_Date = models.DateField()
    time_from = models.TimeField()
    time_to=models.TimeField()
    totalhrs=models.FloatField()
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
        return self.ctname 
