from django import forms
from .models import DrillingSummary


class DrillingSummaryForm(forms.ModelForm):
    start_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    end_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = DrillingSummary
        fields =['start_Date','end_Date','liquid_Rate','water_Cut','gas_Oil_Ratio', 'drilling_Summary']