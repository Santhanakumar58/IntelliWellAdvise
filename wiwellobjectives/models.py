from django.db import models

# Create your models here.

class WIWellobjective(models.Model):
    wiwellid = models.PositiveIntegerField()
    wiwellname = models.CharField(max_length=50) 
    wifgid = models.PositiveIntegerField() 
    wiobjectives = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.wiwellname
