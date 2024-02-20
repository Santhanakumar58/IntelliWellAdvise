from django import forms
from .models import WIFishModel


class WIFishForm(forms.ModelForm):   
    wifish_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = WIFishModel
        fields =['wifish_Date','wifish_Top', 'wifish_Bottom', 'wifish_Nature', 'wifish_Description']
        