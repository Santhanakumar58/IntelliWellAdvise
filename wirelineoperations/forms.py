from .models import WirelineOperation
from django import forms


class WirelineOpsForm(forms.ModelForm):
    op_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    time_from = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    time_to= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:        
        model = WirelineOperation
        fields =['unitname', 'op_Date', 'time_from', 
        'time_to', 'op_code', 'op_details'
         ]
