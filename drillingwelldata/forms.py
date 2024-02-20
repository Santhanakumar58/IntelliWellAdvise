from django import forms
from .models import DrillingWellData


class DrillingWellDataForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = DrillingWellData
        fields =['survey_Date','rkb_to_WH','rkb_to_GL','gl_to_MSL','rkb_to_MSL','wh_to_MSL', 'lattitude', 'longitude', 'total_Measured_Depth', 'total_True_Vertical_Depth', 'afe_No']