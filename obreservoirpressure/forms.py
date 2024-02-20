from django import forms
from .models import OBReservoirPressure

class OBReservoirPressureForm(forms.ModelForm):
    obsurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBReservoirPressure
        fields =['obsurvey_Date', 'obsurvey_Type', 'obgauge_Depth', 'obgauge_Pressure', 'obdatum_Depth',
        'obdatum_Pressure', 'oblayer_permeability', 'oblayer_Thickness', 'oblayer_Skin' ]
  