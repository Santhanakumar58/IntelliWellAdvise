from django import forms
from .models import CementPlug, PumpingData


class CementPlugForm(forms.ModelForm):   
    plug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = CementPlug
        fields =['plug_Date','plug_Top', 'plug_Bottom', 'cement_Density', 'cement_Volume','plug_Description']

class PumpDataForm(forms.ModelForm):   
    pump_Time = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:
        model = PumpingData
        fields =['pump_Time', 'pump_Fluid','pump_Fluid_Density', 'pump_Pressure','pump_Rate']        