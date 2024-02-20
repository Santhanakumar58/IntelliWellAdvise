from django import forms
from .models import GradientSurveyData
    
class GradientSurveyDataForm(forms.ModelForm):    
    class Meta:        
        model = GradientSurveyData
        fields =['gradientsurvey', 'gauge_Depth', 'gauge_Pressure', 'gauge_Temperature']

     