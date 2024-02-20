from django import forms
from .models import GPDrawdowntest
    
class GPDrawdownTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPDrawdowntest
        fields =['gpsurvey_Date', 'gpgauge_Depth', 'gplayer_Porosity', 'gplayer_Thickness',  'gpwellbore_Radius','gptotal_Compressibility', 
                 'gpinitial_Res_Pres', 'gpfbhp', 'gpoil_Viscosity', 'gpoil_FVF', 'gpliquid_Rate', 'gppvt_Well', 'gptest_Type', 'gpfile_Name']

class GPDrawdownTestUploadForm(forms.ModelForm):   
    class Meta:        
        model = GPDrawdowntest
        fields =['gpliquid_Rate', 'gpguess_Value', 'gpfbhp']

     