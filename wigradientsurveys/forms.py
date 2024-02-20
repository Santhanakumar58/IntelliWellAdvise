from django import forms
from .models import WIGradientSurvey
    
class WIGradientSurveyForm(forms.ModelForm):
    wisurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WIGradientSurvey
        fields =['wisurvey_Date', 'wisurvey_Type', 'wishutin_Period', 'witubinghead_Pressure', 'witubinghead_Temperature', 'wiliquid_Rate', 'wiwater_Cut', 'wigas_Oil_Ratio']

     