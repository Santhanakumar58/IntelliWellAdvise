from django import forms
from .models import GICementPlug, GIPumpingData


class GICementPlugForm(forms.ModelForm):   
    giplug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GICementPlug
        fields =['giplug_Date','giplug_Top', 'giplug_Bottom', 'gicement_Density', 'gicement_Volume','giplug_Description']

class GIPumpDataForm(forms.ModelForm):   
    gipump_Time = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:
        model = GIPumpingData
        fields =['gipump_Time', 'gipump_Fluid','gipump_Fluid_Density', 'gipump_Pressure','gipump_Rate']        