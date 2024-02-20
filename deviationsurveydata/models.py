from django.db import models



class Deviationsurveydata(models.Model):    
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField()
    measuredDepth = models.FloatField()     
    angle = models.FloatField()   
    azimuth = models.FloatField() 
    tvd = models.FloatField( null=True, blank=True)     
    northSouth = models.FloatField( null=True, blank=True)     
    eastWest = models.FloatField( null=True, blank=True)     
    netDrift = models.FloatField( null=True, blank=True)      
    netDirection = models.FloatField( null=True, blank=True)      
    verticalSection = models.FloatField( null=True, blank=True)      
    dogLeg = models.FloatField( null=True, blank=True)   
   