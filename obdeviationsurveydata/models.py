from django.db import models



class OBDeviationsurveydata(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField()
    obmeasuredDepth = models.FloatField()     
    obangle = models.FloatField()   
    obazimuth = models.FloatField() 
    obtvd = models.FloatField( null=True, blank=True)     
    obnorthSouth = models.FloatField( null=True, blank=True)     
    obeastWest = models.FloatField( null=True, blank=True)     
    obnetDrift = models.FloatField( null=True, blank=True)      
    obnetDirection = models.FloatField( null=True, blank=True)      
    obverticalSection = models.FloatField( null=True, blank=True)      
    obdogLeg = models.FloatField( null=True, blank=True)   
   
