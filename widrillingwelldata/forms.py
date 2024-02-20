from django import forms
from .models import WIDrillingWellData


class WIDrillingWellDataForm(forms.ModelForm):
    wisurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = WIDrillingWellData
        fields =['wisurvey_Date','wirkb_to_WH','wirkb_to_GL','wigl_to_MSL','wirkb_to_MSL','wiwh_to_MSL', 'wilattitude', 'wilongitude', 
                 'witotal_Measured_Depth', 'witotal_True_Vertical_Depth', 'wiafe_No']