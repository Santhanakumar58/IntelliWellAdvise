from django import forms
from .models import SRPDesignModel


class SRPDesignForm(forms.ModelForm):   
    design_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    
    class Meta:
        model = SRPDesignModel
        fields =['design_Date','design_Liquid', 'water_Cut','gas_Oil_Ratio', 'water_spgr','th_Pres', 'th_Temp',
                'curr_Res_Pres','min_Pwf', 'pvt_Well', 'pump_Depth','fluid_Level', 'pumping_Speed' , 'surface_Stroke_Length',
                'rod_No','plunger_Dia', 'anchored' , 'pvt_Well'      
        ]
        