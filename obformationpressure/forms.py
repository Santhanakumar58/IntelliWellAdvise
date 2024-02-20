from .models import OBFormatioPressureModel
from django import forms

class OBFormationPressureForm(forms.ModelForm):  
    class Meta:        
        model = OBFormatioPressureModel
        fields =["obstat_Group" , "obstat_Formation" , "obstat_Member" , "obmeasured_Depth", "obpressure" ,
                "obporosity",  "obpermeability" , "obtemperature", "obremarks"  ]

