from django.db import models
from django.db import models
from reservoirfluidcomposition.models import FluidComposition

 

# Create your models here.
class FluidCompositionData(models.Model):    
    fluidcomposition = models.ForeignKey(FluidComposition, on_delete=models.CASCADE)
    Components=(
        ("Hydrogen_Sulfide","Hydrogen_Sulfide" ),
        ("Carbon_Dioxide","Carbon_Dioxide" ),
        ("Nitrogen" , "Nitrogen"),
        ("Methane", "Methane"),
        ("Ethane", "Ethane"),
        ("Propane", "Propane"),
        ("iso-Butane", "iso-Butane"),
        ("n-Butane", "n-Butane"),
        ("iso-Pentane","iso-Pentane"),
        ("n-Pentane", "n-Pentane"),
        ("Hexanes","Hexanes"),
        ("Heptanes","Heptanes"),
        ("Octanes","Octanes"),
        ("Nonanes","Nonanes"),
        ("Decanes","Decanes"),  
        ("Undecanes","Undecanes"),
        ("Dodecanes","Dodecanes"),  
        ("Tridecanes","Tridecanes"),
        ("Tetradecanes","Tetradecanes"),
        ("Pentadecanes","Pentadecanes"),
        ("Hexadecanes","Hexadecanes"),
        ("Heptadecanes","Heptadecanes"),        
        ("Octadecanes","Octadecanes"),
        ("Nonadecanes","Nonadecanes"),
        ("Eicosanes","Eicosanes"),
        ("Heneicosanes","Heneicosanes"),
        ("Docosanes","Docosanes"),        
        ("Tricosanes","Tricosanes"),
        ("Tetracosanes","Tetracosanes"),
        ("Pentacosanes","Pentacosanes"),
        ("Hexacosanes","Hexacosanes"),
        ("Heptacosanes","Heptacosanes"),        
        ("Octacosanes","Octacosanes"),
        ("Nonacosanes","Nonacosanes"),
        ("Heptanes_plus"," Heptanes_plus"),
        ("Undecanes_plus","Undecanes_plus"),
        ("Pentadecanes_plus","Pentadecanes_plus"),
        ("Eicosanes_plus","Eicosanes_plus"),
        ("Pentacosanes_plus","Pentacosanes_plus"),  
        ("Triacontanes_plus ","Triacontanes_plus "),
        )
    component = models.CharField(max_length=100, choices=Components, default="Methane" )  
    mole_Percent = models.FloatField()
    weight_Percent = models.FloatField()
    liquid_Density = models.FloatField()
    molecular_Weight = models.FloatField()    

  
