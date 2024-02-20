from .models import WIRigworkover
from django import forms
    
class WIRigworkoverForm(forms.ModelForm):
    wistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    wiend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WIRigworkover
        fields =['wirigname', 'wistart_Date', 'wiend_Date', 
        'wiexpected_liquid', 'wiexpected_WC', 'wiexpected_GOR',
        'wipre_wor_liquid', 'wipre_wor_WC', 'wipre_wor_GOR', 'wipre_wor_Lift',
        'wipost_wor_liquid', 'wipost_wor_WC', 'wipost_wor_GOR', 'wipost_wor_Lift',
        'wijobsummary' ]
