from msilib.schema import AdminExecuteSequence
from django.db import models


class OPWellobjective(models.Model):
    wellid = models.PositiveIntegerField()
    opwellname = models.CharField(max_length=50) 
    opfgid = models.PositiveIntegerField() 
    opobjectives = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.opwellname


   
