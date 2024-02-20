from django.db import models
from blocks.models import Block

class Oilfield(models.Model):    
    oilfieldname = models.CharField(max_length=50,)
    description = models.TextField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True) 
    block = models.ForeignKey(Block, blank=True, null=True, on_delete=models.CASCADE)   

    def __str__(self):
        if self.year:
            return f"{self.oilfieldname} ({self.year})"
        return self.oilfieldname
    
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
             
                if field.verbose_name != 'block' 
                
                else 
                    (field.verbose_name, 
                    Block.objects.get(pk=field.value_from_object(self)).blockname)

                for field in self.__class__._meta.fields[1:]
            ]