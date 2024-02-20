from django import forms
from .models import CementBondLogModel


class CementBondLogForm(forms.ModelForm):
    recorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = CementBondLogModel
        fields =['casingSize', 'analyst', 'recorded_date', 'interpretation', 'cblImage']