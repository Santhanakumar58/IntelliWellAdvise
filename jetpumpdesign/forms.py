from .models import JetPumpDesignModel
from django import forms


class JetPumpDesignForm(forms.ModelForm):   
    design_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    
    class Meta:
        model = JetPumpDesignModel
        fields =['design_Date','design_Liquid', 'water_Cut', 'water_Spgr','th_Pres', 'th_Temp',
                'curr_Res_Pres','min_Pwf', 'gas_Oil_Ratio', 'pvt_Well', 'pump_depth'
                    
        ]
        