from django.db import models

# Create your models here.
class Wireline(models.Model):  
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    unitname = models.CharField(max_length=50)
    start_Date = models.DateField()
    end_Date = models.DateField()
    expected_liquid=models.FloatField()
    expected_WC=models.FloatField()    
    expected_GOR=models.FloatField() 
    pre_wl_liquid=models.FloatField()
    pre_wl_WC=models.FloatField()    
    pre_wl_GOR=models.FloatField() 
    post_wl_liquid=models.FloatField()
    post_wl_WC=models.FloatField()    
    post_wl_GOR=models.FloatField()
    jobsummary = models.TextField(max_length=1000)