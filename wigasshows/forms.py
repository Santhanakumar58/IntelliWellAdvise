from .models import WIGasShowModel
from django import forms

class WIGasShowForm(forms.ModelForm):  
    class Meta:        
        model = WIGasShowModel
        fields =["wiformation" , "witop_MD" , "wibottom_MD" , "witotal_Gas", "wimethane" ,
                "wiethane",  "wipropane" , "wiiso_Butane", "wineo_Butane" , "wiiso_Pentane", "wineo_Pentane", "wiremarks" ]

