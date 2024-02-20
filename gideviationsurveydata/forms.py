from django import forms
from .models import GIDeviationsurveydata


class GIDeviationSurveyDataForm(forms.ModelForm):   
    class Meta:
        model = GIDeviationsurveydata
        fields =['gimeasuredDepth', 'giangle', 'giazimuth']
        