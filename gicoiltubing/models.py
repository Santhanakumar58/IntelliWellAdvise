from django.db import models

# Create your models here.

class GICoiltubing(models.Model):  
    gifgid = models.PositiveIntegerField()   
    giwellid = models.PositiveIntegerField() 
    gictname = models.CharField(max_length=50)
    gistart_Date = models.DateField()
    giend_Date = models.DateField()
    giexpected_liquid=models.FloatField()
    giexpected_WC=models.FloatField()    
    giexpected_GOR=models.FloatField() 
    gipre_ct_liquid=models.FloatField()
    gipre_ct_WC=models.FloatField()    
    gipre_ct_GOR=models.FloatField() 
    gipost_ct_liquid=models.FloatField()
    gipost_ct_WC=models.FloatField()    
    gipost_ct_GOR=models.FloatField()
    gijobsummary = models.TextField(max_length=1000)
   
    def __int__(self):
        return self.giwellid


