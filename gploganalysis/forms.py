from django import forms
from .models import GPLogAnalysisModel


class GPLogAnalysisForm(forms.ModelForm):
    gprecorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPLogAnalysisModel
        fields =['gpcasingSize', 'gpanalyst', 'gprecorded_date', 'gpinterpretation', 'gplogImage', 'gpremarks', 'gpfile_type', 'gpfile_Name']