from django.db import models

# Create your models here.

class OBCoiltubing(models.Model):  
    obfgid = models.PositiveIntegerField()   
    obwellid = models.PositiveIntegerField() 
    obctname = models.CharField(max_length=50)
    obstart_Date = models.DateField()
    obend_Date = models.DateField()
    obexpected_liquid=models.FloatField()
    obexpected_WC=models.FloatField()    
    obexpected_GOR=models.FloatField() 
    obpre_ct_liquid=models.FloatField()
    obpre_ct_WC=models.FloatField()    
    obpre_ct_GOR=models.FloatField() 
    obpost_ct_liquid=models.FloatField()
    obpost_ct_WC=models.FloatField()    
    obpost_ct_GOR=models.FloatField()
    objobsummary = models.TextField(max_length=1000)
   
    def __int__(self):
        return self.obwellid


