from tkinter import CASCADE
from django.db import models
from assets.models import Asset

class Block(models.Model):    
    blockname = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    area = models.FloatField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True) 
    asset = models.ForeignKey(Asset, blank=True, null=True, on_delete=models.CASCADE)   

    def __str__(self):
        if self.year:
            return f"{self.blockname} ({self.year})"
        return self.blockname
    
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
             
                if field.verbose_name != 'asset' 
                
                else 
                    (field.verbose_name, 
                    Asset.objects.get(pk=field.value_from_object(self)).assetname)

                for field in self.__class__._meta.fields[1:]
            ]