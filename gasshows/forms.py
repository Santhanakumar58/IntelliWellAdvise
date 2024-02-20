from .models import GasShowModel
from django import forms

class GasShowForm(forms.ModelForm):  
    class Meta:        
        model = GasShowModel
        fields =["formation" , "top_MD" , "bottom_MD" , "total_Gas", "methane" ,
                "ethane",  "propane" , "iso_Butane", "neo_Butane" , "iso_Pentane", "neo_Pentane", "remarks" ]

