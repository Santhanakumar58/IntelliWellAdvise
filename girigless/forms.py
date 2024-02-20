from .models import GIRigless
from django import forms

class GIRiglessForm(forms.ModelForm):
    gistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    giend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GIRigless
        fields =['giunitname', 'gistart_Date', 'giend_Date', 
        'giexpected_liquid', 'giexpected_WC', 'giexpected_GOR',
         'gipre_rigless_liquid', 'gipre_rigless_WC', 'gipre_rigless_GOR', 
         'gipost_rigless_liquid', 'gipost_rigless_WC', 'gipost_rigless_GOR',
         'gijobsummary'
         ]
