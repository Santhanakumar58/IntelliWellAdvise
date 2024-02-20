from .models import FormatioTopsModel
from django import forms

class FormationTopsForm(forms.ModelForm):  
    class Meta:        
        model = FormatioTopsModel
        fields =["hole_Size" , "stat_Group", "stat_Formation" , "stat_Member", "prognosis_Thickness", "prognosis_Top", "actual_Top", "actual_Thickness", "remarks"  ]

