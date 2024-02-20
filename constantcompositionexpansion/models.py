from tkinter import CASCADE
from django.db import models
from sublayers.models import Sublayer

class CCEPVT(models.Model):    
    fgId = models.PositiveIntegerField()
    wellName = models.CharField(max_length=100)
    subLayer = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True )
    sampleId = models.PositiveIntegerField()
    date = models.DateField() 
    temperature = models.FloatField()  

    def __str__(self):       
        return self.wellName 
    
    
