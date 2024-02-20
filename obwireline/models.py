from django.db import models

# Create your models here.
class OBWireline(models.Model):  
    obfgid = models.PositiveIntegerField()   
    obwellid = models.PositiveIntegerField() 
    obunitname = models.CharField(max_length=50)
    obstart_Date = models.DateField()
    obend_Date = models.DateField()
    obexpected_liquid=models.FloatField()
    obexpected_WC=models.FloatField()    
    obexpected_GOR=models.FloatField() 
    obpre_wl_liquid=models.FloatField()
    obpre_wl_WC=models.FloatField()    
    obpre_wl_GOR=models.FloatField() 
    obpost_wl_liquid=models.FloatField()
    obpost_wl_WC=models.FloatField()    
    obpost_wl_GOR=models.FloatField()
    objobsummary = models.TextField(max_length=1000)
