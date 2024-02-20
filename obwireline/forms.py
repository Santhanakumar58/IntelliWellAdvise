from .models import OBWireline
from django import forms
    
class OBWirelineForm(forms.ModelForm):
    obstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    obend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBWireline
        fields =['obunitname', 'obstart_Date', 'obend_Date', 
        'obexpected_liquid', 'obexpected_WC', 'obexpected_GOR',
         'obpre_wl_liquid', 'obpre_wl_WC', 'obpre_wl_GOR',  
         'obpost_wl_liquid', 'obpost_wl_WC', 'obpost_wl_GOR',  
         'objobsummary' ]
