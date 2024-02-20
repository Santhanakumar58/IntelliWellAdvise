from .models import GICoiltubing
from django import forms

class GICoiltubingForm(forms.ModelForm):
    gistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    giend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GICoiltubing
        fields =['gictname', 'gistart_Date', 'giend_Date', 
        'giexpected_liquid', 'giexpected_WC', 'giexpected_GOR',
         'gipre_ct_liquid', 'gipre_ct_WC', 'gipre_ct_GOR', 
         'gipost_ct_liquid', 'gipost_ct_WC', 'gipost_ct_GOR', 'gijobsummary'
         ]

