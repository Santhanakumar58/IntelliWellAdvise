from django import forms
from .models import OPWellobjectivedata
    
class OPWellObjectivedataForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OPWellobjectivedata
        fields =['wellid','date', 'liquidrate', 'watercut', 'gasoilratio' ]

        
    