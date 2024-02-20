from django import forms
from .models import WIPerforationModel


class WIPerforationForm(forms.ModelForm):
    wiperf_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = WIPerforationModel
        fields =['wiperf_Date', 'wiperf_Top', 'wiperf_Bottom', 'wiperf_Condition', 'wiconveyance_Method', 'wiperf_Gun_Type', 
                 'wiperf_Gun_Size', 'wiperf_Gun_Density', 'wiperf_Charges', 'wiremarks']