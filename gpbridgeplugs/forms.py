from django import forms
from .models import GPBridgePlug


class GPBridgePlugForm(forms.ModelForm):   
    gpplug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPBridgePlug
        fields =['gpplug_Date','gpplug_type', 'gpplug_Depth', 'gpcasing_Size', 'gpplug_OD','gpsetting_range_ppf','gpsetting_mechanism',
                 'gpplug_Make','gpplug_Model', 'gpPressure_rating','gpTemperature_rating' , 'gpplug_setting_Problems']