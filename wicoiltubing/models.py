from django.db import models

# Create your models here.

class WICoiltubing(models.Model):  
    wifgid = models.PositiveIntegerField()   
    wiwellid = models.PositiveIntegerField() 
    wictname = models.CharField(max_length=50)
    wistart_Date = models.DateField()
    wiend_Date = models.DateField()
    wiexpected_liquid=models.FloatField()
    wiexpected_WC=models.FloatField()    
    wiexpected_GOR=models.FloatField() 
    wipre_ct_liquid=models.FloatField()
    wipre_ct_WC=models.FloatField()    
    wipre_ct_GOR=models.FloatField() 
    wipost_ct_liquid=models.FloatField()
    wipost_ct_WC=models.FloatField()    
    wipost_ct_GOR=models.FloatField()
    wijobsummary = models.TextField(max_length=1000)
   
    def __int__(self):
        return self.wiwellid

