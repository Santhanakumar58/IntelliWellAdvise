from .models import WIDrillingPlanVsActual
from django import forms


class WIDrillingPlanForm(forms.ModelForm):
    class Meta:        
        model = WIDrillingPlanVsActual
        fields =['wisection','wisection_Depth_Plan', 'wiplan_Days', 
        'wisection_Depth_Actual', 'wiactual_Days', 'wireason_for_Deviation'
         ]
