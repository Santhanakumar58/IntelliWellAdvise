from django import forms
from .models import WIWellobjectivedata
    
class WIWellObjectivedataForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WIWellobjectivedata
        fields =['wiwellid','date', 'wat_inj_rate', 'wat_inj_pressure', 'tds_ppm', 'pH', 'wat_source' ]
