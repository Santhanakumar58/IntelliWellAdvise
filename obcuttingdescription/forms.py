from .models import OBCuttingDescriptionModel
from django import forms

class OBCuttingDescriptionForm(forms.ModelForm):  
    class Meta:        
        model = OBCuttingDescriptionModel
        fields =["obhole_Size" , "obtop_Depth" , "obbottom_Depth" , "oblitho_1", "oblitho1_Composition" ,
                "oblitho_2",  "oblitho2_Composition" , "oblitho_3", "oblitho3_Composition" , "obdescription" , "obremarks"  ]

