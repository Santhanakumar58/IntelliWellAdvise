from django import forms
from .models import BlackoilPVT
    
class BlackoilPVTForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = BlackoilPVT
        fields =["date", "wellName", "sampleId", "reservoirPressure", "reservoirTemperature", "oilAPIgravity", "gasGravity", "solutionGOR", "pbCorrelation", "viscosityCorrelation"]

     