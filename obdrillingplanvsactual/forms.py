from .models import OBDrillingPlanVsActual
from django import forms


class OBDrillingPlanForm(forms.ModelForm):
    class Meta:        
        model = OBDrillingPlanVsActual
        fields =['obsection','obsection_Depth_Plan', 'obplan_Days', 
        'obsection_Depth_Actual', 'obactual_Days', 'obreason_for_Deviation'
         ]
