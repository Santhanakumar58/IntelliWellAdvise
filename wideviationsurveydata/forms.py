from django import forms
from .models import WIDeviationsurveydata


class WIDeviationSurveyDataForm(forms.ModelForm):   
    class Meta:
        model = WIDeviationsurveydata
        fields =['wimeasuredDepth', 'wiangle', 'wiazimuth']
        