from django.db import models

# Create your models here.
class GIStimulation(models.Model):  
    gifgid = models.PositiveIntegerField()   
    giwellid = models.PositiveIntegerField() 
    giunitname = models.CharField(max_length=50)
    gistart_Date = models.DateField()
    giend_Date = models.DateField()
    giexpected_liquid=models.FloatField()
    giexpected_WC=models.FloatField()    
    giexpected_GOR=models.FloatField() 
    gipre_stim_liquid=models.FloatField()
    gipre_stim_WC=models.FloatField()    
    gipre_stim_GOR=models.FloatField() 
    gipost_stim_liquid=models.FloatField()
    gipost_stim_WC=models.FloatField()    
    gipost_stim_GOR=models.FloatField()
    gijobsummary = models.TextField(max_length=1000)

