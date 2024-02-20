from msilib.schema import CheckBox
from tkinter import CASCADE, HIDDEN
from django.db import models
from assets.models import Asset
from blocks.models import Block
from oilfields.models import Oilfield
from layers.models import Layer
from sublayers.models import Sublayer

class Observer(models.Model): 
    wellname = models.CharField(max_length=50) 
    fgid = models.PositiveIntegerField(default=0) 
    Categories =(
        ("Exploratory", "Exploratory"),
        ("Appraisal", "Appraisal"),
        ("Development", "Development")
    )
    category = models.CharField(max_length=50, choices=Categories, default="Development")
    asset = models.ForeignKey(Asset, blank=True, null=True, on_delete=models.CASCADE)    
    block = models.ForeignKey(Block, blank=True, null=True, on_delete=models.CASCADE)   
    oilfield = models.ForeignKey(Oilfield, blank=True, null=True, on_delete=models.CASCADE)   
    layer = models.ForeignKey(Layer, blank=True, null=True, on_delete=models.CASCADE)   
    sublayer = models.ForeignKey(Sublayer, blank=True, null=True, on_delete=models.CASCADE)
    completion_Types = (
        ("Single", "Single"),
        ("Dual", "Dual"),
        ("Multilateral", "Multilateral")
    ) 
    completiontype=models.CharField(max_length = 20,choices = completion_Types,default = '1')
    deviation_Types = (
        ("Vertical", "Vertical"),
        ("Deviated", "Deviated"),
        ("Horizontal", "Horizontal")
    ) 
    deviationtype=models.CharField(max_length = 20,choices = deviation_Types,default = '1')
    artificiallift_Types = (
        ("Self", "Self Flow"),
        ("GL", "Gas Lift"),
        ("ESP", "ESP"),
        ("SRP", "SRP"),
        ("PCP", "PCP"),
        ("Jetpump", "Jet Pump")
    ) 
    artificiallifttype=models.CharField(max_length = 20,choices = artificiallift_Types,default = '1')
    inflow_Types = (
        ("PI", "Productivity Index"),
        ("Vogel", "Vogel"),
        ("Standing", "Standing's"),
        ("Wiggins", "Wiggins"),
        ("MultiRate", "Multirate"),
        ("Darcy", "Darcy")
    ) 
    
    inflowtype =models.CharField(max_length = 20,choices = inflow_Types,default = '1')
    Gatheringstations = (
        ("GS-1", "GS-1"),
        ("GS-2", "GS-2"),
        ("GS-3", "GS-3"),
        ("GS-4", "GS-4"),
        ("GS-5", "GS-5"),
        ("GS-6", "GS-6")
    ) 
    connectedgatheringstation=models.CharField(max_length = 20,choices = Gatheringstations,default = '1')
    Headers = (
        ("Header1", "Header-1"),
        ("header2", "Header-2"),
        ("header3", "Header-3"),
        ("header4", "Header-4"),
        ("header5", "Header-5"),
        ("header6", "Header-6")
    ) 
    connectedheader =models.CharField(max_length = 20,choices = Headers,default = '1')
    Units = (
        ("Field", "Field Units"),
        ("SI", "SI Units"),
        ("MKS", "MKS units"),
        ("User", "User Selected")        
    ) 
    unitid = models.CharField(max_length = 20,choices = Units,default = '1')    
    is_selected = models.BooleanField()

    def __str__(self):       
        return self.wellname 

    def __str__(self):
        global fgid
        global selectedassetname
        global selectedblockname
        global selectedfielsname
        global selectedlayername
        global selectedsublayername
        if self.wellname:
            return f"{self.asset} ({self.wellname})"
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
