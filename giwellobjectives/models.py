from django.db import models

# Create your models here.

class GIWellobjective(models.Model):
    giwellid = models.PositiveIntegerField()
    giwellname = models.CharField(max_length=50) 
    gifgid = models.PositiveIntegerField() 
    giobjectives = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.giwellname
