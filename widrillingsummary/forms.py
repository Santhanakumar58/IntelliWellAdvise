from django import forms
from .models import WIDrillingSummary


class WIDrillingSummaryForm(forms.ModelForm):
    wistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    wiend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = WIDrillingSummary
        fields =['wistart_Date','wiend_Date','wiliquid_Rate','wiwater_Cut','wigas_Oil_Ratio', 'widrilling_Summary']