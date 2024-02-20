from django import forms
from .models import GIWellobjectivedata
    
class GIWellObjectivedataForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GIWellobjectivedata
        fields =['giwellid','date', 'gas_inj_rate_mmscfd', 'gas_inj_pressure', 'co2_percentage', 'h2s_percentage' ]
