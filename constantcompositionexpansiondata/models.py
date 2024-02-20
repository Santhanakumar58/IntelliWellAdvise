from django.db import models
from django.db import models
from constantcompositionexpansion.models import CCEPVT

# Create your models here.
class CCEPVTData(models.Model):    
    ccepvt = models.ForeignKey(CCEPVT, on_delete=models.CASCADE, null=True, blank=True )   
    pressure = models.FloatField()     
    relative_volume = models.FloatField()   
    y_function = models.FloatField(blank=True, null=True)    
    density = models.FloatField(blank=True, null=True)    

    def __int__(self):       
        return self.ccepvt 