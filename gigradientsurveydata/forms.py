from django import forms
from .models import GIGradientSurveyData
    
class GIGradientSurveyDataForm(forms.ModelForm):    
    class Meta:        
        model = GIGradientSurveyData
        fields =['gigradientsurvey', 'gigauge_Depth', 'gigauge_Pressure', 'gigauge_Temperature']

     