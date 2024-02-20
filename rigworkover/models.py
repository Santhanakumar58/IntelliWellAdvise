from django.db import models

# Create your models here.

class Rigworkover(models.Model):
    fgid = models.IntegerField()   
    wellid = models.IntegerField() 
    rigname = models.CharField(max_length=50)
    start_Date = models.DateField()
    end_Date = models.DateField()
    expected_liquid=models.FloatField()
    expected_WC=models.FloatField()    
    expected_GOR=models.FloatField() 
    pre_wor_liquid=models.FloatField()
    pre_wor_WC=models.FloatField()    
    pre_wor_GOR=models.FloatField() 
    artificiallift_Types = (
        ("Self", "Self Flow"),
        ("GL", "Gas Lift"),
        ("ESP", "ESP"),
        ("SRP", "SRP"),
        ("PCP", "PCP"),
        ("Jetpump", "Jet Pump")
    ) 
    pre_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    post_wor_liquid=models.FloatField()
    post_wor_WC=models.FloatField()    
    post_wor_GOR=models.FloatField() 
    post_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    jobsummary = models.TextField(max_length=1000)
    
 