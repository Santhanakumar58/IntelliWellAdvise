from django import forms
from .models import Layer


class VolumetricForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = Layer        
        fields = '__all__'
   