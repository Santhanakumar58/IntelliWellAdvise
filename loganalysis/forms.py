from django import forms
from .models import LogAnalysisModel


class LogAnalysisForm(forms.ModelForm):
    recorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = LogAnalysisModel
        fields =['casingSize', 'analyst', 'recorded_date', 'interpretation', 'logImage', 'remarks', 'file_type', 'file_Name']