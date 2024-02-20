from django import forms
from .models import OBBridgePlug


class OBBridgePlugForm(forms.ModelForm):   
    obplug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = OBBridgePlug
        fields =['obplug_Date','obplug_type', 'obplug_Depth', 'obcasing_Size', 'obplug_OD','obsetting_range_ppf','obsetting_mechanism',
                 'obplug_Make','obplug_Model', 'obPressure_rating','obTemperature_rating' , 'obplug_setting_Problems']