from .models import OBGasShowModel
from django import forms

class OBGasShowForm(forms.ModelForm):  
    class Meta:        
        model = OBGasShowModel
        fields =["obformation" , "obtop_MD" , "obbottom_MD" , "obtotal_Gas", "obmethane" ,
                "obethane",  "obpropane" , "obiso_Butane", "obneo_Butane" , "obiso_Pentane", "obneo_Pentane", "obremarks" ]

