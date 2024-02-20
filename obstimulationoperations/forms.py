from .models import OBStimulationOperation
from django import forms


class OBStimulationOpsForm(forms.ModelForm):
    obop_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    obtime_from = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    obtime_to= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:        
        model = OBStimulationOperation
        fields =['obunitname', 'obop_Date', 'obtime_from', 
        'obtime_to', 'obop_code', 'obop_details'
         ]
