from django import forms
from .models import GIBridgePlug


class GIBridgePlugForm(forms.ModelForm):   
    giplug_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIBridgePlug
        fields =['giplug_Date','giplug_type', 'giplug_Depth', 'gicasing_Size', 'giplug_OD','gisetting_range_ppf','gisetting_mechanism',
                 'giplug_Make','giplug_Model', 'giPressure_rating','giTemperature_rating' , 'giplug_setting_Problems']