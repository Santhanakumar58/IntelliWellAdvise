from django import forms
from .models import OBLogAnalysisModel


class OBLogAnalysisForm(forms.ModelForm):
    obrecorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = OBLogAnalysisModel
        fields =['obcasingSize', 'obanalyst', 'obrecorded_date', 'obinterpretation', 'oblogImage', 'obremarks', 'obfile_type', 'obfile_Name']