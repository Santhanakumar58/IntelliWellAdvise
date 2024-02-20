from django import forms
from .models import OBDrillingSummary


class DrillingSummaryForm(forms.ModelForm):
    obstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    obend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = OBDrillingSummary
        fields =['obstart_Date','obend_Date','obliquid_Rate','obwater_Cut','obgas_Oil_Ratio', 'obdrilling_Summary']