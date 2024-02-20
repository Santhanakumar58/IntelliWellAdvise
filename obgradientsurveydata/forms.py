from django import forms
from .models import OBGradientSurveyData
    
class OBGradientSurveyDataForm(forms.ModelForm):    
    class Meta:        
        model = OBGradientSurveyData
        fields =['obgradientsurvey', 'obgauge_Depth', 'obgauge_Pressure', 'obgauge_Temperature']

     