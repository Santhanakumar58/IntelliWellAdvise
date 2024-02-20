from .models import GIDrillingOps
from django import forms


class GIDrillingOpsForm(forms.ModelForm):    
    giops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    gitime_From = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    gitime_To= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time'))) 
    class Meta:        
        model = GIDrillingOps
        fields =['giops_Date', 'gitime_From','gitime_To', 'giops_Code', 'giops_Summary' ]
