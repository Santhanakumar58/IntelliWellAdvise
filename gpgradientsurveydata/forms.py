from django import forms
from .models import GPGradientSurveyData
    
class GPGradientSurveyDataForm(forms.ModelForm):    
    class Meta:        
        model = GPGradientSurveyData
        fields =['gpgradientsurvey', 'gpgauge_Depth', 'gpgauge_Pressure', 'gpgauge_Temperature']

     