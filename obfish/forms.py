from django import forms
from .models import OBFishModel


class OBFishForm(forms.ModelForm):   
    obfish_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = OBFishModel
        fields =['obfish_Date','obfish_Top', 'obfish_Bottom', 'obfish_Nature', 'obfish_Description']
        