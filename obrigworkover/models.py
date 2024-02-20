from django.db import models

# Create your models here.

class OBRigworkover(models.Model):
    obfgid = models.IntegerField()   
    obwellid = models.IntegerField() 
    obrigname = models.CharField(max_length=50)
    obstart_Date = models.DateField()
    obend_Date = models.DateField()
    obexpected_liquid=models.FloatField()
    obexpected_WC=models.FloatField()    
    obexpected_GOR=models.FloatField() 
    obpre_wor_liquid=models.FloatField()
    obpre_wor_WC=models.FloatField()    
    obpre_wor_GOR=models.FloatField() 
    artificiallift_Types = (
        ("Self", "Self Flow"),
        ("GL", "Gas Lift"),
        ("ESP", "ESP"),
        ("SRP", "SRP"),
        ("PCP", "PCP"),
        ("Jetpump", "Jet Pump")
    ) 
    obpre_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    obpost_wor_liquid=models.FloatField()
    obpost_wor_WC=models.FloatField()    
    obpost_wor_GOR=models.FloatField() 
    obpost_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    objobsummary = models.TextField(max_length=1000)
    
 

