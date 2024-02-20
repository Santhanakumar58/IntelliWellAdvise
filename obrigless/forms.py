from .models import OBRigless
from django import forms

class OBRiglessForm(forms.ModelForm):
    obstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    obend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBRigless
        fields =['obunitname', 'obstart_Date', 'obend_Date', 
        'obexpected_liquid', 'obexpected_WC', 'obexpected_GOR',
         'obpre_rigless_liquid', 'obpre_rigless_WC', 'obpre_rigless_GOR', 
         'obpost_rigless_liquid', 'obpost_rigless_WC', 'obpost_rigless_GOR',
         'objobsummary'
         ]
