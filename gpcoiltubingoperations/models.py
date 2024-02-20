from django.db import models
from gpcoiltubing.models import  GPCoiltubing

class GPCoiltubingOperation(models.Model):  
    gpcoiltubingid = models.ForeignKey(GPCoiltubing, on_delete=models.CASCADE )
    gpfgid = models.PositiveIntegerField()   
    gpwellid = models.PositiveIntegerField() 
    gpctname = models.CharField(max_length=50)
    gpop_Date = models.DateField()
    gptime_from = models.TimeField()
    gptime_to=models.TimeField()
    gptotalhrs=models.FloatField()
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
        return self.gpctname 

