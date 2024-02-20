from django import forms
from .models import OBCementBondLogModel


class OBCementBondLogForm(forms.ModelForm):
    obrecorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = OBCementBondLogModel
        fields =['obcasingSize', 'obanalyst', 'obrecorded_date', 'obinterpretation', 'obcblImage']