from django.db import models
from gpwellobjectives.models import GPWellobjective

# Create your models here.
class GPWellobjectivedata(models.Model):  
    gpwellobjective = models.ForeignKey(GPWellobjective, on_delete=models.CASCADE)
    gpwellid = models.PositiveIntegerField() 
    date = models.DateField()  
    gasrate_mmscfd = models.FloatField(null=True, blank=True)
    cgr_barrels_per_mmscf = models.FloatField(null=True, blank=True)
    watercut_percentage = models.FloatField(null=True, blank=True)
     
    @property
    def liquidrate(self):        
        return round(self.gasrate_mmscfd * (self.cgr_barrels_per_mmscf),2)
    @property
    def waterate(self):        
        return round(self.liquidrate * self.watercut_percentage/100,2)
    @property
    def condensaterate(self):        
        return round(self.liquidrate - self.waterate,2)
    # oilrate = models.FloatField(null=True, blank=True)
    # waterrate = models.FloatField(null=True, blank=True)
    # gasrate = models.FloatField(null=True, blank=True)
       
    def __int__(self):
        return self.gpwellid    
    
    objects = models.Manager()