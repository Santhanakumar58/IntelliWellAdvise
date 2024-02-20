from django import forms
from .models import WICementPlug, WIPumpingData


class WICementPlugForm(forms.ModelForm):   
    wiplug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = WICementPlug
        fields =['wiplug_Date','wiplug_Top', 'wiplug_Bottom', 'wicement_Density', 'wicement_Volume','wiplug_Description']

class WIPumpDataForm(forms.ModelForm):   
    wipump_Time = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:
        model = WIPumpingData
        fields =['wipump_Time', 'wipump_Fluid','wipump_Fluid_Density', 'wipump_Pressure','wipump_Rate']        