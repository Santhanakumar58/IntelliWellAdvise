from django import forms
from .models import SelectedOilProducer


class SelectedOilProducerForm(forms.ModelForm):
    class Meta:
        model = SelectedOilProducer
        fields =['fgid','unit','wellid','wellname','completion','deviation','artificiallift','inflow','station','header']