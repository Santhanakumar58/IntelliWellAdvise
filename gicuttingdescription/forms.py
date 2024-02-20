from .models import GICuttingDescriptionModel
from django import forms

class GICuttingDescriptionForm(forms.ModelForm):  
    class Meta:        
        model = GICuttingDescriptionModel
        fields =["gihole_Size" , "gitop_Depth" , "gibottom_Depth" , "gilitho_1", "gilitho1_Composition" ,
                "gilitho_2",  "gilitho2_Composition" , "gilitho_3", "gilitho3_Composition" , "gidescription" , "giremarks"  ]

