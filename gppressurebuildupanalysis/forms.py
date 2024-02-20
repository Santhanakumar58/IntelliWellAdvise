from .models import GPPressureBuildupDataUploadModel, GPPressureBuildupModel
from django import forms
    
class GPBuildupTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPPressureBuildupModel
        fields =['gpsurvey_Date', 'gpgauge_Depth', 'gplayer_Thickness', 'gplayer_Porosity', 'gptotal_Compressibility', 'gpmu_oil',
                 'gpoil_FVF' ,'gpwellbore_Radius', 'gpoil_Prod_Rate', 'gpwater_Cut', 'gpt_since_shutin', 'gppvt_Well', 'gptest_Type', 
                 'gpguess_Value', 'gpdataFile']

class GPPressureBuildupDataUploadForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPPressureBuildupDataUploadModel
        fields =['gpsurvey_Date', 'gptime', 'gpelapsedtime', 'gpgauge_pressure']

class GPBuildupTestUploadForm(forms.ModelForm):   
    class Meta:        
        model = GPPressureBuildupModel
        fields =['gpoil_Prod_Rate', 'gpguess_Value', 'gpt_since_shutin']