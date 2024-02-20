from django.db import models



class GPDeviationsurveydata(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()
    gpmeasuredDepth = models.FloatField()     
    gpangle = models.FloatField()   
    gpazimuth = models.FloatField() 
    gptvd = models.FloatField( null=True, blank=True)     
    gpnorthSouth = models.FloatField( null=True, blank=True)     
    gpeastWest = models.FloatField( null=True, blank=True)     
    gpnetDrift = models.FloatField( null=True, blank=True)      
    gpnetDirection = models.FloatField( null=True, blank=True)      
    gpverticalSection = models.FloatField( null=True, blank=True)      
    gpdogLeg = models.FloatField( null=True, blank=True)   
   