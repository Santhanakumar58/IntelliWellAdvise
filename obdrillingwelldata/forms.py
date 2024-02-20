from django import forms
from .models import OBDrillingWellData


class OBDrillingWellDataForm(forms.ModelForm):
    obsurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = OBDrillingWellData
        fields =['obsurvey_Date','obrkb_to_WH','obrkb_to_GL','obgl_to_MSL','obrkb_to_MSL','obwh_to_MSL', 'oblattitude', 'oblongitude', 
                 'obtotal_Measured_Depth', 'obtotal_True_Vertical_Depth', 'obafe_No']