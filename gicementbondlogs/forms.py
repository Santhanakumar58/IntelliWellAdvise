from django import forms
from .models import GICementBondLogModel


class GICementBondLogForm(forms.ModelForm):
    girecorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GICementBondLogModel
        fields =['gicasingSize', 'gianalyst', 'girecorded_date', 'giinterpretation', 'gicblImage']