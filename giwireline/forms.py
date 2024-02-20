from .models import GIWireline
from django import forms
    
class GIWirelineForm(forms.ModelForm):
    gistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    giend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GIWireline
        fields =['giunitname', 'gistart_Date', 'giend_Date', 
        'giexpected_liquid', 'giexpected_WC', 'giexpected_GOR',
         'gipre_wl_liquid', 'gipre_wl_WC', 'gipre_wl_GOR',  
         'gipost_wl_liquid', 'gipost_wl_WC', 'gipost_wl_GOR',  
         'gijobsummary' ]
