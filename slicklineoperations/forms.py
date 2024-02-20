from .models import SlicklineOperation
from django import forms


class SlicklineOpsForm(forms.ModelForm):
    op_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    time_from = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    time_to= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:        
        model = SlicklineOperation
        fields =['unitname', 'op_Date', 'time_from', 
        'time_to', 'op_code', 'op_details'
         ]
