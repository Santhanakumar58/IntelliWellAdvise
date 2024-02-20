from .models import CoiltubingOperation
from django import forms


class CoiltubingOpsForm(forms.ModelForm):
    op_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    time_from = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    time_to= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:        
        model = CoiltubingOperation
        fields =['ctname', 'op_Date', 'time_from', 
        'time_to', 'op_code', 'op_details'
         ]
