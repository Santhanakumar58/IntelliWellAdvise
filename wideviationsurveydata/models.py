from django.db import models



class WIDeviationsurveydata(models.Model):    
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField()
    wimeasuredDepth = models.FloatField()     
    wiangle = models.FloatField()   
    wiazimuth = models.FloatField() 
    witvd = models.FloatField( null=True, blank=True)     
    winorthSouth = models.FloatField( null=True, blank=True)     
    wieastWest = models.FloatField( null=True, blank=True)     
    winetDrift = models.FloatField( null=True, blank=True)      
    winetDirection = models.FloatField( null=True, blank=True)      
    wiverticalSection = models.FloatField( null=True, blank=True)      
    widogLeg = models.FloatField( null=True, blank=True)   
   
