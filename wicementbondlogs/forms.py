from django import forms
from .models import WICementBondLogModel


class WICementBondLogForm(forms.ModelForm):
    wirecorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = WICementBondLogModel
        fields =['wicasingSize', 'wianalyst', 'wirecorded_date', 'wiinterpretation', 'wicblImage']