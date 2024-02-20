from django import forms
from .models import GIPerforationModel


class GIPerforationForm(forms.ModelForm):
    giperf_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIPerforationModel
        fields =['giperf_Date', 'giperf_Top', 'giperf_Bottom', 'giperf_Condition', 'giconveyance_Method', 'giperf_Gun_Type', 
                 'giperf_Gun_Size', 'giperf_Gun_Density', 'giperf_Charges', 'giremarks']