from django.db import models

# Create your models here.


class SelectedGasProducer(models.Model):      
    fgid = models.PositiveIntegerField() 
    unit = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    wellid = models.PositiveIntegerField( null=False, blank=False)  
    wellname = models.CharField(max_length=50, null=False, blank=False)   
    completion=models.CharField(max_length=50)  
    deviation=models.CharField(max_length=50)     
    inflow=models.CharField(max_length=50) 
    station=models.CharField(max_length=50) 
    header=models.CharField(max_length=50) 

    def __str__(self):       
        return self.wellname

