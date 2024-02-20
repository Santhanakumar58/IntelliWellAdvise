from .models import GPRigworkover
from django import forms
    
class GPRigworkoverForm(forms.ModelForm):
    gpstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gpend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPRigworkover
        fields =['gprigname', 'gpstart_Date', 'gpend_Date', 
        'gpexpected_liquid', 'gpexpected_WC', 'gpexpected_GOR',
         'gppre_wor_liquid', 'gppre_wor_WC', 'gppre_wor_GOR', 'gppre_wor_Lift',
         'gppost_wor_liquid', 'gppost_wor_WC', 'gppost_wor_GOR', 'gppost_wor_Lift',
         'gpjobsummary' ]
