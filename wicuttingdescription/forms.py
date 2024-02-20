from .models import WICuttingDescriptionModel
from django import forms

class WICuttingDescriptionForm(forms.ModelForm):  
    class Meta:        
        model = WICuttingDescriptionModel
        fields =["wihole_Size" , "witop_Depth" , "wibottom_Depth" , "wilitho_1", "wilitho1_Composition" ,
                "wilitho_2",  "wilitho2_Composition" , "wilitho_3", "wilitho3_Composition" , "widescription" , "wiremarks"  ]

