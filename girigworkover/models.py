from django.db import models

# Create your models here.

class GIRigworkover(models.Model):
    gifgid = models.IntegerField()   
    giwellid = models.IntegerField() 
    girigname = models.CharField(max_length=50)
    gistart_Date = models.DateField()
    giend_Date = models.DateField()
    giexpected_liquid=models.FloatField()
    giexpected_WC=models.FloatField()    
    giexpected_GOR=models.FloatField() 
    gipre_wor_liquid=models.FloatField()
    gipre_wor_WC=models.FloatField()    
    gipre_wor_GOR=models.FloatField() 
    artificiallift_Types = (
        ("Self", "Self Flow"),
        ("GL", "Gas Lift"),
        ("ESP", "ESP"),
        ("SRP", "SRP"),
        ("PCP", "PCP"),
        ("Jetpump", "Jet Pump")
    ) 
    gipre_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    gipost_wor_liquid=models.FloatField()
    gipost_wor_WC=models.FloatField()    
    gipost_wor_GOR=models.FloatField() 
    gipost_wor_Lift=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    gijobsummary = models.TextField(max_length=1000)
    
 

