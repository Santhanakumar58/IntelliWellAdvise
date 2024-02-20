from django import forms
from .models import OBCementPlug, OBPumpingData


class OBCementPlugForm(forms.ModelForm):   
    obplug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = OBCementPlug
        fields =['obplug_Date','obplug_Top', 'obplug_Bottom', 'obcement_Density', 'obcement_Volume','obplug_Description']

class OBPumpDataForm(forms.ModelForm):   
    obpump_Time = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:
        model = OBPumpingData
        fields =['obpump_Time', 'obpump_Fluid','obpump_Fluid_Density', 'obpump_Pressure','obpump_Rate']        