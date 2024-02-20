from django import forms
from .models import GIFishModel


class GIFishForm(forms.ModelForm):   
    gifish_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIFishModel
        fields =['gifish_Date','gifish_Top', 'gifish_Bottom', 'gifish_Nature', 'gifish_Description']
        