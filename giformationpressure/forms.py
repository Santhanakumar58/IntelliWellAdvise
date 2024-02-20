from .models import GIFormatioPressureModel
from django import forms

class GIFormationPressureForm(forms.ModelForm):  
    class Meta:        
        model = GIFormatioPressureModel
        fields =["gistat_Group" , "gistat_Formation" , "gistat_Member" , "gimeasured_Depth", "gipressure" ,
                "giporosity",  "gipermeability" , "gitemperature", "giremarks"  ]

