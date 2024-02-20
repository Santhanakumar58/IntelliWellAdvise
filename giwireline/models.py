from django.db import models

# Create your models here.
class GIWireline(models.Model):  
    gifgid = models.PositiveIntegerField()   
    giwellid = models.PositiveIntegerField() 
    giunitname = models.CharField(max_length=50)
    gistart_Date = models.DateField()
    giend_Date = models.DateField()
    giexpected_liquid=models.FloatField()
    giexpected_WC=models.FloatField()    
    giexpected_GOR=models.FloatField() 
    gipre_wl_liquid=models.FloatField()
    gipre_wl_WC=models.FloatField()    
    gipre_wl_GOR=models.FloatField() 
    gipost_wl_liquid=models.FloatField()
    gipost_wl_WC=models.FloatField()    
    gipost_wl_GOR=models.FloatField()
    gijobsummary = models.TextField(max_length=1000)

