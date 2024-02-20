from django.db import models

# Create your models here.
class GPWireline(models.Model):  
    gpfgid = models.PositiveIntegerField()   
    gpwellid = models.PositiveIntegerField() 
    gpunitname = models.CharField(max_length=50)
    gpstart_Date = models.DateField()
    gpend_Date = models.DateField()
    gpexpected_liquid=models.FloatField()
    gpexpected_WC=models.FloatField()    
    gpexpected_GOR=models.FloatField() 
    gppre_wl_liquid=models.FloatField()
    gppre_wl_WC=models.FloatField()    
    gppre_wl_GOR=models.FloatField() 
    gppost_wl_liquid=models.FloatField()
    gppost_wl_WC=models.FloatField()    
    gppost_wl_GOR=models.FloatField()
    gpjobsummary = models.TextField(max_length=1000)
