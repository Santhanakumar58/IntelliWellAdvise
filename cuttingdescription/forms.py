from .models import CuttingDescriptionModel
from django import forms

class CuttingDescriptionForm(forms.ModelForm):  
    class Meta:        
        model = CuttingDescriptionModel
        fields =["hole_Size" , "top_Depth" , "bottom_Depth" , "litho_1", "litho1_Composition" ,
                "litho_2",  "litho2_Composition" , "litho_3", "litho3_Composition" , "description" , "remarks"  ]

