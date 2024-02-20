from django import forms
from .models import ConstantPressureDrawdowntest
    
class ConstantPressureDrawdownTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = ConstantPressureDrawdowntest
        fields =['survey_Date', 'gauge_Depth', 'layer_Porosity', 'layer_Thickness',  'wellbore_Radius','total_Compressibility', 'initial_Res_Pres', 'oil_Viscosity', 'oil_FVF', 'file_Name', 'pwf']



     