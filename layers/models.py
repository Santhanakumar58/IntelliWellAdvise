import os
from tkinter import CASCADE
from django.db import models
from oilfields.models import Oilfield


def filepath(request, filename):
    #old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    #filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/layer_volumetrics/', filename)


class Layer(models.Model):    
    layername = models.CharField(max_length=50,)
    description = models.TextField()
    area = models.FloatField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True) 
    oilfield = models.ForeignKey(Oilfield, blank=True, null=True, on_delete=models.CASCADE)   
    volumetric_data = models.FileField(null=True, blank=True , upload_to =filepath )

    def __str__(self):
        if self.year:
            return f"{self.layername} ({self.year})"
        return self.layername
    
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
             
                if field.verbose_name != 'oilfield' 
                
                else 
                    (field.verbose_name, 
                    Oilfield.objects.get(pk=field.value_from_object(self)).oilfieldname)

                for field in self.__class__._meta.fields[1:]
            ]