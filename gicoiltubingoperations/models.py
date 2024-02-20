from django.db import models
from gicoiltubing.models import  GICoiltubing

class GICoiltubingOperation(models.Model):  
    gicoiltubingid = models.ForeignKey(GICoiltubing, on_delete=models.CASCADE )
    gifgid = models.PositiveIntegerField()   
    giwellid = models.PositiveIntegerField() 
    gictname = models.CharField(max_length=50)
    giop_Date = models.DateField()
    gitime_from = models.TimeField()
    gitime_to=models.TimeField()
    gitotalhrs=models.FloatField()
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
        return self.gictname 


