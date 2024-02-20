from .models import GPFormatioTopsModel
from django import forms

class GPFormationTopsForm(forms.ModelForm):  
    class Meta:        
        model = GPFormatioTopsModel
        fields =["gphole_Size" , "gpstat_Group", "gpstat_Formation" , "gpstat_Member", "gpprognosis_Thickness", "gpprognosis_Top", "gpactual_Top", "gpactual_Thickness", "gpremarks"  ]

