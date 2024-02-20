from django import forms
from .models import GPReservoirPressure

class GPReservoirPressureForm(forms.ModelForm):
    gpsurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPReservoirPressure
        fields =['gpsurvey_Date', 'gpsurvey_Type', 'gpgauge_Depth', 'gpgauge_Pressure', 'gpdatum_Depth',
        'gpdatum_Pressure', 'gplayer_permeability', 'gplayer_Thickness', 'gplayer_Skin' ]
  