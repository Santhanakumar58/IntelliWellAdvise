from django import forms
from .models import SelectedWaterInjector


class SelectedWaterInjectorForm(forms.ModelForm):
    class Meta:
        model = SelectedWaterInjector
        fields =['fgid','unit','wellid','wellname','completion','deviation','inflow','station','header']