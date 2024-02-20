from .models import OBReservoirPressureEstimationModel
from django import forms
    
class OBRespresEstimationForm(forms.ModelForm):
    obanalysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBReservoirPressureEstimationModel
        fields =['obanalysis_Date', 'oblayer_Permeability', 'oblayer_Thickness', 'oblayer_Porosity', 'obtotal_Compressibility', 
                 'obmu_oil','oboil_FVF' ,'obwellbore_Radius', 'oboil_Prod_Rate', 'obini_Res_Pres', 'obdrainage_Radius' ]
