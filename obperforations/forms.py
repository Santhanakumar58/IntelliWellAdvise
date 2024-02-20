from django import forms
from .models import OBPerforationModel


class OBPerforationForm(forms.ModelForm):
    obperf_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = OBPerforationModel
        fields =['obperf_Date', 'obperf_Top', 'obperf_Bottom', 'obperf_Condition', 'obconveyance_Method', 'obperf_Gun_Type', 
                 'obperf_Gun_Size', 'obperf_Gun_Density', 'obperf_Charges', 'obremarks']