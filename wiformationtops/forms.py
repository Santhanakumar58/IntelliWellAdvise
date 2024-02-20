from .models import WIFormatioTopsModel
from django import forms

class WIFormationTopsForm(forms.ModelForm):  
    class Meta:        
        model = WIFormatioTopsModel
        fields =["wihole_Size" , "wistat_Group", "wistat_Formation" , "wistat_Member", "wiprognosis_Thickness", 
                 "wiprognosis_Top", "wiactual_Top", "wiactual_Thickness", "wiremarks"  ]


