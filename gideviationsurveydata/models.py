from django.db import models



class GIDeviationsurveydata(models.Model):    
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField()
    gimeasuredDepth = models.FloatField()     
    giangle = models.FloatField()   
    giazimuth = models.FloatField() 
    gitvd = models.FloatField( null=True, blank=True)     
    ginorthSouth = models.FloatField( null=True, blank=True)     
    gieastWest = models.FloatField( null=True, blank=True)     
    ginetDrift = models.FloatField( null=True, blank=True)      
    ginetDirection = models.FloatField( null=True, blank=True)      
    giverticalSection = models.FloatField( null=True, blank=True)      
    gidogLeg = models.FloatField( null=True, blank=True)   
   
