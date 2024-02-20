from .models import OBFormatioTopsModel
from django import forms

class OBFormationTopsForm(forms.ModelForm):  
    class Meta:        
        model = OBFormatioTopsModel
        fields =["obhole_Size" , "obstat_Group", "obstat_Formation" , "obstat_Member", "obprognosis_Thickness", "obprognosis_Top", "obactual_Top", "obactual_Thickness", "obremarks"  ]

