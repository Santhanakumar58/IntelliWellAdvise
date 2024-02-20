from django import forms
from .models import OPReservoirPressure

class ReservoirPressureForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OPReservoirPressure
        fields =['survey_Date', 'survey_Type', 'gauge_Depth', 'gauge_Pressure', 'datum_Depth',
        'datum_Pressure', 'layer_permeability', 'layer_Thickness', 'layer_Skin' ]
  