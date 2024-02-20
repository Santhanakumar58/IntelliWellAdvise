from .models import GPFormatioPressureModel
from django import forms

class GPFormationPressureForm(forms.ModelForm):  
    class Meta:        
        model = GPFormatioPressureModel
        fields =["gpstat_Group" , "gpstat_Formation" , "gpstat_Member" , "gpmeasured_Depth", "gppressure" ,
                "gpporosity",  "gppermeability" , "gptemperature", "gpremarks"  ]

