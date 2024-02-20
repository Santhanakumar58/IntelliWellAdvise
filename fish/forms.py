from django import forms
from .models import FishModel


class FishForm(forms.ModelForm):   
    fish_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = FishModel
        fields =['fish_Date','fish_Top', 'fish_Bottom', 'fish_Nature', 'fish_Description']
        