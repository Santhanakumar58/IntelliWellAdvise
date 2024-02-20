from .models import Coiltubing
from django import forms

class CoiltubingForm(forms.ModelForm):
    start_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    end_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = Coiltubing
        fields =['ctname', 'start_Date', 'end_Date', 
        'expected_liquid', 'expected_WC', 'expected_GOR',
         'pre_ct_liquid', 'pre_ct_WC', 'pre_ct_GOR', 
         'post_ct_liquid', 'post_ct_WC', 'post_ct_GOR', 'jobsummary'
         ]

