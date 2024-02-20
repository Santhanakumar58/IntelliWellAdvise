from django import forms
from .models import FluidComposition 
    
class FluidCompositionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = FluidComposition 
        fields =["date", "wellName", "sampleId", "lab" ]
