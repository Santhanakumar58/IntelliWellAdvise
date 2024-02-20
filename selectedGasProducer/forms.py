from django import forms
from .models import SelectedGasProducer


class SelectedGasProducerForm(forms.ModelForm):
    class Meta:
        model = SelectedGasProducer
        fields =['fgid','unit','wellid','wellname','completion','deviation','inflow','station','header']