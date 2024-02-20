from django import forms
from .models import GPDrillingSummary


class DrillingSummaryForm(forms.ModelForm):
    gpstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gpend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPDrillingSummary
        fields =['gpstart_Date','gpend_Date','gpliquid_Rate','gpwater_Cut','gpgas_Oil_Ratio', 'gpdrilling_Summary']