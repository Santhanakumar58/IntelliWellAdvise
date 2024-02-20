from .models import WIStimulationOperation
from django import forms


class WIStimulationOpsForm(forms.ModelForm):
    wiop_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    witime_from = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    witime_to= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:        
        model = WIStimulationOperation
        fields =['wiunitname', 'wiop_Date', 'witime_from', 
        'witime_to', 'wiop_code', 'wiop_details'
         ]
