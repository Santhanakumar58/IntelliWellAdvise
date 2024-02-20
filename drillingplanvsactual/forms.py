from .models import DrillingPlanVsActual
from django import forms


class DrillingPlanForm(forms.ModelForm):
    class Meta:        
        model = DrillingPlanVsActual
        fields =['section','section_Depth_Plan', 'plan_Days', 
        'section_Depth_Actual', 'actual_Days', 'reason_for_Deviation'
         ]
