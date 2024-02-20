from django import forms
from .models import GradientSurvey
    
class GradientSurveyForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GradientSurvey
        fields =['survey_Date', 'survey_Type', 'shutin_Period', 'tubinghead_Pressure', 'tubinghead_Temperature', 'liquid_Rate', 'water_Cut', 'gas_Oil_Ratio']

     