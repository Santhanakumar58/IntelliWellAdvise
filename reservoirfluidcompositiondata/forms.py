from django import forms
from .models import FluidCompositionData
    
class FluidCompositionDataForm(forms.ModelForm):   
    class Meta:        
        model = FluidCompositionData 
        fields =[ "fluidcomposition", "component","mole_Percent","weight_Percent","liquid_Density", "molecular_Weight" ]
