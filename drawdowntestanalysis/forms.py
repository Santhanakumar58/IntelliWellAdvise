from django import forms
from .models import Drawdowntest
    
class DrawdownTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = Drawdowntest
        fields =['survey_Date', 'gauge_Depth', 'layer_Porosity', 'layer_Thickness',  'wellbore_Radius','total_Compressibility', 'initial_Res_Pres', 'fbhp', 'oil_Viscosity', 'oil_FVF', 'liquid_Rate', 'pvt_Well', 'test_Type', 'file_Name']

class DrawdownTestUploadForm(forms.ModelForm):   
    class Meta:        
        model = Drawdowntest
        fields =['liquid_Rate', 'guess_Value', 'fbhp']

     