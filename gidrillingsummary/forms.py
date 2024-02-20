from django import forms
from .models import GIDrillingSummary


class DrillingSummaryForm(forms.ModelForm):
    gistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    giend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIDrillingSummary
        fields =['gistart_Date','giend_Date','giliquid_Rate','giwater_Cut','gigas_Oil_Ratio', 'gidrilling_Summary']