from django import forms
from .models import GasLiftModel


class GasLiftForm(forms.ModelForm):   
    design_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GasLiftModel
        fields =['design_Date','design_Liquid','water_Cut', 'th_Pres', 'th_Temp',
                'gas_Inj_Pres', 'kick_Off_Pres','kill_Fluid_Grad', 'port_Size',
                'min_Valve_Sapcing',  'available_Gas'   
        ]
        