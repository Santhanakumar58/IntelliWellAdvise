from .models import GPCoiltubing
from django import forms

class GPCoiltubingForm(forms.ModelForm):
    gpstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gpend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPCoiltubing
        fields =['gpctname', 'gpstart_Date', 'gpend_Date', 
        'gpexpected_liquid', 'gpexpected_WC', 'gpexpected_GOR',
         'gppre_ct_liquid', 'gppre_ct_WC', 'gppre_ct_GOR', 
         'gppost_ct_liquid', 'gppost_ct_WC', 'gppost_ct_GOR', 'gpjobsummary'
         ]

