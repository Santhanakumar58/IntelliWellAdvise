from .models import WIDrillingOps
from django import forms


class WIDrillingOpsForm(forms.ModelForm):    
    wiops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    witime_From = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    witime_To= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    class Meta:        
        model = WIDrillingOps
        fields =['wiops_Date', 'witime_From','witime_To', 'wiops_Code', 'wiops_Summary' ]
