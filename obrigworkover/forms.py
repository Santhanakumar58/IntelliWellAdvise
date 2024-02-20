from .models import OBRigworkover
from django import forms
    
class OBRigworkoverForm(forms.ModelForm):
    obstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    obend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBRigworkover
        fields =['obrigname', 'obstart_Date', 'obend_Date', 
        'obexpected_liquid', 'obexpected_WC', 'obexpected_GOR',
         'obpre_wor_liquid', 'obpre_wor_WC', 'obpre_wor_GOR', 'obpre_wor_Lift',
         'obpost_wor_liquid', 'obpost_wor_WC', 'obpost_wor_GOR', 'obpost_wor_Lift',
         'objobsummary' ]
