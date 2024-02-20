from .models import WIFormatioPressureModel
from django import forms

class WIFormationPressureForm(forms.ModelForm):  
    class Meta:        
        model = WIFormatioPressureModel
        fields =["wistat_Group" , "wistat_Formation" , "wistat_Member" , "wimeasured_Depth", "wipressure" ,
                "wiporosity",  "wipermeability" , "witemperature", "wiremarks"  ]

