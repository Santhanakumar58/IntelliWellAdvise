from .models import GPCoiltubingOperation
from django import forms


class GPCoiltubingOpsForm(forms.ModelForm):
    gpop_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gptime_from = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    gptime_to= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:        
        model = GPCoiltubingOperation
        fields =['gpctname', 'gpop_Date', 'gptime_from', 
        'gptime_to', 'gpop_code', 'gpop_details'
         ]
