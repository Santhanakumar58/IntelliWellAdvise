from django import forms
from .models import GPCementBondLogModel


class GPCementBondLogForm(forms.ModelForm):
    gprecorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPCementBondLogModel
        fields =['gpcasingSize', 'gpanalyst', 'gprecorded_date', 'gpinterpretation', 'gpcblImage']