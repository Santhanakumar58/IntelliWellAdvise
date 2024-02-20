from django import forms
from .models import GPConstantPressureDrawdowntest
    
class GPConstantPressureDrawdownTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPConstantPressureDrawdowntest
        fields =['gpsurvey_Date', 'gpgauge_Depth', 'gplayer_Porosity', 'gplayer_Thickness',  'gpwellbore_Radius','gptotal_Compressibility',
                  'gpinitial_Res_Pres', 'gpoil_Viscosity', 'gpoil_FVF', 'gpfile_Name', 'gppwf']



     