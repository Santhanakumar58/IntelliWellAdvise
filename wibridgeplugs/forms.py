from django import forms
from .models import WIBridgePlug


class WIBridgePlugForm(forms.ModelForm):   
    wiplug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = WIBridgePlug
        fields =['wiplug_Date','wiplug_type', 'wiplug_Depth', 'wicasing_Size', 'wiplug_OD','wisetting_range_ppf','wisetting_mechanism',
                 'wiplug_Make','wiplug_Model', 'wiPressure_rating','wiTemperature_rating' , 'wiplug_setting_Problems']