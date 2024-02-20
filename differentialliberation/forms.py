from django import forms
from .models import DifferentialLiberationModel 
    
class DiffLibForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = DifferentialLiberationModel 
        fields =["date", "wellName", "sampleId", "temperature", "residual_oil_gravity", "residual_oil_density"]
