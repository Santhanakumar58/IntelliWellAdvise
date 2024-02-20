from django import forms
from .models import Deviationsurveydata


class DeviationSurveyDataForm(forms.ModelForm):   
    class Meta:
        model = Deviationsurveydata
        fields =['measuredDepth', 'angle', 'azimuth']
        