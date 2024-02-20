from django import forms
from .models import GIReservoirPressure

class GIReservoirPressureForm(forms.ModelForm):
    gisurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GIReservoirPressure
        fields =['gisurvey_Date', 'gisurvey_Type', 'gigauge_Depth', 'gigauge_Pressure', 'gidatum_Depth',
        'gidatum_Pressure', 'gilayer_permeability', 'gilayer_Thickness', 'gilayer_Skin' ]
  