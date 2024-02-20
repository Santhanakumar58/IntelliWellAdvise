from django import forms
from django.db import models

# Create your models here.
class WIRigless(models.Model):  
    wifgid = models.PositiveIntegerField()   
    wiwellid = models.PositiveIntegerField() 
    wiunitname = models.CharField(max_length=50)
    wistart_Date = models.DateField()
    wiend_Date = models.DateField()
    wiexpected_liquid=models.FloatField()
    wiexpected_WC=models.FloatField()    
    wiexpected_GOR=models.FloatField() 
    wipre_rigless_liquid=models.FloatField()
    wipre_rigless_WC=models.FloatField()    
    wipre_rigless_GOR=models.FloatField() 
    wipost_rigless_liquid=models.FloatField()
    wipost_rigless_WC=models.FloatField()    
    wipost_rigless_GOR=models.FloatField()
    wijobsummary = models.TextField(max_length=1000)
