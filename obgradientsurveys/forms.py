from django import forms
from .models import OBGradientSurvey
    
class OBGradientSurveyForm(forms.ModelForm):
    obsurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBGradientSurvey
        fields =['obsurvey_Date', 'obsurvey_Type', 'obshutin_Period', 'obtubinghead_Pressure', 'obtubinghead_Temperature', 'obliquid_Rate', 'obwater_Cut', 'obgas_Oil_Ratio']

     