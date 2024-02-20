from .models import WIRigless
from django import forms

class WIRiglessForm(forms.ModelForm):
    wistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    wiend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WIRigless
        fields =['wiunitname', 'wistart_Date', 'wiend_Date', 
        'wiexpected_liquid', 'wiexpected_WC', 'wiexpected_GOR',
        'wipre_rigless_liquid', 'wipre_rigless_WC', 'wipre_rigless_GOR', 
        'wipost_rigless_liquid', 'wipost_rigless_WC', 'wipost_rigless_GOR',
        'wijobsummary'
         ]
