from tkinter import CASCADE
from django.db import models
from layers.models import Layer

class Sublayer(models.Model):    
    sublayername = models.CharField(max_length=50,)
    description = models.TextField()
    area = models.FloatField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True) 
    layer = models.ForeignKey(Layer, blank=True, null=True, on_delete=models.CASCADE)   

    def __str__(self):
        #if self.year:
         #   return f"{self.sublayername} ({self.year})"
        return self.sublayername
    
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
             
                if field.verbose_name != 'layer' 
                
                else 
                    (field.verbose_name, 
                    Layer.objects.get(pk=field.value_from_object(self)).layername)

                for field in self.__class__._meta.fields[1:]
            ]