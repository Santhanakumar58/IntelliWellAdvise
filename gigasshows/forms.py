from .models import GIGasShowModel
from django import forms

class GIGasShowForm(forms.ModelForm):  
    class Meta:        
        model = GIGasShowModel
        fields =["giformation" , "gitop_MD" , "gibottom_MD" , "gitotal_Gas", "gimethane" ,
                "giethane",  "gipropane" , "giiso_Butane", "gineo_Butane" , "giiso_Pentane", "gineo_Pentane", "giremarks" ]

