from django import forms
from .models import WILogAnalysisModel


class WILogAnalysisForm(forms.ModelForm):
    wirecorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = WILogAnalysisModel
        fields =['wicasingSize', 'wianalyst', 'wirecorded_date', 'wiinterpretation', 'wilogImage', 'wiremarks', 'wifile_type', 'wifile_Name']