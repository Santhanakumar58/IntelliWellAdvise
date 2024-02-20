from django import forms
from .models import GIGradientSurvey
    
class GIGradientSurveyForm(forms.ModelForm):
    gisurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GIGradientSurvey
        fields =['gisurvey_Date', 'gisurvey_Type', 'gishutin_Period', 'gitubinghead_Pressure', 'gitubinghead_Temperature', 'giliquid_Rate', 'giwater_Cut', 'gigas_Oil_Ratio']

     