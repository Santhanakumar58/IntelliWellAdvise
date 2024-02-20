from django import forms
from .models import BridgePlug


class BridgePlugForm(forms.ModelForm):   
    plug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = BridgePlug
        fields =['plug_Date','plug_type', 'plug_Depth', 'casing_Size', 'plug_OD','setting_range_ppf','setting_mechanism',
                 'plug_Make','plug_Model', 'Pressure_rating','Temperature_rating' , 'plug_setting_Problems']