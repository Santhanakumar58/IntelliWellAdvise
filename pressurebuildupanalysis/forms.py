from .models import PressureBuildupDataUploadModel, PressureBuildupModel
from django import forms
    
class BuildupTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = PressureBuildupModel
        fields =['survey_Date', 'gauge_Depth', 'layer_Thickness', 'layer_Porosity', 'total_Compressibility', 'mu_oil','oil_FVF' ,'wellbore_Radius', 'oil_Prod_Rate', 'water_Cut', 't_since_shutin', 'pvt_Well', 'test_Type', 'guess_Value', 'dataFile']

class PressureBuildupDataUploadForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = PressureBuildupDataUploadModel
        fields =['survey_Date', 'time', 'elapsedtime', 'gauge_pressure']

class BuildupTestUploadForm(forms.ModelForm):   
    class Meta:        
        model = PressureBuildupModel
        fields =['oil_Prod_Rate', 'guess_Value', 't_since_shutin']