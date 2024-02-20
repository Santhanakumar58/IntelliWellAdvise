from .models import GIRigworkover
from django import forms
    
class GIRigworkoverForm(forms.ModelForm):
    gistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    giend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GIRigworkover
        fields =['girigname', 'gistart_Date', 'giend_Date', 
        'giexpected_liquid', 'giexpected_WC', 'giexpected_GOR',
         'gipre_wor_liquid', 'gipre_wor_WC', 'gipre_wor_GOR', 'gipre_wor_Lift',
         'gipost_wor_liquid', 'gipost_wor_WC', 'gipost_wor_GOR', 'gipost_wor_Lift',
         'gijobsummary' ]
