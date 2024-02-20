from .models import DrillingOps
from django import forms


class DrillingOpsForm(forms.ModelForm):    
    ops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    time_From = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    time_To= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    class Meta:        
        model = DrillingOps
        fields =['ops_Date', 'time_From',
        'time_To', 'ops_Code', 'ops_Summary'
         ]
