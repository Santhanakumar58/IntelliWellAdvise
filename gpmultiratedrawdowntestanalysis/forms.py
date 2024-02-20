from django import forms
from .models import GPMultiRateDrawdowntest
    
class GPMultiRateDrawdownTestForm(forms.ModelForm):
    gpsurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPMultiRateDrawdowntest
        fields =['gpsurvey_Date', 'gpgauge_Depth', 'gplayer_Porosity', 'gplayer_Thickness',  'gpwellbore_Radius','gptotal_Compressibility',
                 'gpinitial_Res_Pres', 'gpoil_Viscosity', 'gpoil_FVF', 'gpfile_Name' ]



class GPMultiRateDrawdownTestUploadForm(forms.ModelForm):    
    class Meta:        
        model = GPMultiRateDrawdowntest
        fields =['gptime1', 'gppressure1', 'gptime2', 'gppressure2',  'gptime3','gppressure3']


   