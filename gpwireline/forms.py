from .models import GPWireline
from django import forms
    
class GPWirelineForm(forms.ModelForm):
    gpstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gpend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPWireline
        fields =['gpunitname', 'gpstart_Date', 'gpend_Date', 
        'gpexpected_liquid', 'gpexpected_WC', 'gpexpected_GOR',
         'gppre_wl_liquid', 'gppre_wl_WC', 'gppre_wl_GOR',  
         'gppost_wl_liquid', 'gppost_wl_WC', 'gppost_wl_GOR',  
         'gpjobsummary' ]
