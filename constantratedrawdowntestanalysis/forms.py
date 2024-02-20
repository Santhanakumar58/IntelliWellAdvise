from django import forms
from .models import ConstantRateDrawdowntestModel
    
class ConstantRateDrawdownTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = ConstantRateDrawdowntestModel
        fields =['survey_Date', 'gauge_Depth', 'layer_Porosity', 'layer_Thickness',  'wellbore_Radius','total_Compressibility', 'initial_Res_Pres', 'fbhp', 'oil_Viscosity', 'oil_FVF', 'liquid_Rate', 'file_Name']

class ConstantRateDrawdownTestUploadForm(forms.ModelForm):   
    class Meta:        
        model = ConstantRateDrawdowntestModel
        fields =['liquid_Rate', 'guess_Value', 'fbhp']

     