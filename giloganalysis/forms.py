from django import forms
from .models import GILogAnalysisModel


class GILogAnalysisForm(forms.ModelForm):
    girecorded_date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GILogAnalysisModel
        fields =['gicasingSize', 'gianalyst', 'girecorded_date', 'giinterpretation', 'gilogImage', 'giremarks', 'gifile_type', 'gifile_Name']