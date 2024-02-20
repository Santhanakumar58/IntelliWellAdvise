from django import forms
from .models import OBWellobjectivedata
    
class OBWellObjectivedataForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBWellobjectivedata
        fields =['obwellid','date', 'perf_Depth', 'res_pressure', 'well_type' ]
