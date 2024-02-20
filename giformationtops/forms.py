from .models import GIFormatioTopsModel
from django import forms

class GIFormationTopsForm(forms.ModelForm):  
    class Meta:        
        model = GIFormatioTopsModel
        fields =["gihole_Size" , "gistat_Group", "gistat_Formation" , "gistat_Member", "giprognosis_Thickness", "giprognosis_Top", "giactual_Top", "giactual_Thickness", "giremarks"  ]

