from .models import Wireline
from django import forms
    
class WirelineForm(forms.ModelForm):
    start_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    end_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = Wireline
        fields =['unitname', 'start_Date', 'end_Date', 
        'expected_liquid', 'expected_WC', 'expected_GOR',
         'pre_wl_liquid', 'pre_wl_WC', 'pre_wl_GOR',  
         'post_wl_liquid', 'post_wl_WC', 'post_wl_GOR',  
         'jobsummary' ]
