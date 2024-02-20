from .models import OBCoiltubing
from django import forms

class OBCoiltubingForm(forms.ModelForm):
    obstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    obend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBCoiltubing
        fields =['obctname', 'obstart_Date', 'obend_Date', 
        'obexpected_liquid', 'obexpected_WC', 'obexpected_GOR',
         'obpre_ct_liquid', 'obpre_ct_WC', 'obpre_ct_GOR', 
         'obpost_ct_liquid', 'obpost_ct_WC', 'obpost_ct_GOR', 'objobsummary'
         ]

