from django import forms
from .models import ESPDesignModel


class ESPDesignForm(forms.ModelForm):   
    design_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    
    class Meta:
        model = ESPDesignModel
        fields =['design_Date','design_Liquid', 'water_Cut', 'water_Salinity','th_Pres', 'th_Temp',
                'curr_Res_Pres','min_Pwf', 'gas_Oil_Ratio', 'water_spgr', 'pvt_Well', 'gas_Separator', 'gas_Separator_Efficiency','pump_depth', 
                'pump', 'motor'       
        ]
        