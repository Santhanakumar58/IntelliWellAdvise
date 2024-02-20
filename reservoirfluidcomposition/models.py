from django.db import models
from django.db import models
from sublayers.models import Sublayer
 

# Create your models here.
class FluidComposition(models.Model):    
    fgId = models.PositiveIntegerField()
    wellName = models.CharField(max_length=100)
    subLayer = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True )
    sampleId = models.PositiveIntegerField()
    date = models.DateField() 
    lab = models.CharField(max_length=100)
    
    
    def __str__(self):       
        return self.wellName 
