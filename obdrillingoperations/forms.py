from .models import OBDrillingOps
from django import forms


class OBDrillingOpsForm(forms.ModelForm):    
    obops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    obtime_From = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    obtime_To= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    class Meta:        
        model = OBDrillingOps
        fields =['obops_Date', 'obtime_From','obtime_To', 'obops_Code', 'obops_Summary' ]
