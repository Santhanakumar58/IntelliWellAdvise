from django.db import models

# Create your models here.
class MultiRatePBUdesign(models.Model):
    fgid = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()  
    survey_Date = models.DateField()    
    layer_Porosity_fraction =models.FloatField()
    layer_Thickness_ft = models.FloatField()
    wellbore_Radius_ft = models.FloatField()
    total_Compressibility=models.FloatField()
    initial_Res_Pres_psi =models.FloatField()
    oil_Viscosity_cP = models.FloatField()
    oil_FVF_Bo =models.FloatField()    
    time1 = models.FloatField(null=True, blank=True)
    rate1=models.FloatField(null=True, blank=True)
    time2 = models.FloatField(null=True, blank=True)
    rate2=models.FloatField(null=True, blank=True)
    time3 = models.FloatField(null=True, blank=True)
    rate3=models.FloatField(null=True, blank=True)
    time4 = models.FloatField(null=True, blank=True)
    rate4=models.FloatField(null=True, blank=True)
    time5 = models.FloatField(null=True, blank=True)
    rate5=models.FloatField(null=True, blank=True)
    time6 = models.FloatField(null=True, blank=True)
    rate6=models.FloatField(null=True, blank=True)
   
       
    def __int__(self):
        return self.fgid   