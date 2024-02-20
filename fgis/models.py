from msilib.schema import CheckBox
from tabnanny import check
from tkinter import CASCADE
from django.db import models
from assets.models import Asset
from blocks.models import Block
from oilfields.models import Oilfield
from layers.models import Layer
from sublayers.models import Sublayer

class FGIModel(models.Model):  
    asset = models.ForeignKey(Asset, blank=True, null=True, on_delete=models.CASCADE)  
    block = models.ForeignKey(Block, blank=True, null=True, on_delete=models.CASCADE)   
    oilfield = models.ForeignKey(Oilfield, blank=True, null=True, on_delete=models.CASCADE)   
    layer = models.ForeignKey(Layer, blank=True, null=True, on_delete=models.CASCADE)   
    sublayer = models.ForeignKey(Sublayer, blank=True, null=True, on_delete=models.CASCADE)  
    is_selected = models.BooleanField()
    
    def __str__(self):
        global unitid
        global selectedassetname
        global selectedblockname
        global selectedfielsname
        global selectedlayername
        global selectedsublayername
        if self.sublayer:
            return f"{self.asset} ({self.sublayer})"
        return self.asset
    
    def get_fields(self):        
        return [(field.verbose_name, field.value_from_object(self))
             
                if field.verbose_name != 'asset' 
                
                else 
                    (field.verbose_name, 
                    Asset.objects.get(pk=field.value_from_object(self)).assetname)
                
                if field.verbose_name != 'block' 
                
                else 
                    (field.verbose_name, 
                    Block.objects.get(pk=field.value_from_object(self)).blockname)

                if field.verbose_name != 'oilfield' 
                
                else 
                    (field.verbose_name, 
                    Oilfield.objects.get(pk=field.value_from_object(self)).oilfieldname)

                if field.verbose_name != 'layer' 
                
                else 
                    (field.verbose_name, 
                    Layer.objects.get(pk=field.value_from_object(self)).layername)

                if field.verbose_name != 'sublayer' 
                
                else 
                    (field.verbose_name, 
                    Sublayer.objects.get(pk=field.value_from_object(self)).sublayername)

                for field in self.__class__._meta.fields[1:]
            ]