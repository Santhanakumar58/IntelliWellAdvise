from .models import GPReservoirPressureEstimationModel
from django import forms
    
class GPRespresEstimationForm(forms.ModelForm):
    gpanalysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPReservoirPressureEstimationModel
        fields =['gpanalysis_Date', 'gplayer_Permeability', 'gplayer_Thickness', 'gplayer_Porosity', 'gptotal_Compressibility', 
                 'gpmu_oil','gpoil_FVF' ,'gpwellbore_Radius', 'gpoil_Prod_Rate', 'gpini_Res_Pres', 'gpdrainage_Radius' ]
