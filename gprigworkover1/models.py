from django.db import models

# Create your models here.

class GPRigworkover(models.Model):
    gpfgid = models.IntegerField()   
    gpwellid = models.IntegerField() 
    gprigname = models.CharField(max_length=50)
    gpstart_Date = models.DateField()
    gpend_Date = models.DateField()
    gpexpected_liquid=models.FloatField()
    gpexpected_WC=models.FloatField()    
    gpexpected_GOR=models.FloatField() 
    gppre_wor_liquid=models.FloatField()
    gppre_wor_WC=models.FloatField()    
    gppre_wor_GOR=models.FloatField() 
    artificiallift_Types = (
        ("Self", "Self Flow"),
        ("GL", "Gas Lift"),
        ("ESP", "ESP"),
        ("SRP", "SRP"),
        ("PCP", "PCP"),
        ("Jetpump", "Jet Pump")
    ) 
    gppre_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    gppost_wor_liquid=models.FloatField()
    gppost_wor_WC=models.FloatField()    
    gppost_wor_GOR=models.FloatField() 
    gppost_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    gpjobsummary = models.TextField(max_length=1000)
    
 
