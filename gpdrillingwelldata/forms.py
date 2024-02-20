from django import forms
from .models import GPDrillingWellData


class GPDrillingWellDataForm(forms.ModelForm):
    gpsurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPDrillingWellData
        fields =['gpsurvey_Date','gprkb_to_WH','gprkb_to_GL','gpgl_to_MSL','gprkb_to_MSL','gpwh_to_MSL', 'gplattitude', 'gplongitude', 
                 'gptotal_Measured_Depth', 'gptotal_True_Vertical_Depth', 'gpafe_No']