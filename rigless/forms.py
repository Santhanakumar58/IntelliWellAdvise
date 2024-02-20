from .models import Rigless
from django import forms

class RiglessForm(forms.ModelForm):
    start_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    end_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = Rigless
        fields =['unitname', 'start_Date', 'end_Date', 
        'expected_liquid', 'expected_WC', 'expected_GOR',
         'pre_rigless_liquid', 'pre_rigless_WC', 'pre_rigless_GOR', 
         'post_rigless_liquid', 'post_rigless_WC', 'post_rigless_GOR',
         'jobsummary'
         ]
