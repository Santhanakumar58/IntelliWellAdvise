from .models import WICoiltubing
from django import forms

class WICoiltubingForm(forms.ModelForm):
    start_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    end_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WICoiltubing
        fields =['wictname', 'wistart_Date', 'wiend_Date', 
        'wiexpected_liquid', 'wiexpected_WC', 'wiexpected_GOR',
        'wipre_ct_liquid', 'wipre_ct_WC', 'wipre_ct_GOR', 
        'wipost_ct_liquid', 'wipost_ct_WC', 'wipost_ct_GOR', 'wijobsummary'
         ]

