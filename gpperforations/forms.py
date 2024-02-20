from django import forms
from .models import GPPerforationModel


class GPPerforationForm(forms.ModelForm):
    gpperf_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPPerforationModel
        fields =['gpperf_Date', 'gpperf_Top', 'gpperf_Bottom', 'gpperf_Condition', 'gpconveyance_Method', 'gpperf_Gun_Type', 
                 'gpperf_Gun_Size', 'gpperf_Gun_Density', 'gpperf_Charges', 'gpremarks']