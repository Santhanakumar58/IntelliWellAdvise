from django import forms
from .models import GPDeviationsurveydata


class GPDeviationSurveyDataForm(forms.ModelForm):   
    class Meta:
        model = GPDeviationsurveydata
        fields =['gpmeasuredDepth', 'gpangle', 'gpazimuth']
        