from django.db import models

# Create your models here.

class OBWellobjective(models.Model):
    obwellid = models.PositiveIntegerField()
    obwellname = models.CharField(max_length=50) 
    obfgid = models.PositiveIntegerField() 
    obobjectives = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.obwellname
