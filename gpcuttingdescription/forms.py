from .models import GPCuttingDescriptionModel
from django import forms

class GPCuttingDescriptionForm(forms.ModelForm):  
    class Meta:        
        model = GPCuttingDescriptionModel
        fields =["gphole_Size" , "gptop_Depth" , "gpbottom_Depth" , "gplitho_1", "gplitho1_Composition" ,
                "gplitho_2",  "gplitho2_Composition" , "gplitho_3", "gplitho3_Composition" , "gpdescription" , "gpremarks"  ]

