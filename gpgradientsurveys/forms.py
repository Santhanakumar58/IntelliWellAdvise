from django import forms
from .models import GPGradientSurvey
    
class GPGradientSurveyForm(forms.ModelForm):
    gpsurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPGradientSurvey
        fields =['gpsurvey_Date', 'gpsurvey_Type', 'gpshutin_Period', 'gptubinghead_Pressure', 'gptubinghead_Temperature', 
                 'gpliquid_Rate', 'gpwater_Cut', 'gpgas_Oil_Ratio']

     