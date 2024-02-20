from .models import GPDrillingOps
from django import forms


class GPDrillingOpsForm(forms.ModelForm):    
    gpops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    gptime_From = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    gptime_To= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    class Meta:        
        model = GPDrillingOps
        fields =['gpops_Date', 'gptime_From','gptime_To', 'gpops_Code', 'gpops_Summary' ]
