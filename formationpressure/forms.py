from .models import FormatioPressureModel
from django import forms

class FormationPressureForm(forms.ModelForm):  
    class Meta:        
        model = FormatioPressureModel
        fields =["stat_Group" , "stat_Formation" , "stat_Member" , "measured_Depth", "pressure" ,
                "porosity",  "permeability" , "temperature", "remarks"  ]

