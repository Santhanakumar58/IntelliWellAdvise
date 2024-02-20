from django import forms
from .models import OBDeviationsurveydata


class OBDeviationSurveyDataForm(forms.ModelForm):   
    class Meta:
        model = OBDeviationsurveydata
        fields =['obmeasuredDepth', 'obangle', 'obazimuth']
        