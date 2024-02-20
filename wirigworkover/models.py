from django.db import models

# Create your models here.

class WIRigworkover(models.Model):
    wifgid = models.IntegerField()   
    wiwellid = models.IntegerField() 
    wirigname = models.CharField(max_length=50)
    wistart_Date = models.DateField()
    wiend_Date = models.DateField()
    wiexpected_liquid=models.FloatField()
    wiexpected_WC=models.FloatField()    
    wiexpected_GOR=models.FloatField() 
    wipre_wor_liquid=models.FloatField()
    wipre_wor_WC=models.FloatField()    
    wipre_wor_GOR=models.FloatField() 
    artificiallift_Types = (
        ("Self", "Self Flow"),
        ("GL", "Gas Lift"),
        ("ESP", "ESP"),
        ("SRP", "SRP"),
        ("PCP", "PCP"),
        ("Jetpump", "Jet Pump")
    ) 
    wipre_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    wipost_wor_liquid=models.FloatField()
    wipost_wor_WC=models.FloatField()    
    wipost_wor_GOR=models.FloatField() 
    wipost_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    wijobsummary = models.TextField(max_length=1000)
    
 
