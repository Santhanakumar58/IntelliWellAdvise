from django import forms
from .models import GPCementPlug, GPPumpingData


class GPCementPlugForm(forms.ModelForm):   
    gpplug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPCementPlug
        fields =['gpplug_Date','gpplug_Top', 'gpplug_Bottom', 'gpcement_Density', 'gpcement_Volume','gpplug_Description']

class GPPumpDataForm(forms.ModelForm):   
    gppump_Time = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:
        model = GPPumpingData
        fields =['gppump_Time', 'gppump_Fluid','gppump_Fluid_Density', 'gppump_Pressure','gppump_Rate']        