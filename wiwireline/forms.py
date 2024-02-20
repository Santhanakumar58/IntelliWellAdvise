from .models import WIWireline
from django import forms
    
class WIWirelineForm(forms.ModelForm):
    wistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    wiend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WIWireline
        fields =['wiunitname', 'wistart_Date', 'wiend_Date', 
        'wiexpected_liquid', 'wiexpected_WC', 'wiexpected_GOR',
         'wipre_wl_liquid', 'wipre_wl_WC', 'wipre_wl_GOR',  
         'wipost_wl_liquid', 'wipost_wl_WC', 'wipost_wl_GOR',  
         'wijobsummary' ]
