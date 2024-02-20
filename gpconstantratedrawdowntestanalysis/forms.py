from django import forms
from .models import GPConstantRateDrawdowntestModel
    
class GPConstantRateDrawdownTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPConstantRateDrawdowntestModel
        fields =['gpsurvey_Date', 'gpgauge_Depth', 'gplayer_Porosity', 'gplayer_Thickness',  'gpwellbore_Radius','gptotal_Compressibility', 
                 'gpinitial_Res_Pres', 'gpfbhp', 'gpoil_Viscosity', 'gpoil_FVF', 'gpliquid_Rate', 'gpfile_Name']

class GPConstantRateDrawdownTestUploadForm(forms.ModelForm):   
    class Meta:        
        model = GPConstantRateDrawdowntestModel
        fields =['gpliquid_Rate', 'gpguess_Value', 'gpfbhp']

     