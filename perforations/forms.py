from django import forms
from .models import PerforationModel


class PerforationForm(forms.ModelForm):
    perf_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = PerforationModel
        fields =['perf_Date', 'perf_Top', 'perf_Bottom', 'perf_Condition', 'conveyance_Method', 'perf_Gun_Type', 'perf_Gun_Size', 'perf_Gun_Density', 'perf_Charges', 'remarks']