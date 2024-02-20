from .models import GPDrillingPlanVsActual
from django import forms


class GPDrillingPlanForm(forms.ModelForm):
    class Meta:        
        model = GPDrillingPlanVsActual
        fields =['gpsection','gpsection_Depth_Plan', 'gpplan_Days', 
        'gpsection_Depth_Actual', 'gpactual_Days', 'gpreason_for_Deviation'
         ]
