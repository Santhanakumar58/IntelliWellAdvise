from django import forms
from .models import SelectedObserver


class SelectedObserverForm(forms.ModelForm):
    class Meta:
        model = SelectedObserver
        fields =['fgid','unit','wellid','wellname','completion','deviation','inflow','station','header']