from django.db import models

# Create your models here.

class GPWellobjective(models.Model):
    gpwellid = models.PositiveIntegerField()
    gpwellname = models.CharField(max_length=50) 
    gpfgid = models.PositiveIntegerField() 
    gpobjectives = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.gpwellname

