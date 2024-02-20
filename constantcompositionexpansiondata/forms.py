from django import forms
from .models import CCEPVTData 


class CCEPVTDATAForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = CCEPVTData
        fields=["pressure", "relative_volume", "y_function","density"]

     