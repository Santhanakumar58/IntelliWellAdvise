from django import forms
from .models import CCEPVT 
    
class CCEPVTForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = CCEPVT 
        fields =["date", "wellName", "sampleId", "temperature"]
