from django.db import models

# Create your models here.

class Coiltubing(models.Model):  
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    ctname = models.CharField(max_length=50)
    start_Date = models.DateField()
    end_Date = models.DateField()
    expected_liquid=models.FloatField()
    expected_WC=models.FloatField()    
    expected_GOR=models.FloatField() 
    pre_ct_liquid=models.FloatField()
    pre_ct_WC=models.FloatField()    
    pre_ct_GOR=models.FloatField() 
    post_ct_liquid=models.FloatField()
    post_ct_WC=models.FloatField()    
    post_ct_GOR=models.FloatField()
    jobsummary = models.TextField(max_length=1000)
   
    def __int__(self):
        return self.wellid
