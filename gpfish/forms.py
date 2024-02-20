from django import forms
from .models import GPFishModel


class GPFishForm(forms.ModelForm):   
    gpfish_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPFishModel
        fields =['gpfish_Date','gpfish_Top', 'gpfish_Bottom', 'gpfish_Nature', 'gpfish_Description']
        