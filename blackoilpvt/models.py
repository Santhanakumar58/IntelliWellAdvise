from datetime import datetime
from tkinter import CASCADE
from django.db import models
from assets.models import Asset
from sublayers.models import Sublayer

class BlackoilPVT(models.Model):    
    fgId = models.PositiveIntegerField()
    wellName = models.CharField(max_length=100)
    subLayer = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True )
    sampleId = models.PositiveIntegerField()
    date = models.DateField() 
    reservoirPressure = models.FloatField()     
    reservoirTemperature = models.FloatField()   
    oilAPIgravity = models.FloatField()    
    gasGravity = models.FloatField()     
    solutionGOR = models.FloatField()    
    bubblepoint_Correlations = (
        ("_Standing", "Standing"),
        ("_VasquezBeggs", "VasquezBeggs"),
        ("_Glaso", "Glaso"),        
        ("_Marhoun", "Marhoun"),       
        ("_PetroskyFarshad", "PetroskyFarshad")        
    ) 
    pbCorrelation = models.CharField(max_length = 20,choices = bubblepoint_Correlations,default = '_VasquezBeggs') 
    viscosity_Correlations = (
        ("_Beal", "Beal"),       
        ("_Glaso", "Glaso"),
        ("_BeggsRobinson", "BeggsRobinson")
    ) 
    viscosityCorrelation = models.CharField(max_length = 20,choices = viscosity_Correlations,default = '1')

    def __str__(self):       
        return self.wellName 

