from asyncio.windows_events import NULL
from django.db import models
from opwellobjectives.models import OPWellobjective
   
class OPWellobjectivedata(models.Model):  
    opwellobjective = models.ForeignKey(OPWellobjective, on_delete=models.CASCADE)
    wellid = models.PositiveIntegerField() 
    date = models.DateField()
    liquidrate = models.FloatField(null=True, blank=True)
    watercut = models.FloatField(null=True, blank=True)
    gasoilratio = models.FloatField(null=True, blank=True)
     
    @property
    def oilrate(self):        
        return round(self.liquidrate * (1-self.watercut/100),2)
    @property
    def waterate(self):        
        return round(self.liquidrate * self.watercut/100,2)
    @property
    def gasrate(self):        
        return round(self.oilrate * self.gasoilratio,2)
    # oilrate = models.FloatField(null=True, blank=True)
    # waterrate = models.FloatField(null=True, blank=True)
    # gasrate = models.FloatField(null=True, blank=True)
       
    def __int__(self):
        return self.wellid    
    
    objects = models.Manager()
 
