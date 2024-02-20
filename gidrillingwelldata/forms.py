from django import forms
from .models import GIDrillingWellData


class GIDrillingWellDataForm(forms.ModelForm):
    gisurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIDrillingWellData
        fields =['gisurvey_Date','girkb_to_WH','girkb_to_GL','gigl_to_MSL','girkb_to_MSL','giwh_to_MSL', 'gilattitude', 'gilongitude', 
                 'gitotal_Measured_Depth', 'gitotal_True_Vertical_Depth', 'giafe_No']