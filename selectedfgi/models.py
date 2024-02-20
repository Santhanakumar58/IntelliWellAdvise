from django.db import models

class Selectedfgi(models.Model):    
    fgid = models.IntegerField()
    selectedassetname = models.CharField(max_length=50, null=True, blank=True)
    selectedblockname = models.CharField(max_length=50, null=True, blank=True)
    selectedfieldname = models.CharField(max_length=50, null=True, blank=True)
    selectedlayername = models.CharField(max_length=50, null=True, blank=True) 
    selectedsublayername = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):       
        return self.selectedassetname
    
   