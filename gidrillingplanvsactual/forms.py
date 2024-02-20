from .models import GIDrillingPlanVsActual
from django import forms


class GIDrillingPlanForm(forms.ModelForm):
    class Meta:        
        model = GIDrillingPlanVsActual
        fields =['gisection','gisection_Depth_Plan', 'giplan_Days', 
        'gisection_Depth_Actual', 'giactual_Days', 'gireason_for_Deviation'
         ]
