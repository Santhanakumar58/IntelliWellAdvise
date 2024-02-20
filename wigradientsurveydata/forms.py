from django import forms
from .models import WIGradientSurveyData
    
class WIGradientSurveyDataForm(forms.ModelForm):    
    class Meta:        
        model = WIGradientSurveyData
        fields =['wigradientsurvey', 'wigauge_Depth', 'wigauge_Pressure', 'wigauge_Temperature']

     