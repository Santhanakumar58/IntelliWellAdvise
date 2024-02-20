from .models import GPRigless
from django import forms

class GPRiglessForm(forms.ModelForm):
    gpstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gpend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPRigless
        fields =['gpunitname', 'gpstart_Date', 'gpend_Date', 
        'gpexpected_liquid', 'gpexpected_WC', 'gpexpected_GOR',
         'gppre_rigless_liquid', 'gppre_rigless_WC', 'gppre_rigless_GOR', 
         'gppost_rigless_liquid', 'gppost_rigless_WC', 'gppost_rigless_GOR',
         'gpjobsummary'
         ]
