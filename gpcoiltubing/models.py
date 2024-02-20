from django.db import models

# Create your models here.

class GPCoiltubing(models.Model):  
    gpfgid = models.PositiveIntegerField()   
    gpwellid = models.PositiveIntegerField() 
    gpctname = models.CharField(max_length=50)
    gpstart_Date = models.DateField()
    gpend_Date = models.DateField()
    gpexpected_liquid=models.FloatField()
    gpexpected_WC=models.FloatField()    
    gpexpected_GOR=models.FloatField() 
    gppre_ct_liquid=models.FloatField()
    gppre_ct_WC=models.FloatField()    
    gppre_ct_GOR=models.FloatField() 
    gppost_ct_liquid=models.FloatField()
    gppost_ct_WC=models.FloatField()    
    gppost_ct_GOR=models.FloatField()
    gpjobsummary = models.TextField(max_length=1000)
   
    def __int__(self):
        return self.gpwellid

