from django import forms
from .models import PressuredropCalculationModel

class PressureDropCalcForm(forms.ModelForm):   
    model_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = PressuredropCalculationModel
        fields =['model_Date','source_Pressure', 'source_Flowrate', 'source_Temp', 'pipe_Angle','pipe_Length', 'pipe_Diam',
        'fluid_API', 'fluid_WaterCut', 'fluid_GOR', 'fluid_gas_spgr']