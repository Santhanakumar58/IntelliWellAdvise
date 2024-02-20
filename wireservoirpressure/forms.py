from django import forms
from .models import WIReservoirPressure

class WIReservoirPressureForm(forms.ModelForm):
    wisurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WIReservoirPressure
        fields =['wisurvey_Date', 'wisurvey_Type', 'wigauge_Depth', 'wigauge_Pressure', 'widatum_Depth',
        'widatum_Pressure', 'wilayer_permeability', 'wilayer_Thickness', 'wilayer_Skin' ]
  