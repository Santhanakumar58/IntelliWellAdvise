from django import forms
from .models import MultiRateDrawdowntest
    
class MultiRateDrawdownTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = MultiRateDrawdowntest
        fields =['survey_Date', 'gauge_Depth', 'layer_Porosity', 'layer_Thickness',  'wellbore_Radius','total_Compressibility', 'initial_Res_Pres', 'oil_Viscosity', 'oil_FVF', 'file_Name' ]



class MultiRateDrawdownTestUploadForm(forms.ModelForm):    
    class Meta:        
        model = MultiRateDrawdowntest
        fields =['time1', 'pressure1', 'time2', 'pressure2',  'time3','pressure3']


   