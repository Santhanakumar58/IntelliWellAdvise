from django import forms
from .models import SelectedGasInjector


class SelectedGasInjectorForm(forms.ModelForm):
    class Meta:
        model = SelectedGasInjector
        fields =['fgid','unit','wellid','wellname','completion','deviation','inflow','station','header']